---
title: "Reconstructing Cambridge Analytica's 'psychological warfare tool'"
date: 2018-03-28T00:00:00+02:00
image: "509-cambridge-analytica.jpg"
summary: "Building a personality classifier in R  - using facebook data, machine learning and personality traits"
draft:      false
categories:       
    - R
    - DIY
    - Programming
author: 
    name:           "Johannes"
    image:          "johannes.jpg"
    description:    "Johannes hatte 2015 die Idee für CorrelAid und ist seitdem unser Vorstandsvorsitzender. Er studiert im Master 'Evidence-based Policymaking' an der University of Oxford und Policy-Analyse an der Universität Konstanz. Er interessiert sich vor allem für Evaluierungsmethoden, die Nutzung von Evidenz und Daten in Gesellschaft und Politik, und Social Entrepreneurship."
    twitter:        "https://twitter.com/jj_mllr"
    facebook:       ""
    github:         ""
    email:          "johannes.m@correlaid.org"
    website:        ""
meta:
    title:          "CorrelAid - Reconstructing Cambridge Analytica's 'psychological warfare tool'"
    description:    "The British analytics firm helped the Trump campaign to build a massive voter database to inform micro-targeting campaigns. The goal was to reach voters on an individual level with messages they are recpetive to in order to persuade them to vote for the 'right' candidate."
    image:          "509-cambridge-analytica.jpg"
    keywords:       "CorrelAid, Data4Good, Cambridge Analytica, R"
---


