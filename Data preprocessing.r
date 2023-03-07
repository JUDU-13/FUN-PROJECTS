# Load required packages
library(dplyr)
library(tidyr)

# Load the data into a data frame
data <- read.csv("data.csv")

# Remove duplicate rows
data <- distinct(data)

# Remove rows with missing values
data <- na.omit(data)

# Convert categorical variables to factors
data$Category <- as.factor(data$Category)

# Normalize numerical variables
data$Variable1_norm <- scale(data$Variable1)
data$Variable2_norm <- scale(data$Variable2)

# Create new features
data$NewVariable <- data$Variable1 + data$Variable2

# Create dummy variables for categorical variables
data <- data %>%
    pivot_wider(
        names_from = Category,
        values_from = NewVariable,
        names_prefix = "Category_"
    ) %>%
    replace_na(list(
        Category_A = 0,
        Category_B = 0,
        Category_C = 0
    ))

# Export the preprocessed data to a new CSV file
write.csv(data, "data_preprocessed.csv", row.names = FALSE)
