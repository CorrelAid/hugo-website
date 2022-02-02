---
title: German Bundestag meets Twitter
date: '2020-03-08T19:00:00+02:00'
subtitle: A Network Analysis of the Members of the German Bundestag
image: 509-mdb-network.jpg
summary: A Network Analysis of the Members of the German Bundestag
categories:
- Analysis
- Statistics
- Network
author:
  name: Lukas Tatge
  image: lukas-t.jpg
  description: Lukas Tatge heads CorrelAidX Göttingen. He is a Master student of Global
    Business/Management.
  github: ''
  facebook: ''
  email: goettingen@correlaid.org
  website: https://www.linkedin.com/in/lukas-tatge-32282115b/
  twitter: ''
meta:
  title: German Bundestag meets Twitter
  description: A Network Analysis of the Members of the German Bundestag
  image: 509-mdb-network.jpg
  keywords: CorrelAid, Data4Good, Statistics
slug: mdb-network
---

### Investigating German MPs on Twitter

Since Angela Merkel's famous 'Neuland' quote in 2013, the influence and relevance of social media for society, but also for politicians, has greatly increased. Politicians use the Twitter platforms mainly to communicate with the public, the media and with each other. In a fast-moving and attention-driven social media world, I want to use the social network approach to take a look at how elected German politicians are connected to each other and whether the party structure we observe in the real world is also visible in this digital space.

I choose the social network Twitter to perform this analysis because it is often the primary social media platform for politicians to communicate publicly. Also, it offers a good API. In December 2019, I manually collected all the names of Twitter accounts, real life names and party membership based on the official list of politicians who are part of the German Bundestag. Based on this, I build a social network based on which politicians follow each other on Twitter, in order to determine the importance of each politician in that social network.   

To collect the necessary information about the following of the individual politician accounts, I use the R package `{rtweet}`. With the function `get_friends()` it is possible to get all Twitter accounts that someone is following. An important limitation for this API is that it is only possible to send 15 requests every 15 minutes, so I wrote a function that only sends new requests after 15 minutes. After using this function for every politician, I got a file with two columns and more than 400,000 rows. The first column contains the politicians account, and the second column contains the account ID of another account he is following. 

Since the relationship between two politicians can be unilateral or bilateral, I add a third column with the value 1 if the relationship is unilateral, or 2 if the relationship is bilateral. To include party membership, I use my original file on politicians and by using the R package `{dplyr}`, I then include party membership by merging these two tables. For the visual representation of this social network, I use the program `NetGraph`, in which I display only the nodes (a Twitter account) of the politicians and use different colors depending on the party membership. The result is shown in the following picture.

{{< image-subtitle
    image="mdb-network.png"
    >}}
The network graph of German MPs on Twitter
{{< /image-subtitle >}}

In this figure, you first see that each party is well connected internally and has few members who are not close to their fellow party members. A second finding is that the AfD is clearly separated from the other parties. This somehow fits with the public announcement of all large German parties not to cooperate with this radical party. It also shows that SPD, Buendnis 90/Die Gruenen and Die Linke are more closely linked and that CDU/CSU and FDP are also more closely linked. This is in line with previous government coalitions.

In a second step, I then create a non-graphical social network with the R-package {igraph}. There, I create a graph (social network) which is based only on the politician nodes (Twitter accounts) and their relationships (weight of the connection). Then, I calculate the 'Betweenness' and the 'Closeness', which are both different measures for the importance or centralization of a note in a social network. Betweenness centrality measures the number of times a politician node lies on the shortest path between other politicians. 

This measure shows which politicians are 'bridges' between other politician in this network and just counts this number. In contrast to this, the Closeness centrality evaluates each politician's node based on their 'Closeness' to all other politicians in the network. This measure calculates the shortest paths between all politicians, then assigns each politician a rating based on its sum of shortest paths. The results are shown in the following table.


#### Betweenness

