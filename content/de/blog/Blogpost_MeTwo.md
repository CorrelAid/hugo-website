---
title: "#MeTwo: National Identity and Discrimination in Germany in Times of Migration"
subtitle: "A data science perspective on online activism using Twitter data"
image: "pic_header_metwo.jpg"
summary: "Analyzing the #MeTwo movement using Twitter data and R"
categories:       
    - Analysis
    - Dataviz
date: 2019-08-02
author: 
    name:           "Konstantin Gavras, Lisa Hehnke, Paul Meiners, Sandra Meneses & Juan Orduz"
    image:          "team_metwo.png"
    description:    "Konstantin (@kongavras) is a Ph.D. candidate at the Graduate School
    of Economic and Social Sciences in Political Science and research associate at
    the Chair of Political Psychology at the University of Mannheim. Lisa (@DataPlanes)
    is a freelance social data scientist working to address current societal challenges
    in order to make a difference and drive change. Paul Meiners (@plmeiners) is a Ph.D. 
    candidate at the Gradutate School of Politics in Munster and research associate at 
    the department of Political Science at the University of Muenster.
    Sandra Meneses is data scientist at Mercedes Benz.io. Juan Camilo Orduz (@juanitorduz) is data scientist at TD reply."
    github:         ""
    facebook:       ""
    email:          ""
    website:        "https://metwo.correlaid.org/"
    twitter:        ""

meta:
  title: "#MeTwo: Re-defining National Identity"
  description: "#MeTwo: National Identity and Discrimination in Germany in Times of Migration"
  image: "pic_header_metwo.jpg"
  keywords: "CorrelAid, Data4Good, MeTwo, National Identity, Ali Can, Twitter"
---

Introduction
------------

Shortly before the start of the Men's Football World Championship in
2018, a debate on migration and the question of who a *true* German is
erupted on the issue that Mesut Özil took a photo with the Turkish
President Recep Tayyip Erdogan. The presumed reciprocal support of one
of the two most famous Turkish men sparked a vivid debate on whether
Mesut Özil, playing in the dress of the German Football national team,
should distance himself from the policies and authoritarian tendencies
displayed by the President of his father's land. This debate quickly
developed into a wider debate about who actually is German and whether
it is possible that migrants and their children might even feel attached
to two or even more heritages.

Based on this debate, social activist Ali Can developed a hashtag, which
should be a crystallization and manifestation of the struggles,
accusations and latent racism people not stemming from an autochton
German heritage face in their everyday life. Inspired by the MeToo
movement by women experiencing sexual harassment and violence from
partners, superiors and even strangers, \#MeTwo was born. Using this
hashtag, everyone having experienced harassment and discrimination due
to her migration background could unfold their story to make the general
public aware of the problems people with migration background face in
Germany. Based on this insight, reciprocal understanding of people with
and without migration background should emerge, building a more
sustainable and peaceful society.

To empirically test the implications and outcomes of this online
movement, we at CorrelAid decided to scrape all N = 159114 tweets on
\#MeTwo from July 24 to August 03, 2018, and examine the content, scope,
and temporal dynamics of this social media event, which now celebrates
its first birthday. As such, we aim to answer the following questions:

1.  How did the \#MeTwo movement emerge and how did it develop over the
    course of its lifetime?
2.  Which users have been involved in the online movement? Who were the
    most retweeted and favorited users? Do they tweet from personal
    accounts or from verified ones that are of public interest? How
    inclusive is the movement overall?
3.  How does the retweet network look like? Are there any key players
    that could potentially influence and shape the debate as the online
    movement continues? Did the network develop or change during the
    movement?
4.  Which content was shared and discussed? Which opinions and emotions
    are expressed in the tweets? Are the stories presented in the
    \#MeTwo highlighting the staggering experiences people faced in the
    past, or do positive experiences and hopes for a better future
    dominate the discussion? Is there a connection to other prominent
    hashtags?

