#!/usr/bin/env python3

from Main import data_files

from ind_var_CEDIL.eppi_ID_CEDIL import eppiid_df
from ind_var_CEDIL.Author_CEDIL import author_df
from ind_var_CEDIL.Date_CEDIL import year_df
from ind_var_CEDIL.PublicationType_EPPI_CEDIL import pubtype_eppi_df
from ind_var_CEDIL.Abstract_CEDIL import abstract_df
from ind_var_CEDIL.AdminStrand_CEDIL import admin_strand_df
from ind_var_CEDIL.SampleSize_CEDIL import sample_size_df
from ind_var_CEDIL.Gender_CEDIL import gender_df
from ind_var_CEDIL.ses_fsm_CEDIL import ses_fsm_df
from ind_var_CEDIL.Sample_Size_Initial_CEDIL import initial_sample_size_df
from ind_var_CEDIL.Sample_Size_Analyzed_CEDIL import analyzed_sample_size_df
from ind_var_CEDIL.Attrition_CEDIL import attrition_df

import os
import pandas as pd

def make_dataframe(save_file=True, clean_cols=True, verbose=True):

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

    if clean_cols:
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
        all_variables.insert(58, 'attri_perc_CLEAN', '')

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
        outfile_name = outfile_name_mid + "_Sample_Size.csv"
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
