---
title: "Introducing {newsanchor}"
date: 2019-05-01T11:00:00+02:00
image: "509-newsanchor.jpg"
summary: "An easy way to get news headlines from Newsapi.org"
categories:       
    - Projekte
author: 
    name:           "Yannik"
    image:          "yannik.jpg"
    description:    "Yannik holds a MA in Political Science of Mannheim University, works at Stuttgarter Zeitung and co-developed {newsanchor}."
    twitter:        "https://twitter.com/YBuhl"
    facebook:       ""
    github:         ""
    email:          "info@correlaid.org"
    website:        ""
meta:
  title: "Introducing {newsanchor}"
  description: "An easy way to get news headlines from Newsapi.org"
  image: "509-newsanchor.jpg"
  keywords: "CorrelAid, Data4Good, Open Source, Project, News, NLP, R, Scraping"
---

*At CorrelAid, we developed a tool for communication scientists, journalists and data scientists alike. We proudly present: *{newsanchor}*, CorrelAid's first open source R package. It conveniently helps you to access breaking news and articles from over 30,000 news sources and blogs - using the API of newsapi.org.*

The (mostly free) [News API](www.newsapi.org) is one way to access text as a resource for data analyses. It provides news articles and breaking news from a variety of sources across various countries, delivered to the analyst via an API (*HTTP REST*). Users are offered three API endpoints: *top headlines*, *everything*, and *sources*. *Top headlines* provides access to live breaking headlines of the news sources in a given country. *Everything* outputs articles published by these sources on a specified search query, even back in the past. *Sources* helps users to get access to the set of news sources that are available to *top headlines*. 

All search requests come with different meta data (URL, author, date of publication, topic, etc.)and can be refined by a huge variety of additional parameters (sources, topic, time, relevance, etc.). For more details, see [www.newsapi.org](www.newsapi.org). **Note for German scientists and journalists:** In Germany, the following sources are available: Spiegel Online, Handelsblatt, Tagesspiegel, Wired, Gründerszene, BILD, Zeit Online, Focus Online, t3n and Wirtschaftswoche. 

{{< image-subtitle
    image="509-newsanchor-embed.jpg"
    >}}
The hex sticker of the new {newsanchor} package
{{< /image-subtitle >}}

After a short registration, the API can be accessed via code: through client libraries such as JavaScript or Ruby. But until now, there has been no R package that does the work (or search) conveniently. Now, at CorrelAid, a team of five data analysts developed this package. The package is called **{newsanchor}** and is available on *CRAN*: ``install.packages("newsanchor")``:

*Newsanchor* provides three functions that correspond to the API's endpoints: `get_headlines()`, ``get_everything()`` and ``get_sources()``. They help users to conveniently scrape the resources of News API, specify different search parameters and obtain results as 1) a data frame with results and 2) a list with meta data on the search. We also provide comprehensive error messages to make troubleshooting easy. You find details on the usage of newsanchor and its core functions [in our general CRAN vignette](https://cran.r-project.org/web/packages/newsanchor/vignettes/usage-newsanchor.html).

Another reason for us to develop the package was that analyses based on words are becoming increasingly important. Political scientists, for example, classify parties on any ideological dimension using party manifestos. Other scholars focus on news articles to extract the (political) framings of the texts. Using automatisation, it is, for example, possible to calculate the sentiment of a given text fragment such as, for instance, online commentaries. The resulting data prove useful both as a dependent variable as well as an independent variable of any further analysis. 

The importance of text analyses arises from the origin of 'texts': People aim at a certain reaction of their readers. Among the producers of texts with most influence are the media: newspapers, online magazines or blogs. By publishing articles, opinion pieces and analyses, they shape public opinion. The topics they choose (or not choose), the words they use, the quantity of articles on a certain issue - all these factors make them a worthy basis of investigation. 

{{< image-subtitle
    image="509-newsanchor-count.jpeg"
    >}}
The count of downloads of the package at the time of writing
{{< /image-subtitle >}}

As already mentioned, an example would be to calculate the sentiment of news articles. Newsanchor can help to filter and scrape texts from news sources. In our [second vignette]([LINK TO SECOND VIGNETTE](https://cran.r-project.org/web/packages/newsanchor/vignettes/scrape-nyt.html)), our co-developer Jan Dix shows you how to do so by getting URLs of the New York Times with ``newsanchor::get_everything()``, subsequently scraping them with ``{httr}`` and analysing the articles' sentiments. 

We hope, **{newsanchor}** will help scientists, journalists and other data enthusiasts to start scraping and using text data based on news articles.