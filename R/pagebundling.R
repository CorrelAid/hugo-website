# create page bundles
# GERMAN -------
# read metadata
library(purrr)
library(tibble)
library(tidyverse)
library(parsermd)
mds_de <- list.files("content/de/blog/", pattern = "*.md$", full.names = TRUE)
mds_en <- list.files("content/en/blog/", pattern = "*.md$", full.names = TRUE)
mds <- c(mds_de, mds_en)

# get file infos and create folder names
get_file_info <- function(file) {
  print(file)
  yml <- rmarkdown::yaml_front_matter(file)
  
  df <- tibble(date = yml$date %>% lubridate::ymd_hms() %>% format(format = "%Y-%m-%d"), 
               file_base = fs::path_ext_remove(fs::path_file(file)), 
               title = yml$title, 
               file = fs::path_file(file),
               file_abs = .env$file)
  
  df %>% 
    mutate(folder_name = if_else(stringr::str_starts(file_base, "\\d{4}-\\d{2}-\\d{2}"), 
                                 file_base, paste(date, file_base, sep = "_")),
           lang = if_else(str_detect(file_abs, "content/de"), "de", "en"),
           folder_path = fs::path("content", lang, "blog", folder_name),
           file_abs_new = paste(fs::path("content", lang, "blog", folder_name), "index.md", sep = "/"),
           yaml = list(yml))
}

# do it!
file_info <- mds %>% purrr::map_dfr(get_file_info)

# filter out index.md
file_info <- file_info %>% 
  filter(file_base != "_index")

# save
readr::write_rds(file_info, here::here("R", "pagebundling", "file_info.rds"))
