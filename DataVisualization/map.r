library(ggmap)
library(ggplot2)
library(dplyr)


train <- read.csv("train.csv")
map <- get_map(location="San Francisco",zoom=12)

map_crime <- function(crime_df, crime) {
  filtered <- filter(crime_df, Category %in% crime)
  plot <- ggmap(map, extent='device') + 
    geom_point(data=filtered, aes(x=X, y=Y, color=Category), alpha=0.6)
  return(plot)
}

map_crime(train, c('SUICIDE', 'ARSON'))