# load packages
library(correltools)
#install by using remotes::install_github('correlaid/correltools')
library(readr)
library(dplyr)
library(htmlwidgets)

chapters <- get_correlaidx_data()
map <- correlaidx_map(chapters)
map %>% saveWidget(file=here::here("static", "html", "map_en.html"))

chapters_de <- get_correlaidx_data('de')
map_de <- correlaidx_map(chapters, 'de')
map_de %>% saveWidget(file=here::here("static", "html", "map_de.html"))
