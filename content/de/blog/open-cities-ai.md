---
title: "How to do Data Science competitions as a team"
date: 2020-04-28T08:00:00+02:00
image: "headerberlin.jpg"
summary: "Learnings from a DrivenData challenge"
categories:
  - CorrelAid
author:
  name: "Sylvi & Manuel"
  image: "sylvimanuel.jpg"
  description: "Sylvi is a Postdoc in Economics at University of Potsdam and one of the coordinators of the local chapter Berlin. Manuel is a Research Engineer at Creatext, an early-stage NLP startup. He's member of the local chapter Berlin."
  twitter: ""
  facebook: ""
  github: ""
  email: "berlin@correlaid.org"
  website: "https://correlaid.org/correlaid-x/berlin/"
meta:
  title: "How to do Data Science competitions as a team"
  description: "Learnings from a DrivenData challenge"
  image: "headerberlin.jpg"
  keywords: "CorrelAid, CorrelAidX, Data Science, DrivenData"
---

Several members of [CorrelAidX Berlin](/correlaid-x/berlin) recently took part in the [Open Cities AI Challenge](https://www.drivendata.org/competitions/60/building-segmentation-disaster-resilience/page/151/), hosted by DrivenData and co-organized by [Global Facility for Disaster Reduction and Recovery (GFDRR)](https://www.gfdrr.org/en) of the World Bank. In this post, we will share some learnings of our group effort with the CorrelAid community.

### What are data science competitions?

At a data science competition, a problem sponsor asks the worldwide community to solve a data problem in the best possible way. There are a few platforms that host such competitions, [Kaggle](kaggle.com) being the most famous. [DrivenData](https://www.drivendata.org/competitions/) is a similar platform but has a focus on positive social impact competitions, which motivated our participation as CorrelAiders. In our case, the competition was a binary classification problem: we were provided with drone imagery from major African cities and were asked to classify each pixel in the picture, determining whether the pixel represents a building or not. The long-term goal of GFDRR, the competition sponsor, is to be able to quickly estimate the amount of material damages after a natural disaster (earthquakes, etc.) by comparing the drone imagery before and after the disaster. To find the best classifier, all competitors got a training and a test data set. In the end, we submitted a CSV with predictions on the test set, that is on data that the model has not yet seen, and it was rated in terms of a specific performance metric (in our case, the [Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index)).

## Our learnings

1. Setting clear goals for the team in the beginning is key for better planning and estimation of the workload. In our case, the goal was to submit something and learn how to participate in a data science competition.

2. Having experience (or not) with the type of problem and the provided data will have a huge influence on the amount of time necessary to invest in the competition. In our case, nobody had real experience with computer vision, which meant a rather high time investment to produce code for the submission to the DrivenData competition.

3. One way to learn more about computer vision methods was to reach out to people in the CorrelAid network with more experience. This helped a lot. We would recommend that an ideal team has at least one person who already has experience with the type of problems and data, so she or he can better guide the team and maximize the overall learnings.

4. Make sure to use all the existing resources when starting the project. In our case, by looking at the competition forum, we found out that another competitor had already shared his solution, including preprocessing the data and preparing the predictions in the right format for submission. This saved us a ton of time and allowed us to submit a first prediction result in just a few hours. The downside of this is that one does not necessarily completely understand what happens in the code, especially in this case for the file preprocessing, which makes it harder to improve the results afterwards.

5. Set up good collaboration tools. As computer vision needs a graphic processing unit (GPU) and/or a tensor processing unit (TPU) to train the neural network models, we used Google Colab, a cloud solution which provides both for free. It worked well for individual work but was a bit harder to collaborate with. Ideally, one would have a GitHub repository and run the scripts on a server afterwards, if available. That way, one can also track changes more easily through pull requests.

6. Do a kick-off and several group calls along the way (or even meet in person) to keep momentum. We had a kick-off group call where we set-up the technical tools together and loaded the data. We also defined different tasks and divided them among the team members. After that, we had several check-in calls that were very useful in keeping a bit of momentum and team spirit despite working remotely.

In this competition, ranking in the top 10% turned out to be feasible. Our final rank was 50/1106. A good place for our first competition. But what is more, we learned a lot and got even more motivated to continue honing our computer vision skills. We encourage you to try one, too!