Development of an Online movement in Digital Environments
---------------------------------------------------------

In an initial step, we simply plot the number of tweets and retweets
associated with the \#MeTwo Hashtag. As one can immediately see, this
hashtag did trend extremely quickly and particularly strong. Already in
the first hours of \#MeTwo, there were more than 500 tweets per hour. On
July 26 and 27, the online movement had its peak with more than 7000
tweets per hour only interrupted by the night hours in Germany. The
retweets increase at the same pace, indicating that the online movement
did spark wide interest within the Twitter community - the retweet count
peaked at about 2300 retweets an hour on the first two days. On the
following two days, there was still a reasonable amount of tweets and
retweets, but with the online movement already losing its pace of the
first two days. As for other online movements, MeTwo had a sharp peak in
the beginning, which last for a few days and then - hopefully gets
picked up by the offline society. After one week, we could not find any
further substantial input for the MeTwo movement, bringing us to a
preliminary conclusion that MeTwo seems to be comparable to other online
movements, which spark quite fast, but decline from the internet after a
short time period.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-2-1.png" >}}{{< /image-subtitle >}}


When seperating the tweets in original tweets and retweets, we see a
ratio of 1:5, which is actually quite reasonable, given that many users
do not get retweeted quite often. Thus, we are examining a hashtag,
which spread considerably and which was thus able to spark a discussion
about the reality of being German and about national identity in times,
in which millions of people in Germany originate from foreign countries.
The wide coverage of the hashtag allows us to empirically evaluate the
content of the tweets as well as the networks emerging during the online
debate on this topic. In a first step, however, we examine whether the
debate did only occur on twitter or if it spread to other means of
societal communication as well.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-3-1.png" >}}{{< /image-subtitle >}}


### Timeline of MeTwo in- and outside of Twitter

While the first plots provided information about the total volume of
tweets on \#MeTwo, we now turn to the coverage of MeTwo in comparison
with its appearance on Google Trends. This measure indicates how often
certain search phrases are being used in comparison with its average
search occurence. Thus, the peaks do not show absolute but relative
values. In order to re-create the emergence and over-time coverage we do
not only cover the search phrase of 'MeTwo' but also 'Rassismus' as well
as the initial of the movement, 'Mesut Özil', we looked at these
specific keywords.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-4-1.png" >}}{{< /image-subtitle >}}


In our first plot, we first compare the Google Trends index of 'Mesut
Özil' with the Twitter activity on MeTwo. As we can see, Mesut Özil
normally receives only small coverage in Google (perhaps mostly by
hard-core football fans). However, after the outrage concerning his
picture with the Turkish President Erdogan, Mesut Özil was googled
exordinarily often. Yet, in Google this trend did only last for more of
less two days after which Mesut Özil did not receive much of Google
Trends attention any longer. As one can see, MeTwo sparked about one
week after the incident together with a largeer political and societal
debate about rassism, national identity and the criterions of being
German. In order to check whether our asusmption about the essence of
this debate holds true, we now turn to the coverage of the search phrase
'Rassismus' in Google Trends, since it is a common phrase associated
with a public discourse on problems of national identity in times of
migration.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-5-1.png" >}}{{< /image-subtitle >}}


As one can see, the search phrase 'Rassimus' trended at the exact time
as 'Mesut Özil' and thus a few days before MeTwo started. Of course,
this search phrase is much more common on average than 'Mesut Özil',
thus we see a lot of variation in coverage over time. Interesting,
however, is the fact that 'Rassismus' did not trend simultaneous with
'MeTwo' although one might have assumed that these two terms are highly
associated.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-6-1.png" >}}{{< /image-subtitle >}}



