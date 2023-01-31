#!/usr/bin/env python3

from Main import get_metadata, get_data, get_outcome_lvl1, get_outcome_lvl2, data_files

# local imports
from ind_var_CEDIL.eppi_ID_CEDIL import eppiid_df
from ind_var_CEDIL.Author_CEDIL import author_df
from ind_var_CEDIL.Date_CEDIL import year_df
from ind_var_CEDIL.Abstract_CEDIL import abstract_df
from ind_var_CEDIL.AdminStrand_CEDIL import admin_strand_df
from ind_var_CEDIL.PublicationType_EPPI_CEDIL import pubtype_eppi_df
from ind_var_CEDIL.PublicationType_CEDIL import publication_type_df
from ind_var_CEDIL.Country_CEDIL import country_df
from ind_var_CEDIL.EducationalSetting_CEDIL import educational_setting_df
from ind_var_CEDIL.StudyRealism_CEDIL import study_realism_df
from ind_var_CEDIL.Age_CEDIL import student_age
from ind_var_CEDIL.NumberofSchools_CEDIL import number_of_schools_df
from ind_var_CEDIL.NumberofClasses_CEDIL import number_of_classes_df
from ind_var_CEDIL.TreatmentGroup_CEDIL import treatment_group_df
from ind_var_CEDIL.ParticipantAssignment_CEDIL import participant_assignment_df
from ind_var_CEDIL.LevelofAssignment_CEDIL import level_of_assignment_df
from ind_var_CEDIL.StudyDesign_CEDIL import study_design_df
from ind_var_CEDIL.Randomisation_CEDIL import randomisation_df
from ind_var_CEDIL.Other_Outcomes_CEDIL import other_outcomes_df

# standard imports
import os
import pandas as pd


def make_dataframe(save_file=True, clean_cols=True, verbose=True):

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

    if clean_cols:
        
        # insert empty columns per variable for data checkers to log changes
        all_variables.insert(6, 'strand_CLEAN', '')
        all_variables.insert(9, 'pub_eppi_CLEAN', '')
        all_variables.insert(12, 'pub_type_CLEAN', '')
        all_variables.insert(14, 'loc_country_CLEAN', '')
        all_variables.insert(18, 'int_Setting_CLEAN', '')
        all_variables.insert(22, 'eco_valid_CLEAN', '')
        all_variables.insert(26, 'part_age_CLEAN', '')

        # school cols
        all_variables.insert(29, 'school_treat_CLEAN', '')
        all_variables.insert(32, 'school_cont_CLEAN', '')
        all_variables.insert(35, 'school_total_CLEAN', '')
        all_variables.insert(30, 'school_na_CLEAN', '')

        # class cols
        all_variables.insert(42, 'class_treat_CLEAN', '')
        all_variables.insert(44, 'class_cont_CLEAN',  '')
        all_variables.insert(50, 'class_total_CLEAN', '')
        all_variables.insert(52, 'class_na_CLEAN', '')

        all_variables.insert(56, 'treat_group_CLEAN', '')
        all_variables.insert(60, 'part_assig_CLEAN', '')
        all_variables.insert(64, 'level_assig_CLEAN', '')
        all_variables.insert(68, 'int_design_CLEAN', '')
        all_variables.insert(72, 'rand_CLEAN', '')
        all_variables.insert(76, 'out_other_CLEAN', '')
        all_variables.insert(80, 'out_info_CLEAN', '')
        all_variables.insert(83, 'part_other_CLEAN', '')

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
        print("Columns: {}".format(all_variables.shape[1]))
        print("Rows: {}".format(all_variables.shape[0]))
        print("Datapoints: {}".format(all_variables.shape[0] * all_variables.shape[1]))
        print("\n")

    if save_file:

        # get current working dir
        cw = os.getcwd()

        # get file name for output
        outfile_name_pre = data_files.rsplit('/')[-1]
        outfile_name_mid = outfile_name_pre.rsplit('.')[0]  # use for dir name
        outfile_name = outfile_name_mid + "_DataFrame1.csv"
        outfile = os.path.join(cw + "/" + outfile_name_mid, outfile_name)

        # create dir (filename)
        try:
            os.mkdir(outfile_name_mid)
        except OSError:
            print("Create {} dir fail, check if it already exists or permissions".format(outfile_name_mid))
        else:
            print("Successfully created {} directory".format(outfile_name_mid))

        # write to disk
        print("Input file: {}".format(data_files))
        print("Saving extracted output to: {}".format(outfile))
        all_variables.to_csv(outfile, index=False)


make_dataframe(save_file=True, clean_cols=True, verbose=True)
