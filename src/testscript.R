################################################################################
## Load Libraries
################################################################################
pkgs <- c('purrr','plyr','tidyverse', 'plotrix','lubridate','kableExtra','hrbrthemes','ggplot2','extrafont','float','reshape',
          'gridExtra','rsvg','png','devtools','readxl','date', 'ggpubr', 'tidyselect', 'httr', 'jsonlite', 'extrafont', 'colorspace',
          'ggrepel', 'forcats', 'ggpubr', 'readstata13', 'cowplot', 'scales')
lapply(pkgs, require, character.only = TRUE)

################################################################################
## Reading in data
################################################################################

# Setting directories
r.functions.dir <- '/Users/lshvb5/Documents/rammps/'
dir.inputdata <- ('/Users/lshvb5/OneDrive - London School of Hygiene and Tropical Medicine/General/Partners/UNIKIN/SurveyCTO Audits/')

# Malawi
Consentedmw <- read.csv(paste0(r.functions.dir, 'RaMMPS_MWApp/ConsentedMW.csv')) %>%
  mutate(Outcome2 = ifelse(Outcome2 =='NNA'| Outcome2 =='NR', 'NNA/NR', as.character(Outcome2))) 

################################################################################
##  Age and sex distribution
################################################################################
#MW
age_sex_mw <- Consentedmw %>%
  group_by(Resp.Age.pyr, Resp.Sex) %>%
  dplyr::summarize(population = n()) %>%
  ungroup() %>%
  group_by(Resp.Sex) %>%
  dplyr::mutate(npersex = sum(population)) %>% # sum per sex
  ungroup() %>%
  mutate(relfreq = population/npersex*100, 
         Group = "Total")

ggplot(data = age_sex_mw) +
  geom_bar(stat = "identity",aes(x=Resp.Age.pyr, y = relfreq, fill=Resp.Sex), position = "dodge2") + 
  scale_fill_manual(values = c('#F8B7CD','#0671B7')) +
  ylab('Relative Frequency of Respondents (%)') + xlab('Respondent Age') +
  scale_x_discrete(labels = c('15-19','20-29','30-39','40-49','50-59','60-64')) +
  theme_bw() +
  labs(fill='Respondent Sex') +
  coord_cartesian(ylim = c(0,50)) 

ggsave('assets/plot.png')