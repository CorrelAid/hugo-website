---
title: "Gender differences in mobility patterns - an analysis of Madrid"
date:       2021-01-12T00:00:00+02:00
image:      "gender_mobility_header.jpg"
slug:       "gender_bias_and_mobility"
summary: "Data analysis can be gender biased. This article explores how this applies to mobility. We analyzed open mobility data from Madrid to identify differences in mobility behaviour between men and women."
draft:      false
categories:       
    - CorrelAidX
    - Analysis
    - internal project
author: 
    name: "Alexandra, Liam & Marcus"
    image:          "alex_liam_marcus.jpg"
    description:    "[Alexandra](https://twitter.com/lxndrkp), [Liam](https://twitter.com/ldbailey255) and [Marcus](https://www.linkedin.com/in/marcus-vo%C3%9F-5b6944ba/) are part of the local chapter CorrelAid X Berlin. Alexandra is a data analyst in mobility and has been with CorrelAid since 2018. Liam is an ecologist evolving into a data scientist. He's been a member of CorrelAid since late 2019 and using agent-based modelling to study large African carnivores in the rest of my time. Marcus is a PhD student interested in applying machine learning and artificial intelligence to support the energy transition. "
    twitter: "https://twitter.com/correlaid"
    facebook: "https://facebook.com/WeAreCorrelAid"
    github: "https://github.com/correlaid"
    email: "info@correlaid.org"
    website:        "https://www.correlaid.org/"
meta:
    title: "Gender differences in mobility patterns - an analysis of Madrid"
    description: "Data analysis can be gender biased. This article explores how this can occur using mobility data as an example."
    image:          "gender_mobility_header.jpg"
    keywords: "CorrelAidX, Analysis, internal project"
---
## Data analysis is (gender) biased