Turning to the buzzword of MeTwo itself, we see that it experienced
broader societal coverage (measured via Google Trends), but only during
the Twitter debate on this topic and some weeks afterwards. As one can
see, Google Trends and Twitter peaked on this search phrase on the exact
same day, indicating that the online movement wasn't restricted on
Twitter only, but it also spread to a broader audience. As one can see,
MeTwo was still relevant for the public until the end of August 2018,
but faded afterwards. Summarizing, we can see that MeTwo was not only
restricted to Twitter, but became publicly important. Furthermore, it is
obvious that the debate on Mesut Özil sparked the online movement, which
was heavily associated with the more general problem of rassism whilst
discussing this issue.

Users and Participants in the MeTwo debate
------------------------------------------

### Most active users (number of tweets, retweets, and favorites)

After these aggregated insights into the emergence and development of
\#MeTwo, we now turn to more fine-grained analyses, including both the
accounts involved as well as the content articulated in their tweets.
Here, we first examine the accounts which used the hashtag the most in
their tweets and retweets. All of these accounts have impressive numbers
of tweets and retweets on \#MeTwo with more than 200, ranging up to 350
tweets, which is suprising given that the online movement did only last
for about a week. As can be seen in the following plot, among the most
active users are rather infamous accounts. Actually, the most active
users with regard to the \#MeTwo hashtag seem to be personal accounts
with only very modest numbers of followers. However, all of them are
extremely active twitter users in general.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-7-1.png" >}}{{< /image-subtitle >}}



Favorites are one of the most important currencies on Twitter, enabling
us to examine which accounts were most prominent in a social media
movement. The ten most favorited accounts in \#MeTwo included members
from civil society spreading the movement of Ali Can to a broader
audience, which is key to successful online movement. As one can see Ali
Can did not even receive the most favorites during the \#MeTwo debate
(alicanglobal: 6913), indicating that some even more famous social
activists and members of civil society also took place in the debate,
enabling it to make it more popular. In general, the 10 Twitter-accounts
with the most favorites were the following:

1.  Hasnain Kazim (Journalist of SPIEGEL ONLINE)
2.  Miriam Davoudvandi (DJ and editor of splash! Mag)
3.  Shahak Shapira (artist, author and musician)
4.  missanphan (unknown)
5.  Mahret Ifeoma Kupka (curator, writer)
6.  problematash (unknown, but currently blocked)
7.  Ali Can (social activist, author)
8.  Oguz Yilmaz (Youtuber)
9.  JanaRennsteig (unknown)
10. DieAgnosie (unknown)

As one can see, most of the highly favorited accounts are famous members
of civil societies and have a migration background. This indicates at
first that the debate was supported and developed through the active
participation of these accounts. Furthermore, all seemed to have some
direct or indirect personal relationship towards this topic, making it
both societally and personally relevant for them. Yet, these famous
Twitter-accounts seemed to have their share in the success of \#MeTwo.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-8-1.png" >}}{{< /image-subtitle >}}


Turning to the number of retweets an account received, we find an
extremely surprising picture. Among the top 10 of accounts having
received most retweets there is actually no particular famous account.
Although we are not quite sure, whether it might be an error in the
display of the numbers, it seems that retweets did not depend on the
popularity of the accounts during the \#MeTwo movement. This, however,
would indicate that \#MeTwo has been a grassroot online movement with
lots of people sharing their personal stories on national identity and
acceptance within the German society.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-9-1.png" >}}{{< /image-subtitle >}}


Summing up the most active Twitter users on \#MeTwo, we find that these
accounts are primarily social activists and famous member of civil
society (most have a migration background). Given that these accounts
have lots of followers it becomes a bit clearer why MeTwo has been such
a success.

### Account status

Our previous results strongly indicate that social activists and popular
members of civil society shaped the debate. To check whether the debate
indeed was strongly influenced by specific groups of accounts, we
classified all accounts into the following categories: \* Verified
account: Account is of public interest and thus officially verified by
Twitter \* Influencer: Account has more than 500 followers and its
number of followers is at least three times higher than the number of
followed accounts \* Verified influencer: Account is both officially
verified and an influencer (the most important accounts when trying to
spread a social media movement) \* Personal account: Account that is
neither verified nor classified as an influencer

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-10-1.png" >}}{{< /image-subtitle >}}


