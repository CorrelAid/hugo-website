library(jsonlite)
library(purrr)

projects <- jsonlite::read_json("https://correlaid.github.io/projects/projects.json")


ids <- projects %>% 
    purrr::walk(function(proj) { 
        file_id <- tolower(proj$project_id)
        for (lang in c("de", "en")) {
            file_path <- here::here("content", lang, "projects", paste0(file_id, ".md"))
            # check whether file exists
            if (!file.exists(file_path)) {
                file.create(file_path)
                file_content <- glue::glue('---
                title: {proj$title[[lang]]}
                date: 2020-08-07T09:38:32+02:00
                project_id: {proj$project_id}
                lang: {lang}
                ---')
                readr::write_lines(file_content, file_path)
            }
        }
    })
    

ids
