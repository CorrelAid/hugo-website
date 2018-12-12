---
title: "From the data to the story"
date: 2017-10-28T00:00:00+02:00
image: "509-data-to-story.jpg"
summary: "Journocode: A typical DDJ workflow in R"
author: "Marie-Louise"
categories:       
    - Data Science
    - R
    - Data Journalism
author: 
    name:           "Marie-Louise Timcke (Journocode)"
    image:          "marie-louise-t.jpg"
    description:    "Marie-Louise Timcke is co-founder of journocode.com and now works for the interactive branch of the Berliner Morgenpost. Journocode consists of enthusiastic journalists and computer scientists trying to close the gap between journalism and data science and help other enthusiasts learn to do so, too. They also offer workshops on workshops.journocode.com."
    twitter:        "https://twitter.com/@journocode"
    facebook:       ""
    github:         ""
    email:          "contact@journocode.com"
    website:        "https://journocode.com"
meta:
  title: "CorrelAid - From the data to the story"
  description: "R is getting more and more popular among Data Journalists worldwide, as Timo Grossenbacher from SRF Data pointed out in a talk at user!2017 conference in Brussels."
  image: "509-data-to-story.jpg"
  keywords: "CorrelAid, Data Journalism, journocode"
---


R is getting more and more popular among Data Journalists worldwide, as
Timo Grossenbacher from SRF Data pointed out in a [talk at user!2017
conference](https://channel9.msdn.com/Events/useR-international-R-User-conferences/useR-International-R-User-2017-Conference/The-growing-popularity-of-R-in-data-journalism)
in Brussels. Working as a data trainee at [Berliner Morgenpost’s
Interactive Team](https://www.morgenpost.de/interaktiv/), I can confirm
that R indeed played an important role in many of our lately published
projects, [for example when we identified the strongholds of German
parties](https://interaktiv.morgenpost.de/parteien-hochburgen-deutschland/).
While we also use the software for more complex statistics from time to
time, something that R helps us with on a near-daily basis is the act of
cleaning, joining and superficially analyzing data. Sometimes it’s just
to briefly check if there is a story hiding in the data. But sometimes,
the steps you will learn in this tutorial are just the first part of a
bigger, deeper data analysis.

So the following tutorial will guide you through the standard steps I
always take when getting the data for a new data driven project at the
Morgenpost. For this exemplary data journalism R workflow, we’ll have a
look at data from [BBSR Germany](http://inkar.de/). As always, you’ll
find the data and the (less well-commented) code on our [GitHub
page](https://github.com/journocode/rstats_ddj_workflow). This time, the
R script is organized as an *R Project*, which makes collaboration
easier because the working directory is automatically set to the
directory where the *Rproj* file is located. A double click on the
*Rproj* file opens a new RStudio Window that is already set to the right
working directory of the analysis. Then you can open the R script as
usual.

I always subdivide my R scripts into three parts:

**Head:** The part where I load packages and data

**Preprocessing:** The part where I clean and, well, preprocess the data
for analysis

**Analysis:** The part where I analyze the data

The three parts don’t necessarily have to be in the same script. To make
the analysis cleaner, you could save the head and preprocessing in a
separate R-file that can either be sourced in the beginning of the
analysis script or have the preprocessed data saved as a new data source
that can be loaded in the analysis script.


**Head**

Enough talk! Let’s start with loading the packages we need for our
analysis

```r
# R
#install.packages("needs")
#library(needs)
needs(readxl,tidyr,dplyr,ggplot2,magrittr)
```

Next, we need to load the data. For this example, I prepared an Excel
Worksheet with two data sheets. Both contain data on Germany’s 402 city
districts. We have the unique district ID and the district name as well
as information on whether the district is a county or a city district.
The first Excel sheet contains the average age of the district’s male
population, the second contains the same data for the female population.


**Preprocessing**

Now that we have the data, we have to do a little preprocessing. We want
to merge both dataframes into one that contains the age of the male and
female population for each district. Let’s have a look at the frames to
check whether we can do the merge:

```r
# R
# Load the two data sheets into two different data variables:
# Example if your data is in a CSV: file <- read.csv("file.csv", sep=",", dec=";", fileEncoding="latin1", na.strings="#")
age_male <- read_excel("age_data.xlsx", sheet=1)
age_female <- read_excel("age_data.xlsx", sheet=2)
```


We have two findings:

-   The dataframes aren’t sorted in the same way and the column names
    aren’t the same either. Luckily, the order isn’t important for the
    merge. We’ll get there later.
-   *age\_female* has more rows than *age\_male* and more rows than
    there are german districts. What’s the reason for this?

Maybe there are duplicated rows:

```r
# R
head(age_male) # check the first rows of the male age data
head(age_female) # check the first rows of the female age data
# check the number of rows
nrow(age_male)
nrow(age_female)
```

Great, we just had to remove some duplicated rows. Now, let’s merge the
dataframes! If they were ordered in exactly the same way, we could use
the function cbind() to simply add the age column of *age\_female* to
*age\_male*. But because the order isn’t the same, we have to use
*merge()*. *merge()* joins dataframes according to a column containing
unique values that both have in common. For our example, the unique
district ID seems to be the best choice. Because we just want to add the
age column of *age\_female* and not all its columns, we only select its
first and fourth column by indexing *age\_female\[c(1,4)\]*. Then we
have to tell *merge()* the name of the matching column with the
parameters *by.x* for the first and *by.y* for the second dataframe. If
the matching columns had the same name, we could just use the parameter
*by*.

```r
# R
# merging
age_data <- merge(age_male, age_female[c(1,4)], by.x="district_id", by.y="dist_id")
head(age_data) # looks good!
```

P.S.: Merging also works with data frames of different lengths. In that
case, you can specify whether you want to keep unmatchable rows. Type
*?merge* into the R console for more information.

Now for the tidyverse: We want the columns *average\_age\_males* and
*average\_age\_females* to be converted into one column containing the
variables name and one containing the matching values. With the
parameter *key*, we tell *gather()* what the new column with the
attribute names should be called. We give value the new column name for
the values and then specify the columns that should be gathered by
applying the columns’ indexes.

```r
# R
# tidyverse
age_data <- gather(age_data, key=key, value=age, 4:5)
head(age_data) # that's what I call tidy!
```

By the way: *1:3* is just the same as *c(1,2,3)*.

**Analysis**

As mentioned before, a very nice package that’s great for getting a
first overview of your data is *dplyr*. Like *tidyr*, it’s a package by
Hadley Wickham and designed to work well with the tidy data format.

Let’s get an overview of our data by filtering and summarizing the
values:

```r
# R
# Summarize the data to get the average age in Germany
age_data %>% summarize(mean=mean(age))
# Now group by the column key to get the average age for males and females in Germany
age_data %>% group_by(key) %>% summarize(mean=mean(age))
# In the same way, we can group by other columns, for example:
age_data %>% group_by(city_county) %>% summarize(mean=mean(age))
# Now calculate the average age per district. But instead of summarizing, save the result in a new column.
# This time, save the new dataset as a variable in the R environment
age2 <- age_data %>% group_by(district_id) %>% mutate(district_mean=mean(age))
head(age2)
# We now want to find the youngest cities of Germany.
# We won't need the columns key and age for that. We remove those columns and then reduce the dataset to the unique rows
age2 %<>% select(-c(4,5)) %>% unique()
head(age2)
# Now, use filter to only keep the cities, not the counties and arrange the dataset in descending order according to the district_mean
youngest_cities <- age2 %>% filter(city_county %in% "city") %>% arrange(district_mean)
head(youngest_cities)
# Next, we only want to have a look at bavarian cities, whose district IDs all start with "09". A great base function
# called startsWith() can easily find all district IDs that start with certain characters:
youngest_cities %>% filter(startsWith(district_id, "09"))
# Let's find the oldest bavarian city
youngest_cities %>% filter(startsWith(district_id, "09")) %>% arrange(desc(district_mean))
```

See how *dplyr* makes it really easy to have a look at different aspects
of your data by just combining different functions? You can even easily
answer questions that seem a little bit more difficult at first, as long
as you know your R functions. This is something that won’t be as simple
with tools like Excel.

For example: *Let’s find the youngest city for every German state*

The states have unique IDs, represented by the first two numbers of the
district ID. So we have to group the data by the first two numbers of
*district\_id*, then only select the row in each group with the minimum
value in *district\_mean*. To make this specific grouping possible, we
need help from the base function *substr()*. To check out how it works,
just type *?substr* into your console.

Finally, arrange the data in ascending order according to the
*district\_mean*.

```r
# R
youngest_cities %>% group_by(state=substr(district_id, 1, 2)) %>%
filter(district_mean %in% min(district_mean)) %>% arrange(district_mean)
```


**Visualize**

We’ve now found out a lot about our data by simply filtering,
summarizing and arranging it. But sometimes, a simple visualization
helps a lot in finding patterns, too. In a [previous
post](http://journocode.com/2016/03/02/r-the-ggplot2-package/), we
already explained how *ggplot2* works. This is why this time, we’ll go a
step further and plot the data as a static choropleth map using the
package. The following guide is just one possible approach to such a
map.

First, we need some geodata. It can be provided in different formats,
for example as a GeoJSON. In this example, we have an ESRI Shapefile of
Germany’s city and county districts. An ESRI Shapefile contains multiple
files that have to be stored in the same directory. Nevertheless, we
only will load the SHP file into R using *rgdal’s readOGR()*.


```r
# R
needs(rgdal,broom)
krs_shape <- readOGR(dsn="krs_shape/krs_shape_germany.shp", layer="krs_shape_germany", stringsAsFactors=FALSE, encoding="utf-8")
```

*krs\_shape* basically consists of two parts: A dataframe in
*krs\_shape@data* and the geographic information in
*krs\_shape@polygons*. The dataframe has a column *KRS* containing the
very same unique district IDs as our age dataframe. We could merge the
dataframes, plot the shapefile and colorize the plot according to the
age values. But, as always, I like to work with tidy data. This is why
we’ll loaded the package *broom* before. If you take a look at the
shapefile…

```r
# R
head(krs_shape)
head(krs_shape@data)
head(krs_shape@polygons)
```

…you may understand why I’d like to keep the data a little bit more
simple. *broom’s tidy()*-function simplifies the geodata:

```r
# R
head(tidy(krs_shape))
```

Much better! We now have one row per polygon point and group IDs so we
know which points belong to the same shape. But we have a loss of
information here, too: **Where’s the district ID?** The district ID is
swept away by *broom*. We still have IDs though, starting at zero and
identifying the districts in the same order as they appeared in
*krs\_shape@data*. So “Schweinfurt” now has id=0 and “Würzburg” id=1.
There may be a simpler way to work around this problem, but here is what
I usually do:

In the first step, I save the shapefiles’ district IDs as numerics in a
new variable

```r
# R
shape_district_ids <- as.numeric(krs_shape$KRS)
```

Next, I arrange my dataframe to match the order of the IDs in the
shapefile, then add new IDs from 0 to 401 that will match the tidied
shapefile IDs:

```r
# R
age2 %<>% arrange(match(as.numeric(district_id), shape_district_ids))
age2$id <- 0:401
```

Now I merge the tidied shapefile with my data by the new ID. It is
important to not lose any shapefile rows while merging and keep the
*plott order* straight, so be sure to set *all.x* to *TRUE* and arrange
in ascending order according to the ID column.


```r
# R
plot_data <- merge(tidy(krs_shape), age2, by="id", all.x=T) %>% arrange(id)
head(plot_data)
```

This is our final plotting data. Every point of each district’s
shapefile now has additional information like the district’s average
age. Let’s plot this data with *ggplot2*!

Because we already explained how ggplot basically works in a [previous
post](http://journocode.com/2016/03/02/r-the-ggplot2-package/), I’ll
only comment the code for the choropleth:

```r
# R
cols <- c("#e5f5e0","#c7e9c0","#a1d99b","#74c476","#41ab5d","#238b45", "#006d2c","#00441b") # set individual color scheme
ggplot(data=plot_data, aes(x=long, y=lat, group=group)) + # never forget the grouping aestethic!
geom_polygon(aes(fill=district_mean)) +
theme_void() + # clean background theme
ggtitle("Average Age of Germanys districts") +
theme(plot.title = element_text(face="bold", size=12, hjust=0, color="#555555")) +
scale_fill_gradientn(colors=cols, space = "Lab", na.value = "#bdbdbd", name=" ") +
coord_map() # change projection
```

And this is what the result should look like:



{{< image 
    image="509-jcgermany.png"
>}}
Polymap Germany
{{< /image >}}


Of course, our analyzed example data isn’t a data story treasure. The
old eastern Germany might be a story, one of our arranged lists might
be, too. Or the results just gave you a hint where to dig deeper.
Whatever conclusions you draw from your brief data analysis with R: It
was brief! With the few R methods we’ve shown you today, it won’t take
you much time to be able to draw the first important conclusions from
any given data.

As always, you’ll find the entire code for this example on [our GitHub
page](https://github.com/journocode/rstats_ddj_workflow). If you have
any questions, suggestions or feedback, feel free to leave a comment!
We’ll try to answer fast.

*This post originally was published on journocode.com. We are very
grateful that the team has allowed us to cross-post this very insightful
post on our blog. You can find the original blog post
[here.](http://journocode.com/2017/08/16/datajournalism-workflow-ddj-r-rstats-rstudio-dplyr-ggplot2-tidyr/)*

------------------------------------------------------------------------


