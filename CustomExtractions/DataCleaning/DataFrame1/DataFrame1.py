from Main import file
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
from Other_Outcomes import other_outcomes_df
import pandas as pd

all_variables = pd.concat([
    eppiid_df, 
    author_df, 
    year_df, 
    abstract_df, 
    admin_strand_df, 
    pubtype_eppi_df, 
    publication_type_df,
    country_df, 
    educational_setting_df, 
    study_realism_df, 
    student_age, 
    number_of_schools_df, 
    number_of_classes_df, 
    treatment_group_df, 
    participant_assignment_df, 
    level_of_assignment_df, 
    study_design_df, 
    randomisation_df,
    other_outcomes_df
], axis=1, sort=False)

# insert empty columns per variable for data checkers to log changes
all_variables.insert(7,  'strand_CLEAN', '')
all_variables.insert(9,  'pub_eppi_CLEAN', '')
all_variables.insert(13, 'pub_type_CLEAN', '')
all_variables.insert(15, 'loc_country_CLEAN', '')
all_variables.insert(19, 'int_Setting_CLEAN', '')
all_variables.insert(23, 'eco_valid_CLEAN', '')
all_variables.insert(27, 'part_age_CLEAN', '')

all_variables.insert(30, 'school_treat_CLEAN', '')
all_variables.insert(33, 'school_cont_CLEAN', '')
all_variables.insert(36, 'school_total_CLEAN', '')
all_variables.insert(40, 'school_na_CLEAN', '')

all_variables.insert(43, 'class_treat_CLEAN', '')
all_variables.insert(46, 'class_cont_CLEAN',  '')
all_variables.insert(49, 'class_total_CLEAN', '')
all_variables.insert(53, 'class_na_CLEAN', '')

all_variables.insert(57, 'treat_group_CLEAN', '')
all_variables.insert(61, 'part_assig_CLEAN', '')
all_variables.insert(65, 'level_assig_CLEAN', '')
all_variables.insert(69, 'int_design_CLEAN', '')
all_variables.insert(73, 'rand_CLEAN', '')
all_variables.insert(77, 'out_other_CLEAN', '')
all_variables.insert(81, 'out_info_CLEAN', '')
all_variables.insert(84, 'part_other_CLEAN', '')

# remove problematic text from outputs
all_variables.replace('\r', ' ', regex=True, inplace=True)
all_variables.replace('\n', ' ', regex=True, inplace=True)
all_variables.replace(':', ' ',  regex=True, inplace=True)
all_variables.replace(';', ' ',  regex=True, inplace=True)

print(list(all_variables))

# temporary whilst 'Update' strands have not been integrated into the main section
''' del all_variables["MSR_Update 2020"] '''

# useful
print("Columns:", all_variables.shape[1])
print("Rows:", all_variables.shape[0])
print("Datapoints:", all_variables.shape[0] * all_variables.shape[1])

# get file name for output
outfile_name = file.rsplit('/')[-1]
outfile_name = outfile_name.rsplit('.')[0]
outfile_name = outfile_name + "_DataFrame1.csv"

# write to disk
print("saving {}".format(outfile_name))
all_variables.to_csv(outfile_name, index=False)
