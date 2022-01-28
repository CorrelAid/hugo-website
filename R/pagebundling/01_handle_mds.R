library(tidyverse)
library(parsermd)

file_info <- readr::read_rds("R/pagebundling/file_info.rds")

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


