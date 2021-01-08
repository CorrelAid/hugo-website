# load packages
library(tidyverse)
library(CoordinateCleaner)
library(readr)
library(rvest)
library(sf)
library(leaflet)
library(tmaptools)
library(htmltools)
library(here)
library(htmlwidgets)

# FUNCTIONS --------
## crawling lc-chapters from CorrelAid-Website with package rvest
# correlaid website

get_data <- function(base_url) {
  base_url <- base_url
  h <- read_html(
    base_url
  )
  
  # lc-names
  lc_nodes <- h %>%
    html_nodes("a.nav-item.nav-link.active") 
  
  lc_names <- lc_nodes %>% html_text()
  
  # lc-urls 
  lc_urls <- lc_nodes %>% 
    html_attr("href")
  
  
  # data frame
  lc <- tibble(name = lc_names, url = lc_urls) %>% 
    filter(!grepl("\\n", name)) %>% 
    distinct() %>% 
    mutate(content = (glue::glue("<b><a target='_parent' href='{url}'>{name}</a></b>"))) 
  lc
}

# Plotting with leaflet (clustering)
cax_leaflet_map <- function(data) {
  leaflet(data) %>%
    addProviderTiles(providers$CartoDB.Positron) %>%
    addMarkers(icon = correlaidxicon,
               label = ~as.character(name),
               popup = ~(content))
}



# COMMON PREP --------
# creating a custom icon
correlaidxicon <- makeIcon(
  iconUrl = "https://gblobscdn.gitbook.com/spaces%2F-MMQj6Rqry0D6V-FfMJP%2Favatar-1605792600232.png",
  iconWidth = 30, iconHeight = 30,
  iconAnchorX = 30, iconAnchorY = 30
)

# centroids of regions (manualy)
regions <- tibble(name = c("Ruhrgebiet", "Rhein-Main"),
                  lat = c(51.5, 50.1),
                  lng = c(7.5, 8.7),
                  iso2 = c("DE", "DE"))
#source: Ruhrgebiet: https://geohack.toolforge.org/geohack.php?pagename=Ruhr&params=51_30_N_7_30_E_region:DE_type:city
# Rhein-Main: https://geohack.toolforge.org/geohack.php?pagename=Frankfurt_Rhine-Main&params=50.1_N_8.7_E_scale:1000000_region:DE

# centroids of countries from package "CoordinateCleaner"
countries <- countryref %>% 
  filter(name == "Netherlands" | name == "Switzerland") %>%
  distinct(name, .keep_all = TRUE) %>%
  rename(lat = centroid.lat) %>% 
  rename(lng = centroid.lon) %>% 
  select(name, lat, lng, iso2)

# ENGLISH VERSION ---------------
# international cities with lon/lat (source: https://simplemaps.com/data/de-cities)
cities <- read_csv(here::here("R", "worldcities.csv")) %>% # internationale Buchstabierung
  filter(iso2 == "DE" | iso2 == "FR" |  iso2 == "NL" |  iso2 == "CH") %>%
  rename(name = city) %>% 
  select(name, lat, lng, iso2)

# binding to one dataframe
geo_en <- rbind(countries, regions, cities)

df_en <- get_data("https://correlaid.org")
## joining data for mapping
# matching lc-names and city-names
df_en <- left_join(df_en, geo_en, by = "name") %>%
  select(name, url, content, lat, lng)

# filter out rows with missing lat / long
df_en_sub <- df_en %>%
  filter(!is.na(lat) & !is.na(lng))
# difficulty with local chapters like "Ruhrgebiet" or Rhine-Main"

## Converting data frame to sf-Format (geometry list) with package sf
df_aggr_en <- st_as_sf(df_en_sub, coords = c("lng", "lat"))
df_aggr_en


cax_leaflet_map(df_aggr_en) %>% saveWidget(file=here::here("static", "html", "map_en.html"))


# german ---------
df_de <- get_data("https://correlaid.org/de") 
cities_de <- geocode_OSM(df_de$name[!df_de$name %in% c("Rhein-Main", "Ruhrgebiet", "Switzerland", "Nederland")])

cities_de <- cities_de %>% 
  select(name = query, lat, lng = lon) %>% 
  mutate(iso2 = if_else(name == "Paris", "FR", "DE"))

countries_de <- countries %>% 
  mutate(name = if_else(name == "Netherlands", "Nederland", name))

geo_de <- rbind(countries_de, regions, cities_de)

df_de <- left_join(df_de, geo_de, by = "name") %>%
  select(name, url, content, lat, lng)

# filter out rows with missing lat / long
df_de_sub <- df_de %>%
  filter(!is.na(lat) & !is.na(lng))

## Converting data frame to sf-Format (geometry list) with package sf
df_aggr_de <- st_as_sf(df_de_sub, coords = c("lng", "lat"))
df_aggr_de


cax_leaflet_map(df_aggr_de) %>% saveWidget(file=here::here("static", "html", "map_de.html"))
