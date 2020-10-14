from eppi_ID import eppiid_df 
from Author import author_df 
from Date import year_df 
from Abstract import abstract_df
from AdminStrand import admin_strand_df 
from PublicationType_EPPI import pubtype_eppi_df
from PublicationType import publication_type_df 
from Country import country_df 
from EducationalSetting import educational_setting_df 
from StudyRealism import study_realism_df 
from Age import student_age
from NumberofSchools import number_of_schools_df 
from NumberofClasses import number_of_classes_df 
from TreatmentGroup import treatment_group_df 
from ParticipantAssignment import participant_assignment_df 
from LevelofAssignment import level_of_assignment_df
from StudyDesign import study_design_df
from Randomisation import randomisation_df 

import pandas as pd

all_variables = pd.concat([
    eppiid_df, author_df, year_df, abstract_df, 
    admin_strand_df, pubtype_eppi_df, publication_type_df,
    country_df, educational_setting_df, study_realism_df, 
    student_age, number_of_schools_df, number_of_classes_df, 
    treatment_group_df, participant_assignment_df, level_of_assignment_df, 
    study_design_df, randomisation_df
], axis=1, sort=False)

# insert empty columns per variable for data checkers to log changes
all_variables.insert(6, 'strand_CLEAN', '')
all_variables.insert(8, 'pub_eppi_CLEAN', '')
all_variables.insert(12, 'pub_type_CLEAN', '')
all_variables.insert(16, 'loc_country_CLEAN', '')
all_variables.insert(20, 'int_Setting_CLEAN', '')
all_variables.insert(24, 'eco_valid_CLEAN', '')
all_variables.insert(28, 'part_age_CLEAN', '')
all_variables.insert(31, 'school_treat_CLEAN', '')
all_variables.insert(34, 'school_cont_CLEAN', '')
all_variables.insert(37, 'school_total_CLEAN', '')
all_variables.insert(41, 'school_na_CLEAN', '')
all_variables.insert(44, 'class_treat_CLEAN', '')
all_variables.insert(47, 'class_cont_CLEAN', '')
all_variables.insert(50, 'class_total_CLEAN' '')
all_variables.insert(54, 'class_na_CLEAN', '')
all_variables.insert(58, 'treat_group_CLEAN', '')
all_variables.insert(62, 'part_assig_CLEAN', '')
all_variables.insert(66, 'level_assig_CLEAN', '')
all_variables.insert(70, 'int_design_CLEAN', '')
all_variables.insert(74, 'rand_CLEAN', '')

# remove problematic text from outputs
all_variables.replace('\r',' ', regex=True, inplace=True)
all_variables.replace('\n',' ', regex=True, inplace=True)
all_variables.replace(':',' ', regex=True, inplace=True)
all_variables.replace(';',' ', regex=True, inplace=True)

all_variables.to_csv("DataFrame1.csv", index=False) 

print("Columns:", all_variables.shape[1])
print("Rows:", all_variables.shape[0])
print("Datapoints:", all_variables.shape[0] * all_variables.shape[1])