The following plot shows that the \#MeTwo movement was actually quite
widespread among the normal Twitter users. Far more than 40000 personal
accounts took place in the movement, or at least retweet or favorized
some tweets during the movement. Furthermore, we find support for the
movement by a large share of verified and non-verified influencers
amounting to more than 1000 individuals accounts. Lastly, also some
verified accounts without a broader set of followers took part in the
debate. These accounts, however, are mostly from political, social or
academic institutions and should not contribute heavily to the movement.
When taking a closer look at the non-personal accounts, it shows that
many social activists simply are not verified by Twitter yet and
elucidates that one should never fully rely on coding by third parties
when analysing data.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-11-1.png" >}}{{< /image-subtitle >}}


As expected, the following plot shows us that personal accounts are by
far more likely to retweet than tweet by themselves in the \#MeTwo
debate. For influencers, verified accounts and especially verified
influencer this we find a much higher evenness in the frequency of
tweets and retweets. Based on our knowledge on participation within
social movements this can be easily explained using the idea of actual
participants (gladiators) and spectators. It seems that actually all
influencer and verified accounts who took part in the movement actually
engaged in it, whereby lots of personal accounts did only retweet
messages to spread the word. This is of course not at all reprehensible,
but reflects our initial idea that \#MeTwo follows the principle of
classic social movements.

Tweeting about MeTwo in a Network
---------------------------------

After analyzing how \#We2 spread in our particular Twitter
subpopulation, we now turn to the analysis of the retweet network during
the debate. At first, we explain our directed retweet network. We define
the nodes as follows: The source is the retweeting account and the
target is the retweeted account. We define edges as a connection between
two nodes if the source retweeted the target at least once. The coloring
of the nodes follows the coloring of our categorization, with red nodes
indicating influencers, dark blue personal accounts, light blue verified
accounts, and purple verified influencers.

The layout of the network was calculated once for the entire time span.
The only things that changes from one plot to the other is the activity,
i.e. the connections between nodes. To make the plots more easily
readable, we only show accounts that engaged at least 7 times with other
accounts unsing the \#MeTwo.

We plot the retweet network with the size of the nodes relative to their
respective betweenness centrality. This measure represents the number of
the shortest connections between different nodes pass through a node.
Therefore, the higher the betweenness centrality, the higher the amount
of information that has to pass through a node to reach another node in
the network. The activities of nodes with high betweenness centrality
are not only important for their own messages but for those of other as
well, since they act as message distributors in the network.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/Plot1-2.png" >}}{{< /image-subtitle >}}


In the first plot we look at the first two days of activity. We can see
that the most central actors in the network are the personal accounts.
Only one influencer with an already strong following appears central in
the network. Accounts from verified users (for example media-related
accounts) are almost completely absent.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/Plot2-5.png" >}}{{< /image-subtitle >}}


The second plot shows the time between day 2 and 5 in our observation
period. Similarly to the first two days, personal accounts are dominant.
Essentially, only 6 accounts have high betweenness centrality.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/Plot5-7.png" >}}{{< /image-subtitle >}}



During the last two days, we can see that activity between the actors in
the network is starting to die down. But even here, no highly popular
accounts appear to be able to profit from the activity of the hashtag.

Overall, the network seems to strenghten the results from previous
analyses, when it comes to the most active category of users.
Interestingly, the network appears highly interconnected, which means
that most accounts are talking to each other. Even though we can see a
small amount of clustered users, there are no clear "pro" or "contra"
groups visible that do not interact. If there were separate
conversations going on, the network layout algorithm would have arranged
the nodes into clearly separable groups. However, this does not imply
that all users agreed with each other. A retweet can also be used to
express discontent with a message.

Tweet content
-------------

