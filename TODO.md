# DATA preprocess✅
## get the processed data by running "donnees_processeur.py" with the file in the path 'original_data/job_postings.csv'
1. only keep DATA that WORK_TYPE = FULL_TIME✅
2. only keep DATA that pay_period = MONTHLY ou YEARLY✅
3. calculate the salary: med_salary -> (min_salary+max_salary)/2 -> min_salary -> max_salary.✅
4. change the formatted_experience_level from a string into a number from 0 to 5 according to the experience needed ✅
nan = 0
'Internship' = 0
'Entry level' = 1 
'Mid-Senior level' =2
'Associate' = 3
'Director' = 4 
'Executive' = 5
*the ranking of these 5 type is refer to https://www.linkedin.com/pulse/what-do-linkedin-experience-levels-actually-mean-brannen-she-her-/
5. Utiliser original_listed_date - expiry pour calculer esposed_time🚫
cancelled: people usually didn't setup a expiry period, it has no reference value
# ACP
dimensions réservées pour l’ACP: salary (yearly), views, applies, formatted_experience_level, re-
mote_allowed, sponsored_posting
# ACF
dimensions réservées pour l’AFC: salary (yearly), views, applies, formatted_experience_level, re-
mote_allowed, sponsored_posting, location
original_listed_time (date du poste) et expiry ou closed_time pour avoir temps que l’annonce est
rester sur linkedin
# clustering

# classification supervisée