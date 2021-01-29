from Main import file
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
    eppiid_df, 
    author_df, 
    year_df, 
    admin_strand_df,
    sample_size_df, 
    gender_df, 
    ses_fsm_df, 
    initial_sample_size_df,
    analyzed_sample_size_df, 
    attrition_df
], axis=1, sort=False)

# insert empty columns per variable for data checkers to log changes
all_variables.insert(6, 'strand_CLEAN', '')
all_variables.insert(9, 'sample_analysed_CLEAN', '')
all_variables.insert(13, 'part_gen_CLEAN', '')
all_variables.insert(16, 'fsm_prop_CLEAN', '')
all_variables.insert(19, 'fsm_perc_CLEAN', '')
all_variables.insert(22, 'fsm_info_CLEAN', '')
all_variables.insert(25, 'fsm_na_CLEAN', '')
all_variables.insert(28, 'base_n_treat_CLEAN', '')
all_variables.insert(31, 'base_n_cont_CLEAN', '')
all_variables.insert(34, 'base_n_treat2_CLEAN', '')
all_variables.insert(37, 'base_n_treat3_CLEAN', '')
all_variables.insert(40, 'n_treat_CLEAN', '')
all_variables.insert(43, 'n_cont_CLEAN', '')
all_variables.insert(46, 'n_treat2_CLEAN', '')
all_variables.insert(49, 'n_cont2_CLEAN', '')
all_variables.insert(53, 'attri_CLEAN', '')
all_variables.insert(56, 'attri_treat_CLEAN', '')
all_variables.insert(59, 'attri_perc_CLEAN', '')

all_variables.replace('\r', ' ', regex=True, inplace=True)
all_variables.replace('\n', ' ', regex=True, inplace=True)
all_variables.replace(':', ' ',  regex=True, inplace=True)
all_variables.replace(';', ' ',  regex=True, inplace=True)

""" del all_variables["OL_Update_2020"] """

for counter, i in enumerate(all_variables):
    print(counter, i)

# get file name for output
outfile_name = file.rsplit('/')[-1]
outfile_name = outfile_name.rsplit('.')[0]
outfile_name = outfile_name + "_Sample_Size.csv"

# write to disk
print("saving {}".format(outfile_name))
all_variables.to_csv(outfile_name, index=False)