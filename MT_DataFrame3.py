#!/usr/bin/env python3

import os
import sys

import pandas as pd

from ind_var_Gen.eppi_ID import eppiid_df
from ind_var_Gen.Author import author_df
from ind_var_Gen.Date import year_df
from ind_var_Gen.PublicationType_EPPI import pubtype_eppi_df
from ind_var_Gen.Abstract import abstract_df
from ind_var_Gen.AdminStrand import admin_strand_df
from ind_var_Gen.SampleSize import sample_size_df
from ind_var_Gen.Gender import gender_df
from ind_var_Gen.ses_fsm import ses_fsm_df
from ind_var_Gen.Sample_Size_Initial import initial_sample_size_df
from ind_var_Gen.Sample_Size_Analyzed import analyzed_sample_size_df
from ind_var_Gen.Attrition import attrition_df

datafile = sys.argv[1]

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
        all_variables.insert(5, 'strand_CLEAN', '')
        all_variables.insert(8, 'sample_analysed_CLEAN', '')
        all_variables.insert(12, 'part_gen_CLEAN', '')
        all_variables.insert(15, 'fsm_perc_CLEAN', '')
        all_variables.insert(18, 'fsm_info_CLEAN', '')
        all_variables.insert(21, 'fsm_na_CLEAN', '')
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
        cw = os.getcwd() + "/Extractions"

        # get file name for output
        outfile_name_pre = datafile.rsplit('/')[-1] # 
        outfile_name_mid = outfile_name_pre.rsplit('.')[0]  # use for dir name
        outfile_name = outfile_name_mid + "_DataFrame3_Sample_Size.csv"
        outfile = os.path.join(cw + "/" + outfile_name_mid, outfile_name)

        # create dir (filename)
        try:
            os.mkdir("Extractions/" + outfile_name_mid)
        except OSError:
            print("Create {} dir fail, check if it already exists or permissions".format("Extractions/" + outfile_name_mid))
        else:
            print("Successfully created {} directory".format("Extractions/" + outfile_name_mid))

        # write to disk
        print("Input file: {}".format(datafile))
        print("Saving extracted output to: {}".format(outfile))
        all_variables.to_csv(outfile, index=False)

make_dataframe(save_file=True, clean_cols=True, verbose=True)
