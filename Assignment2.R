# load libraries
library(dplyr)
library(ggplot2)

# load dataset
attrition_data <- read.csv("Downloads/updated_data.csv", stringsAsFactors = FALSE)

# explore dataset
str(attrition_data)
summary(attrition_data)

# check for missing values
sapply(attrition_data, function(x) sum(is.na(x)))
# create plot
attrition_data %>%
  group_by(Department) %>%
  summarize(Attrition = sum(Attrition == "Yes")/n()) %>%
  ggplot(aes(x = Department, y = Attrition, fill = Department)) +
  geom_col() +
  labs(x = "Department", y = "Attrition Rate", fill = "Department") +
  ggtitle("Attrition Rate by Department") +
  theme_minimal()
