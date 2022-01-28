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
  yml$file_base <- fs::path_ext_remove(fs::path_file(file))
  yml$file <- fs::path_file(file)
  df <- tibble(date = yml$date %>% lubridate::ymd_hms() %>% format(format = "%Y-%m-%d"), 
               file_base = yml$file_base, 
               title = yml$title, 
               file = yml$file,
               file_abs = .env$file)
  
  df %>% 
    mutate(folder_name = if_else(stringr::str_starts(file_base, "\\d{4}-\\d{2}-\\d{2}"), 
                                 file_base, paste(date, file_base, sep = "_")),
           lang = if_else(str_detect(file_abs, "content/de"), "de", "en"),
           folder_path = fs::path("content", lang, "blog", folder_name),
           file_abs_new = paste(fs::path("content", lang, "blog", folder_name), "index.md", sep = "/"))
}

# do it!
file_info <- mds %>% purrr::map_dfr(get_file_info)

# filter out index.md
file_info <- file_info %>% 
  filter(file_base != "_index")

# create folders
file_info$folder_path %>% purrr::walk(dir.create)

# copy the files 
purrr::walk2(file_info$file_abs, file_info$folder_path, function(file, folder) {
  print(file)
  file.copy(file, paste(folder, "index.md", sep = "/"))
  file.remove(file)
})

# add the old file name as a "slug" to the header so that we don't have the date in the URL
# parse the markdown
file_info %>% 
  select(file_abs_new, file_base) %>% 
  purrr::pwalk(function(file_abs_new, file_base) {
    slug <- file_base
    parsed <- parsermd::parse_rmd(file_abs_new)
    # only do something if the document has no slug
    if (is.null(parsed[[1]]$slug)) {
      parsed[[1]]$slug <- file_base
      txt <- parsermd::as_document(parsed) %>% paste(collapse = "\n")
      readr::write_lines(txt, file_abs_new)
    }
  })
