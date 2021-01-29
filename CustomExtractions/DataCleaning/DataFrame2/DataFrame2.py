from Main import file
from eppi_ID import eppiid_df
from Author import author_df
from Date import year_df
from AdminStrand import admin_strand_df
from InterventionName import intervention_name_df
from InterventionDescription import intervention_description_df
from InterventionObjectives import intervention_objectives_df
from InterventionOrganizationType import intervention_org_type
from InterventionTrainingProvided import intervention_training_provided_df
from InterventionFocus import intervention_focus_df
from InterventionTeachingApproach import intervention_teaching_approach_df
from InterventionInclusion import intervention_inclusion_df
from InterventionTime import intervention_time_df
from InterventionDelivery import intervention_delivery_df
from InterventionDuration import intervention_duration_df
from InterventionFrequency import intervention_frequency_df
from InterventionSessionLength import intervention_session_length_df
from InterventionDetail import intervention_detail_df
from InterventionCostsReported import intervention_costs_df
from InterventionEvaluation import intervention_evaluation_df  # includes EEF evaluation
from Baseline_Differences import baseline_differences_df
from Comparability import comparability_df
from Comparability_Variables_Reported import comparability_vars_reported_df
from Clustering import clustering_df
import pandas as pd

all_variables = pd.concat([
    eppiid_df, 
    author_df, 
    year_df, 
    admin_strand_df, 
    intervention_name_df, 
    intervention_description_df,
    intervention_objectives_df, 
    intervention_org_type, 
    intervention_training_provided_df,
    intervention_focus_df, 
    intervention_teaching_approach_df, 
    intervention_inclusion_df,
    intervention_time_df, 
    intervention_delivery_df, 
    intervention_duration_df, 
    intervention_frequency_df,
    intervention_session_length_df, 
    intervention_detail_df, 
    intervention_costs_df,
    intervention_evaluation_df, 
    baseline_differences_df, 
    comparability_df,
    comparability_vars_reported_df, 
    clustering_df
], axis=1, sort=False)

# insert empty columns per variable for data checkers to log changes
all_variables.insert(6,  'strand_CLEAN',        '')
all_variables.insert(9,  'int_name_CLEAN',      '')
all_variables.insert(12, 'int_desc_CLEAN',      '')
all_variables.insert(15, 'int_object_CLEAN',    '')
all_variables.insert(19, 'int_prov_CLEAN',      '')
all_variables.insert(23, 'int_training_CLEAN',  '')
all_variables.insert(27, 'int_part_CLEAN',      '')
all_variables.insert(31, 'int_approach_CLEAN',  '')
all_variables.insert(35, 'digital_tech_CLEAN',  '')
all_variables.insert(39, 'parent_partic_CLEAN', '')
all_variables.insert(43, 'int_when_CLEAN',      '')
all_variables.insert(46, 'int_who_CLEAN',       '')
all_variables.insert(50, 'int_dur_CLEAN',       '')
all_variables.insert(53, 'int_freq_CLEAN',      '')
all_variables.insert(56, 'int_leng_CLEAN',      '')
all_variables.insert(60, 'int_fidel_CLEAN',     '')
all_variables.insert(64, 'int_cost_CLEAN',      '')
all_variables.insert(68, 'out_eval_CLEAN',      '')
all_variables.insert(70, 'eef_eval_CLEAN',      '')
all_variables.insert(74, 'base_diff_CLEAN',     '')
all_variables.insert(78, 'comp_anal_CLEAN',     '')
all_variables.insert(82, 'comp_var_rep_CLEAN',  '')
all_variables.insert(86, 'comp_var_CLEAN',      '')
all_variables.insert(90, 'clust_anal_CLEAN',    '')

all_variables.replace('\r', ' ', regex=True, inplace=True)
all_variables.replace('\n', ' ', regex=True, inplace=True)
all_variables.replace(':', ' ',  regex=True, inplace=True)
all_variables.replace(';', ' ',  regex=True, inplace=True)

# temporary whilst 'Update' strands have not been integrated into the main section
""" del all_variables["MSR_Update 2020"] """

print("Columns:", all_variables.shape[1])
print("Rows:", all_variables.shape[0])
print("Datapoints:", all_variables.shape[0] * all_variables.shape[1])

# get file name for output
outfile_name = file.rsplit('/')[-1]
outfile_name = outfile_name.rsplit('.')[0]
outfile_name = outfile_name + "_DataFrame2.csv"

# write to disk
print("saving {}".format(outfile_name))
all_variables.to_csv(outfile_name, index=False)