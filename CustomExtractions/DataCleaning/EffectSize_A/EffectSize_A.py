from Main import file
from eppi_ID import eppiid_df
from Author import author_df
from Date import year_df
from AdminStrand import admin_strand_df
from PrimaryOutcomeDescStatsReported import DescStatsOutcomeReported_df
from PrimaryOutcomeDescStatsInterventionGroup import DescStatsPrimaryOutcomeReported_Intervention_df
from PrimaryOutcomeDescStatsControlGroup import DescStatsPrimaryOutcomeReported_Control_df
from PrimaryOutcomeDescStatsInterventionGroup_TWO import DescStatsPrimaryOutcomeReported_Intervention_TWO_df
from PrimaryOutcomeDescStatsControlGroup_TWO import DescStatsPrimaryOutcomeReported_Control_TWO_df
import pandas as pd

all_variables = pd.concat([
    eppiid_df, 
    author_df, 
    year_df, 
    admin_strand_df, 
    DescStatsOutcomeReported_df,
    DescStatsPrimaryOutcomeReported_Intervention_df, 
    DescStatsPrimaryOutcomeReported_Control_df,
    DescStatsPrimaryOutcomeReported_Intervention_TWO_df, 
    DescStatsPrimaryOutcomeReported_Control_TWO_df
], axis=1, sort=False)

# insert empty columns per variable for data checkers to log changes
all_variables.insert(9, 'desc_stats_CLEAN', '')
all_variables.insert(12, 'n_treat_CLEAN', '')
all_variables.insert(15, 'pre_t_mean_CLEAN', '')
all_variables.insert(18, 'pre_t_sd_CLEAN', '')
all_variables.insert(21, 'post_t_mean_CLEAN', '')
all_variables.insert(24, 'post_t_sd_CLEAN', '')
all_variables.insert(27, 'gain_t_mean_CLEAN', '')
all_variables.insert(30, 'gain_t_sd_CLEAN', '')
all_variables.insert(33, 'out_t_other_CLEAN', '')
all_variables.insert(36, 'n_cont_ht_CLEAN', '')
all_variables.insert(39, 'pre_c_mean_CLEAN', '')
all_variables.insert(42, 'pre_c_sd_CLEAN', '')
all_variables.insert(45, 'post_c_mean_CLEAN', '')
all_variables.insert(48, 'post_c_sd_CLEAN', '')
all_variables.insert(51, 'gain_c_mean_CLEAN', '')
all_variables.insert(54, 'gain_c_sd_CLEAN', '')
all_variables.insert(57, 'out_c_other_CLEAN', '')
all_variables.insert(60, 'n_treat2_CLEAN', '')
all_variables.insert(63, 'pre_t2_mean_CLEAN', '')
all_variables.insert(66, 'pre_t2_sd_CLEAN', '')
all_variables.insert(69, 'post_t2_mean_CLEAN', '')
all_variables.insert(72, 'post_t2_sd_CLEAN', '')
all_variables.insert(75, 'gain_t2_mean_CLEAN', '')
all_variables.insert(78, 'gain_t2_sd_CLEAN', '')
all_variables.insert(81, 'out_t2_other_CLEAN', '')
all_variables.insert(84, 'n_cont2_CLEAN', '')
all_variables.insert(87, 'pre_c2_mean_CLEAN', '')
all_variables.insert(90, 'pre_c2_sd_CLEAN', '')
all_variables.insert(93, 'post_c2_mean_CLEAN', '')
all_variables.insert(96, 'post_c2_sd_CLEAN', '')
all_variables.insert(99, 'gain_c2_mean_CLEAN', '')
all_variables.insert(102, 'gain_c2_sd_CLEAN', '')
all_variables.insert(105, 'out_c2_other_CLEAN', '')
all_variables.insert(109, 'follow_up_CLEAN', '')

all_variables.replace('\r', ' ', regex=True, inplace=True)
all_variables.replace('\n', ' ', regex=True, inplace=True)
all_variables.replace(':', ' ',  regex=True, inplace=True)
all_variables.replace(';', ' ',  regex=True, inplace=True)

''' del all_variables["MSR_Update 2020"] '''

for counter, i in enumerate(all_variables):
    print(counter, i)

print("Columns:", all_variables.shape[1])
print("Rows:", all_variables.shape[0])
print("Datapoints:", all_variables.shape[0] * all_variables.shape[1])

# get file name for output
outfile_name = file.rsplit('/')[-1]
outfile_name = outfile_name.rsplit('.')[0]
outfile_name = outfile_name + "_Effect_Size_A.csv"

# write to disk
print("saving {}".format(outfile_name))
all_variables.to_csv(outfile_name, index=False)