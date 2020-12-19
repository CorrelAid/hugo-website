---
title:      "Gender differences in mobility patterns - an analysis on the example of Madrid"
date:       2020-12-19T00:00:00+02:00
image:      "gender_mobility_header.jpg"
slug:       "gender_bias_and_mobility"
summary:    "Data analysis can be gender biased. This article explores how and how this applies to mobility. We analysed open mobility data of Madrid to identify differences in mobility behavior between men and women."
draft:      false
categories:       
    - CorrelAidX
    - Analysis
    - internal project
author: 
    name:           "Alexandra, Liam & Marcus"
    image:          "alex_liam.jpg"
    description:    "[Alexandra](https://twitter.com/lxndrkp), [Liam](https://twitter.com/ldbailey255) and Marcus are part of the local chapter CorrelAid X Berlin. Alexandra is a data analyst in mobility and has been with CorrelAid since 2018. Liam is an ecologist evolving into a data scientist. He's been a member of CorrelAid since late 2019 and using agent based modelling to study large African carnivores in the rest of my time. Marcus ... "
    twitter:        "https://twitter.com/correlaid"
    facebook:       "https://facebook.com/WeAreCorrelAid"
    github:         "https://github.com/correlaid"
    email:          "info@correlaid.org"
    website:        "https://www.correlaid.org/"
meta:
    title:          "Gender differences in mobility patterns - an analysis on the example of Madrid"
    description:    "Data analysis can be gender biased. This article explores how and how this applies to mobility."
    image:          "gender_mobility_header.jpg"
    keywords:       "CorrelAidX, Analysis, internal project"
---
## Data analysis is (gender) biased

