# Load required packages
library(rvest)
library(stringr)

# Define the URL of the webpage to scrape
url <- "https://www.example.com"

# Scrape the webpage using rvest package
webpage <- read_html(url)

# Extract the data using CSS selectors
data <- webpage %>%
    html_nodes("table") %>%
    html_table()

# Clean the data
data_cleaned <- data %>%
    # Remove unwanted columns
    select(-c("Column1", "Column2")) %>%
    # Rename columns
    rename(
        NewColumn1 = "OldColumn1",
        NewColumn2 = "OldColumn2"
    ) %>%
    # Remove rows with missing values
    na.omit()