| Rank | Name |	Party |	Betweenness |
|:-------:|:-------:|:-------:|:-------:|
| 1 |	Stefan Liebich |	Die Linke  |	43065	|
| 2	| Kordula Schulz-Asche	|	B90/Gruene	|	7387	|
| 3	| Frank Schaeffler |	FDP |	7343 |
| 4	| Frank Pasemann |	AfD |	6767 |
| 5 |	Dorothee Baer |	CSU |	6491 |
| 6 |	Andreas Nick |	CDU |	5904 |
| 7 |	Heiko Maas |	SPD |	5686 |
| 8 |	Johannes Kahrs |	SPD |	5434 |
| 9 |	Konstantin von Notz |	B90/Gruene |	4528 |
| 10 |	Uwe Kamann |	- |	3736 |

<br>


#### Closeness

| Rank | Name |	Party |	Closeness |
|:-------:|:-------:|:-------:|:-------:|
| 1 |	Frank Pasemann |	AfD |	0.0016420361 |
| 2 |	Uwe Kamann |	- |	0.0009832842 |
| 3 |	Johannes Kahrs |	SPD |	0.0009242144 |
| 4 |	Frank Schaeffler |	FDP |	0.0009107468 |
| 5 |	Ulli Nissen |	SPD |	0.0009025271 |
| 6 |	Stefan Liebich |	Die Linke |	0.0009017133 |
| 7 |	Florian Pronold |	SPD |	0.0008888889 |
| 8 |	Felix Schreiner |	CDU |	0.0008873114 |
| 9 |	Edgar Franke |	- |	0.0008826125 |
| 10 | Tobias Lindner |	- |	0.0008810573 |



You can see that each party has a few members who seem to play an important role/position in this social network. An interesting finding could be that the two largest parties in the current parliament, CDU/CSU and SPD, do not have as many members in the first places as you might expect. These places are rather taken by smaller parties like AfD, FDP, Die Linke. These unexpected results should be further investigated in the future to find the reason for this. Possible explanations could be the difference between opposition and government parties, different communication strategies of the parties or the adoption rate of social media in each party.

In a big picture this network analysis can confirm that many of the expected relationships within each party and between the parties can also be shown in social media. In the future, this analysis could be further strengthened by also examining how politicians have interacted with each other through retweets, answers or the liking of other posts of politicians. It should also be further investigated why certain politicians are particularly important for this network and whether it is possible to draw conclusions about their power within their party.  

For the people who are interested in the actual code, I have put the most important parts into the appendix. If you would like to receive the underlying data or have further questions, please send me a message on LinkedIn.


### The Code

#### Capture the data from Twitter  

```r
library(rtweet)

appname <- 'Research Politicians'
key <- 'Input your own key'
secret <- 'Input your own key'
access_token <- 'Input your own key'
access_secret <- 'Input your own key'

twitter_token <- create_token(
  app = appname,
  consumer_key = key,
  consumer_secret = secret,
  access_token = access_token,
  access_secret = access_secret)


name_ politician <- read.csv('list_ politician.csv',header = FALSE)

i = 0
user_follows_list_var = ()
user_follows_list = ()

while (i<=len(name_ politician[1]) {
  user_follows_list_var <- get_friends(list_pol[i])
  user_follows_list <- rbind(user_follows_list,user_follows_list_var)
  print(i)
  
  user_follows_list_var <- c()
  if (i%%15==0) {
    Sys.sleep(910)
    print('Break')
  }
  i <- i + 1
}

user_follows = data.frame(user_follows_list)

library(dplyr)
colnames(name_ politician) <- c('user_id','user')
joined_data <- left_join(user_follows, name_politician,by='user')


fwrite(joined_data, file='twitter_relation.txt',sep = '\t')

fwrite(name_politician,file='twitter_account.txt',row.names = FALSE,sep = '\t')
```



#### Social Network Analysis

```r
library(igraph)
relation <- read.csv('twitter_relation.txt',sep = '\t')
account <- read.csv('twitter_account.txt',sep = '\t')
graph_politician <- graph.data.frame(relation)
get.edge.attribute(graph_politician, 'weight')
V(graph_politician)
E(graph_politician)

betweenness(graph_politician)
closeness(graph_politician)

tail(sort(betweenness(graph_politician)), 10)
tail(sort(closeness(graph_politician)), 10)

plot.igraph(graph_politician)
```