After examining the accounts who participated in the \#MeTwo debate, we
now turn to the actual content of the tweets. Ali Can's original idea
was to spark a discussion about people's experiences with racism in
Germany and the underlying question of national identity and belonging
to Germany. As such, the focus of the hashtag should both be inward and
outward looking as well as retro- and prospective, sparking a debate on
national identity in a society having to deal with a new self-conception
as an immigration society.

The next step of our analysis is structured by two main questions:
First, what does the Twitter community actually tweet about their
statements about their experiences with rassism and whether they feel
accepted as Germans in Germany. Second, we examine whether the overall
debate is more positive or negative. A positive sentiment would indicate
that the Twitter community is willing to share their positive
experiences and believes that Germany is able to find a good way to
re-define its national identity, whereas a negative sentiment might
indicate that either the debate has been captured by trolls or actual
accounts mourning about the current stage of nationhood and their
experiences as 'new sort of Germans'.

### Most common words

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-15-1.png" >}}{{< /image-subtitle >}}


In a first analysis, we filtered the most common words that were used in
the debate. In order to get a clean picture of these words, we removed
stop words and user names prior to plotting. The remaining words show
that 'racism' and 'Germany' were actually the dominating words
structuring the debate in the \#MeTwo movement. Turning to a word cloud
with the 100 most used words, this picture becomes more nuanced, since
words like society, foreigners, migration background, Turks,
experiences, parents and teacher also show up. It seems that most of the
debate is actually about the experiences Germans with migration
background faced while growing up in Germany. In order to check how
these stories untold, we now turn to analyses on the manner of writing
about the individual experiences.

<!--html_preserve-->

<script type="application/json" data-for="htmlwidget-b1f3ab4973f00273ae0b">{"x":{"word":["rassismus","deutschland","immer","menschen","deutsch","deutsche","schon","deutschen","wurde","mehr","gibt","gut","einfach","hashtag","geht","viele","land","warum","germany","erfahrungen","deutscher","klasse","ausländer","leute","sagt","kommt","racism","frau","wer","türken","nie","ganz","debatte","heute","tweets","eigentlich","sagen","rassistisch","leben","lehrer","beim","gar","wäre","eltern","müssen","wegen","macht","mann","kommen","jahren","lesen","migrationshintergrund","nein","bitte","frage","danke","german","gerade","problem","schule","mutter","sprechen","hast","seit","migranten","wirklich","sei","de","weiß","genau","rassisten","welt","oft","namen","özil","gefragt","gemacht","kinder","twitter","geschichten","tun","alltagsrassismus","jahre","dafür","besser","diskriminierung","leider","wohl","geboren","weiße","darf","herkunft","bekommen","gesellschaft","kind","u","lassen","hätte","dabei","vater"],"freq":[4116,2420,2037,1943,1875,1869,1718,1568,1556,1532,1333,1258,1254,1170,1109,1069,973,967,938,933,915,881,856,853,851,849,816,815,799,772,767,761,756,756,732,729,728,720,706,706,705,688,674,673,664,664,662,649,647,644,639,610,606,605,605,603,601,590,590,586,580,580,572,572,567,564,556,554,544,534,533,530,526,518,514,511,509,503,499,494,493,489,484,480,474,473,469,464,461,461,460,460,458,455,455,451,448,447,446,444],"fontFamily":"Segoe UI","fontWeight":"bold","color":"#1DA1F2","minSize":0,"weightFactor":0.043731778425656,"backgroundColor":"white","gridSize":0,"minRotation":-0.785398163397448,"maxRotation":0.785398163397448,"shuffle":true,"rotateRatio":0.4,"shape":"circle","ellipticity":0.65,"figBase64":null,"hover":null},"evals":[],"jsHooks":{"render":[{"code":"function(el,x){\n                        console.log(123);\n                        if(!iii){\n                          window.location.reload();\n                          iii = False;\n\n                        }\n  }","data":null}]}}</script>
<!--/html_preserve-->

### Co-occurring hashtags

