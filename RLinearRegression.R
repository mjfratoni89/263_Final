install.packages("gdata")
library(gdata)
library(sandwich)
data <- read.xls("leagues_NBA_2014_team.xls")
rk = data[[2]]
FG = data[[7]]
twop = data[[10]]
threep = data[[13]]
pts = data[[18]]
drb = data[[25]]

bbfit = lm(rk ~ FG + twop + threep + pts + drb)
summary(bbfit)
eps <- residuals(bbfit)

