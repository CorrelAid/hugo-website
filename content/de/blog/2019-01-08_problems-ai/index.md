---
title: Three problems of the current hype around *Artificial Intelligence*
date: '2019-01-09T00:00:00+02:00'
image: 509-a-data-scientist.jpg
summary: Why we think that the current usage of the term *AI* is problematic
categories: Veranstaltungen
author:
  name: Frie und Johannes
  image: friejohannes.png
  description: Frie is a data scientist at Codecentric and a board member of CorrelAid;
    she tweets under [@ameisen_strasse](https://twitter.com/ameisen_strasse). Johannes
    is the founder and head of the board of CorrelAid; he tweets under [@jj_mllr](https://twitter.com/jj_mllr).
  twitter: ''
  facebook: ''
  github: ''
  email: info@correlaid.org
  website: ''
meta:
  title: Three problems of the current hype around *Artificial Intelligence*
  description: why we think that the current usage of the term *AI* is problematic
  image: 509-a-data-scientist.jpg
  keywords: CorrelAid, Data4Good, AI, buzzword, hype
slug: problems-ai
---

The term *Big Data* is out of fashion. *Artifical Intelligence* is the new kid in town. Sharing the faith of the previous buzzword: **It means everything and nothing.** In the public discourse it now roughly translates to "everything with data and something digitalization and something neural networks". This became apparent once more after the German government published its 3 billion AI strategy. The German Association for Information Processing called the usage of the term by the government "[very arbitrary](https://gi.de/meldung/gi-kommentiert-eckpunkte-einer-ki-strategie-der-bundesregierung/)". 

At CorrelAid we are deeply passionate about the potential of data and analytics. However, we do have our problems with the way the term is used lately and see multiple problems that arise from this imprecise language.  In this blog post, we want to explain why we think that the current usage of the term "Artificial intelligence" is problematic, both in the broader sense, but also with a focus on our **Data-for-Good** work at CorrelAid. 


# AI in Data Science  

> *"Difference between machine learning and AI:
>If it is written in Python, it's probably machine learning. 
>If it is written in PowerPoint, it's probably AI."* [@matvelloso 5:25 PM - 22 Nov 2018](https://twitter.com/matvelloso/status/1065778379612282885?lang=en) 


Today AI is mostly used synonymously with applied **machine learning** (ML). The intelligent part of Machine Learning is that we can develop models that can predict outcomes (supervised learning), or find patterns (unsupervised learning) that were not explicitly coded by a programmer but are "learned" by the computer. This is done using **linear algebra and applied statistics**. In its most advanved forms ML helps us to tackle enourmously complex tasks like [protein folding](https://thenewstack.io/deepmind-ai-makes-breakthrough-with-protein-folding-problem/) or [diagnosing diseases](https://thenewstack.io/scientists-artificially-intelligent-nanoarray-can-diagnose-disease-using-breath/). However, the sophistication of most ML models in production is far away from the latest "breakthroughs" dicussed in the news.

The study of these ML algorithms started roughly 50 years ago and originated in different schools of thought in the computer science community. One thing all approaches have in common is that they are grounded in philosophical beliefs about what "knowledge" is, how it is created and the way **[humans make decisions](https://www.youtube.com/watch?v=B8J4uefCQMc&t=711s)**. Take for example neural networks: "Neural networks mimic the way neurons work in our brains". Sounds catchy, yet is highly misleading in terms of what is actually happening.

These underlying ideas create the **narratives of AI**, fuel the hype and shape our discourse. Let's look at some practical problems this creates. 


# The problems

## It sets unrealistic expectations

First of all, the extensive and imprecise usage of *AI* creates **unrealistic expectations**.

Models are only as good as the data you put into them. While this may be less true for deep learning approaches that are very good at learning from unstructured data, it certainly is for the majority of data science models. For those models, data scientists need to create meaningful data structures. This process is called feature engineering and it requires [**high-quality data**](https://hbr.org/2018/04/if-your-data-is-bad-your-machine-learning-tools-are-useless) from which it is actually *possible* to extract those meaningful features. Getting access to this data is one of the major obstacles data scientists face in their day-to-day work because it requires data scientists to convince the "data owners" - most of which are non technical people - of this need for good data. 

This challenge gets even harder if everything - "classical" data science models, deep learning, exploratory analysis, data visualization - is lumped under *Artificial Intelligence*. Non-technical people will think there is no need for any good quality data for anything because well … the machine is *intelligent*, right? 

**Machine learning is an intelligent way of using applied math and statistics, but it doesn’t make the decision-making intelligent in itself.** This has to be clear to non data scientists who are an important part of a data science project. Declaring everything and nothing to be "intelligent" does not foster the differentiated debate that is necessary for that knowledge transfer.


## It introduces unnecessary barriers  

### For Data Scientists

Artificial intelligence has the potential to attract and amaze new people for the field of data science. However, this kind of framing attracts certain people more than others and might even **discourage some from getting into the field of data science**. The brilliant project [fast.ai](fast.ai) (which has the goal to make machine learning more inclusive) describes the problem with the current framing of AI as follows: 

> "*Being cool is about being exclusive, and that’s the opposite of what we want. We want to make deep learning as accessible as possible– including to people using uncool languages like C#, uncool operating systems like Windows (which is used by the majority of the world), uncool datasets (way smaller than anything at Google, and in domain areas you’d consider obscure), and with uncool backgrounds (maybe you didn’t go to Stanford)*"

On another level this creates the next problem: Not all people are in the lingo and know that currently "can you do AI?" in 80% of cases basically means: "can you do some intermediate data science?" This could keep people with realistic views of their own skills who are probably good data scientists from getting into IT jobs. This will probably disproportionately affect people from groups currently underrepresented in IT as they are less likely to know people in the business - not only [gender minorities](https://www.wired.com/story/artificial-intelligence-researchers-gender-imbalance/) but also people from non-technical backgrounds. **Data science is an inherently diverse and interdisciplinary field** - it would be a shame (and economically unwise) if this potential was kept out by a buzzword hype.


### For civil society organisations

A similar problem arises in the context of data-for-good. In principal, hypes like "big data" or "AI" are good at getting attention for the potential of using data. At the same time, those hypes mostly speak to decision makers in NPOs who are already in some way citizens of the digital world. Again, a typical example of **selection bias**. 

This is unfortunate because there is also a lot of potential of data science for NPOs that are not as technology-driven. Good examples are traditional German civil society organisations such as sports clubs or scouts associations. The projects CorrelAid has done with this kind of organizations came about through personal connections. This is a totally valid way of project aquisition but it does not scale well. Instead, we need a way of communicating the potential of data science to the wider public that is not as fuzzy and obscure as the "AI" hype but more **focused on specific use cases** (At CorrelAid we are currently working on a tool to tackle this problem, stay tuned!).

If everything is lumped under "AI", the benefits of using data won't be visible anymore and some NPOs will probably think "ah well, another tech hype that certainly does not apply to our work."


## It puts the focus on methods, not impact

Non-profit organizations (NPO) tend to have a **pretty good bullshit detector**. If you advertise something that is not making their life easier or helps in the terms of their impact logig: it is not interesting to them. As a consequence, even if we use machine learning techniques in our projects we don’t advertise them as such – we rather talk about what it can do for the organisation. 

At Correlaid about 2/3 of our projects involve some kind of Machine Learning techniques (e.g. classification, predictive modelling, NLP) - yet the goal is more important than the methods. Two examples: 

* Project Together connects voluntary coaches to young people who want to start a social project. We help Project Together improve mentor-mentee relationships by providing insights to why some pairings fail and how to recognize early which pairings might fail (*using automated text analysis and classification*)
 
* Ashoka facilitates social entrepreneurship around the world. We helped to identify potential biases in the selection process for a scholarship (*using statistical modelling and text analysis*).

Data science is not about using specific methods, it's about getting insights from data and solving problems.


# “AI” done right

In this blogpost we discussed several problems with the use of AI in the public discourse:

1. It sets unrealistic expactations by masking what is actually done (No magic; just a lot of data wrangeling, applied maths, and statistics)!
2. It gatekeeps people who want to get into the field of data science by being unnecessarily intimitading.
3. The focus on methods (and not impact) sets the barrier for entry unnecessarily high for non-tech organisations - especially NPOs! 

Data science yields huge potential for companies, NPOs and the society at large. On the other hand, we face many challenges. To harness the potential and deal with problems we need clearer language and a more thoughtful mode of discussion. We should use a language that is centered around solutions and use cases - and not around meta discussions and buzzwords. 


