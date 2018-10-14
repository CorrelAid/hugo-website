---
 title: "Spatial Analysis of Airplane Accidents"
 date: 2017-10-14T00:00:00+02:00
 image: map_usa2.png
 summary: "Employing a Point Pattern Analysis on the Case of Florida"
 author: "Lisa"
---


Technological advances, increased safety standards and a greater
importance of risk management led to a decreasing number of airplane
accidents over the last decades. Despite these improved conditions,
however, accidents still occur, be it due to human error, mechanical
failure or further causes.

Inspired by the seminal work of Clarke (1946) on the distribution of V-2
rockets strikes on London during World War II, this blog post seeks to
identify the spatial pattern of airplane accidents that happened in
Florida in 2014 by employing a basic point pattern analysis. By
visualizing and analyzing the accidents’ geographical distribution, it
is assessed whether spatial patterns pointing towards risk-inducing
contextual factors, e.g., a high traffic density or unfavourable
environmental conditions, were present.

**Data and Methods**

Data on all airplane accidents for the subsequent spatial analysis were
obtained from the National Transportation Safety Board (NTSB) [aviation
accident
database](https://www.ntsb.gov/_layouts/ntsb.aviation/index.aspx).
Generally speaking, the NTSB compiles data on both commercial and
general aviation accidents for the United States and its territories
from 1962 onwards along with contextual information on, e.g., the number
of injuries and fatalities or weather conditions. The precise locations
of the accidents are identified by their respective latitude and
longitude coordinates in degrees and decimal degrees.

Information on geographical borders for 2014 were obtained from the
[Census Bureau’s MAF/TIGER geographic
database](https://www.census.gov/geo/reference/gtc/gtc_maftiger.html)
which provides cartographic boundary files on various administrative
levels. For both the visualizations and all spatial analyses, the
nation-based shapefiles for the state-level were chosen and cropped to
the geographic extent of Continental US and Florida, respectively.

The analysis proceeds as follows. In the first step, all airplane
accidents in Florida are visualized as two-dimensional maps. In the
second step, a point pattern analysis is conducted. Following the
recommendations of Baddeley et al. (2015), the PPA starts with analyzing
the first-order properties of the point pattern, i.e., the spatial
distribution of the events under scrutiny. For this purpose, the density
of the observed accidents is computed and visualized by employing
quadrat counting methods and kernel density estimation to account for
the non-constant intensity of the point process. Subsequently, the
second-order properties of the point pattern, i.e., the spatial
interactions between events, are examined. In doing so, the observed
point pattern is compared with both random and regular samples to
determine whether the spatial pattern resulted from a complete spatial
randomness (CSR) process, that is, if the observed events within the
study area are distributed at random. Moreover, Ripley’s reduced second
moment function K(r) is computed to formally assess whether there are
interactions between accidents, given the inhomogeneity of the point
process.

All spatial analyses and visualizations were carried out in the R
software environment for statistical computing and graphics (version
3.2.3). Replication data and R scripts can be retrieved from [the
author’s GitHub
page](https://github.com/lhehnke/aircrash-analysis-data).

**Results**

In order to visualize the spatial pattern, all airplane accidents were
coded and stored as spatial points. Several accidents occurred close to
but not within the state borders of Florida and were excluded from the
analyses by taking a geographic subset of all points lying inside the
boundary of the Florida polygon. For aesthetic reasons, an unprojected
map using latitude and longitude coordinates was chosen.

As can be seen in figure 1, a total number of N=76 airplane accidents
occurred. By looking at the map, accidents seem to cluster along the
East Coast and in Central Florida, respectively, whereas fewer accidents
seem to happen in North and South Florida.

\
![](airplanes1.jpg){.img-responsive
.no-border}*Figure 1: Accidents seem to cluster along the East Coast and
in Central Florida.*\
\

While visualizations provide a first insight into the spatial
distribution of events, they do not suffice for (dis-)confirming spatial
clustering hypotheses due to the so-called clustering illusion, i.e.,
the tendency to erroneously perceive random events as clustered
(Gilovich et al. 1985).

To address this problem, a point pattern analysis (PPA) was employed
which required two modifications of the spatial data. First, the
projection was changed from unprojected longitude and latitude
coordinates to an equal-area projection (Albers equal-area conic) to
minimize distortions. Second, the spatial points were transformed into a
two-dimensional spatial point pattern object containing information
about the observation window.

A basic step of PPA is to investigate the intensity (<U+03BB>) of the spatial
point pattern, i.e., the average number of events per unit. <U+03BB> can either
be homogeneous or inhomogeneous, depending on whether the number of
events varies across the area being studied. When dealing with airplane
accidents, contextual factors leading to variations in the spatial
distribution of these accidents will most likely be present, be it
demographic, environmental or regulatory characteristics. Hence, the
intensity of accidents will not be constant across space but rather vary
spatially.

To assess whether the intensity of accidents is indeed (non-)constant,
the so-called quadrat counting technique can be applied (see, e.g.,
Diggle 2014: 29-32). The rationale behind quadrat counting is to
partition the study area into a certain number of equal-sized quadrats
and count the number of events being located within each quadrat. If the
intensity is homogeneous, the number of events within each quadrat
should, approximately, be the same.

\
![](airplanes2.jpg){.img-responsive
.no-border}*Figure 2: The intensity of the point process is
inhomogeneous.*\
\
Figure 2 indicates that the intensity of the point process is
inhomogeneous since the number of airplane accidents varies spatially.
With regard to the spatial distribution of the depicted quadrats,
accidents seem to occur more often in Central Florida, whereas fewer
accidents happen in Northern Florida. However, a major drawback of the
quadrat counting technique is its sensitivity to the number and size of
the plotted quadrats which are user-defined and, thus, arbitrarily
chosen.

Nonparametric kernel density estimation offers a fruitful solution to
this problem. For estimating the intensity of the point process by means
of kernel smoothing, an isotropic Gaussian kernel was used. As with the
quadrat counts approach, one drawback of this method is that the kernel
estimator is sensitive to the selected bandwidth. Following Diggle
(1985), the bandwidth was chosen to minimise the mean square error of
the kernel smoother. As indicated by the lighter areas in figure 3,
there are several accident hotspots in Central Florida and along the
eastern coastline of Florida.

\
![](airplanes3.jpg){.img-responsive
.no-border}*Figure 3: There are several accident hotspots in Central
Florida and along the eastern coastline of Florida.*\
\
After assessing the first-order properties, PPA proceed with testing
whether events tend to cluster spatially. By employing nonparametric
distance functions, it can be analyzed if the observed spatial pattern
is the result of a CSR process, which disconfirms clustering hypotheses.
In other words, if spatial clustering of accidents is present, they did
not occur (geographically) at random. However, while spatial variations
of airplane accidents are to be expected, spatial clustering of airplane
accidents should not necessarily be present in the data as the
occurrence of an airplane accident – at least in most cases – neither
increases nor decreases the propability of other accidents happening
nearby.

\
![](airplanes4.jpg){.img-responsive
.no-border}*Figure 4: From Left to Right: (a) Observed points, (b)
Random points, (c) Regular points.*\
\
One common testing procedure is to plot the observed points, i.e.,
accidents, within the study alongside sampled random and regular points
(see, e.g., Bivand et al. 2008). For the sampled point locations, the
sample size was chosen to match the number of observed points (N=76). If
spatial clustering were present in the accident data, substantial
differences should be visible when comparing the observed pattern to
both random and regular point patterns. As can be seen in figure 4, the
observed point pattern does not resemble a regular pattern. Still,
clustering cannot be ruled out (or confirmed, for that matter) by means
of these visual inspections only.

Distance functions, on the other hand, provide a more formal approach to
testing whether spatial clustering occurs or not. The rationale is to
compare the observed empirical values to theoretically expected values
under CSR. Since conventional distance functions (i.e., the nearest
neighbour distance distribution function, the empty space function or
Ripley’s reduced second moment function) assume homogeneity of the point
process and are estimated under the assumption of the intensity of the
events being constant across the study area, a generalisation of
Ripley’s K function (1977) for inhomogeneous point patterns was
computed.

\
![](airplanes5.jpg){.img-responsive
.no-border}*Figure 5: A statistically significant clustering of airplane
accidents occurred only at smaller distances.*\
\
The plotted K function in figure 5 shows that a statistically
significant clustering of airplane accidents occurred only at smaller
distances, whereas the empirical values Kˆ(r) at greater distances lie
close to the expected values K(r) under CSR within the (simulated)
envelope. Generally speaking, empirical values above the envelope would
indicate a clustered distribution of the spatial points, while empirical
values below the envelope would indicate a regular, i.e., dispersed,
pattern. Thus, at best, only a marginal clustering of airplane accidents
seems to be present, which is line with the preceding results.

**Conclusion**

The main objective of this blog post was to identify the spatial pattern
of airplane accidents that occurred in Florida in 2014. In a nutshell,
the results of the spatial analyses indicate that while the average
number of airplane accidents per unit area varies spatially, only a
marginal clustering of accidents was found with hotspots being in
Central Florida and along the East Coast, respectively. However, these
empirical findings should only serve as a point of departure for more
advanced future analyses taking both covariates (e.g., causes of
accidents, traffic volumes or air networks) and the temporal dimension
of airplane accidents into account.

**Literature**

Baddeley, A., Rubak, E., & Turner, R. (2015). Spatial Point Patterns:
Methodology and Applications with R. London: Chapman and Hall/CRC Press.

Bivand, R. S., Pebesma, E., & Gómez-Rubio, V. (2008). Applied Spatial
Data Analysis with R. 2nd edition. New York: Springer.

Clarke, R. D. (1946). An application of the Poisson distribution.
Journal of the Institute of Actuaries, 72, 481.

Diggle, P. J. (1985). A kernel method for smoothing point process data.
Applied Statis- tics, 34(2), 138-147.

Diggle, P. J. (2014). Statistical Analysis of Spatial and
Spatio-Temporal Point Patterns. 3rd edition. Boca Raton: CRC Press.

Gilovich, T., Vallone, R., & Tversky, A. (1985). The hot hand in
basketball: On the misperception of random sequences. Cognitive
Psychology, 17(3), 295-314.

Ripley, B. D. (1977). Modelling spatial patterns. Journal of the Royal
Statistical Society, Series B (Methodological), 39(2), 172-212.

------------------------------------------------------------------------


