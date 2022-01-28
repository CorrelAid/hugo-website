---
title: "#We2: Re-defining European identity"
date: 2019-05-26T00:00:00+02:00
subtitle: "A data science perspective on online activism using Twitter data"
image: "we2_network.png"
summary: "Analyzing the #We2 movement using Twitter data and R"
categories:       
    - Analysis
    - Dataviz
author: 
    name:           "Konstantin Gavras & Lisa Hehnke"
    image:          "konstantin_lisa.jpeg"
    description:    "Konstantin (@kongavras) is a Ph.D. candidate at the Graduate School of Economic and Social Sciences in Political Science and research associate at the Chair of Political Psychology at the University of Mannheim. Lisa (@DataPlanes) is a freelance social data scientist working to address current societal challenges in order to make a difference and drive change."
    github:         "https://github.com/lhehnke/we2-twitter-analysis"
    facebook:       ""
    email:          ""
    website:        ""
    twitter:        ""
meta:
  title: "#We2: Re-defining European identity"
  description: "Analyzing the #We2 movement using Twitter data and R"
  image: "we2_network.png"
  keywords: "CorrelAid, Data4Good, EuropeanElections, Europe, #We2, Twitter"
---

*Acknowledgements:* Parts of the code for this analysis are based on the
\#MeTwo project we conducted together with [Paul
Meiners](https://www.uni-muenster.de/IfPol/personen/meiners.html),
[Sandra Meneses](https://github.com/symeneses), and [Juan
Orduz](https://juanitorduz.github.io/). The final results of our project
can soon be found [here](https://metwo.correlaid.org/).

Introduction
------------

The European project is at stake with today's election of the European
Parliament. In nearly all European countries, populist and anti-European
parties are on the rise. They try to gain votes by providing simple
answers to complicated questions, most prominently, that the European
Union should not bother with politics within the European nations,
emphasizing the supremacy of national sovereignty and exploiting the
feelings of national identity. Yet, after more than 60 years of European
integration, is it actually that easy to pinpoint the nation one belongs
to, feels emotionally attached to, and identifies with?

In order to tackle this challenge, social activist [Ali
Can](https://ali-can.de/), the founder of the \#MeTwo movement, launched
a new hashtag on May 20, 2019: \#We2. Using this hashtag, Ali draws
attention to the new realities in an integrated Europe. People nowadays
not only have one identity; instead, identity is multi-faceted,
hierarchical and sometimes even contradicting. But no matter the
nation(s) people feel attached to, European unification taught us that
identities should always be inclusive.

To empirically test the implications and outcomes of this new movement,
we decided to scrape all N = 793 tweets on \#We2 from May 20 to May 26,
2019 (last retrieval: 1:30 p.m.), and examine the content, scope, and
temporal dynamics of this ongoing social media event. As such, we aim to
answer the following questions:

1.  How did the \#We2 movement emerge and develop until the European
    election day on May 26, 2019?
2.  Which users have been involved in the online movement so far? Who
    are the most retweeted and favorited users? Do they tweet from
    personal accounts or verified ones that are of public interest? How
    inclusive is the movement overall?
3.  How does the retweet network currently look like? Are there any key
    players that could potentially influence and shape the debate as the
    online movement continues?
4.  Which content was shared and discussed during these first days?
    Which opinions and emotions are expressed in the tweets? Is there a
    connection to other prominent hashtags? Did the hashtag manage to
    spread to other European countries?

Twitter activities
------------------

### Tweets & retweets stats

In an initial step, we simply plot the number of tweets and retweets
associated with the \#We2 hashtag. As is evident at first glance, the
hashtag did not trend particularly strong with less than 1000
tweets in total. When seperating the tweets in original tweets and
retweets, we find a ratio of 1:3 which is a rather low number compared to more prominent hashtags.
Thus, \#We2 did not spread as widely as its pendants
\#Metoo and \#MeTwo that were both highly popular and managed to change public
discourse and politics on gender equality, sexual harassment, national
identity, and discrimination. Although trying to foster a discourse on
multiple and particular European identities, the \#We2 hashtag was 
apparently not as successful as its predecessor \#MeTwo. In the following analyses we try to
answer the question of why this movement did not work out as intended, although other
and quite comparable movements were extremely successful and sparked discussions on social and political issues.

{{< image-subtitle image="we-2-analysis/figure-markdown_strict/unnamed-chunk-8-1.png" >}}{{< /image-subtitle >}}

### Timeline

While the first plot provides information about the total volume of
tweets on \#We2, the second plot shows the number of tweets and retweets
over time. Online movements usually follow a certain chronological
order, starting with a triggering event. These events were easy to
identify for similar hashtags such as \#MeToo with the accusations of
sexual misconduct against Harvey Weinstein or \#MeTwo with the scandal
of Mesut Özil openly supporting the Turkish president Recep Tayyip
Erdoğan. When triggering events are salient for a large group of people
and can be channeled through an easy-to-understand hashtag, a social
media movement is likely to stage. Contrary to this, there was no
particular event which might have triggered a high-profile discussion
about \#We2. Although being launched in the final week of the European
elections, elections as such are often too abstract and formalized to
spark outrage or particular social media attention. This is exactly what
we find with the \#We2 tweets. The peak is on May 21 when the hashtag
first trended and after this initial peak we can see a steady decline.
Thus, without a formative event happening outside the social media
sphere and being extremely salient for a large group of people, social
media phenomena seem to have a difficult time emerging successfully.

{{< image-subtitle image="we-2-analysis/figure-markdown_strict/unnamed-chunk-9-1.png" >}}{{< /image-subtitle >}}

### Most active users (number of tweets, retweets, and favorites)

After these aggregated insights into the emergence and development of
\#We2, we now turn to more fine-grained analyses. Here, we first examine
the accounts which used the hashtag the most in their tweets and
retweets. As can be seen in the following plot, among the most active
users are Ali Can (alicanglobal), the founder of both \#MeTwo and \#We2,
Malcolm Ohanwe (MalcolmMusic), a journalist who strongly influenced the
\#MeTwo debate when sharing his own experiences with racism, and several
politicians from the Social Democratic Party of Germany (hereafter:
SPD). Interestingly, there are hardly any non-famous individuals or
traditional media accounts among the most active users, indicating that
\#We2 remained in a very particular subgroup of the Twitter community.
Notable exceptions to this are individual accounts such as StopNS2,
Der\_Dude80 or straeubchen and projects like ColorfulGermany or Amnesty
International Göttingen (amnestygoe).

{{< image-subtitle image="we-2-analysis/figure-markdown_strict/unnamed-chunk-10-1.png" >}}{{< /image-subtitle >}}

Favorites are one of the most important currencies on Twitter, enabling
us to examine which accounts were most prominent in a social media
movement. The ten most favorited accounts in \#We2 were mostly
politicians from the SPD: \* Katarina Barley: Lead candidate for the
2019 European elections (SPD) \* Heiko Maas: German Minister of Foreign
Affairs (SPD) \* Luisa Neubauer: Climate activist who co-organized
Fridays for Future in Germany \* Sawsan Chebli: State Secretary for
Federal Affairs in the state government of Berlin (SPD) \* Martin
Schulz: German politician (SPD) \* Andrea Nahles: German politician
(SPD) \* Lars Klingbeil: German politician (SPD) \* Damian Boeselager:
Lead candidate for the 2019 European elections (Volt Germany)

In addition, Ali Can and Malcolm Ohanwe can be found among the ten most
favorited accounts again. This finding points to another challenge for
\#We2: There were no prominent Twitter influencers spreading the word.
In fact, only Ali Can and Luisa Neubauer can be denoted social media
influencers to some degree. But without getting other prominent and thus
influential social media users or traditional media accounts on board,
online movements seem to lose momentum.

{{< image-subtitle image="we-2-analysis/figure-markdown_strict/unnamed-chunk-11-1.png" >}}{{< /image-subtitle >}}

Turning to the number of retweets an account received, a pretty similar
picture emerges. We only find one personal, but unusually active,
account here: liebmeinland.

{{< image-subtitle image="we-2-analysis/figure-markdown_strict/unnamed-chunk-12-1.png" >}}{{< /image-subtitle >}}

Summing up the most active Twitter users on \#We2, we find that these
accounts are primarily social activists (Ali Can and Luisa Neubauer) or,
to a larger extent, politicians (most often from the SPD). Yet, no media
accounts or journalists other than Malcolm Ohanwe show up in our
analysis.

### Account status

Since our previous results strongly indicate that political elites
shaped the debate and neither activists nor journalists played a larger
role so far. To check whether the debate indeed was strongly influenced
by political officials, we classified all accounts into the following
categories: \* Verified account: Account is of public interest and thus
officially verified by Twitter \* Influencer: Account has more than 500
followers and its number of followers is at least three times higher
than the number of followed accounts \* Verified influencer: Account is
both officially verified and an influencer (the most important accounts
when trying to spread a social media movement) \* Personal account:
Account that is neither verified nor classified as an influencer

The following plot shows that, unlike what might have been expected
given the previous results, the broader scope of the online movement
seems to be less elitist and more inclusive with over 500 unique
accounts - a rather large number given that there are only approximately
800 tweets containing \#We2 overall. This finding shows that most people
tweet from personal accounts, followed with a great distance by
(verified) influencers and, lastly, verified accounts who do not fall
into the influencer category.

However, when taking a closer look at those accounts, it shows that many
politicians simply are not verified by Twitter yet and elucidates that
one should never fully rely on coding by third parties when analysing
data. Still, while not being personal accounts in a proper sense,
unverified politicans most often do not have a larger following on
Twitter, which makes them reasonable candidates for being classified as
personal accounts. Since these semantics are not of particular interest
for our analysis, we rely on the scheme partially provided by Twitter
for now.

{{< image-subtitle image="we-2-analysis/figure-markdown_strict/unnamed-chunk-14-1.png" >}}{{< /image-subtitle >}}

The next figure shows the number of tweets and retweets by status
category in order to gain a deeper insight into the respective Twitter
behavior. It turns out that personal accounts are to a large extent only
retweeting existing tweets and do not take part in the debate as
actively as the potentially could. In contrast, verified influencers and
verified accounts have a fairly balanced ratio between retweets and
tweets. The same is also true for influencers, though they appear to
tweet more than retweet, resembling the classical behavior assumed by
influencers.

{{< image-subtitle image="we-2-analysis/figure-markdown_strict/unnamed-chunk-15-1.png" >}}{{< /image-subtitle >}}

Retweet network
---------------

After analyzing how \#We2 spread in our particular Twitter
subpopulation, we now turn to the analysis of the retweet network during
the debate. At first, we explain our directed retweet network. We define
the nodes as follows: The source is the retweeting account and the
target is the retweeted account. We define edges as a connection between
two nodes if the source retweeted the target at least once. The coloring
of the nodes follows the coloring of our categorization, with red nodes
indicating influencers, dark blue personal accounts, light blue verified
accounts, and purple verified influencers.

We plot the retweet network with the size of the nodes relative to their
respective in-degree centrality (i.e. the number of retweets an account
received). Moreover, we labeled only nodes with centrality scores larger
or equal to 10 (i.e. only users that were retweeted at least 10 times
are labeled). The edge weight is defined as the number of retweets
between two nodes.

The following network graph confirms the findings of our previous
analyses. Activists and SPD politicians are the most central nodes in
the Twitter retweet network. As expected, the SPD accounts appear to be
rather closely connected, with Fridays for Future climate activist Luisa
Neubauer and Damian Boeselager - the lead candidate of the Volt party,
who recently gained some fame for temporarily getting the
[Wahl-O-Mat](https://www.wahl-o-mat.de/europawahl2019/) shut down -
being quite distant to the nodes of the SPD politicans.

{{< image-subtitle image="we-2-analysis/figure-markdown_strict/unnamed-chunk-17-1.png" >}}{{< /image-subtitle >}}

Tweet content
-------------

After examining the accounts who participated in the \#We2 debate, we
now turn to the actual content of the tweets. Ali Can's original idea
was to spark a discussion about people's multiple European identities
and let the Twitter community express their feelings towards and
associations with the European Union more generally. In doing so, \#We2
should form a counter-movement to the emerging nationalism and growing
chauvinism in several European countries.

The next step of our analysis is structured by two main questions:
First, what does the Twitter community actually tweet about the European
Union and its implication of more and more people having multiple
identities. Second, we examine whether the overall debate is more
positive or negative. A positive sentiment would indicate that the
Twitter community is willing to share their positive associations with
the European idea, whereas a negative sentiment might indicate that
either the debate has been captured by trolls or actual accounts
mourning about the current stage of the European Union.

### Most common words

In a first analysis, we filtered the most common words that were used in
the debate. In order to get a clean picture of these words, we removed
stop words and user names prior to plotting. The remaining words show
that Europe as such, identity, and references to gratefulness are among
the most common words in the tweets. Hence, the people using \#We2 seem
to discuss exactly the issues that Ali Can had in mind when creating the
hashtag. Using a word cloud, we corroborate our first intuition by
mapping the 100 most common words.

{{< image-subtitle image="we-2-analysis/figure-markdown_strict/unnamed-chunk-22-1.png" >}}{{< /image-subtitle >}}

{{< image-subtitle image="we-2-analysis/we2_wordcloud.png" >}}{{< /image-subtitle >}}

### Co-occurring hashtags

Another layer of content in Twitter debates comes with the usage of
additional hashtags to highlight specific aspects users want to
emphasize. With regard to the \#We2 debate, we see that most of the
hashtags are expressing a strong dislike against the right-wing
political party Alternative for Germany (AfD) and, more generally,
against racism and antisemitism. Thus, the co-occurring hashtags align
with and supplement our previous content-related findings by rejecting
nationalism and favoring diversity.

{{< image-subtitle image="we-2-analysis/figure-markdown_strict/unnamed-chunk-24-1.png" >}}{{< /image-subtitle >}}

### Tweet sentiments

The last layer of our content analysis concerns the sentiments
associated with the respective tweets mentioning \#We2. Our sentiment
analysis is based on a dictionary approach using the
[SentiWS](http://wortschatz.uni-leipzig.de/de/download) dictionary by
the University of Leipzig. The dictionary classifies which German words
have a negative and positive meaning, respectively, and assigns numeric
values to them. We then can simply map the words used in the tweets
against the words included in the dictionary along with their values.

As we can see in our first analysis, the overall sentiment of the \#We2
debate is mostly positive with a ratio of 5:1 compared to negative
words. This confirms the findings we got when analyzing both the most
common words and the co-occurring hashtags.

{{< image-subtitle image="we-2-analysis/figure-markdown_strict/unnamed-chunk-27-1.png" >}}{{< /image-subtitle >}}


When examining the sentiment distribution over time, we see that we
actually almost always have more positive words than negative ones. We
only see a minor negative peak around May 23 to May 24, 2019. Given the
extremely low number of words on these two days, however, this peak
should not be overstated.

{{< image-subtitle image="we-2-analysis/figure-markdown_strict/unnamed-chunk-28-1.png" >}}{{< /image-subtitle >}}

But which words are actually classified as positive and negative words
in the \#We2 debate? In the following overview we see that peace,
freedom and unity are the most frequently used positive words in the
debate. This indicates that most users still seem to associate the core
values and principles of the European Union with this fundamental
political project on the European continent. On the negative side, we
see worries and damages. This might refer to nationalist and populist
movements, which are campaigning to damage and overthrow the European
Union and its institutions.

{{< image-subtitle image="we-2-analysis/figure-markdown_strict/unnamed-chunk-29-1.png" >}}{{< /image-subtitle >}}

These findings can be visualized in a comparison cloud as well:

{{< image-subtitle image="we-2-analysis/figure-markdown_strict/unnamed-chunk-30-1.png" >}}{{< /image-subtitle >}}



### Tweets in foreign languages

Lastly, we examine whether the debate spread beyond a German-speaking
subgroup on Twitter. Using automated language recognition functions, we
classified the tweets in different languages. The following plot shows
all languages with a minimum share of 0.001% that were present in the
tweets. We see that the majority of the debate took place among
German-speaking users. However, we also find some tweets in English,
French, Dutch, and Russian. Although not being particular popular among
foreign Twitter users, it seems that \#We2 has somewhat spread to other
European countries as well.

{{< image-subtitle image="we-2-analysis/figure-markdown_strict/unnamed-chunk-32-1.png" >}}{{< /image-subtitle >}}


Conclusion
----------

Taken together, \#We2 is still a very modest debate, but our Twitter
analysis already conveys some very interesting results. Our findings
show that \#We2 is unusually positive in its tenor and, maybe even more
surprisingly, strongly influenced by prominent SPD politicians and only
a handful of social media activists. Personal accounts as well as the
media and individual journalists, who are essential for social media
events to become successful, are not part of the debate yet.

When compared to Ali Can's other hashtag \#MeTwo (see the final results
of our project soon [here](https://metwo.correlaid.org/)), we can see
that \#We2 is mainly driven and supported by political elites rather
than the general population. Unlike \#MeTwo with the debate on Mesut
Özil's retirement from the German national football team, there was no
triggering event of broader public interest when \#We2 emerged. As a
result, the media response is largely absent and hence the potential of
traditional media channels has not been fully exploited yet.

To conlude, \#We2 did not went as viral as \#MeTwo or its predecessor
\#MeToo did to date. While we believe the hashtag has the potential to
spread further, the future of \#We2 largely depends on the active
involvement of the traditional media. It is possible that the results of
the European election will once again draw the attention of Twitter
users to the hashtag. We are staying on the case and provide you with
the latest results as they come in!