Data is not an objective truth - despite what we data analysts would like to believe. Analyses reflect the perspective from which they were created. If a team is  too uniform in their experiences then the diverse perspectives of different age groups, genders, or ethnicities are easily forgotten. Such bias is often observed in relation to gender, where most analyses focus on the ‘default male’ (Invisible Women, Caroline Criado-Perez), leading to serious, even deadly consequences for women [^1]. For example, crash dummies tend to represent the average male size, which is [one of the reasons why women are more likely to be injured or killed in a crash](https://www.consumerreports.org/car-safety/crash-test-bias-how-male-focused-testing-puts-female-drivers-at-risk/). Women are also more likely to be [misdiagnosed when having a heart attack](https://www.leeds.ac.uk/news/article/4269/women_more_at_risk_of_dying_after_a_heart_attack)because studies have mostly been done with male participants, who show very different symptoms to women. There is a growing awareness of this gender bias in data science, with great books written on this issue by [Caroline Criado-Perez](https://www.goodreads.com/book/show/41104077-invisible-women), [Catherine D’Ignazio and Lauren F. Klein](https://www.goodreads.com/book/show/51777543-data-feminism), and [Cathy O’Neil](https://www.goodreads.com/book/show/28186015-weapons-of-math-destruction).

Having no (or not enough) data about women isn’t the only issue: If there is data on men and women alike, it’s often not gender disaggregated, which is necessary to reveal gender related differences. For example, gender disaggregated data is necessary to understand gender biases in working hours (including both paid and unpaid work): Gender disaggregated data does not exist for all countries, but in almost all countries where it exists there is a clear trend that women work longer - on average 50 min more each day (see The [Global Gender Gap Report 2016](http://www3.weforum.org/docs/GGGR16/WEF_Global_Gender_Gap_Report_2016.pdf)). Another example where gender disaggregated data is important is the area of mobility behaviour, which we want to investigate closer in this blog post.

## Mobility: an issue of gender bias

### Women trip chain, men take the car to work during rush hour

Is mobility gender biased? And if so, how? In most western cultures, women are still responsible for the majority of care work. Bringing children to school, going grocery shopping and taking care of elderly parents. Bias in the distribution of care work also leads to different mobility behavior: Women do more trip chaining, with many, shorter trips, and greater use of public transport - especially buses. In comparison, a typical “male trip” involves long car trips to and from work during rush hour. This difference in mobility behaviour is reflected in city design and public transport networks, which is usually mainly designed by men with a focus on work related and rush hour traffic - traffic that is considered to be most important. Connections optimized for the typical male “workforce” with fast connections from residential areas to the city center, where most offices are located, and poor connections for close trips to kindergartens, schools, supermarkets, and tangential lines to neighboring residential areas. (TODO find sth to cite by Inés Sánchez de Madariaga directly?  This issue has moved more and more into the focus of transport planners (e.g. [this publication by the GIZ](https://womenmobilize.org/wp-content/uploads/2020/02/iNUA-Paper.Gender-and-Urban-Transport-min.pdf) or this by [CIVITAS](https://civitas.eu/sites/default/files/civ_pol-an2_m_web.pdf)).

## A closer look on Madrid’s mobility data

### An internal CorrelAid project

Madrid offers a large and detailed mobility data set from 2018. Unlike other cities and countries, Madrid published the data as open data allowing us to investigate gender biases in mobility. About 85.000 people each reported their trips over the course of one day, including mode, motive, origin and destination combined with demographic data. Find the [documentation (spanish) here](https://www.crtm.es/media/712934/edm18_sintesis.pdf) and the [data set here](https://crtm.maps.arcgis.com/apps/MinimalGallery/index.html?appid=a60bb2f0142b440eadee1a69a11693fc).
Within our team, we wanted to use this as an opportunity to analyse the data to answer the following questions:
1. Can we reproduce the results on gender differences from other studies?
2. Do we find additional differences with an exploratory analysis?
3. Can we find evidence that the existing public transport network is more efficient for one gender group?

### Analysis and results

The data set provides a weighting for people and trips that allows us to make representative statements on the Madrid population from the sample data. All results take the given weights into account.

For detailed information on the analysis see the [Python Jupyter Notebooks on GitHub](https://github.com/CorrelAid/gender-equality-and-mobility).

*1. Can we reproduce the results on gender differences from other studies?*

Short answer: yes. Our results show clear evidence of differing mobility behaviour between men and women, exactly as has been shown in other studies, with women showing trip characteristics typical of ‘trip chaining’ and greater public transport use.

**On average women travel shorter distances than 
men: 6.4 km for women compared to 7.9 km for men.**


{{< image 
    image="20201220_gender_mobility_dist.png"
>}}
{{< /image >}}


**Women rely on public transport and walking more than men.**

Men drive the car for 44% of their trips while women only use it for 35% of their trips. Instead, they walk or use public transport more often than men.

{{< image 
    image="20201220_gender_mobility_modalsplit.png"
>}}
{{< /image >}}

*2. Do we find additional differences with an exploratory analysis?*

Digging further into the data we found a number of other interesting gender differences in mobility behaviour.
**The evening rush hour peak is earlier for working women than men.**

While working men and women show similar travel patterns in the morning, working women show an earlier travel peak in the evening (~3 p.m. compared to ~6 p.m.). This is likely due to the larger share of women working part time, about 25% of women but only 6% of men in Spain (data from 2011,  [European social statistics 2013](https://ec.europa.eu/eurostat/documents/3930297/5968986/KS-FP-13-001-EN.PDF/6952d836-7125-4ff5-a153-6ab1778bd4da)). This may also reflect the added burden of unpaid work that women have to balance (e.g. picking up children from school).


{{< image 
    image="20201220_gender_mobility_rushhour.png"
>}}
{{< /image >}}

**Women between 25 and 55 do more trips on average than men.**
Average trip counts across all ages only differ very slightly (2.7 trips for women vs. 2.6 trips for men), but if the data are additionally age disaggregated we see that working age women (25 to 55) have more trips than men in the same age group. Interestingly, this pattern then flips for people + 55 years. What could explain this pattern?

{{< image 
    image="20201220_gender_mobility_tripcount.png"
>}}
{{< /image >}}

46 % of trips done by women in the age between 25 and 55 are for care purposes / running errands [^2] while for men it’s only 30 %. While the absolute amount of work trips are fairly similar, it only makes up 40% of trips by women compared to 56% by men. 

Mens' absolute trip counts by purpose:

{{< image 
    image="20201220_gender_mobility_motive_m.png"
>}}
{{< /image >}}

Womens’ absolute trip counts by purpose:

{{< image 
    image="20201220_gender_mobility_motive_w.png"
>}}
{{< /image >}}

Women older than 25 do significantly more care trips compared to men. Especially for men the leisure trips peak once they retire. Together with the decreasing care trips of women the average trip count flips.

*3. Can we find evidence that the existing street and public transport network is not accounting as much for female needs as it is for male needs?*

We now know that women and men in Madrid show differing travel patterns, but how well are these different patterns supported by the characteristics of the city, such as street or public transport networks? To investigate this we analysed the travel speed of men and women using different modes of transport, using the straightline distance and start and end time of each trip reported by participants. From the data we see that across all trips women move slower on average than men (11.6 km/h to 13.5km/h). Of course the speed varies with the mode of transport - a car is faster than a bus is faster than walking. But even if we take a look at the single modes the difference remains: On public transport women move 11.3 km/h on average while men move 12.4 km/h. The average speed for car trips is 21.9 km/h for men and 19.7 km/h for women. This suggests that transport networks are better suited for male travel behaviour than for that of women. But we need to be careful with this interpretation! We should take into account that longer trips, like those taken by men as we see in Figure X, can usually be done at faster speeds. Taking the subway four stops does not take twice as long as taking it two stops, as the time it takes to walk to and from the station and wait for the subway does not change. The same is true for cars, where the time to walk to the car and find a parking spot is unrelated to the distance travelled. Indeed we see a strong positive correlation between trip speed and distance in both public transport trips (0.70) and car trips (0.75). 

Once we account for distance we can get a better estimate of how travel speed may differ for men and women across Madrid. Unsurprisingly, we see that men and women walking show similar speeds (~2.8km/h). Similarly, we found that men and women travelling by car have little difference in speed when they’re travelling the same distance (23.5 km/h for males and 23.6 km/h for females). However, women travelling on public transport showed slightly slower travel speeds (13.0 km/h for males 12.7 km/h for females). Large sample sizes, as we have in this survey, can easily produce significant results from very slight differences, but are these differences actually meaningful? The answer to this question does not lie within the statistics but is a matter of interpretation. In our view, this difference is not large enough to support a strong gendered effect of city planning or public transport design for commuters in Madrid. Digging deeper into the data might reveal disadvantaged subgroups, in a similar way that age disaggregation revealed clear patterns in trip count data, though this is purely speculative. 
Speed difference corrected for travel time: There is a slight significant difference for men in women in public transport speed - but significant does not necessarily mean meaningful.

{{< image 
    image="20201220_gender_mobility_speed.png"
>}}
{{< /image >}}


Another indicator for poorer public transport service is the amount of transfers needed for the trip. The hypothesis being: if the public transport network is less suited for needs of women, women will need more transfers on average than men, as less lines connect their origin and destinations directly. This hypothesis does not hold for Madrid as both, men and women, need on average 1.62 transfers. 

### Conclusion of Analysis: 

We can find the prognosed differences between genders in the Madrid data set, but in terms of speed and amount of transfers we cannot find a meaningful differences.
From our analyses we cannot infer a disadvantage for women, which is as a positive result for the Madrid public transport. Yet, we do not claim to have checked all possible disadvantages, e.g. the frequency of connections, or public transport alternatives for routes the car was used for - would the public transport offer a similar suited option for men and women if they were to switch from car to public transport? 
Also, additional factors are relevant for gender equitable infrastructure which have not been considered, including price policy (e.g. pay for distance vs. amount of trips), quality of streets (e.g. as women walk more, likely with strollers or elderly people, so the quality of the pavement is more relevant) or the safety and comfort (e.g. on dark streets or stations).
At this point we would also like to mention that none of us from the team has any domain or expert knowledge on Madrid or Spain, which also limits our ability to draw conclusions.

## What now? General learnings from this analysis.

A good data scientist should be aware that they potentially overlook crucial perspectives in their analyses.   We can never be certain that we have considered all variables or data. We still need to ask:
1. Are all relevant groups represented in the data?
2. Do certain groups within the data need to be looked at specifically?

Gender is an obvious factor to keep in mind but there are many others, such as ethnicity, which we were just recently reminded about, when a twitter thread went viral where zoom did not detect black faces for virtual backgrounds and twitter auto focused on white rather than Black people. There have also been studies showing that especially Black women are misclassified in facial recognition algorithms.  Intersectional feminists state that e.g. Black women have different issues than “just” the issues of women and black people combined and therefore need to be considered additionally. Then there are more genders than male and female, people of different ages, socio-economic backgrounds, disabled people,  … . Our society is diverse and we need to find solutions that account for this diversity.
Educating yourself on potential biases is an important step. Next step is to ensure diverse teams and to make sure future data sets reflect different perspectives, for example by including diverse participants in surveys, usability tests or labeled machine learning data sets. We should also be aware that there is potential harm in analyses and machine learning algorithms and sometimes it might even be better not to proceed with a possibly discriminating analysis or automatisation.

[^1]: We want to acknowledge that there are more than the two genders male and female. Yet, most literature and data sets simplify only using those two. For this blog post we also focus on the difference between men and women, even though we are aware that there are additional issues for non-binary people.

[^2]: “Care” is not a purpose specified within the data set. We recategorized the given options as follows: "Care / errand" consists of *purchases*, *doctor visits*, *escorting another person* and *personal business*. See also [Sánchez de Madariaga & Roberts](https://www.researchgate.net/publication/291932081_Fair_shared_cities_The_impact_of_gender_planning_in_Europe)