A first indicator of the general notion of the content in the tweets
comes with the hashtags also used when posting. These co-occuring
hashtags provide a certain frame by which the content of the tweets can
be interpreted. As one can see, rassism and metoo are the two most often
co-occuring hashtags for the \#MeTwo movement. These two hashtags
highlight both the overall tone of the movement as well as its
predecessor - the MeToo movement, sheding light at sexual harassment,
violence and discrimination against women.

The third most often used hashtag shed lights to one fundamental problem
of social movements - being hijacked by trolls and those feeling
offended by emphasizing latent rassism in Germany. The so-called K.O.
Challenge, initiated by Fatlind Albo, invoking young men with migration
background to beat up autochton Germans. This, of course, attract the
attention of right-wing activists associating with challenge with MeTwo
and dis-credit all men with migration background as potential violent
criminals. As this hashtag co-occured the third-most often in our data,
we have to take care that a substantial share of tweets are posted by
members of right-wing activist groups to discredit the MeTwo movement.

The remaining hashtags seem again to be related with the idea of MeTwo
as such, although AfD might be highlighted as a political party denying
the new realities in Germany and 29TemmuzDünyaGüzelLikGünü refer to the
World Beauty Day, which we are not able to associate with the MeTwo
movement at all. It seems a bit as if the movement did not only face
right-wing trolls, but also interaction from users based in Turkey.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-17-1.png" >}}{{< /image-subtitle >}}


### Tweet sentiments

