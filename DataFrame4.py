#!/usr/bin/env python3

""" from files import data_files """

# local imports
from ind_var_Gen.eppi_ID import eppiid_df
from ind_var_Gen.Author import author_df
from ind_var_Gen.Date import year_df
from ind_var_Gen.AdminStrand import admin_strand_df
from ind_var_Gen.PrimaryOutcomeDescStatsReported import DescStatsOutcomeReported_df
from ind_var_Gen.PrimaryOutcomeDescStatsInterventionGroup import DescStatsPrimaryOutcomeReported_Intervention_df
from ind_var_Gen.PrimaryOutcomeDescStatsControlGroup import DescStatsPrimaryOutcomeReported_Control_df
from ind_var_Gen.PrimaryOutcomeDescStatsInterventionGroup_TWO import DescStatsPrimaryOutcomeReported_Intervention_TWO_df
from ind_var_Gen.PrimaryOutcomeDescStatsControlGroup_TWO import DescStatsPrimaryOutcomeReported_Control_TWO_df

# standard imports
import os
import sys
import pandas as pd

data_files = sys.argv[1]

def make_dataframe(save_file=True, clean_cols=True, verbose=True):

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

    if clean_cols:
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

    if verbose:
        # print dataframe
        print(all_variables)
        print("\n")

        # list column names and position
        for counter, i in enumerate(all_variables):
            print(counter, i)
        print("\n")

        # print dataframe info
        print("Columns: {}".format(all_variables.shape[1]))
        print("Rows: {}".format(all_variables.shape[0]))
        print("Datapoints: {}".format(
            all_variables.shape[0] * all_variables.shape[1]))
        print("\n")

    if save_file:

        # get current working dir
        cw = os.getcwd()

        # get file name for output
        outfile_name_pre = data_files.rsplit('/')[-1]
        outfile_name_mid = outfile_name_pre.rsplit('.')[0]  # use for dir name
        outfile_name = outfile_name_mid + "_Effect_Size_A.csv"
        outfile = os.path.join(cw + "/" + outfile_name_mid, outfile_name)

        # create dir (filename)
        try:
            os.mkdir(outfile_name_mid)
        except OSError:
            print("Create {} dir fail, check if it already exists or permissions".format(
                outfile_name_mid))
        else:
            print("Successfully created {} directory".format(outfile_name_mid))

        # write to disk
        print("Input file: {}".format(data_files))
        print("Saving extracted output to: {}".format(outfile))
        all_variables.to_csv(outfile, index=False)


make_dataframe(save_file=True, clean_cols=True, verbose=True)
