from eppi_ID import eppiid_df 
from Author import author_df 
from Date import year_df
from PublicationType_EPPI import pubtype_eppi_df
from Abstract import abstract_df
from AdminStrand import admin_strand_df 
from SampleSize import sample_size_df
from Gender import gender_df
from ses_fsm import ses_fsm_df
from Sample_Size_Initial import initial_sample_size_df
from Sample_Size_Analyzed import analyzed_sample_size_df
from Attrition import attrition_df

import pandas as pd 

all_variables = pd.concat([
    eppiid_df, author_df, year_df, pubtype_eppi_df, abstract_df, admin_strand_df,
    sample_size_df, gender_df, ses_fsm_df, initial_sample_size_df, 
    analyzed_sample_size_df, attrition_df], 
axis=1, sort=False)

# insert empty columns per variable for data checkers to log changes
all_variables.insert(4,  'pub_eppi_CLEAN', '')
all_variables.insert(8,  'strand_CLEAN', '')
all_variables.insert(11, 'sample_analysed_CLEAN', '')
all_variables.insert(15, 'part_gen_CLEAN', '')
all_variables.insert(21, 'fsm_CLEAN', '')
all_variables.insert(24, 'base_n_treat_CLEAN', '')
all_variables.insert(27, 'base_n_cont_CLEAN', '')
all_variables.insert(30, 'base_n_treat2_CLEAN', '')
all_variables.insert(33, 'base_n_treat3_CLEAN', '')
all_variables.insert(36, 'n_treat_CLEAN', '')
all_variables.insert(39, 'n_cont_CLEAN', '')
all_variables.insert(42, 'n_treat2_CLEAN', '')
all_variables.insert(45, 'n_cont2_CLEAN', '')
all_variables.insert(49, 'attri_CLEAN', '')
all_variables.insert(52, 'attri_treat_CLEAN', '')
all_variables.insert(55, 'attri_perc_CLEAN', '')

all_variables.replace('\r',' ', regex=True, inplace=True)
all_variables.replace('\n',' ', regex=True, inplace=True)
all_variables.replace(':',' ',  regex=True, inplace=True)
all_variables.replace(';',' ',  regex=True, inplace=True)

all_variables.to_csv("DataFrame3.csv", index=False) 