---
title: "The potential political power of citizens with a migration background: showcasing results from CorrelAid's #tidytuesday inspired challenge"
date: 2021-09-16T11:05:24+01:00
draft: false
image:      "2021-09-16_parliamentJL.png"
imageattribution: "Data visualization by Arndt Leininger and Julius Lagodny"
slug:       "potential-political-power"
summary: "As part of a successful cooperation between [Citizens For Europe](https://citizensforeurope.org/), [Arndt Leininger](https://aleininger.eu/) (long-time member of CorrelAid and assistant professor for political science research methods at Chemnitz University of Technology) and [Julius Lagodny](https://www.juliuslagodny.com/) (PhD candidate in political science at Cornell University), CorrelAid volunteers met up for the first TidyTuesday inspired Challenge to explore different ways to visualize the potential electoral power of people with so-called migration background in Germany."
draft:  false
categories:       
    - education
    - rstats
    - dataviz
    - activism
author: 
    name: "Long and Andreas"
    image:          "correlaid.jpg"
    description:    "
    Long and Andreas are volunteers at CorrelAid. They co-organize the informal CorrelAid TidyTuesday coding hangout which takes place every 2nd and 4th Tuesday per month, where participants can both translate tidied data sets from the [TidyTuesday project](https://github.com/rfordatascience/tidytuesday) into beautiful plots and refine their skills in R or Python data viz. You can join Long and Andreas for the next coding hangout by registering [here](https://pretix.eu/correlaid/tidytuesday/)."
    email: "education@correlaid.org"
meta:
    title: "The potential political power of citizens with a migration background: showcasing results from CorrelAid's #tidytuesday inspired challenge"
    description: "As part of a successful cooperation between [Citizens For Europe](https://citizensforeurope.org/), [Arndt Leininger](https://aleininger.eu/) (long-time member of CorrelAid and assistant professor for political science research methods at Chemnitz University of Technology) and [Julius Lagodny](https://www.juliuslagodny.com/) (PhD candidate in political science at Cornell University), CorrelAid volunteers met up for the first TidyTuesday inspired Challenge to explore different ways to visualize the potential electoral power of people with so-called migration background in Germany."
    image:          "509-2021-02-23-correlaid-strategy.jpg"
    keywords: "data4good, education, correlaid, R, NPO, Zivilgesellschaft"
---


On 9 September 2021, [Citizens For Europe](https://citizensforeurope.org/), an NGO and dear friend of CorrelAid, have published a policy paper entitled "Wähler*innen mit Migrationshintergrund als wahlentscheidender Faktor. Ihr potentieller Einfluss auf die Bundestagswahl 2021". In cooperation with Citizens for Europe, [Arndt Leininger](https://aleininger.eu/) (long-time member of CorrelAid and assistant professor for political science research methods at Chemnitz University of Technology) and [Julius Lagodny](https://www.juliuslagodny.com/) (PhD candidate in political science at Cornell University) have for the first time estimated how influential the voices of people with a migration background can be on the upcoming national elections in Germany. To do so, they used the German micro census to estimate the number of eligible voters with an immigrant background for each of the 299 federal electoral districts. They estimate that the share of eligible voters with a migration background stands at 12.2 per cent of the eligible population, which corresponds to at least 74 seats in the Bundestag. At present, however, only 58 members of the Bundestag have a migration background. Furthermore, it turns out that in many constituencies, eligible voters with a migration background can make the difference: their number in more than half of the constituencies exceeds the number of votes that lie between the first- and second-place direct candidates.

In August, Citizens for Europe, Arndt and Julius had provided their dataset exclusively for CorrelAid's first TidyTuesday inspired DataViz Challenge - a challenge inspired by the [TidyTuesday](https://github.com/rfordatascience/tidytuesday) R community project - organised and hosted by Andreas Neumann and Long Nguyen. The dataset that participants worked with included contained information on the number of eligible voters with a migration background, the number of residents with a migration background overall, the results of the 2017 Bundestag election, and socioeconomic and demographic structural data for each of Germany's 299 constituencies for the national election. The dataset, especially in combination with [shapefiles provided by the Federal Returning Officer](https://www.bundeswahlleiter.de/en/bundestagswahlen/2017/wahlkreiseinteilung/downloads.html), offers a wide range of possibilities for data visualizations.

The participants of the #tidytuesday inspired challenge created a great many data visualizations with a visual "wow" and a political "aha" factor. While some of these visualizations are featured as figures in the policy paper, there were simply to many good visualizations to include them all. Hence, in this blog post, we showcase some of the visualizations that participants created and let their creators explain them. If you want to have a go at the data yourself, it is freely available at [Harvard Dataverse](https://doi.org/10.7910/DVN/GPEV4P). 

## Visualizing the potential electoral power of resident aliens and underage Germans with migration background as a parliamentary group in the Bundestag

{{< image 
    image="2021-09-16_parliamentJL.png"
>}}
{{< /image >}}



This plot, which is also included in the [policy paper](https://vielfaltentscheidet.de/waehlerinnen-mit-migrationshintergrund-als-wahlentscheidender-faktor/), visualizes the potential electoral power of resident aliens who are not (yet?) able to vote because they lack citizenship. More than half of residents in Germany lack citizenship, although many of them have been living in the country for many years or even decades. They might vote in the future if they acquire German citizenship, possibly after regulations have been liberalized or if voting rights are extended to resident aliens. Additionally, there are many Germans with migration background who are simply not yet old enough to vote. They will be able to vote in the future. Both of these groups together represent not yet realized but future potential of residents with a migration background. To visualize this potential, we proceeded as follows: First, we obtained the absolute vote counts for the party lists nationwide ("Zweitstimme) from the official national result of the 2017 Bundestag election. In a second step, we added the number of resident aliens and underage Germans with a migration background to this small dataset. We then calculated the seat distribution that would follow from these numbers in a 598 seat parliament. We chose the minimum size of 598 because it is hard to predict how many seats parliament will comprise after the 2021 election. In making these calculations, we obviously make the grossly simplifying that all these currently non-eligible citizens will be eligible in the future, will all vote and vote for the same party. We make this assumption simply for visualizing the size of the group.

We created the plot using R and the packages `ggplot2` and `ggparliament`. The latter provides the functionality to draw 'parliament plots' that mimic the layout of actual national parliaments, such as the German Bundestag or the UK House of Commons. We have no GitHub repository for the code, but it is available upon request.

*[Julius Lagodny](https://www.juliuslagodny.com/) is a PhD candidate in the Department of Government, Cornell University working on political behavior and public opinion. [Arndt Leininger](https://aleininger.eu/) assistant professor for political science research methods at Chemnitz University of Technology and works on political behavior and applied quantitative methods.*


## The electoral potential of migrant communities-a case study for Germany

{{< image-subtitle 
    image="2021-09-16_neumann.png"
>}}
Please right click on the image and click on "open image in new tab" to get a better view of the subplots.
{{< /image-subtitle  >}}

In this highly hypothetical thought experiment we assume the following:

* there exists a migrant party-all voters with a migrant background share a similar political orientation represented by the migrant party
* all voters of immigrant origin vote for the migrant party (no abstentions)
* only the first votes (“Erststimmen”) were being assessed. With the first vote, an electorate can vote the MP directly into parliament. Hence, the contestant with the highest number of votes wins the seat in parliament

The top left plot portrays the first scenario in which all eligible migrant voters vote for the migrant party. In 4 constituencies, the number of votes given to the migrant party would outnumber the party with the highest share of votes in 2017, namely

Constituency        |Party                                            |No. of votes |Migrant party votes|
|------------------|-----------------------------------|-------------|--------------------|
|Berlin Mitte          | Social Democratic Party (SPD)      | 35036 votes |53602 votes         |
|DuisburgII            |Social Democratic Party (SPD)       | 34799 votes |37339 votes         |
|Frankfurt a. Main I|Christian Democratic Union (CDU)|43663 votes  |58684 votes         |
|Augsburg Stadt    | Christian Social Union (CSU)         |52769 votes   |62766 votes        |

In the second scenario we added non-eligible immigrant voters in our evaluation (i.e. minors). This time, the migrant party would win additional 146 seats. In total:

- 35MPs would represent Baden-Wurttemberg, 
- Bavaria: 14MPs, 
- Berlin: 10MPs, 
- Bremen: 2MPs, 
- Hamburg: 6MPs, 
- Hesse: 18MPs, 
- Lower-Saxony: 8MPs, 
- North Rhine-Westfalia: 45MPs, 
- Rhineland-Palatinate: 8MPs, 
- Saarland: 2MPs 
  and 2MPs would come from Schleswig-Holstein.

You can find the code for the plot [here](https://gist.github.com/anneumann1/ac439481c6e1b01a72d4954f337cd6ec).

*Andreas Neumann is a volunteer at CorrelAid. You can follow Andreas' GitHub [here](https://github.com/anneumann1).*

## Exploring the Migrazensus data 

As I explored the Migrazensus data, as part of August's Correlaid TidyTuesday event, I put together three visualisations showing: 



1. How many people with a "migration background" live in each German region, and the proportion of these people who are eligible to vote;

{{< image-subtitle 
    image="2021-09-16_martin-chris-1.png"
>}}
Please right click on the image and click on "open image in new tab" to get a better view.
{{< /image-subtitle  >}}

2. How the votes of people with a "migration background" translate into seats in the Bundestag;


{{< image-subtitle 
    image="2021-09-16_martin-chris-2.png"
>}}
Please right click on the image and click on "open image in new tab" to get a better view.
{{< /image-subtitle  >}}

3. And, where political parties could gain district seats by winning the votes of more people with a "migration background".

{{< image-subtitle 
    image="2021-09-16_martin-chris-3.svg"
>}}
Please right click on the image and click on "open image in new tab" to get a better view.
{{< /image-subtitle  >}}

[Here is the repo with my R code, graphic design files and a QGIS project](https://github.com/tbk03/tidy_tuesday_correlaid), basically everything I used while exploring the data and producing the visualisations. Sorry the repo is a bit of mess, but I hope it gives some insights into the exploratory processes I apply when visualizing data. It would be a bit misleading if I posted some polished R code, when I tend to use ggplot2 to produce the basis of visualisations before exporting these into graphic design software (Affinity Designer/Publisher at the moment).

*[Dr. Chris Martin](https://twitter.com/analytics_urban) is a researcher and visualisation designer. He conducts research, and produces visualisations, that help people to better understand urban life with all its complexities. His work draws on more than decade of interdisciplinary experience spanning fields including computer science, urban studies and innovation studies.*

## Latitudinal ridgeline plot – proportion of persons with a migration background who are not entitled to vote in the population


{{< image-subtitle 
    image="2021-09-16_ridge_lat_log_bloom.png"
>}}
Please right click on the image and click on "open image in new tab" to get a better view.
{{< /image-subtitle  >}}

A less serious take on exploring the Migrazensus data. This latitudinal ridgeline plot is inspired by some of the more artistic terrain elevation maps. Here, the height of the "peaks" corresponds to the density of persons with a migration background who are not eligible to vote in the population.

Unsurprisingly ¯\\\_ (ツ)_/¯ the constituencies with the highest percentages of non-eligible voters with a migration background are in big cities: Frankfurt am Main I (40.4%), Berlin-Mitte (36.1%), Stuttgart II (35.2%), München-Nord (33.4%), and Leverkusen – Köln IV (32.7%).

You can find the code for this plot [here](https://gist.github.com/long39ng/8924497dd82e2907169e7abf97f7d3aa
). 

*Long Nguyen is a volunteer at CorrelAid and PhD student in sociology at the Leibniz ScienceCampus SOEP RegioHub, Bielefeld University. You can follow Long on [Twitter](https://twitter.com/long39ng).*


## In how many constituencies could eligible citizens with a migration background make a difference?

{{< image-subtitle 
    image="2021-09-16_leininger_ponne.png"
>}}
Please right click on the image and click on "open image in new tab" to get a better view.
{{< /image-subtitle  >}}

This plot, which is also included in the [policy paper](https://vielfaltentscheidet.de/waehlerinnen-mit-migrationshintergrund-als-wahlentscheidender-faktor/), visualizes the potential electoral power of eligible citizens with a migration background in the constituencies ("Erststimme"). About 12% of eligible citizens have a migration background. For each constituency, we checked whether the number of eligible voters with a migration background exceeds the difference in votes between the first and second-placed direct candidates in the last Bundestag election. It turns out that in 167 of 299 constituencies, citizens with a migration background could make the difference who wins or loses a district. We visualize which districts these are on a map. Of course, eligible voters with a migration background could already vote for both the first and the second party, and some of them did, of course. Nevertheless, we include all eligible voters with a migration background, including those who actually voted, in the calculation of the power potential, because it is, of course, possible for the parties to convince both citizens with a migration background who voted or have not yet voted to defend or win a direct mandate. We make these simplifying assumptions to provide an intuitive understanding of the maximum electoral potential of citizens with a migration background.

We created the plot using R and the packages `ggplot2`, `tidyr`, and `sf`. We used `tidyr` to calculate the margin between first- and second-placed party, turning the data from wide to long format and back, and `sf` to read in the [shape files of constituencies provided by Germany's Federal Returning Officer](https://www.bundeswahlleiter.de/en/bundestagswahlen/2021/wahlkreiseinteilung/downloads.html). Finally, we used `ggplot2` to produce the plot. We have no GitHub repository for the code, but it is available upon request.

*[Arndt Leininger](https://aleininger.eu/) assistant professor for political science research methods at Chemnitz University of Technology and works on political behavior and applied quantitative methods. [Bruno Ponne](https://twitter.com/brunoponne) works in the Brazilian parliament and holds a Masters in Public Policy from the Hertie School in Berlin, which is where he got involved with CorrelAid.*




### Interactive Map

{{< iframe 
    src="/html/tidytuesday_challenge_map.html"
    height=600px
>}}
