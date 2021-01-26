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
all_variables.insert(8, 'desc_stats_CLEAN', '')
all_variables.insert(11, 'n_treat_CLEAN', '')
all_variables.insert(14, 'pre_t_mean_CLEAN', '')
all_variables.insert(17, 'pre_t_sd_CLEAN', '')
all_variables.insert(20, 'post_t_mean_CLEAN', '')
all_variables.insert(23, 'post_t_sd_CLEAN', '')
all_variables.insert(26, 'gain_t_mean_CLEAN', '')
all_variables.insert(29, 'gain_t_sd_CLEAN', '')
all_variables.insert(32, 'out_t_other_CLEAN', '')
all_variables.insert(35, 'n_cont_ht_CLEAN', '')
all_variables.insert(38, 'pre_c_mean_CLEAN', '')
all_variables.insert(41, 'pre_c_sd_CLEAN', '')
all_variables.insert(44, 'post_c_mean_CLEAN', '')
all_variables.insert(47, 'post_c_sd_CLEAN', '')
all_variables.insert(50, 'gain_c_mean_CLEAN', '')
all_variables.insert(53, 'gain_c_sd_CLEAN', '')
all_variables.insert(56, 'out_c_other_CLEAN', '')
all_variables.insert(59, 'n_treat2_CLEAN', '')
all_variables.insert(62, 'pre_t2_mean_CLEAN', '')
all_variables.insert(65, 'pre_t2_sd_CLEAN', '')
all_variables.insert(68, 'post_t2_mean_CLEAN', '')
all_variables.insert(71, 'post_t2_sd_CLEAN', '')
all_variables.insert(74, 'gain_t2_mean_CLEAN', '')
all_variables.insert(77, 'gain_t2_sd_CLEAN', '')
all_variables.insert(80, 'out_t2_other_CLEAN', '')
all_variables.insert(83, 'n_cont2_CLEAN', '')
all_variables.insert(86, 'pre_c2_mean_CLEAN', '')
all_variables.insert(89, 'pre_c2_sd_CLEAN', '')
all_variables.insert(92, 'post_c2_mean_CLEAN', '')
all_variables.insert(95, 'post_c2_sd_CLEAN', '')
all_variables.insert(98, 'gain_c2_mean_CLEAN', '')
all_variables.insert(101, 'gain_c2_sd_CLEAN', '')
all_variables.insert(104, 'out_c2_other_CLEAN', '')
all_variables.insert(108, 'follow_up_CLEAN', '')

all_variables.replace('\r', ' ', regex=True, inplace=True)
all_variables.replace('\n', ' ', regex=True, inplace=True)
all_variables.replace(':', ' ',  regex=True, inplace=True)
all_variables.replace(';', ' ',  regex=True, inplace=True)

print(list(all_variables))

''' del all_variables["MSR_Update 2020"] '''

for counter, i in enumerate(all_variables):
    print(counter, i)

print("Columns:", all_variables.shape[1])
print("Rows:", all_variables.shape[0])
print("Datapoints:", all_variables.shape[0] * all_variables.shape[1])

# save to disk
all_variables.to_csv("MSR_14jan21_Effect_Size_A.csv", index=False)
