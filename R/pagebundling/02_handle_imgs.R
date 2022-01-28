library(tidyverse)
library(parsermd)

file_info <- readr::read_rds("R/pagebundling/file_info.rds")

# copy images to folder 
# one of the advantages of page bundling is that we can use the image processing of Hugo
# this means that we don't have to store various versions of the same image anymore
# here we copy the title image the the respective folder
file_info <- file_info %>% 
  mutate(image = yaml %>% purrr::map_chr("image"))

file_info %>% 
  select(image, folder_name)