The last layer of our content analysis concerns the sentiments
associated with the respective tweets mentioning \#MeTwo. Our sentiment
analysis is based on a dictionary approach using the
[SentiWS](http://wortschatz.uni-leipzig.de/de/download) dictionary by
the University of Leipzig. The dictionary classifies which German words
have a negative and positive meaning, respectively, and assigns numeric
values to them. We then can simply map the words used in the tweets
against the words included in the dictionary along with their values.

As we can see in our first analysis, the overall sentiment of the
\#MeTwo debate is rather balanced, however, with about 30 percent more
positive than negative words. This rather high number of negative words
indicates that many people had negative experiences when growing up in
Germany. On the other side, however, we see lot of positive words,
reiterating our assumption that many people also have made positive
erperiences and have a positive stance towards this movement.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-18-1.png" >}}{{< /image-subtitle >}}


When examining the sentiment distribution over time, we see that we
actually almost always have more positive words than negative ones.
However, the margins between positive and negative words are steadily
decreasing with only a few more positive than negative sentiments in the
last days of the movement. Yet, in the first day one clearly sees the
excitement which came along with this new social movement, transporting
a positive reinterpretation of what Germany might look like in the
future.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-19-1.png" >}}{{< /image-subtitle >}}

But which words are actually classified as positive and negative words
in the \#MeTwo debate? In the following overview we see that good,
better, understanding, right, luck and love are the most frequently used
positive words in the debate. This indicates that most users try to tell
a positive story on their experiences but also their expectation for the
future. On the negative side, we see problems, discrimination, hate and
sorrow. This might refer to crucial negative experiences faced in the
past, highlighting that people with migration background actually face
problems of racism in the past, but perhaps up until now in their
everyday life.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-20-1.png" >}}{{< /image-subtitle >}}



These findings can be visualized in a comparison cloud as well:

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-21-1.png" >}}{{< /image-subtitle >}}



### Tweets in foreign languages

Lastly, we examine whether the debate spread beyond a German-speaking
subgroup on Twitter. Using automated language recognition functions, we
classified the tweets in different languages. The following plot shows
all languages with a minimum share of 0.001% that were present in the
tweets. We see that the majority of the debate took place among
German-speaking users. However, we also find some tweets in English,
French, Japanese, Spanish and French. Although not being particular
popular among foreign Twitter users, it seems that \#MeTwo has somewhat
spread to other European countries as well.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-22-1.png" >}}{{< /image-subtitle >}}



MeTwo and the Media
-------------------

In a final step, we examined how the gate-keepers of societally relevant
information - the media - took part in the MeTwo movement. In order to
identify media accounts, we match all accounts refering to media
institutions or journalism among the verified accounts to get a better
picture of the total amount of journalists being willing to take up the
story of Ali Can and \#MeTwo.

As we can see, more than 200 media institutions and 150 journalists from
all over the world reported on MeTwo. This is a considerably high
number, showing that MeTwo was not only a Twitter movement, but spread
to a broader audience, which can be targeted by the journalists. These
actors are among the most important to lead social movements (especially
in their online version) to success. They are able to spark public
discourse about these topics and might even change public perception on
topics like \#MeTwo.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-23-1.png" >}}{{< /image-subtitle >}}



In order to check whether journalists and media institutions actually
took part in the \#MeTwo debate, we again examine the number of tweets,
retweets, foavorites and followers for this sub-group of accounts. In
the following plots, we present the results for these measures and
compare them with the remaining verified accounts, not being affiliated
to the media. At first, we can see that media institutions were actually
tweeting far more than retweeting on \#MeTwo. For journalists we find
the exact opposite. Given the function of these accounts, this is very
reasonable and confirms our assumption that \#MeTwo has travelled to a
broader public via the media. since institutions should not post
personal stories, they should refer to shows in their program associated
to \#MeTwo using Twitter. This is a first indicator that \#MeTwo has
received a broad coverage also outside of the Twitter community.
Journalists, however, actually took part in the debate - perhaps even
because they wanted to share their stories as well. For non-media
accounts, we find a comparable pattern to journalists.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-24-1.png" >}}{{< /image-subtitle >}}


Taking a closer look at actual media accounts being most active in the
debate, Hasnain Kazim (journalist SPIEGEL), Düzen Tekkal (filmmaker and
journalist), Tobias Huch (journalist and author), Dunja Hayali
(journalist ARD) and Jens Clasen (editor Womens Health) stand out in
particular. All of these perons are well-known to be active in fighting
for a liberal and value-driven German society and have a large
followership. Thus, they are both credible in speaking up in the \#MeTwo
movement and also able to mobilize a lot of people. Among the media
institutions, Perspective Daily (online-magazine), SPIEGEL ONLINE and
the Süddeutsche Zeitung are to be named as most active and influencial.
Again, we see a clear pattern of left-liberal outlets being willing to
spread the word on \#MeTwo and helping the movement getting recognition
and shaping public discourse.

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-25-1.png" >}}{{< /image-subtitle >}}

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-26-1.png" >}}{{< /image-subtitle >}}

{{< image-subtitle image="metwo-analysis/figure-markdown_strict/unnamed-chunk-27-1.png" >}}{{< /image-subtitle >}}


Conclusion
----------

Taken together, \#MeTwo has been a rather successful online debate. With
our Twitter analysis we tried to confirm existing assumptions about the
debate and conveys some additional and interesting results. Our findings
show that \#MeTwo is both positive and negative in its tenor and,
strongly influenced by prominent social media activists and journalists
already focussing on societal problems concerning national identity and
immigration. The hashtag seems to had a unifying effect on those
persons, most often fighting for these issues by themselves. Personal
accounts as well as the media and individual journalists, who are
essential for social media events to become successful, were part of
this movement. This explains why it was so successful in last year's
summer.

When compared to Ali Can's other hashtag \#We2 (see a short blog post
[here](https://correlaid.org/blog/we2-twitter-analysis/)), we can see
that \#We2 is mainly driven and supported by political elites rather
than the general population. Unlike \#MeTwo with the debate on Mesut
Özil's retirement from the German national football team, there was no
triggering event of broader public interest when \#We2 emerged. As a
result, the media response is largely absent and hence the potential of
traditional media channels has not been fully exploited yet.

To conlude, \#MeTwo went extremely viral and perhaps sparked a debate on
national identity and Germanhood in a migration society. Using data
science, we hope that we were able to provide insights about certain
aspects of the movement and were able to show which aspects are crucial
for social media movements to become successful.
