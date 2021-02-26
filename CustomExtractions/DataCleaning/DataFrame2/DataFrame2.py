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

import os
import pandas as pd

def make_dataframe(save_file=True, clean_cols=True, verbose=True):

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
    all_variables.insert(5,  'strand_CLEAN',        '')
    all_variables.insert(8,  'int_name_CLEAN',      '')
    all_variables.insert(11, 'int_desc_CLEAN',      '')
    all_variables.insert(14, 'int_object_CLEAN',    '')
    all_variables.insert(15, 'int_prov_CLEAN',      '')
    all_variables.insert(22, 'int_training_CLEAN',  '')
    all_variables.insert(26, 'int_part_CLEAN',      '')
    all_variables.insert(30, 'int_approach_CLEAN',  '')
    all_variables.insert(34, 'digital_tech_CLEAN',  '')
    all_variables.insert(38, 'parent_partic_CLEAN', '')
    all_variables.insert(42, 'int_when_CLEAN',      '')
    all_variables.insert(45, 'int_who_CLEAN',       '')
    all_variables.insert(49, 'int_dur_CLEAN',       '')
    all_variables.insert(52, 'int_freq_CLEAN',      '')
    all_variables.insert(54, 'int_leng_CLEAN',      '')
    all_variables.insert(59, 'int_fidel_CLEAN',     '')
    all_variables.insert(63, 'int_cost_CLEAN',      '')
    all_variables.insert(67, 'out_eval_CLEAN',      '')
    all_variables.insert(69, 'eef_eval_CLEAN',      '')
    all_variables.insert(73, 'base_diff_CLEAN',     '')
    all_variables.insert(77, 'comp_anal_CLEAN',     '')
    all_variables.insert(81, 'comp_var_rep_CLEAN',  '')
    all_variables.insert(85, 'comp_var_CLEAN',      '')
    all_variables.insert(89, 'clust_anal_CLEAN',    '')

    # remove problematic text from outputs
    all_variables.replace('\r', ' ', regex=True, inplace=True)
    all_variables.replace('\n', ' ', regex=True, inplace=True)
    all_variables.replace(':', ' ',  regex=True, inplace=True)
    all_variables.replace(';', ' ',  regex=True, inplace=True)

    if verbose:
        # print dataframe
        print(all_variables)
        print("\n")

        # list column names and position
        for counter, i in enumerate(all_variables):
            print(counter, i)
        print("\n")

        # print dataframe info
        print("Columns:", all_variables.shape[1])
        print("Rows:", all_variables.shape[0])
        print("Datapoints:", all_variables.shape[0] * all_variables.shape[1])
        print("\n")

    if save_file:

        # get current working dir
        cw = os.getcwd()

        # get file name for output
        outfile_name_pre = file.rsplit('/')[-1]
        outfile_name_mid = outfile_name_pre.rsplit('.')[0]  # use for dir name
        outfile_name = outfile_name_mid + "_DataFrame2_compare.csv"
        outfile = os.path.join(cw + "/" + outfile_name_mid, outfile_name)

        # write to disk
        print("Input file: {}".format(file))
        print("Saving extracted output to: {}".format(outfile))
        all_variables.to_csv(outfile, index=False)

make_dataframe(save_file=True, clean_cols=True, verbose=True)