Data is not objective truth - despite what we data analysts would like to believe. Analyses reflect the perspective from which they were created. If a team is too uniform in their experiences, then the diverse perspectives of different age groups, genders, or ethnicities are easily forgotten. Such bias is often observed in relation to gender, where most analyses focus on the 'default male'[^1], leading to serious, even deadly consequences for women[^2]. For example, crash dummies tend to represent the average male size, which is [one of the reasons why women are more likely to be injured or killed in a crash](https://www.consumerreports.org/car-safety/crash-test-bias-how-male-focused-testing-puts-female-drivers-at-risk/). Women are also more likely to be [misdiagnosed when having a heart attack](https://www.leeds.ac.uk/news/article/4269/women_more_at_risk_of_dying_after_a_heart_attack) because studies have mostly been done with male participants, who show very different symptoms to women. There is a growing awareness of this gender bias in data science, with great books written on this issue by Caroline Criado Pérez[^1], Catherine D'Ignazio and Lauren F. Klein[^3], and Cathy O'Neil[^4].

Having no (or not enough) data about women isn't the only issue: Even if there is data on both men and women, it's often not gender disaggregated which is necessary to reveal gender related differences. For example, gender disaggregated data is necessary to understand gender biases in working hours (including both paid and unpaid work): Gender disaggregated data does not exist for all countries, but in almost all countries where it exists, there is a clear trend that women work longer - on average 50 min more each day (see the [Global Gender Gap Report 2016](http://www3.weforum.org/docs/GGGR16/WEF_Global_Gender_Gap_Report_2016.pdf)). Another example where gender disaggregated data is important is the area of mobility behaviour which we want to investigate closer in this blog post.

## Mobility: an issue of gender bias

**Women "trip chain", men take the car to work during rush hour**

Is mobility gender biased? And if so, how? In most western cultures, women are still responsible for the majority of care work. Bringing children to school, going grocery shopping and taking care of elderly parents. Bias in the distribution of care work also leads to different mobility behaviour: Women do more trip chaining, with many, shorter trips, and greater use of public transport - especially buses. In comparison, a typical "male trip" involves long car trips to and from work during rush hour. This difference in mobility behaviour is reflected in city design and public transport networks, which are usually designed by men with a focus on work-related and rush hour traffic - traffic that is considered to be most important. Connections optimized for the typical male "workforce" with fast connections from residential areas to the city centre, where most offices are located, and poor connections for short trips to kindergartens, schools, supermarkets, and tangential lines to neighbouring residential areas[^5]. This topic is not new to researchers (see, e.g. [the work of Prof. Inés Sánchez de Madariaga](https://unhabitat.org/mobility-of-care-ines-sanchez-de-madariaga)) but in recent years it has gained much greater attention (e.g. [this publication by CIVITAS](https://civitas.eu/sites/default/files/civ_pol-an2_m_web.pdf) or  [this publication by the GIZ](https://www.connective-cities.net/en/media-centre/publications/publications-details/gender-and-urban-transport-1)).

## A closer look at Madrid's mobility data

### An internal CorrelAid project

The city of Madrid offers a large and detailed mobility data set, published by the Consorcio Regional de Transportes de Madrid (CRMT) in 2018. Unlike other cities and countries, Madrid has published the data as open data allowing us to investigate gender biases in mobility. About 85.000 people each reported their trips over the course of a day, including mode, motive, origin and destination, combined with demographic data. Find the documentation (Spanish) [here](https://www.crtm.es/media/712934/edm18_sintesis.pdf) and the data set [here](https://crtm.maps.arcgis.com/apps/MinimalGallery/index.html?appid=a60bb2f0142b440eadee1a69a11693fc).
Within our team, we wanted to use this as an opportunity to analyze the data and answer the following questions:
1. Can we reproduce the results on gender differences from other studies?
2. Do we find additional differences with an exploratory analysis?
3. Can we find evidence that the existing public transport network is more efficient for one gender group?

### Analysis and results

The data set provides a weighting for people and trips that allows us to make representative statements on the Madrid population from the sample data. All results take the given weights into account.

For detailed information on the analysis see the [Python Jupyter Notebooks on GitHub](https://github.com/CorrelAid/gender-equality-and-mobility).

*1. Can we reproduce the results on gender differences from other studies?*

Short answer: yes. Our results show clear evidence of differing mobility behaviour between men and women, exactly as shown in other studies, with women showing trip characteristics typical of 'trip chaining' and greater public transport use.

**On average women travel shorter distances than 
men: 6.4 km for women compared to 7.9 km for men.**


{{< image-no-border
    image="20201220_gender_mobility_dist.png"
>}}
{{< /image-no-border >}}


**Women rely on public transport and walking more than men.**

Men drive the car for 44% of their trips while women only use it for 35% of their trips. Instead, they walk or use public transport more often than men.

{{< image-no-border
    image="20201220_gender_mobility_modalsplit.png"
>}} 
{{< /image-no-border >}}

*2. Do we find additional differences with an exploratory analysis?*

Digging further into the data, we found several other interesting gender differences in mobility behaviour.

**The evening rush hour peak is earlier for working women than working men.**

While working men and women show similar travel patterns in the morning, working women show an earlier travel peak in the evening (~3 p.m. compared to ~6 p.m.). This is likely due to the larger share of women working part-time, [about 25% of Spanish women but only 6% of Spanish men](https://ec.europa.eu/eurostat/documents/3930297/5968986/KS-FP-13-001-EN.PDF/6952d836-7125-4ff5-a153-6ab1778bd4da). This may also reflect the added burden of unpaid work that women have to balance (e.g. picking up children from school).


{{< image-no-border
    image="20201220_gender_mobility_rushhour.png"
>}}
{{< /image-no-border >}}

**Women between 25 and 55 make more trips on average than men.**

Average trip counts across all ages only differ very slightly (2.7 trips for women vs. 2.6 trips for men), but if the data are additionally age-disgregated, we see that working-age women (25 to 55) have more trips than men in the same age group. Interestingly, this pattern then flips for people over 55. What could explain this pattern?

{{< image-no-border
    image="20201220_gender_mobility_tripcount.png"
>}}
{{< /image-no-border >}}

46 % of trips done by women aged between 25 and 55 are for care purposes / running errands [^6] while for men, it's only 30 %. While the absolute amount of work trips are fairly similar, it only makes up 40% of trips by women compared to 56% by men. 

{{< image-no-border
    image="20201220_gender_mobility_motive.png"
>}}
{{< /image-no-border >}}


Women older than 25 make significantly more care trips compared to men. Especially for men, the leisure trips peak once they retire. Together with the decreasing care trips of women, the average trip count flips.

*3. Can we find evidence that the existing public transport network is more efficient for one gender group?*

We now know that women and men in Madrid show differing travel patterns, but how well are these different patterns supported by the city's characteristics, such as street or public transport networks? To investigate this, we analyzed the travel speed of men and women using different modes of transport, using the straight-line distance and start and end time of each trip reported by participants. From the data, we see that across all trips, **women move slower on average than men (11.6 km/h to 13.5km/h).** 

**Of course, the speed varies with the mode of transport** - a car is faster than a bus, which is faster than walking. But even if we take a look at the single modes the difference remains: **On public transport women move 11.3 km/h on average while men move 12.4 km/h. The average speed for car trips is 21.9 km/h for men and 19.7 km/h for women.** This suggests that transport networks are better suited for male travel behaviour than for that of women. 
But we need to be careful with this interpretation! We should take into account that longer trips, like those taken by men as we see in the first figure, can usually be done at faster speeds. Taking the subway four stops does not take twice as long as taking it two stops, as the time it takes to walk to and from the station and wait for the subway does not change. The same is true for cars, where the time to walk to the car and find a parking spot is unrelated to the distance travelled. **Indeed we see a strong positive correlation between trip speed and distance in both public transport trips (0.70) and car trips (0.75)**. 

Once we account for distance, we can better estimate how travel speed may differ for men and women across Madrid. Unsurprisingly, we see that men and women walking show similar speeds (~2.8km/h). Similarly, we found that men and women travelling by car have little difference in speed when travelling the same distance (23.5 km/h for males and 23.6 km/h for females). 

**However, women travelling on public transport showed slightly slower travel speeds (13.0 km/h for males 12.7 km/h for females)**. Large sample sizes, as we have in this survey, can easily produce significant results from very slight differences, but are these differences actually meaningful? The answer to this question does not lie within the statistics but is a matter of interpretation. **In our view, this difference is not large enough** to support a strong gendered effect of city planning or public transport design for commuters in Madrid. Digging deeper into the data might reveal disadvantaged subgroups, in a similar way that age disaggregation revealed clear patterns in trip count data, though this is purely speculative. 

{{< image-no-border
    image="20201220_gender_mobility_speed.png"
>}}
{{< /image-no-border >}}


Another indicator for poorer public transport service is the amount of transfers needed for the trip. The hypothesis being: if the public transport network is less suited for the needs of women, women will need more transfers on average than men, as fewer lines connect their origin and destinations directly. This hypothesis does not hold for Madrid as both, men and women, need on average 0.62 transfers. 

**No strong evidence for gender differences in speed or transfers were found.**

### Conclusion of Analysis: 

We observed many of the expected differences between genders in the Madrid data set, but did not find meaningful differences in terms of speed and amount of transfers.
**Our analyses do not show a clear disadvantage for women, which is as a positive result for the Madrid public transport network. Yet, we do not claim to have checked all possible disadvantages**, e.g. the frequency of connections, or public transport alternatives for routes the car was used for - would public transport offer a similar suited option for men and women if they were to switch from car to public transport? 
Other factors are also relevant for gender equitable infrastructure which have not been considered here, including price policy (e.g. pay for distance vs. the amount of trips), quality of streets (e.g. as women walk more, likely with strollers or elderly people, so the quality of the pavement is more relevant) or safety and comfort (e.g. on dark streets or stations).
At this point, we would also like to mention that none of us from the team has any domain or expert knowledge on Madrid or Spain, which also limits our ability to draw conclusions.

## What now? General learnings from this analysis.

A good data scientist should be aware that they potentially overlook crucial perspectives in their analyses.   We can never be certain that we have considered all variables or data. We still need to ask:
1. Are all relevant groups represented in the data?
2. Do certain groups within the data need to be looked at specifically?

Gender is an obvious factor to keep in mind when analysing data, but there are many others, such as ethnicity, which we were just recently reminded about when a Twitter thread went viral where Zoom did not detect black faces for virtual backgrounds and Twitter auto-focused on white rather than Black people. 
There have also been studies showing that [Black women are especially likely to be misclassified in facial recognition algorithms](https://venturebeat.com/2020/09/24/in-facial-recognition-challenge-top-ranking-algorithms-show-bias-against-black-women/). 
Intersectional feminists state that particular sub-groups, such as Black women, have different issues than "just" the issues of women and Black people combined and therefore need to be considered additionally.
Our society is diverse, and we need to find solutions that account for diversity in characteristics such as genders (more than just male and female), age, socio-economic background, and disability.

Educating yourself on potential biases is an important step. The next step is to ensure diverse teams and to make sure future data sets reflect different perspectives, for example, by including diverse participants in surveys, usability tests, or labelled machine learning data sets. We should also be aware that there is potential harm in analyses and machine learning algorithms. Sometimes, it might even be better not to proceed with a possibly discriminating analysis or automatization all together.

[^1]: Criado Pérez, C. Invisible Women: Data Bias in a World Designed for Men. New York, USA: Vintage. 2019.

[^2]: We want to acknowledge that there are more genders than male and female. Yet, most literature and data sets only take those into account. For this blog post, we also focus on the difference between men and women, even though we are aware that a) other genders exist and b) that there potentially are additional issues for non-binary people.

[^3]: D'Ignazio, C. & Klein, LF. Data Feminism. Cambridge, USA: MIT Press. 2020.

[^4]: O'Neil, C. Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy. New York, USA: Crown. 2016

[^5]: de Madariaga, I.S. Mobility of Care: Introducing New Concepts in Urban Transport. In: de Madariaga, I.S. & Roberts M., (eds.). Fair shared cities: The impact of gender planning in Europe. Farnham, UK: Ashgate Publishing, 2013. pp. 33 - 48.

[^6]: "Care" is not a purpose specified within the data set. We categorized a trip as  "Care / errand" if it included *purchases*, *doctor visits*, *escorting another person* and *personal business*. See also [Sánchez de Madariaga & Zucchini](https://www.researchgate.net/publication/330905894_Measuring_Mobilities_of_Care_a_Challenge_for_Transport_Agendas_From_One_to_Many_Tracks) on measuring travel associated with care tasks.