Last week the [story about Cambridge
Analytica](https://www.theguardian.com/news/2018/mar/17/data-war-whistleblower-christopher-wylie-faceook-nix-bannon-trump)
broke
([again](https://motherboard.vice.com/en_us/article/mg9vvn/how-our-likes-helped-trump-win)).
The British analytics firm helped the Trump campaign to build a massive
voter database to inform micro-targeting campaigns. The goal was to
reach voters on an individual level with messages they are recpetive to
in order to persuade them to vote for the "right" candidate. So far,
this is nothing new. Obama has used this approach in 2008 and 2012 and
Hillary Clinton has used this form of voter targeting as well for sure
(on a budget that was certainly bigger than that from the Trump
campaign).

What is different with Cambridge Analytica and the Trump campaign are
two things: Firstly, they obtained facebook data in very sketchy ways,
which is a severe problem, especially on the side of Facebook. The
second issue - which is getting the greater attention - is that
Cambridge Analytica used something called psychometrics to create
psychological profiles of all the voters. This raises two questions: How
does it work and is it really that powerful?

So, let's first take a look at the idea behind [Steve Bannon's
psychological warfare mindfuck
tool](https://www.theguardian.com/news/2018/mar/17/data-war-whistleblower-christopher-wylie-faceook-nix-bannon-trump)
(Christopher Wylie) and then build our own version in R to understand
how it works.

### The idea behind the Cambridge Analytica tool

The approach of Cambridge Analytica is based on the OCEAN model (or [Big
Five Model](https://en.wikipedia.org/wiki/Big_Five_personality_traits))
which is popular in psychology to describe the personality of a person.
It is based on five latent personality traits that are represented as
scales:

-   Openness to experience (inventive/curious vs. consistent/cautious)
-   Conscientiousness (efficient/organized vs. easy-going/careless)
-   Extraversion (outgoing/energetic vs. solitary/reserved)
-   Agreeableness (friendly/compassionate vs. challenging/detached)
-   Neuroticism (sensitive/nervous vs. secure/confident)

The idea of Cambridge Analytica was as follows: If you know the
personality type of a person you can use that to feed them ads and
information which they are most receptive to. The problem is: To assess
somebody’s personality, you usually have to give them a questionnaire
with validated survey items. That poses the question where to get that
data for millions of voters. This is where social media and machine
learning comes into play.

The original idea was developed by the Cambridge University researcher
Michal Kosinski. He developed an app for Facebook which lets people
assess their personality type. He then uses the information of the
Facebook profiles (which the people agree to be accessed by the
application) like their *status updates* and *likes* to see which
factors are related to which personality type. He claims to have shown
"that a wide range of pervasive and often publicly available digital
footprints such as Facebook profiles or data from mobile devices can be
used to infer personality"
([Paper](https://4f46691c-a-dbcb5f65-s-sites.googlegroups.com/a/michalkosinski.com/michalkosinski/ieee2.pdf?attachauth=ANoY7co1suMv6DxwXXtgZMd6aB4QUKgvkzX1guxoJWkDaKc_A8E_XDwNynAA0yukiVm32xPK7fWz8nG_ZqRvkdLlB2Nv15J3tKXieFw90nPiYYscbjzblQ8VcMd0FAN7PKmjcZOGrcAesTEbi0BMtu9Uf3_QxH-W7aRiS-SJ5vDtSFKLiDNmEeUwOQw-EhDOKYXcsIgAlGJgapFbS-zDiS0ptveY1UNZrw%3D%3D&attredirects=0)).

This opens the possibility to extrapolate the scores of people on the
five personality scales just using their Facebook page information. As
people didn't only agree that their profile information was accessible
but also the information of their friends, the creator of the app
suddenly has a lot of information on a lot of people. Cambridge
Analytica didn't get the data from Kosinski but got information on 50
millions Facebook users from another Cambridge researcher [Alex
Kogan](https://motherboard.vice.com/en_us/article/ywxgeg/cambridge-analytica-researcher-interview).

### How could Cambridge Analytica's algorithm look like

Let's see how it can be done. In this blogpost I will build a
super-simplified version of the tool of Cambridge Analytica - or at
least what I believe how it looks like. I will start from the end and
start by developing two different versions of an ad that match two
different personality profiles.

1\. Firstly, we need different ads and information that we can feed to
people with different personality types. At this point we must make
qualitative assumptions about which ads work best for which people. For
this blog post we will use one strategy that is [believed to be
used](https://www.theverge.com/2018/3/20/17138854/cambridge-analytica-facebook-data-trump-campaign-psychographic-microtargeting)
by Cambridge Analytica: Targeting neurotic voters.

2\. Secondly, we need data from an app on Facebook where people were
happy to fill out the personality quiz. We will use an anonymised
dataset from a personality app that can be used for research purposes.

3\. Thirdly, we need an algorithm that lets us extrapolate the
personality profile for people who didn’t fill out the questionnaire.
For this purpose, we will train a basic machine learning model that
predicts whether a facebook user is neurotic or not based on their
status updates.

4\. Lastly, we need Facebook data from other users which we can then
target with our ads. For this step, we will use the Facebook API to get
access to public FB profiles.

\
#### Step 1: The ads

For this blogpost we will simplify things a bit. Instead of looking at
all five factors we will only look at the neuroticism scale. To simplify
it even further we will say that people who are above the median of the
neuroticism scale are sensitive and nervous and those below are more
confident and rational - this makes it a simple classification problem.
For both groups we want to design a good fake ad that will appeal to
their personality. Let's look at the two versions we want to spread on
Facebook:

****
Version 1: "immigrants ... mayham ... build a wall ... "

{{< image 
    image="509-trump_ad_immigrants.jpg"
>}}
Trump Ad Immigrants
{{< /image >}}

The first ad we are using is a classic fear mongering example of a Trump
campaign ad. We assume that this one will work well with people with
high values on the neuroticism scale.

****
Version 2: "Crooked Hillary ... emails ... unfit ..."

{{< image 
    image="509-trump_ad_clinton.jpg"
>}}
Trump Ad Immigrants
{{< /image >}}

The second ad creates the image of Hillary Clinton as a corrupt
politician. We want to feed this ad to people who are less neurotic and
are unlikely to vote for Trump anyways. The goal targeting this group is
rather to discourage voting for Clinton and going to the polls on
election day.

\
#### Step 2: Personality data

Next, we need some data to train our targeting algorithm. If we would
have a lot of money and wouldn’t give a damn about ethics we would just
buy the data from some personality app-provider. Luckily, we don't have
to go there and can just use a dataset provided by Kosinski himself. He
published a dataset on 10.000 Facebook updates by 250 users. For those
users we also have the scores for the personality traits as they used
the Kosinksi's FB app. The data is anonymised, and the users agreed that
the data can be used for research purposes. The dataset can be
downloaded
[here](http://mypersonality.org/wiki/doku.php?id=download_databases) .

```r
library(readr)
library(caret)
library(tm)

data <- read_csv("~/projects/cambridge_ana/mypersonality_final.csv")
head(data)
```

```r
# A tibble: 6 x 21
  `#AUT~ STATUS    sEXT  sNEU  sAGR  sCON  sOPN cEXT  cNEU  cAGR  cCON  cOPN  DATE  NETW~
                   
1 b7b77~ likes t~  2.65  3.00  3.15  3.25  4.40 n     y     n     n     y     06/1~   180
2 b7b77~ is so s~  2.65  3.00  3.15  3.25  4.40 n     y     n     n     y     07/0~   180
3 b7b77~ is sore~  2.65  3.00  3.15  3.25  4.40 n     y     n     n     y     06/1~   180
4 b7b77~ likes h~  2.65  3.00  3.15  3.25  4.40 n     y     n     n     y     06/2~   180
5 b7b77~ is home~  2.65  3.00  3.15  3.25  4.40 n     y     n     n     y     07/2~   180
6 b7b77~ www.the~  2.65  3.00  3.15  3.25  4.40 n     y     n     n     y     07/1~   180
# ... with 7 more variables: BETWEENNESS , NBETWEENNESS , DENSITY ,
#   BROKERAGE , NBROKERAGE , TRANSITIVITY , neu_dummy
```

As already mentioned above, we simplify things again. Let's say we only
want to assess whether one Facebook status was written by a neurotic
person. Neglecting that the 10.000 updates are not independent from each
other, we now have some data points to train our model. Obviously, we
can't expect to get a great model fit as we try to make a prediction
based on a facebook post.

Before we build the model we first must clean and prepare the data. We
perform a median split on the neuroticism variable to create our two
groups we want to target (1=neurotic, 0=balanced). We then clean the
status updates by removing stop words, numbers, punctuation and endings
to retain only the word stems. We then create a document term matrix,
which provides us with single words as features to build our
classifiers.

```r
# Preparing the outcome variable Neuroticism
data$neu_dummy <- rep(0, nrow(data))
data$neu_dummy[data$sNEU > median(data$sNEU)] <- 1  #median split

# Preparing the document term matrix
data$STATUS <- iconv(data$STATUS, "ASCII", "UTF-8", sub="")
corpus <- VCorpus(VectorSource(data$STATUS))
tdm <- DocumentTermMatrix(corpus, list(removePunctuation = TRUE,
                                       stopwords = TRUE,
                                       stemming = TRUE,
                                       removeNumbers = TRUE))
```


#### Step 3: Train the model

Now we can train a model to predict whether a status was written by a
neurotic person. For this purpose, we will use a simple linear support
vector machine implemented in the caret package.

```r
# Prepare dataframe for modelling
train <- as.data.frame(as.matrix(tdm))
keep <- (colSums(train) >=5) #drop words that appear less than 5 times in the dataset. This decreases our accuracy but also might prevent overfitting.
  train <- train[, keep]
train$y <- as.factor(as.character(data$neu_dummy))

# Training the model using a linear svm
fit <- train(y ~ ., data = train, method = 'svmLinear3')
```

```r
# Check accuracy on training.
predict(fit, newdata = train)
sum(predict(fit, newdata = train) == train$y)/nrow(train)
```

```r
[1] 0.707472
```

If we check the in-sample accuracy we see that our algorithm can
classify 70 % of the status updates correctly. This is not great and we
haven’t even checked how good it classifies new examples, but it doesn't
matter. We don't have to provide any evidence of how good our algorithm
works anyways (as Cambridge Analytica isn't revealing their algorithms
either - obviously). We will just say we created a "psychological
warfare tool". Something with machine learning, big data, facebook and
personality traits. People will buy it.

\
#### Step 4: Use the classifier to target new voters

We can now classify people just based on their facebook updates and use
the information to feed them the ads they are more receptive to. If we
are an unethical and scrupulous data company we would use the
information to update our huge database of semi-legally or illegally
obtained facebook users. We will instead use the Facebook API to get
some status updates from public facebook profiles. Let's determine which
ad we should show Paul Ryan, speaker of the House of Representatives, as
an example:

```r
library(Rfacebook)

token <- "******" # get your token under https://developers.facebook.com/tools/explorer/

paulryan_page <- getPage("paulryanwi", token, n = 100, since='2016/01/01', until='2016/06/01')

# Use one random status update of Paul Ryan for classification
paulryan_status <- page_paulryan$message[sample(nrow(paulryan_page), 1)]

# Prepare document term matrix
corpus <- VCorpus(VectorSource(paulryan_status))
tdm <- DocumentTermMatrix(corpus, control = list(dictionary = Terms(tdm), removePunctuation = TRUE, stopwords = TRUE, stemming = TRUE, removeNumbers = TRUE))
paulryan_tdm <- as.matrix(tdm)

# Predict which group Paul Ryan belongs to
predict(fit, newdata = paulryan_tdm)
```

```r
[1] 0
Levels: 0 1
```

Our classifier would suggest that Paul Ryan is in the calmer, more
rational group. Therefore, we would show him the second ad (the
anti-Clinton ad).

### Wrap-Up: Is it really that scary?

This blogpost walked you through how I imagine how the Cambridge
Analytica Targeting Tool roughly works. I have no idea how it actually
looks like, how accurate it is and how it is used. The real algorithm
includes many more features and a multidimensional outcome, but you can
probably imagine how well it could work if it is trained on large
datasets. However, how good that works is questionable. You can try out
what your FB data reveals about you with the tool by Kosniski on his
page <https://applymagicsauce.com/>. My results were not impressive at
all: It got my religious orientation, my political orientation and
education background all wrong (so if you're really worried about this
mind manipulation thing, maybe try the website and you will feel much
better afterwards). In the end, the inference about someone's
personality type is based on the correlation of likes and personality
profiles in the training data. That can easily go wrong.

Even if the algorithm is really efficient in predicting the five
personality traits, the question remains if it is actually effective in
getting people to buy a product or even vote for a specific candidate.
There is not much evidence about the effects and their magnitude of
psychmetric microtargeting. The idea of using available information to
micro-target internet users is not new. Quite the opposite, it is the
main business model of companies like Google and Facebook. They will use
data such as your demographic background, which device you use, where
you go shopping, who your friends are, what pages you like and so on to
optimize their ad targeting (again, mostly based on correlational
evidence). Personally, I am highly sceptical that this new layer of
building psychometric models is really improving micro-targeting as much
as Cambridge Analytica claims it does.

I think it is fair to say that Cambridge Analytica is dangerous in the
way they are meddling in elections around the world in a highly
unethical and often illegal ways. I also understand that the media jumps
on the narrative of "Bannon/Trump + unethical data science company +
Facebook + big data + mind manipulation", because it sounds scary.
However, I would argue that big data and mind manipulation are the two
smallest problems in this equation and we should not just repeat the
narrative of a company that wallows in this public image of omnipotence.
Cambridge Analytica sure knows how to market their services or to use
the words of Alexander Nix, founder of CA: "It doesn't have to be true,
it just has to be believed."

------------------------------------------------------------------------


