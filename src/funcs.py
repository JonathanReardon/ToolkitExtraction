#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__Author__ = "Jonathan Reardon"

# System imports
import os
import sys
import json

# Third Party imports
import pandas as pd
import numpy as np
from toolz import interleave
from rich import print
from rich import box
from rich.console import Console
from rich.table import Table
from rich.progress import track

# Local imports
from src.attributeIDs import *

# improve for error checking
data_file = sys.argv[1]

#/****************/
#/ CORE FUNCTIONS /
#/****************/

EXCLUDE = "NA"


def load_json():
    global data
    script_dir = os.path.dirname(__file__)
    datafile = os.path.join(script_dir, data_file)
    with open(datafile) as f:
        data = json.load(f)


def get_metadata(var):
    ''' """ 
    Extracts study-level metadata. """
    Params: Variable name e.g. "Year", "ShortTitle".
    Returns: A list of extracted data. One datapoint per study.
    '''
    varlist = []
    for section in range(len(data["References"])):
        if data["References"][section][var]:
            varlist.append(data["References"][section][var])
        else:
            varlist.append(EXCLUDE)
    return varlist


def get_data(codes):
    '''
    Extract study-level main data.
    Params: List/dict [{..}] of one or more AttributeID's and Attribute labels.
    Returns: A list of extracted data. One or more datapoints per study.
    '''
    df = []
    for var in range(len(codes)):
        holder = []
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                holderfind = []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            holderfind.append(value)
                if len(holderfind) == 0:
                    holderfind = EXCLUDE
                holder.append(holderfind)
        df.append(holder)
    return df


def comments(codes):
    ''' 
    Extracts study level "comment" data.
    Params: List/dict [{..}] of one or more AttributeID's and Attribute labels.
    Returns: A list of extracted data. One or more datapoints per study.
    '''
    all_comments, comments = [], []
    for var in range(len(codes)):
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                user_comments = []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            if "AdditionalText" in data["References"][section]["Codes"][study]:
                                user_comments = data["References"][section]["Codes"][study]["AdditionalText"]
                if not user_comments:
                    comments.append(EXCLUDE)
                else:
                    comments.append(user_comments)
            else:
                comments.append(EXCLUDE)
        all_comments.append(comments)
        comments = []
    return all_comments


def highlighted_text(codes):
    ''' 
    Extracts Study level "highlighted text" data.
    Params: List/dict [{..}] of one or more AttributeID's and Attribute labels.
    Returns: A list of extracted data. One or more datapoints per study.
    '''
    all_highlighted_text, highlighted_text = [], []
    for var in range(len(codes)):
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                user_highlighted_text = []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            if "ItemAttributeFullTextDetails" in data["References"][section]["Codes"][study]:
                                if data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"]:
                                    for i in range(len(data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"])):
                                        user_highlighted_text.append(
                                            data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"][i]["Text"])
                if not user_highlighted_text:
                    highlighted_text.append(EXCLUDE)
                else:
                    highlighted_text.append(user_highlighted_text)
            else:
                highlighted_text.append(EXCLUDE)
        all_highlighted_text.append(highlighted_text)
        highlighted_text = []
    return all_highlighted_text


def get_outcome_lvl1(var):
    ''' 
    Extracts first-level outcome data.
    Params: Variable name (str) e.g. "SMD", "OutcomeID".
    Returns: A list of extracted data. One datapoint per outcome, 
    multiple possible outcomes per study.
    '''
    outcome_number=[]
    for study in range(len(data["References"])):
        if "Outcomes" in data["References"][study]:
            outcome_number.append(len(data["References"][study]["Outcomes"]))
    varlist = []
    for section in range(len(data["References"])):
        holder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(outcome_number)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    holder.append(data["References"][section]["Outcomes"][subsection][var])
                else:
                    holder.append(EXCLUDE)
            varlist.append(holder)
        else:
            for i in range(max(outcome_number)):
                holder.append(EXCLUDE)
            varlist.append(holder)
    return varlist


def get_outcome_lvl2(var):
    '''
    Extracts second-level (nested) outcome data.
    Params: List/dict [{..}] of one or more AttributeID's and Attribute labels.
    Returns: A list of extracted data. Multiple possible datapoints per outcome,
    multiple possible outcomes per study.  
    '''
    varlist = []
    for variable in range(len(var)):
        for study in range(len(data["References"])):
            if "Codes" in data["References"][study]:
                if "Outcomes" in data["References"][study]:
                    outerholder = []
                    for item in range(len(data["References"][study]["Outcomes"])):
                        innerholderholder = []
                        if "OutcomeCodes" in data["References"][study]["Outcomes"][item]:
                            for subsection in range(len(data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"])):
                                for key, value in var[variable].items():
                                    if key == data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeId"]:
                                        innerholderholder.append(
                                            data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeName"])
                        else:
                            innerholderholder = EXCLUDE
                        if len(innerholderholder) == 0:
                            innerholderholder = EXCLUDE
                        outerholder.append(innerholderholder)
                else:
                    outerholder = EXCLUDE
            varlist.append(outerholder)
    return varlist


# CEDIL Project
""" def get_data(codes):
    '''
    Extract study-level main data.
    Params: List/dict [{..}] of one or more AttributeID's and Attribute labels.
    Returns: A list of extracted data. One or more datapoints per study.
    '''
    df = []
    for var in range(len(codes)):
        holder = []
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                holderfind = []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            holderfind.append(value)
                if len(holderfind) == 0:
                    holderfind = EXCLUDE
                holder.append(holderfind)
        df.append(holder)
    return df """

#/*********************/
#/ SECONDARY FUNCTIONS /
#/*********************/


def getOutcomeData(dataframe, out_label, out_container, var_names):
    '''
    Extract strand level outcome data for main analysis dataframe
    '''
    from outcome_check import outcome_num
    for counter, row in enumerate(dataframe['out_type_1']):
            found = False
            for outcome_n in range(1, outcome_num + 1):
                if out_label in dataframe[f'out_type_{outcome_n}'][counter]:
                    found = True
                    for counter2, holder in enumerate(out_container):
                        holder.append(dataframe[var_names[counter2] + f"{outcome_n}"][counter])
                    break
            if not found:
                for holder in out_container:
                    holder.append("NA")
    return out_container


def get_outcome_data_lvl1(attribute_text, column_prefix):
    outcome_data = get_outcome_lvl1(attribute_text)
    outcome_df = pd.DataFrame(outcome_data)
    # round data to 4 decimal places
    outcome_df = outcome_df.applymap(lambda x: round(x, 4) if isinstance(x, (int, float)) else x)
    # name each column (number depends on outcome number)
    outcome_df.columns = [column_prefix+'{}'.format(column+1) for column in outcome_df.columns]
    outcome_df.fillna("NA", inplace=True)
    outcome_df = outcome_df.replace(r'^\s*$', "NA", regex=True)
    outcome_df.replace('\r', ' ', regex=True, inplace=True)
    outcome_df.replace('\n', ' ', regex=True, inplace=True)
    return outcome_df


def get_outcome_data_lvl2(attribute_codes, column_prefix):
    # get outcome data
    outcome_data = get_outcome_lvl2(attribute_codes)
    outcome_df = pd.DataFrame(outcome_data)
    # name each column (number depends on outcome number)
    outcome_df.columns = [column_prefix+'{}'.format(column+1) for column in outcome_df.columns]
    # fill blanks with NA
    outcome_df.fillna("NA", inplace=True)
    return outcome_df


def get_outfile_dir(df, df_name):
    '''
    Gets output file directory
    '''
    # Get current working dir
    cw = os.getcwd() + "/output"
    # get file name for output
    outfile_name_pre = data_file.rsplit('/')[-1] # 
    outfile_name_mid = outfile_name_pre.rsplit('.')[0]  # use for dir name
    outfile_name = outfile_name_mid + df_name
    outfile = os.path.join(cw + "/" + outfile_name_mid, outfile_name)  
    return outfile


def save_dataframe(df, df_name):
    '''
    Saves a .csv of the dataframe to output/
    '''
    # Get current working dir
    cw = os.getcwd() + "/output"
    # get file name for output
    outfile_name_pre = data_file.rsplit('/')[-1] # 
    outfile_name_mid = outfile_name_pre.rsplit('.')[0]  # use for dir name
    outfile_name = outfile_name_mid + df_name
    outfile = os.path.join(cw + "/" + outfile_name_mid, outfile_name)
    # Create dir (filename)
    try:
        os.mkdir("output/" + outfile_name_mid)
    except OSError:
        pass
    else:
        print("Successfully created {} directory".format("output/" + outfile_name_mid))
    # write to disk
    #print("Input file: {}\n".format(data_file))
    #print("Saving extracted output to: {}\n".format(outfile))
    df.to_csv(outfile, index=False)
    return outfile


def verbose_display(df):
    '''
    Displays further info
    '''
    # print dataframe
    print(df)
    print("\n")
    # list column names and position
    for counter, i in enumerate(df):
        print(counter, i)
    print("\n")
    # print dataframe info
    print("Columns: {}".format(df.shape[1]))
    print("Rows: {}".format(df.shape[0]))
    print("Datapoints: {}".format(df.shape[0] * df.shape[1]))
    print("\n")


def clean_up(df):
    """
    """
    df.replace('\r', ' ', regex=True, inplace=True)
    df.replace('\n', ' ', regex=True, inplace=True)
    df.replace(':', ' ',  regex=True, inplace=True)
    df.replace(';', ' ',  regex=True, inplace=True)

#/***********************************************/
#/   COMPILE DATA FRAMES FOR CHECKING/CLEANING   /
#/***********************************************/


def make_dataframe_1(save_file=True, clean_cols=True, verbose=True):
    """
    """
    eppiid_df = retrieve_metadata("ItemId", "id")
    author_df = retrieve_metadata("ShortTitle", "pub_author")
    year_df = retrieve_metadata("Year", "pub_year")
    abstract_df = retrieve_metadata("Abstract", "abstract")
    admin_strand_data = retrieve_data(admin_strand_output, "strand_raw")
    admin_strand_info = retrieve_info(admin_strand_output, "strand_info")
    pubtype_eppi_df = retrieve_metadata("TypeName", "pub_eppi")
    pub_type_data = retrieve_data(publication_type_output, "pub_type_raw")
    pub_type_ht = retrieve_ht(publication_type_output, "pubtype_ht")
    pub_type_info = retrieve_info(publication_type_output, "pubtype_info")
    country_df = retrieve_data(countries, "loc_country_raw")
    edu_setting_data = retrieve_data(edu_setting_output, "int_setting_raw")
    edu_setting_ht = retrieve_ht(edu_setting_output, "int_setting_ht")
    edu_setting_info = retrieve_info(edu_setting_output, "int_setting_info")
    study_realism_data = retrieve_data(study_realism_output, "eco_valid_raw")
    study_realism_ht = retrieve_ht(study_realism_output, "eco_valid_ht")
    study_realism_info = retrieve_info(study_realism_output, "eco_valid_info")
    student_age_data = retrieve_data(student_age_output, "part_age_raw")
    student_age_ht = retrieve_ht(student_age_output, "part_age_ht")
    student_age_info = retrieve_info(student_age_output, "part_age_info")
    number_of_school_int_info = retrieve_info(number_of_schools_intervention_output, "school_treat_info")
    number_of_school_int_ht = retrieve_ht(number_of_schools_intervention_output, "school_treat_ht")
    number_of_school_control_info = retrieve_info(number_of_schools_control_output, "school_cont_info")
    number_of_school_control_ht = retrieve_ht(number_of_schools_control_output, "school_cont_ht")
    number_of_school_total_info = retrieve_info(number_of_schools_total_output, "school_total_info")
    number_of_school_total_ht = retrieve_ht(number_of_schools_total_output, "school_total_ht")
    number_of_school_na_data = retrieve_data(number_of_schools_not_provided_output, "school_na_raw")
    number_of_school_na_info = retrieve_info(number_of_schools_not_provided_output, "school_na_info")
    number_of_school_na_ht = retrieve_ht(number_of_schools_not_provided_output, "school_na_ht")
    number_of_classes_int_info = retrieve_info(num_of_class_int_output, "class_treat_info")
    number_of_classes_int_ht = retrieve_ht(num_of_class_int_output, "class_treat_ht")
    number_of_classes_control_info = retrieve_info(num_of_class_cont_output, "class_cont_info")
    number_of_classes_control_ht = retrieve_ht(num_of_class_cont_output, "class_cont_ht")
    number_of_classes_total_info = retrieve_info(num_of_class_tot_output, "class_total_info")
    number_of_classes_total_ht = retrieve_ht(num_of_class_tot_output, "class_total_ht")
    number_of_classes_na_data = retrieve_data(numb_of_class_np_output, "class_na_raw")
    number_of_classes_na_info = retrieve_info(numb_of_class_np_output, "class_na_info")
    number_of_classes_na_ht = retrieve_ht(numb_of_class_np_output, "class_na_ht")
    treatment_group_data = retrieve_data(treatment_group, "treat_group_raw")
    treatment_group_ht = retrieve_ht(treatment_group, "treat_group_ht")
    treatment_group_info = retrieve_info(treatment_group, "treat_group_info")
    part_assig_data = retrieve_data(part_assign_output, "part_assig_raw")
    part_assig_ht = retrieve_ht(part_assign_output, "part_assig_ht")
    part_assig_info = retrieve_info(part_assign_output, "part_assig_info")
    level_of_assign_data = retrieve_data(level_of_assignment_output, "level_assig_raw")
    level_of_assign_ht = retrieve_ht(level_of_assignment_output, "level_assig_ht")
    level_of_assign_info = retrieve_info(level_of_assignment_output, "level_assig_info")
    study_design_data = retrieve_data(study_design_output, "int_desig_raw")
    study_design_ht = retrieve_ht(study_design_output, "int_design_ht")
    study_design_info = retrieve_info(study_design_output, "int_design_info")
    rand_data = retrieve_data(randomisation_details, "rand_raw")
    rand_ht = retrieve_ht(randomisation_details, "rand_ht")
    rand_info = retrieve_info(randomisation_details, "rand_info")
    other_outcomes_data = retrieve_data(other_out_output, "out_other_raw")
    other_outcomes_ht = retrieve_ht(other_out_output, "out_other_ht")
    other_outcomes_info = retrieve_info(other_out_output, "out_other_info")
    addit_out_data = retrieve_data(addit_out_output, "out_info_raw")
    addit_out_ht = retrieve_ht(addit_out_output, "out_info_ht")
    addit_out_info = retrieve_info(addit_out_output, "out_info_info")
    other_part_ht = retrieve_ht(other_part_output, "part_other_ht")
    other_part_info = retrieve_info(other_part_output, "part_other_info")
    all_variables = pd.concat([
        eppiid_df,
        author_df,
        year_df,
        abstract_df,
        admin_strand_data,
        admin_strand_info,
        pubtype_eppi_df,
        pub_type_data,
        pub_type_ht,
        pub_type_info,
        country_df,
        edu_setting_data,
        edu_setting_ht,
        edu_setting_info,
        study_realism_data,
        study_realism_ht,
        study_realism_info,
        student_age_data,
        student_age_ht,
        student_age_info,
        number_of_school_int_info,
        number_of_school_int_ht,
        number_of_school_control_info,
        number_of_school_control_ht,
        number_of_school_total_info,
        number_of_school_total_ht,
        number_of_school_na_data,
        number_of_school_na_info,
        number_of_school_na_ht,
        number_of_classes_int_info,
        number_of_classes_int_ht,
        number_of_classes_control_info,
        number_of_classes_control_ht,
        number_of_classes_total_info,
        number_of_classes_total_ht,
        number_of_classes_na_data,
        number_of_classes_na_info,
        number_of_classes_na_ht,
        treatment_group_data,
        treatment_group_ht,
        treatment_group_info,
        part_assig_data,
        part_assig_ht,
        part_assig_info,
        level_of_assign_data,
        level_of_assign_ht,
        level_of_assign_info,
        study_design_data,
        study_design_ht,
        study_design_info,
        rand_data,
        rand_ht,
        rand_info,
        other_outcomes_data,
        other_outcomes_ht,
        other_outcomes_info,
        addit_out_data,
        addit_out_ht,
        addit_out_info,
        other_part_ht,
        other_part_info,
    ], axis=1, sort=False)
    all_variables['part_assig_raw'] = all_variables['part_assig_raw'].str[0]
    all_variables['level_assig_raw'] = all_variables['level_assig_raw'].str[0]
    all_variables['rand_raw'] = all_variables['rand_raw'].apply(lambda x: ",".join(x) if isinstance(x, list) else x)
    all_variables['eco_valid_raw'] = all_variables['eco_valid_raw'].str[0]
    if clean_cols == True:
        # Insert empty columns for each variable for data 
        # checkers to log errors prior to main analysis
        cols_to_insert = {
            'strand_CLEAN': 6,
            'pub_eppi_CLEAN': 8,
            'pub_type_CLEAN': 12,
            'loc_country_CLEAN': 14,
            'int_Setting_CLEAN': 18,
            'eco_valid_CLEAN': 22,
            'part_age_CLEAN': 26,
            'school_treat_CLEAN': 29,
            'school_cont_CLEAN': 32,
            'school_total_CLEAN': 35,
            'school_na_CLEAN': 39,
            'class_treat_CLEAN': 42,
            'class_cont_CLEAN': 45,
            'class_total_CLEAN': 48,
            'class_na_CLEAN': 52,
            'treat_group_CLEAN': 56,
            'part_assig_CLEAN': 60,
            'level_assig_CLEAN': 64,
            'int_design_CLEAN': 68,
            'rand_CLEAN': 72,
            'out_other_CLEAN': 76,
            'out_info_CLEAN': 80,
            'part_other_CLEAN': 83
        }
    # Insert empty columns at specified locations
    for col_name, col_idx in cols_to_insert.items():
        all_variables.insert(col_idx, col_name, '')
    # Remove problematic text from outputs
    clean_up(all_variables)
    if verbose:
        verbose_display(all_variables)
    if save_file:
        outfile1 = save_dataframe(all_variables, "_DataFrame1.csv")
    return all_variables, outfile1


def make_dataframe_2(save_file=True, clean_cols=False, verbose=True):
    """
    """
    eppiid_df = retrieve_metadata("ItemId", "id")
    author_df = retrieve_metadata("ShortTitle", "pub_author")
    year_df = retrieve_metadata("Year", "pub_year")
    admin_strand_data = retrieve_data(admin_strand_output, "strand_raw")
    admin_strand_info = retrieve_info(admin_strand_output, "strand_info")
    intervention_name_ht = retrieve_ht(int_name_output, "int_name_ht")
    intervention_name_info = retrieve_info(int_name_output, "int_name_info")
    intervention_desc_ht = retrieve_ht(intervention_description_output, "int_desc_ht")
    intervention_desc_info = retrieve_info(intervention_description_output, "int_desc_info")
    intervention_objec_ht = retrieve_ht(intervention_objectives_output, "int_objec_ht")
    intervention_objec_info = retrieve_info(intervention_objectives_output, "int_objec_info")
    intervention_org_type_data = retrieve_data(int_org_type_output, "int_prov_raw")
    intervention_org_type_ht = retrieve_ht(int_org_type_output, "int_prov_ht")
    intervention_org_type_info = retrieve_info(int_org_type_output, "int_prov_info")
    intervention_training_prov_data = retrieve_data(int_training_provided_output, "int_training_raw")
    intervention_training_prov_ht = retrieve_ht(int_training_provided_output, "int_training_ht")
    intervention_training_prov_info = retrieve_info(int_training_provided_output, "int_training_info")
    intervention_focus_data = retrieve_data(int_focus_output, "int_part_raw")
    intervention_focus_ht = retrieve_ht(int_focus_output, "int_part_ht")
    intervention_focus_info= retrieve_info(int_focus_output, "int_part_info")
    intervention_teaching_app_data = retrieve_data(intervention_teaching_approach, "int_approach_raw")
    intervention_teaching_app_ht = retrieve_ht(intervention_teaching_approach, "int_approach_ht")
    intervention_teaching_app_info = retrieve_info(intervention_teaching_approach, "int_approach_info")
    digit_tech_data = retrieve_data(int_appr_dig_tech, "digit_tech_raw")
    digit_tech_ht = retrieve_ht(int_appr_dig_tech, "digit_tech_ht")
    digit_tech_info = retrieve_info(int_appr_dig_tech, "digit_tech_info")
    par_eng_data = retrieve_data(int_appr_par_or_comm_vol, "parent_partic_raw")
    par_eng_ht= retrieve_ht(int_appr_par_or_comm_vol, "parent_partic_ht")
    par_eng_info = retrieve_info(int_appr_par_or_comm_vol, "parent_partic_info")
    intervention_time_data = retrieve_data(intervention_time_output, "int_when_raw")
    intervention_time_ht = retrieve_ht(intervention_time_output, "int_when_ht")
    intervention_time_info = retrieve_info(intervention_time_output, "int_when_info")
    intervention_delivery_data = retrieve_data(intervention_delivery_output, "int_who_raw")
    intervention_delivery_ht = retrieve_ht(intervention_delivery_output, "int_who_ht")
    intervention_delivery_info = retrieve_info(intervention_delivery_output, "int_who_info")
    intervention_duration_ht = retrieve_ht(int_dur_output, "int_dur_ht")
    intervention_duration_info = retrieve_info(int_dur_output, "int_dur_info")
    intervention_frequency_ht = retrieve_ht(inte_freq_output, "int_freq_ht")
    intervention_frequency_info = retrieve_info(inte_freq_output, "int_freq_info")
    intervention_sess_length_ht = retrieve_ht(intervention_session_length_output, "int_leng_ht")
    intervention_sess_length_info = retrieve_info(intervention_session_length_output, "int_leng_info")
    intervention_detail_data = retrieve_data(int_impl_details, "int_fidel_raw")
    intervention_detail_ht = retrieve_ht(int_impl_details, "int_fidel_ht")
    intervention_detail_info = retrieve_info(int_impl_details, "int_fidel_info")
    intervention_costs_data = retrieve_data(int_costs_reported, "int_cost_raw")
    intervention_costs_ht = retrieve_ht(int_costs_reported, "int_cost_ht")
    intervention_costs_info = retrieve_info(int_costs_reported, "int_cost_info")
    #int_evaluation = retrieve_data(int_eval, "out_eval_raw")    
    #int_evaluation_ht = retrieve_ht(int_eval, "out_eval_ht")
    #int_evaluation_info = retrieve_info(int_eval, "out_eval_info")
    int_evaluation = int_eval()
    baseline_diff_data = retrieve_data(baseline_diff_output, "base_diff_raw")    
    baseline_diff_ht = retrieve_ht(baseline_diff_output, "base_diff_ht")
    baseline_diff_info = retrieve_info(baseline_diff_output, "base_diff_info")
    comp_anal_data = retrieve_data(comparability_output, "comp_anal_raw")    
    comp_anal_ht = retrieve_ht(comparability_output, "comp_anal_ht")
    comp_anal_info = retrieve_info(comparability_output, "comp_anal_info")
    comp_var_rep_data = retrieve_data(comp_vars_rep, "comp_var__raw")    
    comp_var_rep_ht = retrieve_ht(comp_vars_rep, "comp_var__ht")
    comp_var_rep_info = retrieve_info(comp_vars_rep, "comp_var__info")
    comp_var_rep_which_data = retrieve_data(which_comp_vars_rep_output, "comp_var_rep_raw")    
    comp_var_rep_which_ht = retrieve_ht(which_comp_vars_rep_output, "comp_var_rep_ht")
    comp_var_rep_which_info = retrieve_info(which_comp_vars_rep_output, "comp_var_rep_info")
    clustering_data = retrieve_data(clustering_output, "clust_anal_raw")    
    clustering_ht = retrieve_ht(clustering_output, "clust_anal_ht")
    clustering_info = retrieve_info(clustering_output, "clust_anal_info")
    all_variables = pd.concat([
        eppiid_df,
        author_df,
        year_df,
        admin_strand_data,
        admin_strand_info,
        intervention_name_ht,
        intervention_name_info,
        intervention_desc_ht,
        intervention_desc_info,
        intervention_objec_ht,
        intervention_objec_info,
        intervention_org_type_data,
        intervention_org_type_ht,
        intervention_org_type_info,
        intervention_training_prov_data,
        intervention_training_prov_ht,
        intervention_training_prov_info,
        intervention_focus_data,
        intervention_focus_ht,
        intervention_focus_info,
        intervention_teaching_app_data,
        intervention_teaching_app_ht,
        intervention_teaching_app_info,
        digit_tech_data,
        digit_tech_ht,
        digit_tech_info,
        par_eng_data,
        par_eng_ht,
        par_eng_info,
        intervention_time_data,
        intervention_time_ht,
        intervention_time_info,
        intervention_delivery_data,
        intervention_delivery_ht,
        intervention_delivery_info,
        intervention_duration_ht,
        intervention_duration_info,
        intervention_frequency_ht,
        intervention_frequency_info,
        intervention_sess_length_ht,
        intervention_sess_length_info, 
        intervention_detail_data,
        intervention_detail_ht,
        intervention_detail_info,
        intervention_costs_data,
        intervention_costs_ht,
        intervention_costs_info,
        int_evaluation,
        #int_evaluation,
        #int_evaluation_ht,
        #int_evaluation_info,
        baseline_diff_data,
        baseline_diff_ht,
        baseline_diff_info,
        comp_anal_data,
        comp_anal_ht,
        comp_anal_info,
        comp_var_rep_data, 
        comp_var_rep_ht,
        comp_var_rep_info,
        comp_var_rep_which_data,   
        comp_var_rep_which_ht,
        comp_var_rep_which_info,
        clustering_data,    
        clustering_ht,
        clustering_info,
    ], axis=1, sort=False)
    all_variables["eef_eval_raw"] = all_variables["out_eval_raw"].map(
                set(["Is this an EEF evaluation?"]).issubset).astype(int)
    all_variables["eef_eval_raw"] = all_variables["eef_eval_raw"].replace(
                to_replace=[0, 1], value=["No", "Yes"])
    if clean_cols:
        # Insert empty columns per variable for data checkers to log changes
        cols_to_insert = {
            'strand_CLEAN': 5,
            'int_name_CLEAN': 8,
            'int_desc_CLEAN': 11,
            'int_objec_CLEAN': 14,
            'int_prov_CLEAN': 18,
            'int_training_CLEAN': 22,
            'int_part_CLEAN': 26,
            'int_approach_CLEAN': 30,
            'digital_tech_CLEAN': 34,
            'parent_partic_CLEAN': 38,
            'int_when_CLEAN': 42,
            'int_who_CLEAN': 46,
            'int_dur_CLEAN': 49,
            'int_freq_CLEAN': 52,
            'int_leng_CLEAN': 55,
            'int_fidel_CLEAN': 59,
            'int_cost_CLEAN': 63,
            'out_eval_CLEAN': 67,
            'eef_eval_CLEAN': 69,
            'base_diff_CLEAN': 73,
            'comp_anal_CLEAN': 77,
            'comp_var_rep_CLEAN': 81,
            'comp_var_CLEAN': 85,
            'clust_anal_CLEAN': 89
        }
        for col_name, col_idx in cols_to_insert.items():
            all_variables.insert(col_idx, col_name, '')
    # Clean up data frame
    clean_up(all_variables)
    all_variables.replace(r'^\s*$', "NA", regex=True)
    if verbose:
        verbose_display(all_variables)
    if save_file:
        outfile2 = save_dataframe(all_variables, "_DataFrame2.csv")
    return all_variables, outfile2


def make_dataframe_3(save_file=True, clean_cols=False, verbose=False):
    """
    """
    eppiid_df = retrieve_metadata("ItemId", "id")
    author_df = retrieve_metadata("ShortTitle", "pub_author")
    year_df = retrieve_metadata("Year", "pub_year")
    admin_strand_data = retrieve_data(admin_strand_output, "strand_raw")
    admin_strand_info = retrieve_info(admin_strand_output, "strand_info")
    gender_df = retrieve_data(student_gender, "part_gen_raw")
    gender_ht_df = retrieve_ht(student_gender, "part_gen_ht")
    gender_comments_df = retrieve_info(student_gender, "part_gen_info")
    sample_size_comments_df = retrieve_info(sample_size_output, "sample_analysed_info")
    sample_size_ht_df = retrieve_ht(sample_size_output, "sample_analysed_ht")
    low_ses_percentage_Comments_df = retrieve_info(percentage_low_fsm_output, "fsm_perc_info")
    low_ses_percentage_HT_df = retrieve_ht(percentage_low_fsm_output, "fsm_perc_ht")
    further_ses_info_Comments_df = retrieve_info(further_ses_fsm_info_output, "fsm_info_info")
    further_ses_fsm_info_HT_df = retrieve_ht(further_ses_fsm_info_output, "fsm_info_ht")
    no_low_ses_fsm_info_df = retrieve_data(no_ses_fsm_info_provided_output, "fsm_na_raw")
    no_low_ses_fsm_info_comments_df = retrieve_info(no_ses_fsm_info_provided_output, "fsm_na_info")
    sample_size_intervention_HT_df = retrieve_ht(sample_size_intervention_output, "base_n_treat_ht")
    sample_size_intervention_Comments_df = retrieve_info(sample_size_intervention_output, "base_n_treat_info")
    sample_size_control_HT_df = retrieve_ht(sample_size_control_output,"base_n_cont_ht")
    sample_size_control_Comments_df = retrieve_info(sample_size_control_output,"base_n_cont_info")
    sample_size_second_intervention_HT_df = retrieve_ht(sample_size_second_intervention_output, "base_n_treat2_ht")
    sample_size_second_intervention_Comments_df = retrieve_info(sample_size_second_intervention_output, "base_n_treat2_info")
    sample_size_third_intervention_HT_df = retrieve_ht(sample_size_third_intervention_output, "base_n_treat3_ht")
    sample_size_third_intervention_Comments_df = retrieve_info(sample_size_third_intervention_output, "base_n_treat3_info")
    sample_size_anal_int_df = retrieve_ht(samp_size_anal_int_output, "n_treat_ht")
    sample_size_anal_int_comments_df = retrieve_info(samp_size_anal_int_output, "n_treat_info")
    sample_size_anal_cont_df = retrieve_ht(samp_size_anal_cont_output, "n_cont_ht")
    sample_size_anal_cont_comments_df = retrieve_info(samp_size_anal_cont_output, "n_cont_info")
    sample_size_anal_sec_int_df = retrieve_ht(samp_size_anal_sec_int_output, "n_treat2_ht")
    sample_size_anal_sec_int_comments_df = retrieve_info(samp_size_anal_sec_int_output, "n_treat2_info")
    sample_size_anal_sec_cont_df = retrieve_ht(samp_size_anal_sec_cont_output, "n_cont2_ht")
    sample_size_anal_sec_cont_comments_df = retrieve_info(samp_size_anal_sec_cont_output, "n_cont2_info")
    attr_dropout_rep_df = retrieve_data(attr_dropout_rep_output, "attri_raw")
    attr_dropout_rep_HT_df = retrieve_ht(attr_dropout_rep_output, "attri_ht")
    attr_dropout_rep_comments_df = retrieve_info(attr_dropout_rep_output, "attri_info")
    treat_grp_attr_HT_df = retrieve_ht(treat_grp_attr, "attri_treat_ht")
    treat_grp_attr_comments_df = retrieve_info(treat_grp_attr, "attri_treat_info")
    overall_perc_attr_HT_df = retrieve_ht(overall_perc_attr, "attri_perc_ht")
    overall_perc_attr_comments_df = retrieve_info(overall_perc_attr, "attri_perc_info")
    all_variables = pd.concat([
        eppiid_df,
        author_df,
        year_df,
        admin_strand_data,
        admin_strand_info,
        sample_size_comments_df,
        sample_size_ht_df,
        gender_df,
        gender_ht_df,
        gender_comments_df,
        low_ses_percentage_Comments_df,
        low_ses_percentage_HT_df,
        further_ses_info_Comments_df,
        further_ses_fsm_info_HT_df,
        no_low_ses_fsm_info_df,
        no_low_ses_fsm_info_comments_df,
        sample_size_intervention_HT_df,
        sample_size_intervention_Comments_df,
        sample_size_control_HT_df,
        sample_size_control_Comments_df,
        sample_size_second_intervention_HT_df,
        sample_size_second_intervention_Comments_df,
        sample_size_third_intervention_HT_df,
        sample_size_third_intervention_Comments_df,
        sample_size_anal_int_df,
        sample_size_anal_int_comments_df,
        sample_size_anal_cont_df,
        sample_size_anal_cont_comments_df,
        sample_size_anal_sec_int_df,
        sample_size_anal_sec_int_comments_df,
        sample_size_anal_sec_cont_df,
        sample_size_anal_sec_cont_comments_df,
        attr_dropout_rep_df,
        attr_dropout_rep_HT_df,
        attr_dropout_rep_comments_df,
        treat_grp_attr_HT_df,
        treat_grp_attr_comments_df,
        overall_perc_attr_HT_df,
        overall_perc_attr_comments_df,
    ], axis=1, sort=False)
    if clean_cols:
        # Insert empty columns per variable for data checkers to log changes
        cols_to_insert = {
            'strand_CLEAN': 5,
            'sample_analysed_CLEAN': 8,
            'part_gen_CLEAN': 12,
            'fsm_perc_CLEAN': 15,
            'fsm_info_CLEAN': 18,
            'fsm_na_CLEAN': 21,
            'base_n_treat_CLEAN': 24,
            'base_n_cont_CLEAN': 27,
            'base_n_treat2_CLEAN': 30,
            'base_n_treat3_CLEAN': 33,
            'n_treat_CLEAN': 36,
            'n_cont_CLEAN': 39,
            'n_treat2_CLEAN': 42,
            'n_cont2_CLEAN': 45,
            'attri_CLEAN': 49,
            'attri_treat_CLEAN': 52,
            'attri_perc_CLEAN': 55,
        }
        # Insert empty columns at specified locations
        for col_name, col_idx in cols_to_insert.items():
            all_variables.insert(col_idx, col_name, '')
    all_variables.replace('\r', ' ', regex=True, inplace=True)
    all_variables.replace('\n', ' ', regex=True, inplace=True)
    all_variables.replace(':', ' ',  regex=True, inplace=True)
    all_variables.replace(';', ' ',  regex=True, inplace=True)
    if verbose:
        verbose_display(all_variables)
    if save_file:
        outfile3 = save_dataframe(all_variables, "_DataFrame3_Sample_Size.csv")
    return all_variables, outfile3


def make_dataframe_4(save_file=True, clean_cols=True, verbose=True):
    """
    """
    eppiid_df = retrieve_metadata("ItemId", "id")
    author_df = retrieve_metadata("ShortTitle", "pub_author")
    year_df = retrieve_metadata("Year", "pub_year")
    admin_strand_data = retrieve_data(admin_strand_output, "strand_raw")
    admin_strand_info = retrieve_info(admin_strand_output, "strand_info") 
    desc_stats_prim_out_rep_df = retrieve_data(desc_stats_primary_outcome, "desc_stats_raw")
    desc_stats_prim_out_rep_ht_df = retrieve_ht(desc_stats_primary_outcome, "desc_stats_ht")
    descs_tats_prim_out_rep_comments_df = retrieve_info(desc_stats_primary_outcome, "desc_stats_info")
    int_grp_num_ht_df = retrieve_ht(int_grp_number, "n_treat_ht")
    int_grp_num_comments_df = process_info(int_grp_number, "n_treat_info")
    int_grp_pretest_mean_ht_df = retrieve_ht(int_grp_pretest_mean, "pre_t_mean_ht")
    int_grp_pretest_mean_comments_df = retrieve_info(int_grp_pretest_mean, "pre_t_mean_info")
    int_grp_pretest_sd_ht_df = retrieve_ht(int_grp_pretest_sd, "pre_t_sd_ht")
    int_grp_pretest_sd_comments_df = retrieve_info(int_grp_pretest_sd, "pre_t_sd_info")
    int_grp_posttest_mean_ht_df = retrieve_ht(intn_grp_posttest_mean, "post_t_mean_ht_t_sd_ht")
    int_grp_posttest_mean_comments_df = retrieve_info(intn_grp_posttest_mean, "post_t_mean_info")
    int_grp_posttest_sd_ht_df = retrieve_ht(int_grp_posttest_sd, "post_t_sd_ht")
    int_grp_posttest_sd_comments_df = retrieve_info(int_grp_posttest_sd, "post_t_sd_info")
    int_grp_gain_score_mean_ht_df = retrieve_ht(int_grp_gain_score_mean, "gain_t_mean_ht")
    int_grp_gain_score_mean_comments_df = retrieve_info(int_grp_gain_score_mean, "gain_t_mean_info")
    int_grp_gain_score_sd_ht_df = retrieve_ht(int_grp_gain_score_sd, "gain_t_sd_ht")
    int_grp_gain_score_sd_comments_df = retrieve_info(int_grp_gain_score_sd, "gain_t_sd_info")
    int_grp_other_info_ht_df = retrieve_ht(int_grp_any_other_info, "out_t_other_ht")
    int_grp_other_info_comments_df = retrieve_info(int_grp_any_other_info, "out_t_other_info")
    ctrl_grp_num_ht_df = retrieve_ht(ctrl_grp_number, "n_cont_ht")
    ctrl_grp_num_comments_df = retrieve_info(ctrl_grp_number, "n_cont_info")
    ctrl_grp_pretest_mean_ht_df = retrieve_ht(ctrl_grp_pretest_mean, "pre_c_mean_ht")
    ctrl_grp_pretest_mean_comments_df = retrieve_info(ctrl_grp_pretest_mean, "pre_c_mean_info")
    ctrl_grp_pretest_sd_ht_df = retrieve_ht(ctrl_grp_pretest_sd, "pre_c_sd_ht")
    ctrl_grp_pretest_sd_comments_df = retrieve_info(ctrl_grp_pretest_sd, "pre_c_sd_info")
    ctrl_grp_post_test_mean_ht_df = retrieve_ht(ctrl_grp_posttest_mean, "post_c_mean_ht")
    ctrl_grp_post_test_mean_comments_df = retrieve_info(ctrl_grp_posttest_mean, "post_c_mean_info")
    ctrl_grp_post_test_sd_ht_df = retrieve_ht(ctrl_grp_posttest_sd, "post_c_sd_ht")
    ctrl_grp_post_test_sd_comments_df = retrieve_info(ctrl_grp_posttest_sd, "post_c_sd_info")
    Ctrl_grp_gain_score_mean_ht_df = retrieve_ht(ctrl_grp_gain_score_mean, "gain_c_mean_ht")
    ctrl_grp_gain_score_mean_comments_df = retrieve_info(ctrl_grp_gain_score_mean, "gain_c_mean_info")
    ctrl_grp_gain_score_sd_ht_df = retrieve_ht(ctrl_grp_gain_score_sd, "gain_c_sd_ht")
    ctrl_grp_gain_score_sd_comments_df = retrieve_info(ctrl_grp_gain_score_sd, "gain_c_sd_info")
    ctrl_grp_other_info_ht_df = retrieve_ht(ctrl_grp_any_other_info, "out_c_other_ht")
    ctrl_grp_other_info_comments_df = retrieve_info(ctrl_grp_any_other_info, "out_c_other_info")
    int_grp_num2_ht_df = retrieve_ht(int_grp_two_number, "n_treat2_ht")
    int_grp_num2_comments_df = retrieve_info(int_grp_two_number, "n_treat2_info")
    int_grp_pretest2_mean_ht_df = retrieve_ht(int_grp_two_pretest_mean, "pre_t2_mean_ht")
    int_grp_pretest2_mean_comments_df = retrieve_info(int_grp_two_pretest_mean, "pre_t2_mean_info")
    int_grp_pretest2_sd_ht_df = retrieve_ht(int_grp_two_pretest_sd, "pre_t2_sd_ht")
    int_grp_pretest2_sd_comments_df = retrieve_info(int_grp_two_pretest_sd, "pre_t2_sd_info")
    int_grp_post2_test_mean_ht_df = retrieve_ht(int_grp_two_posttest_mean, "post_t2_mean_ht")
    int_grp_post2_test_mean_comments_df = retrieve_info(int_grp_two_posttest_mean, "post_t2_mean_info")
    int_grp_post2_test_sd_ht_df = retrieve_ht(int_grp_two_posttest_sd, "post_t2_sd_ht")
    int_grp_post2_test_sd_comments_df = retrieve_info(int_grp_two_posttest_sd, "post_t2_sd_info")
    int_grp_gain2_score_mean_ht_df = retrieve_ht(int_grp_two_gain_score_mean, "gain_t2_mean_ht")
    int_grp_gain2_score_mean_comments_df = retrieve_info(int_grp_two_gain_score_mean, "gain_t2_mean_info")
    int_grp_gain2_score_sd_ht_df = retrieve_ht(int_grp_two_gain_score_sd, "gain_t2_sd_ht")
    int_grp_gain2_score_sd_comments_df = retrieve_info(int_grp_two_gain_score_sd, "gain_t2_sd_info")
    int_grp_other2_info_ht_df = retrieve_ht(int_grp_two_any_other_info, "out_t2_other_ht")
    int_grp_other2_info_comments_df = retrieve_info(int_grp_two_any_other_info, "out_t2_other_info")
    ctrl_grp_num2_ht_df = retrieve_ht(control_group_two_number, "n_cont2_ht")
    ctrl_grp_num2_comments_df = retrieve_info(control_group_two_number, "n_cont2_info")
    ctrl_grp_pretest2_mean_ht_df = retrieve_ht(control_group_two_pretest_mean, "pre_c2_mean_ht")
    ctrl_grp_pretest2_mean_comments_df = retrieve_info(control_group_two_pretest_mean, "pre_c2_mean_info")
    ctrl_grp_pretest2_sd_ht_df = retrieve_ht(control_group_two_pretest_sd, "pre_c2_sd_ht")
    ctrl_grp_pretest2_sd_comments_df = retrieve_info(control_group_two_pretest_sd, "pre_c2_sd_info")
    ctrl_grp_post2_test_mean_ht_df = retrieve_ht(control_group_two_posttest_mean, "post_c2_mean_ht")
    ctrl_grp_post2_test_mean_comments_df = retrieve_info(control_group_two_posttest_mean, "post_c2_mean_info")
    ctrl_grp_post2_test_sd_ht_df = retrieve_ht(control_group_two_posttest_sd, "post_c2_sd_ht")
    ctrl_grp_post2_test_sd_comments_df = retrieve_info(control_group_two_posttest_sd, "post_c2_sd_info")
    Ctrl_grp_gain2_score_mean_ht_df = retrieve_ht(control_group_two_gain_score_mean, "gain_c2_mean_ht")
    ctrl_grp_gain2_score_mean_comments_df = retrieve_info(control_group_two_gain_score_mean, "gain_c2_mean_info")
    ctrl_grp_gain2_score_sd_ht_df = retrieve_ht(control_group_two_gain_score_sd, "gain_c2_sd_ht")
    ctrl_grp_gain2_score_sd_comments_df = retrieve_info(control_group_two_gain_score_sd, "gain_c2_sd_info")
    ctrl_grp_other2_info_ht_df = retrieve_ht(control_group_two_any_other_info, "out_c2_other_ht")
    ctrl_grp_other2_info_comments_df = retrieve_info(control_group_two_any_other_info, "out_c2_other_info")
    followupdata = retrieve_data(follow_up_data_reported, "follow_up_raw")
    followupdata_HT = retrieve_ht(follow_up_data_reported, "follow_up_ht")
    followupdata_comments = retrieve_info(follow_up_data_reported, "follow_up_info")
    all_variables = pd.concat([
        eppiid_df,
        author_df,
        year_df,
        admin_strand_data,
        admin_strand_info,
        desc_stats_prim_out_rep_df,
        desc_stats_prim_out_rep_ht_df,
        descs_tats_prim_out_rep_comments_df,
        int_grp_num_ht_df,
        int_grp_num_comments_df,
        int_grp_pretest_mean_ht_df,
        int_grp_pretest_mean_comments_df,
        int_grp_pretest_sd_ht_df,
        int_grp_pretest_sd_comments_df,
        int_grp_posttest_mean_ht_df,
        int_grp_posttest_mean_comments_df,
        int_grp_posttest_sd_ht_df,
        int_grp_posttest_sd_comments_df,
        int_grp_gain_score_mean_ht_df,
        int_grp_gain_score_mean_comments_df,
        int_grp_gain_score_sd_ht_df,
        int_grp_gain_score_sd_comments_df,
        int_grp_other_info_ht_df,
        int_grp_other_info_comments_df,
        ctrl_grp_num_ht_df,
        ctrl_grp_num_comments_df,
        ctrl_grp_pretest_mean_ht_df,
        ctrl_grp_pretest_mean_comments_df,
        ctrl_grp_pretest_sd_ht_df,
        ctrl_grp_pretest_sd_comments_df,
        ctrl_grp_post_test_mean_ht_df,
        ctrl_grp_post_test_mean_comments_df,
        ctrl_grp_post_test_sd_ht_df,
        ctrl_grp_post_test_sd_comments_df,
        Ctrl_grp_gain_score_mean_ht_df,
        ctrl_grp_gain_score_mean_comments_df,
        Ctrl_grp_gain_score_mean_ht_df,
        ctrl_grp_gain_score_mean_comments_df,
        ctrl_grp_gain_score_sd_ht_df,
        ctrl_grp_gain_score_sd_comments_df,
        ctrl_grp_other_info_ht_df,
        ctrl_grp_other_info_comments_df,
        int_grp_num2_ht_df,
        int_grp_num2_comments_df,
        int_grp_pretest2_mean_ht_df,
        int_grp_pretest2_mean_comments_df,
        int_grp_pretest2_sd_ht_df,
        int_grp_pretest2_sd_comments_df,
        int_grp_post2_test_mean_ht_df,
        int_grp_post2_test_mean_comments_df,
        int_grp_post2_test_sd_ht_df,
        int_grp_post2_test_sd_comments_df,
        int_grp_gain2_score_mean_ht_df,
        int_grp_gain2_score_mean_comments_df,
        int_grp_gain2_score_sd_ht_df,
        int_grp_gain2_score_sd_comments_df,
        int_grp_other2_info_ht_df,
        int_grp_other2_info_comments_df,
        ctrl_grp_num2_ht_df,
        ctrl_grp_num2_comments_df,
        ctrl_grp_pretest2_mean_ht_df,
        ctrl_grp_pretest2_mean_comments_df,
        ctrl_grp_pretest2_sd_ht_df,
        ctrl_grp_pretest2_sd_comments_df,
        ctrl_grp_post2_test_mean_ht_df,
        ctrl_grp_post2_test_mean_comments_df,
        ctrl_grp_post2_test_sd_ht_df,
        ctrl_grp_post2_test_sd_comments_df,
        Ctrl_grp_gain2_score_mean_ht_df,
        ctrl_grp_gain2_score_mean_comments_df,
        ctrl_grp_gain2_score_sd_ht_df,
        ctrl_grp_gain2_score_sd_comments_df,
        ctrl_grp_other2_info_ht_df,
        ctrl_grp_other2_info_comments_df,
        followupdata,
        followupdata_HT,
        followupdata_comments,
    ], axis=1, sort=False)
    if clean_cols:
        # Define columns to insert and their corresponding indices
        cols_to_insert = {
            'desc_stats_CLEAN': 8,
            'n_treat_CLEAN': 11,
            'pre_t_mean_CLEAN': 14,
            'pre_t_sd_CLEAN': 17,
            'post_t_mean_CLEAN': 20,
            'post_t_sd_CLEAN': 23,
            'gain_t_mean_CLEAN': 26,
            'gain_t_sd_CLEAN': 29,
            'out_t_other_CLEAN': 32,
            'n_cont_ht_CLEAN': 35,
            'pre_c_mean_CLEAN': 38,
            'pre_c_sd_CLEAN': 41,
            'post_c_mean_CLEAN': 44,
            'post_c_sd_CLEAN': 47,
            'gain_c_mean_CLEAN': 50,
            'gain_c_sd_CLEAN': 53,
            'out_c_other_CLEAN': 56,
            'n_treat2_CLEAN': 59,
            'pre_t2_mean_CLEAN': 62,
            'pre_t2_sd_CLEAN': 65,
            'post_t2_mean_CLEAN': 68,
            'post_t2_sd_CLEAN': 71,
            'gain_t2_mean_CLEAN': 74,
            'gain_t2_sd_CLEAN': 77,
            'out_t2_other_CLEAN': 80,
            'n_cont2_CLEAN': 83,
            'pre_c2_mean_CLEAN': 86,
            'pre_c2_sd_CLEAN': 89,
            'post_c2_mean_CLEAN': 92,
            'post_c2_sd_CLEAN': 95,
            'gain_c2_mean_CLEAN': 98,
            'gain_c2_sd_CLEAN': 101,
            'out_c2_other_CLEAN': 104,
            'follow_up_CLEAN': 108
        }
        # Insert empty columns into DataFrame
        for col_name, col_idx in cols_to_insert.items():
            all_variables.insert(col_idx, col_name, '')
        clean_up(all_variables)
    if verbose:
        verbose_display(all_variables)
    if save_file:
        outfile4 = save_dataframe(all_variables, "_DataFrame4_Effect_Size_A.csv")
    return all_variables, outfile4


def make_dataframe_5(save_file=True, clean_cols=True, verbose=True):
    """
    """
    OUTCOME_VARS = (
        "out_type_",
        "smd_",
        "se_",
        "ci_lower_",
        "ci_upper_",
        "out_label_",
        "out_samp_",
        "out_comp_",
        "out_es_type_",
        "out_measure_",
        "out_tit_",
        "out_g1_n_",
        "out_g2_n_",
        "out_g1_mean_",
        "out_g2_mean_",
        "out_g1_sd_",
        "out_g2_sd_",
        "out_desc_",
        "out_test_type_raw_"
    )
    global toolkit_test_type, toolkit_es_type
    from outcome_check import outcome_num
    eppiid_df = retrieve_metadata("ItemId", "id")
    author_df = retrieve_metadata("ShortTitle", "pub_author")
    year_df = retrieve_metadata("Year", "pub_year")
    admin_strand_data = retrieve_data(admin_strand_output, "strand_raw")
    admin_strand_info = retrieve_info(admin_strand_output, "strand_info")
    outcometype_df = get_outcome_data_lvl2(outcome_type_codes, "out_type_")
    smd_df = get_outcome_data_lvl1("SMD", "smd_")
    sesmd_df = get_outcome_data_lvl1("SESMD", "se_")
    cilowersmd_df = get_outcome_data_lvl1("CILowerSMD", "ci_lower_")
    ciuppersmd_df = get_outcome_data_lvl1("CIUpperSMD", "ci_upper_")
    outcome_df = get_outcome_data_lvl1("OutcomeText", "out_label_")
    sample_df = get_outcome_data_lvl2(sample_output, "out_samp_")
    sample_check = sample_main_check()
    out_comp_df = get_outcome_data_lvl1("ControlText", "out_comp_")
    effectsizetype_df = get_outcome_data_lvl2(es_type_output, "out_es_type_")
    outcome_measure_df = get_outcome_data_lvl1("InterventionText", "out_measure_")
    outcome_title_df = get_outcome_data_lvl1("Title", "out_tit_")
    group1N_df = group_desc_stats("Data1", "out_g1_n_")
    group2N_df = group_desc_stats("Data2", "out_g2_n_")
    group1mean_df = group_desc_stats("Data3", "out_g1_mean_")
    group2mean_df = group_desc_stats("Data4", "out_g2_mean_")
    group1sd_df = group_desc_stats("Data5", "out_g1_sd_")
    group2sd_df = group_desc_stats("Data6", "out_g2_sd_")
    outcome_description_df = get_outcome_data_lvl1("OutcomeDescription", "out_desc_")
    testtype_outcome_df = get_outcome_data_lvl2(test_type_output, "out_test_type_raw_")
    # Concatenate record detail data frames
    record_details_df = pd.concat([
        eppiid_df,
        author_df,
        year_df,
        admin_strand_data,
        admin_strand_info
    ], axis=1)
    # Concatenate all main dataframes
    df = pd.concat([
        outcometype_df,
        smd_df,
        sesmd_df,
        cilowersmd_df,
        ciuppersmd_df,
        outcome_df,
        sample_df,
        sample_check,
        out_comp_df,
        effectsizetype_df,
        outcome_measure_df,
        outcome_title_df,
        group1N_df,
        group2N_df,
        group1mean_df,
        group2mean_df,
        group1sd_df,
        group2sd_df,
        outcome_description_df,
        testtype_outcome_df
    ], axis=1)[list(interleave([
        outcometype_df,
        smd_df,
        sesmd_df,
        cilowersmd_df,
        ciuppersmd_df,
        outcome_df,
        sample_df,
        sample_check,
        out_comp_df,
        effectsizetype_df,
        outcome_measure_df,
        outcome_title_df,
        group1N_df,
        group2N_df,
        group1mean_df,
        group2mean_df,
        group1sd_df,
        group2sd_df,
        outcome_description_df,
        testtype_outcome_df
    ]))]
    toolkit_lists = [[] for _ in range(19)]
    # Initialize empty lists to hold data
    (toolkit_prim,
    toolkit_prim_smd,
    toolkit_prim_se,
    toolkit_prim_ci_lower,
    toolkit_prim_ci_upper,
    toolkit_prim_outcome,
    toolkit_prim_sample,
    toolkit_prim_outcomp,
    toolkit_es_type,
    toolkit_out_measure,
    toolkit_out_tit,
    toolkit_g1_n,
    toolkit_g2_n,
    toolkit_g1_mean,
    toolkit_g2_mean,
    toolkit_g1_sd,
    toolkit_g2_sd,
    toolkit_out_desc,
    toolkit_test_type) = toolkit_lists
    toolkit_lists = getOutcomeData(df, 'Toolkit primary outcome', toolkit_lists, OUTCOME_VARS)
    reading_lists = [[] for _ in range(19)]
    (reading_prim,
    reading_prim_smd,
    reading_prim_se,
    reading_prim_ci_lower,
    reading_prim_ci_upper,
    reading_prim_outcome,
    reading_prim_sample,
    reading_prim_outcomp,
    reading_prim_es_type,
    reading_prim_out_measure,
    reading_prim_out_tit,
    reading_prim_g1_n,
    reading_prim_g2_n,
    reading_prim_g1_mean,
    reading_prim_g2_mean,
    reading_prim_g1_sd,
    reading_prim_g2_sd,
    reading_prim_out_desc,
    reading_test_type) = reading_lists
    reading_lists = getOutcomeData(df, 'Reading primary outcome', reading_lists, OUTCOME_VARS)
    writing_and_spelling_lists = [[] for _ in range(19)]
    (Writing_and_spelling_prim,
    Writing_and_spelling_prim_smd,
    Writing_and_spelling_prim_se,
    Writing_and_spelling_prim_ci_lower,
    Writing_and_spelling_prim_ci_upper,
    Writing_and_spelling_prim_outcome,
    Writing_and_spelling_prim_sample,
    Writing_and_spelling_prim_outcomp,
    Writing_and_spelling_prim_es_type,
    Writing_and_spelling_prim_out_measure,
    Writing_and_spelling_prim_out_tit,
    Writing_and_spelling_prim_g1_n,
    Writing_and_spelling_prim_g2_n,
    Writing_and_spelling_prim_g1_mean,
    Writing_and_spelling_prim_g2_mean,
    Writing_and_spelling_prim_g1_sd,
    Writing_and_spelling_prim_g2_sd,
    Writing_and_spelling_prim_out_desc,
    Writing_and_spelling_test_type) = writing_and_spelling_lists
    writing_and_spelling_lists = getOutcomeData(df, 'Writing and spelling primary outcome', writing_and_spelling_lists, OUTCOME_VARS)
    mathematics_lists = [[] for _ in range(19)]
    (Mathematics_prim,
    Mathematics_prim_smd,
    Mathematics_prim_se,
    Mathematics_prim_ci_lower,
    Mathematics_prim_ci_upper,
    Mathematics_prim_outcome,
    Mathematics_prim_sample,
    Mathematics_prim_outcomp,
    Mathematics_prim_es_type,
    Mathematics_prim_out_measure,
    Mathematics_prim_out_tit,
    Mathematics_prim_g1_n,
    Mathematics_prim_g2_n,
    Mathematics_prim_g1_mean,
    Mathematics_prim_g2_mean,
    Mathematics_prim_g1_sd,
    Mathematics_prim_g2_sd,
    Mathematics_prim_out_desc,
    Mathematics_test_type) = mathematics_lists
    mathematics_lists = getOutcomeData(df, 'Mathematics primary outcome', mathematics_lists, OUTCOME_VARS)
    science_lists = [[] for _ in range(19)]
    (Science_prim,
    Science_prim_smd,
    Science_prim_se,
    Science_prim_ci_lower,
    Science_prim_ci_upper,
    Science_prim_outcome,
    Science_prim_sample,
    Science_prim_outcomp,
    Science_prim_es_type,
    Science_prim_out_measure,
    Science_prim_out_tit,
    Science_prim_g1_n,
    Science_prim_g2_n,
    Science_prim_g1_mean,
    Science_prim_g2_mean,
    Science_prim_g1_sd,
    Science_prim_g2_sd,
    Science_prim_out_desc,
    Science_test_type) = science_lists
    science_lists = getOutcomeData(df, 'Science primary outcome', science_lists, OUTCOME_VARS)
    fsm_lists = [[] for _ in range(19)]
    (FSM_prim,
    FSM_prim_smd,
    FSM_prim_se,
    FSM_prim_ci_lower,
    FSM_prim_ci_upper,
    FSM_prim_outcome,
    FSM_prim_sample,
    FSM_prim_outcomp,
    FSM_prim_es_type,
    FSM_prim_out_measure,
    FSM_prim_out_tit,
    FSM_prim_g1_n,
    FSM_prim_g2_n,
    FSM_prim_g1_mean,
    FSM_prim_g2_mean,
    FSM_prim_g1_sd,
    FSM_prim_g2_sd,
    FSM_prim_out_desc,
    FSM_test_type) = fsm_lists
    science_lists = getOutcomeData(df, 'SES/FSM primary outcome', fsm_lists, OUTCOME_VARS)
    df_zip = list(zip(
        toolkit_out_tit,
        toolkit_out_desc,
        toolkit_prim,
        toolkit_prim_smd,
        toolkit_prim_se,
        toolkit_out_measure,
        toolkit_g1_n,
        toolkit_g1_mean,
        toolkit_g1_sd,
        toolkit_g2_n,
        toolkit_g2_mean,
        toolkit_g2_sd,
        toolkit_prim_ci_lower,
        toolkit_prim_ci_upper,
        toolkit_prim_outcome,
        toolkit_prim_sample,
        toolkit_prim_outcomp,
        toolkit_es_type,
        toolkit_test_type,
        reading_prim_out_tit,
        reading_prim_out_desc,
        reading_prim,
        reading_prim_smd,
        reading_prim_se,
        reading_prim_out_measure,
        reading_prim_g1_n,
        reading_prim_g1_mean,
        reading_prim_g1_sd,
        reading_prim_g2_n,
        reading_prim_g2_mean,
        reading_prim_g2_sd,
        reading_prim_ci_lower,
        reading_prim_ci_upper,
        reading_prim_outcome,
        reading_prim_sample,
        reading_prim_outcomp,
        reading_prim_es_type,
        reading_test_type,
        Writing_and_spelling_prim_out_tit,
        Writing_and_spelling_prim_out_desc,
        Writing_and_spelling_prim,
        Writing_and_spelling_prim_smd,
        Writing_and_spelling_prim_se,
        Writing_and_spelling_prim_out_measure,
        Writing_and_spelling_prim_g1_n,
        Writing_and_spelling_prim_g1_mean,
        Writing_and_spelling_prim_g1_sd,
        Writing_and_spelling_prim_g2_n,
        Writing_and_spelling_prim_g2_mean,
        Writing_and_spelling_prim_g2_sd,
        Writing_and_spelling_prim_ci_lower,
        Writing_and_spelling_prim_ci_upper,
        Writing_and_spelling_prim_outcome,
        Writing_and_spelling_prim_sample,
        Writing_and_spelling_prim_outcomp,
        Writing_and_spelling_prim_es_type,
        Writing_and_spelling_test_type,
        Mathematics_prim_out_tit,
        Mathematics_prim_out_desc,
        Mathematics_prim,
        Mathematics_prim_smd,
        Mathematics_prim_se,
        Mathematics_prim_out_measure,
        Mathematics_prim_g1_n,
        Mathematics_prim_g1_mean,
        Mathematics_prim_g1_sd,
        Mathematics_prim_g2_n,
        Mathematics_prim_g2_mean,
        Mathematics_prim_g2_sd,
        Mathematics_prim_ci_lower,
        Mathematics_prim_ci_upper,
        Mathematics_prim_outcome,
        Mathematics_prim_sample,
        Mathematics_prim_outcomp,
        Mathematics_prim_es_type,
        Mathematics_test_type,
        Science_prim_out_tit,
        Science_prim_out_desc,
        Science_prim,
        Science_prim_smd,
        Science_prim_se,
        Science_prim_out_measure,
        Science_prim_g1_n,
        Science_prim_g1_mean,
        Science_prim_g1_sd,
        Science_prim_g2_n,
        Science_prim_g2_mean,
        Science_prim_g2_sd,
        Science_prim_ci_lower,
        Science_prim_ci_upper,
        Science_prim_outcome,
        Science_prim_sample,
        Science_prim_outcomp,
        Science_prim_es_type,
        Science_test_type,
        FSM_prim_out_tit,
        FSM_prim_out_desc,
        FSM_prim,
        FSM_prim_smd,
        FSM_prim_se,
        FSM_prim_out_measure,
        FSM_prim_g1_n,
        FSM_prim_g1_mean,
        FSM_prim_g1_sd,
        FSM_prim_g2_n,
        FSM_prim_g2_mean,
        FSM_prim_g2_sd,
        FSM_prim_ci_lower,
        FSM_prim_ci_upper,
        FSM_prim_outcome,
        FSM_prim_sample,
        FSM_prim_outcomp,
        FSM_prim_es_type,
        FSM_test_type
    ))
    df = pd.DataFrame(df_zip)
    df.rename(columns={
        0: "out_tit_tool",
        1: "out_desc_tool",
        2: "out_type_tool",
        3: "smd_tool",
        4: "se_tool",
        5: "out_measure_tool",
        6: "out_g1_n_tool",
        7: "out_g1_mean_tool",
        8: "out_g1_sd_tool",
        9: "out_g2_n_tool",
        10: "out_g2_mean_tool",
        11: "out_g2_sd_tool",
        12: "ci_lower_tool",
        13: "ci_upper_tool",
        14: "out_label_tool",
        15: "out_samp_tool",
        16: "out_comp_tool",
        17: "out_es_type_tool",
        18: "out_test_type_raw_tool",
        19: "out_tit_red",
        20: "out_desc_red",
        21: "out_type_red",
        22: "smd_red",
        23: "se_red",
        24: "out_measure_red",
        25: "out_g1_n_red",
        26: "out_g1_mean_red",
        27: "out_g1_sd_red",
        28: "out_g2_n_red",
        29: "out_g2_mean_red",
        30: "out_g2_sd_red",
        31: "ci_lower_red",
        32: "ci_upper_red",
        33: "out_label_red",
        34: "out_samp_red",
        35: "out_comp_red",
        36: "out_es_type_red",
        37: "out_test_type_raw_red",
        38: "out_tit_wri",
        39: "out_desc_wri",
        40: "out_type_wri",
        41: "smd_wri",
        42: "se_wri",
        43: "out_measure_wri",
        44: "out_g1_n_wri",
        45: "out_g1_mean_wri",
        46: "out_g1_sd_wri",
        47: "out_g2_n_wri",
        48: "out_g2_mean_wri",
        49: "out_g2_sd_wri",
        50: "ci_lower_wri",
        51: "ci_upper_wri",
        52: "out_label_wri",
        53: "out_samp_wri",
        54: "out_comp_wri",
        55: "out_es_type_wri",
        56: "out_test_type_raw_wri",
        57: "out_tit_math",
        58: "out_desc_math",
        59: "out_type_math",
        60: "smd_math",
        61: "se_math",
        62: "out_measure_math",
        63: "out_g1_n_math",
        64: "out_g1_mean_math",
        65: "out_g1_sd_math",
        66: "out_g2_n_math",
        67: "out_g2_mean_math",
        68: "out_g2_sd_math",
        69: "ci_lower_math",
        70: "ci_upper_math",
        71: "out_label_math",
        72: "out_samp_math",
        73: "out_comp_math",
        74: "out_es_type_math",
        75: "out_test_type_raw_math",
        76: "out_tit_sci",
        77: "out_desc_sci",
        78: "out_type_sci",
        79: "smd_sci",
        80: "se_sci",
        81: "out_measure_sci",
        82: "out_g1_n_sci",
        83: "out_g1_mean_sci",
        84: "out_g1_sd_sci",
        85: "out_g2_n_sci",
        86: "out_g2_mean_sci",
        87: "out_g2_sd_sci",
        88: "ci_lower_sci",
        89: "ci_upper_sci",
        90: "out_label_sci",
        91: "out_samp_sci",
        92: "out_comp_sci",
        93: "out_es_type_sci",
        94: "out_test_type_raw_sci",
        95: "out_tit_fsm",
        96: "out_desc_fsm",
        97: "out_type_fsm",
        98: "smd_fsm",
        99: "se_fsm",
        100: "out_measure_fsm",
        101: "out_g1_n_fsm",
        102: "out_g1_mean_fsm",
        103: "out_g1_sd_fsm",
        104: "out_g2_n_fsm",
        105: "out_g2_mean_fsm",
        106: "out_g2_sd_fsm",
        107: "ci_lower_fsm",
        108: "ci_upper_fsm",
        109: "out_label_fsm",
        110: "out_samp_fsm",
        111: "out_comp_fsm",
        112: "out_es_type_fsm",
        113: "out_test_type_raw_fsm"
    }, inplace=True)
    # Concatenate record details and main dataframes
    all_variables = pd.concat([record_details_df, df], axis=1, sort=False)
    if clean_cols:
        new_cols = [
            "out_tit_tool",
            'out_tit_tool_CLEAN',
            "out_desc_tool",
            'out_desc_tool_CLEAN', 
            "out_type_tool",
            'out_type_tool_CLEAN',
            "smd_tool",
            'smd_tool_CLEAN',
            "se_tool",
            'se_tool_CLEAN',
            "out_measure_tool",
            'out_measure_tool_CLEAN',
            "out_g1_n_tool",
            'out_g1_n_tool_CLEAN',
            "out_g1_mean_tool",
            'out_g1_mean_tool_CLEAN',
            "out_g1_sd_tool",
            'out_g1_sd_tool_CLEAN',
            "out_g2_n_tool",
            'out_g2_n_tool_CLEAN',
            "out_g2_mean_tool",
            'out_g2_mean_tool_CLEAN',
            "out_g2_sd_tool",
            'out_g2_sd_tool_CLEAN',
            "ci_lower_tool",
            'ci_lower_tool_CLEAN', 
            "ci_upper_tool",
            'ci_upper_tool_CLEAN',
            "out_label_tool",
            'out_label_tool_CLEAN',
            "out_samp_tool",
            'out_samp_tool_CLEAN',
            "out_comp_tool",
            'out_comp_tool_CLEAN', 
            "out_es_type_tool",
            'out_es_type_tool_CLEAN',
            "out_test_type_raw_tool",
            'out_test_type_raw_tool_CLEAN'
        ]
        all_variables = df.reindex(columns=new_cols, fill_value='')
        all_variables = pd.concat([record_details_df, all_variables], axis=1, sort=False)
    if verbose:
        verbose_display(all_variables)
    if save_file:
        outfile5 = save_dataframe(all_variables, "_DataFrame5_Effect_Size_B.csv")
    return all_variables, outfile5


def make_dataframe_6(ss_df, save_file=True, verbose=True):
    """
    """
    eppiid_df = retrieve_metadata("ItemId", "id")
    author_df = retrieve_metadata("ShortTitle", "pub_author")
    year_df = retrieve_metadata("Year", "pub_year")
    pub_type_data = retrieve_data(publication_type_output, "pub_type_raw")
    toolkitstrand_df = get_outcome_data_lvl2(toolkit_strand_codes, "out_strand_")
    smd_df = get_outcome_data_lvl1("SMD", "smd_")
    sesmd_df = get_outcome_data_lvl1("SESMD", "se_")
    out_title_df = get_outcome_data_lvl1("Title", "out_tit_")
    out_type_df = get_outcome_data_lvl2(outcome_type_codes, "out_type_")
    sample_df = get_outcome_data_lvl2(sample_output, "out_samp_")
    out_comp_df = get_outcome_data_lvl1("ControlText", "out_comp_")
    effectsizetype_df = get_outcome_data_lvl2(es_type_output, "out_es_type_")
    out_measure_df = get_outcome_data_lvl1("InterventionText", "out_measure_")
    testtype_df = get_outcome_data_lvl2(test_type_output, "out_test_type_raw_")
    admin_strand_data = retrieve_data(admin_strand_output, "strand_raw")
    admin_strand_info = retrieve_info(admin_strand_output, "strand_info")
    country_df = retrieve_data(countries, "loc_country_raw")
    intervention_training_prov_data = retrieve_data(int_training_provided_output, "int_training_raw")
    intervention_training_prov_ht = retrieve_ht(int_training_provided_output, "int_training_ht")
    intervention_training_prov_info = retrieve_info(int_training_provided_output, "int_training_info")
    intervention_teaching_app_data = retrieve_data(intervention_teaching_approach, "int_approach_raw")
    intervention_teaching_app_ht = retrieve_ht(intervention_teaching_approach, "int_approach_ht")
    intervention_teaching_app_info = retrieve_info(intervention_teaching_approach, "int_approach_info")
    digit_tech_data = retrieve_data(int_appr_dig_tech, "digit_tech_raw")
    digit_tech_ht = retrieve_ht(int_appr_dig_tech, "digit_tech_ht")
    digit_tech_info = retrieve_info(int_appr_dig_tech, "digit_tech_info")
    par_eng_data = retrieve_data(int_appr_par_or_comm_vol, "parent_partic_raw")
    par_eng_ht= retrieve_ht(int_appr_par_or_comm_vol, "parent_partic_ht")
    par_eng_info = retrieve_info(int_appr_par_or_comm_vol, "parent_partic_info")
    intervention_time_data = retrieve_data(intervention_time_output, "int_when_raw")
    intervention_time_ht = retrieve_ht(intervention_time_output, "int_when_ht")
    intervention_time_info = retrieve_info(intervention_time_output, "int_when_info")
    intervention_delivery_data = retrieve_data(intervention_delivery_output, "int_who_raw")
    intervention_delivery_ht = retrieve_ht(intervention_delivery_output, "int_who_ht")
    intervention_delivery_info = retrieve_info(intervention_delivery_output, "int_who_info")
    intervention_duration_info = retrieve_info(int_dur_output, "int_dur_info")
    intervention_frequency_info = retrieve_info(inte_freq_output, "int_freq_info")
    intervention_sess_length_info = retrieve_info(intervention_session_length_output, "int_leng_info")
    edu_setting_data = retrieve_data(edu_setting_output, "int_setting_raw")
    edu_setting_ht = retrieve_ht(edu_setting_output, "int_setting_ht")
    edu_setting_info = retrieve_info(edu_setting_output, "int_setting_info")
    student_age_data = retrieve_data(student_age_output, "part_age_raw")
    student_age_ht = retrieve_ht(student_age_output, "part_age_ht")
    student_age_info = retrieve_info(student_age_output, "part_age_info")
    number_of_school_total_info = retrieve_info(number_of_schools_total_output, "school_total_info")
    number_of_classes_total_info = retrieve_info(num_of_class_tot_output, "class_total_info")
    study_design_data = retrieve_data(study_design_output, "int_desig_raw")
    study_design_ht = retrieve_ht(study_design_output, "int_design_ht")
    study_design_info = retrieve_info(study_design_output, "int_design_info")
    sample_size_comments_df = retrieve_info(sample_size_output, "sample_analysed_info")
    low_ses_percentage_Comments_df = retrieve_info(percentage_low_fsm_output, "fsm_perc_info")

    record_details_df = pd.concat([
            eppiid_df,
            author_df,
            year_df,
            pub_type_data
    ], axis=1)

    df = pd.concat([
            toolkitstrand_df,
            smd_df,
            sesmd_df,
            out_title_df,
            out_type_df,
            sample_df,
            out_comp_df,
            effectsizetype_df,
            out_measure_df,
            testtype_df
        ], axis=1, sort=False)

    df = df[list(interleave([
            toolkitstrand_df,
            smd_df,
            sesmd_df,
            out_title_df,
            out_type_df,
            sample_df,
            out_comp_df,
            effectsizetype_df,
            out_measure_df,
            testtype_df
        ]))]

    general_df = pd.concat([
            admin_strand_data,
            admin_strand_info,
            country_df,
            intervention_training_prov_data,
            intervention_training_prov_ht,
            intervention_training_prov_info,
            intervention_teaching_app_data,
            intervention_teaching_app_ht,
            intervention_teaching_app_info,
            digit_tech_data,
            digit_tech_ht,
            digit_tech_info,
            par_eng_data,
            par_eng_ht,
            par_eng_info,
            intervention_time_data,
            intervention_time_ht,
            intervention_time_info,
            intervention_delivery_data,
            intervention_delivery_ht,
            intervention_delivery_info,
            intervention_duration_info,
            intervention_frequency_info,
            intervention_sess_length_info,
            edu_setting_data,
            edu_setting_ht,
            edu_setting_info,
            student_age_data,
            student_age_ht,
            student_age_info,
            number_of_school_total_info,
            number_of_classes_total_info,
            study_design_data,
            study_design_ht,
            study_design_info,
            sample_size_comments_df,
            low_ses_percentage_Comments_df
    ], axis=1)

    toolkit_lists = [[] for _ in range(10)]

    (toolkit_prim, 
     toolkit_prim_smd, 
     toolkit_prim_se, 
     toolkit_out_tit, 
     toolkit_prim_sample, 
     toolkit_prim_outcomp, 
     toolkit_es_type, 
     toolkit_out_measure, 
     toolkit_out_testtype, 
     toolkit_out_strand) = toolkit_lists

    outcome_vars = (
        "out_type_",
        "smd_",
        "se_",
        "out_tit_",
        "out_samp_",
        "out_comp_",
        "out_es_type_",
        "out_measure_",
        "out_test_type_raw_",
        "out_strand_",
    )

    getOutcomeData(df, 'Toolkit primary outcome', toolkit_lists, outcome_vars)

    reading_lists = [[] for _ in range(3)]

    (reading_prim, 
     reading_prim_smd, 
     reading_prim_se) = reading_lists

    getOutcomeData(df, 'Reading primary outcome', reading_lists, outcome_vars)

    writing_lists = [[] for _ in range(3)]

    (Writing_and_spelling_prim,
     Writing_and_spelling_prim_smd,
     Writing_and_spelling_prim_se) = writing_lists

    getOutcomeData(df, 'Writing and spelling primary outcome', writing_lists, outcome_vars)

    mathematics_lists = [[] for _ in range(3)]

    (Mathematics_prim,
     Mathematics_prim_smd,
     Mathematics_prim_se) = mathematics_lists

    getOutcomeData(df, 'Mathematics primary outcome', mathematics_lists, outcome_vars)

    science_lists = [[] for _ in range(3)]

    (Science_prim, Science_prim_smd, Science_prim_se) = science_lists

    getOutcomeData(df, 'Science primary outcome', science_lists, outcome_vars)

    fsm_lists = [[] for _ in range(3)]

    (fsm_prim, fsm_prim_smd, fsm_prim_se) = fsm_lists

    getOutcomeData(df, 'FSM primary outcome', fsm_lists, outcome_vars)

    df_zip = list(zip(
        toolkit_out_strand,
        toolkit_prim_smd,
        toolkit_prim_se,
        toolkit_out_tit,
        toolkit_prim,
        toolkit_prim_sample,
        toolkit_prim_outcomp,
        toolkit_es_type,
        toolkit_out_measure,
        toolkit_out_testtype,
        reading_prim,
        reading_prim_smd,
        reading_prim_se,
        Writing_and_spelling_prim,
        Writing_and_spelling_prim_smd,
        Writing_and_spelling_prim_se,
        Mathematics_prim,
        Mathematics_prim_smd,
        Mathematics_prim_se,
        Science_prim,
        Science_prim_smd,
        Science_prim_se,
        fsm_prim,
        fsm_prim_smd,
        fsm_prim_se
    ))

    df = pd.DataFrame(df_zip)

    df = df.rename(columns={
        0: "out_strand",
        1: "smd_tool",
        2: "se_tool",
        3: "out_tit",
        4: "out_out_type_tool",
        5: "out_samp",
        6: "out_comp",
        7: "out_es_type",
        8: "out_measure",
        9: "out_test_type_raw",
        10: "out_out_type_red",
        11: "smd_red",
        12: "se_red",
        13: "out_out_type_wri",
        14: "smd_wri",
        15: "se_wri",
        16: "out_out_type_math",
        17: "smd_math",
        18: "se_math",
        19: "out_out_type_sci",
        20: "smd_sci",
        21: "se_sci",
        22: "out_out_type_fsm",
        23: "smd_fsm",
        24: "se_fsm"
    })

    df_all = pd.concat([record_details_df, df, general_df], axis=1, sort=False)

    # add fsm_50 TRUE/FALSE column
    df_all["fsm_perc_info"] = (df_all["fsm_perc_info"].str.strip('%'))
    df_all["fsm_perc_info"] = pd.to_numeric(df_all["fsm_perc_info"], errors='coerce')

    # percentage taught by research staff only
    conditions = [
        df_all["fsm_perc_info"] > 49,
        df_all["fsm_perc_info"] < 50,
    ]
    values = ['TRUE', 'FALSE']

    df_all['fsm_50'] = np.select(conditions, values)

    df_all["fsm_perc_info"] = df_all["fsm_perc_info"].replace(
        to_replace=np.nan, value="NA", regex=True
    )

    df_all['fsm_50'] = df_all['fsm_50'].replace("0", "NA", regex=True)

    df_all = df_all[[
        'id',
        'pub_author',
        'pub_year',
        'pub_type_raw',
        'strand_raw',
        'out_out_type_tool',
        'smd_tool',
        'se_tool',
        'out_es_type',
        'out_tit',
        'out_comp',
        'out_samp',
        'out_measure',
        'out_test_type_raw',
        'out_out_type_red',
        'smd_red',
        'se_red',
        'out_out_type_wri',
        'smd_wri',
        'se_wri',
        'out_out_type_math',
        'smd_math',
        'se_math',
        'out_out_type_sci',
        'smd_sci',
        'se_sci',
        'out_out_type_fsm',
        'smd_fsm',
        'se_fsm',
        'sample_analysed_info',
        'school_total_info',
        'class_total_info',
        'int_setting_raw',
        'part_age_raw',
        'fsm_50',
        'fsm_perc_info',
        'loc_country_raw',
        'int_desig_raw',
        'int_approach_raw',
        'int_training_raw',
        'digit_tech_raw',
        'parent_partic_raw',
        'int_when_raw',
        'int_who_raw',
        'int_dur_info',
        'int_freq_info',
        'int_leng_info',
        'out_strand'
    ]]

    df_all_SS = pd.concat([df_all, ss_df], axis=1, sort=False)

    replacements = [('\r', ' '), ('\n', ' '), (':', ' '), (';', ' ')]
    for old, new in replacements:
        df_all_SS.replace(old, new, regex=True, inplace=True)

    if verbose:
        verbose_display(df_all_SS)

    if save_file:
        save_dataframe(df_all_SS, "_Main_Analysis_SS.csv")


#/**********************************************/
#/   RETRIEVE INDIVIDUAL VARIABLE DATAFRAMES    /
#/**********************************************/

def process_data(output, data_col):
    data = get_data(output)
    data_df = pd.DataFrame(data)
    data_df = data_df.T
    data_df.columns = [data_col]
    clean_up(data_df)
    return data_df


def process_ht(output, ht_col):
    ht = highlighted_text(output)
    ht_df = pd.DataFrame(ht)
    ht_df = ht_df.T
    ht_df.columns = [ht_col]
    clean_up(ht_df)
    return ht_df


def process_info(output, info_col):
    comment = comments(output)
    comments_df = pd.DataFrame(comment)
    comments_df = comments_df.T
    comments_df.columns = [info_col]
    clean_up(comments_df)
    return comments_df


def process_metadata(output, info_col):
    # get metadata
    metadata = get_metadata(output)
    metadata_df = pd.DataFrame(metadata)
    #metadata_df = metadata_df.T
    metadata_df.columns = [info_col]
    return metadata_df


def retrieve_metadata(metadata_type, metadata_value):
    metadata_df = process_metadata(metadata_type, metadata_value)
    clean_up(metadata_df)
    metadata_df.fillna("NA", inplace=True)
    return metadata_df


def group_desc_stats(attribute_text, column_prefix):
    group_data = get_outcome_lvl1(attribute_text)
    group_data_df = pd.DataFrame(group_data)
    # name each column (number depends on outcome number)
    group_data_df.columns = [
        column_prefix+'{}'.format(column+1) for column in group_data_df.columns
    ]
    group_data_df.fillna("NA", inplace=True)
    group_data_df = group_data_df.replace(r'^\s*$', "NA", regex=True)
    # get outcometypeId data (to check)
    outcometypeid = get_outcome_lvl1("OutcomeTypeId")
    outcometypeid_df = pd.DataFrame(outcometypeid)
    # name each column (number depends on outcome number)
    outcometypeid_df.columns = [
        "outcometype_df_"+'{}'.format(column+1) for column in outcometypeid_df.columns
    ]
    mask = pd.DataFrame(outcometypeid_df["outcometype_df_1"] == 0)
    mask.columns = ["mask"]
    mask = mask.iloc[:, 0]
    # replace all 0 instances (null data) with "NA"
    for col in group_data_df.columns:
        group_data_df.loc[mask, col] = "NA"
    return group_data_df


def retrieve_data(id, col_name):
    data = get_data(id)
    data_df = pd.DataFrame(data)
    data_df = data_df.T
    data_df.columns = [col_name]
    clean_up(data_df)
    return data_df


def retrieve_ht(id, col_name):
    ht = highlighted_text(id)
    ht_df = pd.DataFrame(ht)
    ht_df = ht_df.T
    ht_df.columns = [col_name]
    clean_up(ht_df)
    return ht_df


def retrieve_info(id, col_name):
    info = comments(id)
    info_df = pd.DataFrame(info)
    info_df = info_df.T
    info_df.columns = [col_name]
    clean_up(info_df)
    return info_df


def city():
    """
    Retrieve city data and return it as a cleaned up DataFrame.
    Returns:
    -------
    city_df : pandas.DataFrame
        DataFrame containing publication author data.
    """
    # Get city metadata
    city_df = process_metadata("City", "City")
    # Clean up data frame
    city_df.fillna("NA", inplace=True)
    return city_df


def doi():
    # get author data
    doi = get_metadata("DOI")
    doi_df = pd.DataFrame(doi)
    doi_df.columns = ["DOI"]
    doi_df.fillna("NA", inplace=True)
    return doi_df


def editors():
    # get abstract data
    editedby = get_metadata("EditedBy")
    editedby_df = pd.DataFrame(editedby)
    editedby_df.columns = ["Editor(s)"]
    editedby_df.fillna("NA", inplace=True)
    return editedby_df


def gender_split():
    """
    """
    from src.attributeIDs import gender_split_output
    # Get gender split highlighted text
    gen_split_ht_df = process_ht(gender_split_output, "Gender_Split_HT")
    # Get gender split comments data
    gen_split_comments_df = process_info(gender_split_output, "Gender_Split_comments")
    # Concatenate all dataframes
    dataframes = [gen_split_ht_df, gen_split_comments_df]
    gen_split_df = pd.concat(dataframes, axis=1, sort=False)
    # Clean up data frame
    gen_split_df.replace('\r',' ', regex=True, inplace=True)
    gen_split_df.replace('\n',' ', regex=True, inplace=True)
    gen_split_df.fillna("NA", inplace=True)
    return gen_split_df


def inst():
    """
    """
    # Get author data
    institution = get_metadata("Institution")
    institution_df = pd.DataFrame(institution)
    institution_df.columns = ["Institution"]
    institution_df.fillna("NA", inplace=True)
    return institution_df


def int_eval():
    """
    """
    from src.attributeIDs import int_eval
    # get intervention costs reported main data
    int_eval_df = process_data(int_eval, "out_eval_raw")
    int_eval_df["eef_eval_raw"] = int_eval_df["out_eval_raw"].map(
                set(["Is this an EEF evaluation?"]).issubset).astype(int)
    int_eval_df["eef_eval_raw"] = int_eval_df["eef_eval_raw"].replace(
                to_replace=[0, 1], value=["No", "Yes"])
    # get intervention costs reported highlighted text
    int_eval_ht_df = process_ht(int_eval, "out_eval_ht")
    # get intervention costs reported user comments
    int_eval_comments_df = process_info(int_eval, "out_eval_info")
    # Concatenate data frames
    dataframes = [int_eval_df, int_eval_ht_df, int_eval_comments_df]
    int_eval_df = pd.concat(dataframes, axis=1, sort=False)
    int_eval_df=int_eval_df[[
        "out_eval_raw", 
        "out_eval_ht", 
        "out_eval_info", 
        "eef_eval_raw"
    ]]
    clean_up(int_eval_df)
    int_eval_df.fillna("NA", inplace=True)
    return int_eval_df


def issue():
    # get issue data
    issue = get_metadata("Issue")
    issue_df = pd.DataFrame(issue)
    issue_df.columns = ["Issue"]
    issue_df.fillna("NA", inplace=True)
    return issue_df


def out_id():
    """
    """
    # Get outcome ID data
    outcome_ID = get_outcome_lvl1("OutcomeId")
    outcome_ID_df = pd.DataFrame(outcome_ID)
    # Name each column (number depends on outcome number)
    outcome_ID_df.columns = [
        "Outcome_ID_"+'{}'.format(column+1) for column in outcome_ID_df.columns]
    # Clean up data frame
    outcome_ID_df.fillna("NA", inplace=True)
    outcome_ID_df = outcome_ID_df.replace(r'^\s*$', "NA", regex=True)
    return outcome_ID_df


def pages():
    # get author data
    pages = get_metadata("Pages")
    pages_df = pd.DataFrame(pages)
    pages_df.columns = ["Pages"]
    pages_df.fillna("NA", inplace=True)
    return pages_df


def par_auth():
    # get abstract data
    parentauthors = get_metadata("ParentAuthors")
    parentauthors_df = pd.DataFrame(parentauthors)
    parentauthors_df.columns = ["Parent_Authors"]
    parentauthors_df.fillna("NA", inplace=True)
    return parentauthors_df


def par_tit():
    # get author data
    parentittle = get_metadata("ParentTitle")
    parentittle_df = pd.DataFrame(parentittle)
    parentittle_df.columns = ["ParentTitle"]
    parentittle_df.fillna("NA", inplace=True)
    return parentittle_df


def publisher():
    """
    """
    # Get author data
    publisher = get_metadata("Publisher")
    publisher_df = pd.DataFrame(publisher)
    publisher_df.columns = ["Publisher"]
    publisher_df.fillna("NA", inplace=True)
    return publisher_df


def short_tit():
    # get eppiID data
    shorttitle = get_metadata("Title")
    shorttitle_df = pd.DataFrame(shorttitle)
    shorttitle_df.columns = ["title"]
    shorttitle_df.fillna("NA", inplace=True)
    return shorttitle_df


def source():
    from src.attributeIDs import source_output
    from src.attributeIDs import source_EEF_Report_options
    # get source raw data
    source = get_data(source_output)
    source_df = pd.DataFrame(source)
    source_df = source_df.T
    source_df.columns = ["source_raw"]
    # get source EED options (nested) data
    eef_options = get_data(source_EEF_Report_options)
    eef_options_df = pd.DataFrame(eef_options)
    eef_options_df = eef_options_df.T
    eef_options_df.columns = ["source_eef_reports"]
    # concatenate data frames
    source_all_df = pd.concat([
        source_df,
        eef_options_df,
    ], axis=1, sort=False)
    # fill blanks with NA
    source_all_df.fillna("NA", inplace=True)
    return source_all_df


def study_place():
    from src.attributeIDs import location_info
    # get study place info data
    study_place = get_data(location_info)
    study_place_df = pd.DataFrame(study_place)
    study_place_df = study_place_df.T
    study_place_df.columns = ["study_place_info"]
    # get study place ht data
    study_place_ht = highlighted_text(location_info)
    study_place_ht_df = pd.DataFrame(study_place_ht)
    study_place_ht_df = study_place_ht_df.T
    study_place_ht_df.columns = ["study_place_ht"]
    # concatenate data frames
    study_place_df = pd.concat([
        study_place_df,
        study_place_ht_df,
    ], axis=1, sort=False)
    # fill blanks with NA
    study_place_df.fillna("NA", inplace=True)
    return study_place_df


def sample_main_check():
    sample_main_check = get_data(sample_output)
    sample_main_check_df = pd.DataFrame(sample_main_check)
    sample_main_check_df = sample_main_check_df.T
    sample_main_check_df.columns = ["main_check"]
    sample_main_check_df.fillna("NA", inplace=True)
    return sample_main_check_df


def title():
    # get eppiID data
    title = get_metadata("Title")
    title_df = pd.DataFrame(title)
    title_df.columns = ["title"]
    title_df.fillna("NA", inplace=True)
    return title_df


def toolkit_strand():
    from src.attributeIDs import toolkit_strand_codes
    # get toolkit strand data
    toolkitstrand = get_outcome_lvl2(toolkit_strand_codes)
    toolkitstrand_df = pd.DataFrame(toolkitstrand)
    # get toolkit strand comments
    toolkitstrand_Comments = comments(toolkit_strand_codes)
    toolkitstrand_Comments_df = pd.DataFrame(toolkitstrand_Comments)
    toolkitstrand_Comments_df = toolkitstrand_Comments_df.T
    toolkitstrand_Comments_df.columns = ["_info"]
    # fill blanks with NA
    toolkitstrand_df.fillna("NA", inplace=True)
    # name each column (number depends on outcome number)
    toolkitstrand_df.columns = [
        "out_strand_"+'{}'.format(column+1) for column in toolkitstrand_df.columns]
    return toolkitstrand_df


def type_name():
    # get author data
    typename = get_metadata("TypeName")
    typename_df = pd.DataFrame(typename)
    typename_df.columns = ["typename"]
    typename_df.fillna("NA", inplace=True)
    return typename_df


def url():
    # get author data
    url = get_metadata("URL")
    url_df = pd.DataFrame(url)
    url_df.columns = ["URL"]
    url_df.fillna("NA", inplace=True)
    return url_df


def volume():
    # get author data
    volume = get_metadata("Volume")
    volume_df = pd.DataFrame(volume)
    volume_df.columns = ["Volume"]
    volume_df.fillna("NA", inplace=True)
    return volume_df


def web_loc():
    from src.attributeIDs import study_loc
    from src.attributeIDs import study_loc_type
    # get location info highlighted text
    loc_HT = highlighted_text(study_loc)
    loc_HT_df = pd.DataFrame(loc_HT)
    loc_HT_df = loc_HT_df.T
    loc_HT_df.columns = ["loc_ht"]
    # get location type further info highlighted text
    loc_type_HT = highlighted_text(study_loc_type)
    loc_type_HT_df = pd.DataFrame(loc_type_HT)
    loc_type_HT_df = loc_type_HT_df.T
    loc_type_HT_df.columns = ["loc_type_ht"]
    # concatenate datafeames
    loc_info = pd.concat([
        loc_HT_df,
        loc_type_HT_df,
    ], axis=1, sort=False)
    return loc_info
#/*********************************/
#/   STRAND SPECIFIC DATAFRAMES    /
#/*********************************/


def arts_participation_ss():
    # get focus data
    ap_focus_df = retrieve_data(ap_focus_output, "ap_focus")
    # get who involved data
    ap_who_invol_df = retrieve_data(ap_who_output, "ap_involved")
    # get where data
    ap_where_df = retrieve_data(ap_where_output, "ap_where")
    ap_ss_df = pd.concat([
        ap_focus_df,
        ap_who_invol_df,
        ap_where_df,
    ], axis=1, sort=False)
    # fill blanks with NA
    ap_ss_df.fillna("NA", inplace=True)
    return ap_ss_df


def behaviour_int_ss():
    bi_target_group_df = retrieve_data(bi_target_group_output, "bi_targ_group")
    bi_target_group_HT_df = retrieve_ht(bi_intervention_approach_output, "bi_targ_group_ht")
    bi_target_group_Comments_df = retrieve_info(bi_intervention_components_output, "bi_targ_group_info")
    # BEHAVIOR INTERVENTION APPROACH
    bi_int_approach_df = retrieve_data(bi_intervention_approach_output, "bi_int_approach")
    bi_int_approach_HT_df = retrieve_ht(bi_intervention_approach_output, "bi_int_approach_ht")
    bi_int_approach_Comments_df = retrieve_info(bi_intervention_approach_output, "bi_int_approach_info")
    bi_int_components_df = retrieve_data(bi_intervention_components_output, "bi_int_components")
    bi_int_components_HT_df = retrieve_ht(bi_intervention_components_output, "bi_int_components_ht")
    bi_int_components_Comments_df = retrieve_info(bi_intervention_components_output, "bi_int_components_info")
    bi_int_comp_counselling_df = retrieve_data(ind_comp_counselling, "bi_components_counselling")
    bi_int_comp_monitoring_df = retrieve_data(ind_comp_monitoring, "bi_components_monitoring")
    bi_int_comp_self_man_df = retrieve_data(ind_comp_self_management, "bi_components_self")
    bi_int_comp_role_play_df = retrieve_data(ind_comp_role_play, "bi_components_roleplay")
    bi_int_comp_par_invol_df = retrieve_data(ind_comp_parental_involv, "bi_components_parentalinv")
    bi_int_comp_ac_focus_df = retrieve_data(ind_comp_academic_focus, "bi_academic")
    bi_int_comp_dig_tech_df = retrieve_data(ind_comp_digit_tech, "bi_components_digital")
    bi_ss_df = pd.concat([
        bi_target_group_df,
        bi_int_approach_df,
        bi_int_components_df,
        bi_int_comp_counselling_df,
        bi_int_comp_monitoring_df,
        bi_int_comp_self_man_df,
        bi_int_comp_role_play_df,
        bi_int_comp_par_invol_df,
        bi_int_comp_ac_focus_df,
        bi_int_comp_dig_tech_df
    ], axis=1, sort=False)
    # fill blanks with NA
    bi_ss_df.fillna("NA", inplace=True)
    return bi_ss_df


def collab_learning_ss():
    cl_approach_spec_df = retrieve_data(cl_approach_spec_output, "cl_approach_spec")
    cl_grp_size_df = retrieve_data(cl_group_size_output, "cl_grp_size")
    cl_collab_kind_df = retrieve_data(cl_collab_kind_output, "cl_collab_kind")
    cl_stud_collab_df = retrieve_data(cl_stud_collab_output, "cl_stud_collab")
    cl_stud_collab_HT_df = retrieve_ht(cl_stud_collab_output, "cl_stud_collab_HT")
    cl_extr_rewards_df = retrieve_data(cl_extr_rewards_output, "cl_extr_rewards")
    cl_extr_rewards_HT_df = retrieve_ht(cl_extr_rewards_output, "cl_extr_rewards_HT")
    cl_if_yes_rewards_df = retrieve_data(cl_if_yes_rewards_output, "cl_what_rewards")
    cl_if_yes_rewards_HT_df = retrieve_ht(cl_if_yes_rewards_output, "cl_what_rewards_HT")
    cl_comp_elem_df = retrieve_data(cl_comp_elem_output, "cl_comp_elem")
    cl_comp_elem_HT_df = retrieve_ht(cl_comp_elem_output, "cl_comp_elem_HT")
    cl_teach_role_info_df = retrieve_data(cl_teacher_role_info_output, "cl_teacher_role_info")
    cl_teach_role_info_HT_df = retrieve_ht(cl_teacher_role_info_output, "cl_teacher_role_info_HT")
    cl_pup_feedback_df = retrieve_data(cl_pupil_feedback_output, "cl_pup_feedback")
    cl_pup_feedback_HT_df = retrieve_ht(cl_pupil_feedback_output, "cl_pup_feedback_HT")
    cl_pup_feedback_who_df = retrieve_data(cl_pupil_feedback_who_output, "cl_pup_feedback_who")
    cl_pup_feedback_who_HT_df = retrieve_ht(cl_pupil_feedback_who_output, "cl_pup_feedback_who_HT")
    cl_ss_df = pd.concat([
        cl_approach_spec_df,
        cl_grp_size_df,
        cl_collab_kind_df,
        cl_stud_collab_df,
        cl_extr_rewards_df,
        cl_if_yes_rewards_df,
        cl_comp_elem_df,
        cl_teach_role_info_df,
        cl_pup_feedback_df,
        cl_pup_feedback_who_df,
    ], axis=1, sort=False)
    # fill blanks with NA
    cl_ss_df.fillna("NA", inplace=True)
    return cl_ss_df


def ey_early_lit_approaches_ss():
    lit_act_df = retrieve_data(ela_literacy_activities, "lit_activities")
    lit_act_HT_df = retrieve_ht(ela_literacy_activities, "lit_activities_HT")
    prog_comp_df = retrieve_data(ela_comprehensive, "prog_comp")
    prog_comp_HT_df = retrieve_ht(ela_comprehensive, "prog_comp_HT")
    prog_desc_df = retrieve_data(ela_prog_desc, "prog_desc")
    prog_desc_HT_df = retrieve_ht(ela_prog_desc, "prog_desc_HT")
    # concatenate data frames
    ela_ss_df = pd.concat([
        lit_act_df,
        #lit_act_HT_df,
        prog_comp_df,
        #prog_comp_HT_df,
        prog_desc_df,
        #prog_desc_HT_df,
    ], axis=1, sort=False)
    return ela_ss_df


def ey_early_num_approaches_ss():
    math_incl_df = retrieve_data(ena_maths_included, "math_incl")
    math_incl_HT_df = retrieve_ht(ena_maths_included, "math_incl_ht")
    prog_comp_df = retrieve_data(ena_prog_comp, "prog_comp")
    prog_act_df = retrieve_data(ena_prog_activities, "prog_act")
    # concatenate data frames
    ena_ss_df = pd.concat([
        math_incl_df,
        #math_incl_HT_df,
        prog_comp_df,
        prog_act_df,
    ], axis=1, sort=False)
    # fill blanks with NA
    ena_ss_df.fillna("NA", inplace=True)
    return ena_ss_df


def ext_school_time_ss():
    # EXTENDED HOW?
    # get extended how? data
    extended_how = get_data(extended_how_output)
    extended_how_df = retrieve_data(extended_how_output, "est_how")
    # Get extended how? highlighted text
    extended_how_HT_df = retrieve_ht(extended_how_output, "est_how_ht")
    # Get extended how? user comments
    extended_how_Comments_df = retrieve_info(extended_how_output, "est_how_info")
    # TIME ADDED
    # get time added data
    time_added_df = retrieve_data(time_Added_output, "est_time_added")
    time_added_HT_df = retrieve_ht(time_Added_output, "est_time_added_ht")
    time_added_Comments_df = retrieve_info(time_Added_output, "est_time_added_info")
    purpose_df = retrieve_data(purpose_or_aim_output, "est_purpose")
    purpose_HT_df = retrieve_ht(purpose_or_aim_output, "est_purpose_ht")
    purpose_Comments_df = retrieve_info(purpose_or_aim_output, "est_purpose_info")
    target_group_df = retrieve_data(target_group_output, "est_target_group")
    target_group_HT_df = retrieve_ht(target_group_output, "est_target_group_ht")
    target_group_Comments_df = retrieve_info(target_group_output, "est_target_group_info")
    pupil_participation_df = retrieve_data(pupil_participation_output, "est_pupil_participation")
    pupil_participation_HT_df = retrieve_ht(pupil_participation_output, "est_pupil_participation_ht")
    pupil_participation_Comments_df = retrieve_info(pupil_participation_output, "est_pupil_participation_info")
    activity_focus_df = retrieve_data(activity_focus_output, "est_activity_focus")
    activity_focus_HT_df = retrieve_ht(activity_focus_output, "est_activity_focus_ht")
    activity_focus_Comments_df = retrieve_info(activity_focus_output, "est_activity_focus_info")
    staff_kind_df = retrieve_data(staff_kind_output, "est_staff_kind")
    staff_kind_HT_df = retrieve_ht(staff_kind_output, "est_staff_kind_ht")
    staff_kind_Comments_df = retrieve_info(staff_kind_output, "est_staff_kind_info")
    parent_involved_df = retrieve_data(parental_involvement_output, "est_parental_involvement")
    parent_involved_HT_df = retrieve_ht(parental_involvement_output, "est_parental_involvement_ht")
    parent_involved_Comments_df = retrieve_info(parental_involvement_output, "est_parental_involvement_info")
    digit_tech_df = retrieve_data(digital_tech_output, "est_digital_tech")
    digit_tech_HT_df = retrieve_ht(digital_tech_output, "est_digital_tech_ht")
    digit_tech_Comments_df = retrieve_info(digital_tech_output, "est_digital_tech_info")
    attend_mon_df = retrieve_data(attendance_monitored_output, "est_attend_monitored")
    attend_mon_HT_df = retrieve_ht(attendance_monitored_output, "est_attend_monitored_ht")
    attend_mon_Comments_df = retrieve_info(attendance_monitored_output, "est_attendance_monitored_info")
    # concatenate data frames
    est_ss_df = pd.concat([
        extended_how_df,
        time_added_df,
        time_added_Comments_df,
        purpose_df,
        target_group_df,
        pupil_participation_df,
        activity_focus_df,
        staff_kind_df,
        parent_involved_df,
        digit_tech_df,
        attend_mon_df,
    ], axis=1, sort=False)
    # remove problematic text from outputs
    clean_up(est_ss_df)
    return est_ss_df


def ey_earlier_start_age_ss():
    prev_start_age_df = retrieve_data(ey_esa_prev_starting_age, "prev_start_age")
    new_start_age_df = retrieve_data(ey_esa_new_starting_age, "new_start_age")
    addit_time_f_pt_df = retrieve_data(ey_esa_addit_time_f_pt, "addit_time_f_pt")
    add_time_struct_df = retrieve_data(ey_esa_addit_time_struct, "addit_time_struct")
    earl_child_addit_time_df = retrieve_data(ey_esa_earlier_child_addit_time, "early_child_addit_time")
    earl_child_addit_time_info_df = retrieve_info(ey_esa_earlier_child_addit_time_other, "early_child_addit_time_info")
    setting_type_df = retrieve_data(ey_esa_setting_type, "setting_type")
    ey_esa_df = pd.concat([
        prev_start_age_df,
        new_start_age_df,
        addit_time_f_pt_df,
        add_time_struct_df,
        earl_child_addit_time_df,
        earl_child_addit_time_info_df,
        setting_type_df,
    ], axis=1, sort=False)
    # fill blanks with NA
    ey_esa_df.fillna("NA", inplace=True)
    return ey_esa_df


def ey_extra_hours_ss():
    time_org_df = retrieve_data(time_organsised, "time_org")
    addit_time_struc_df = retrieve_data(addit_time_struct, "addit_time_struct")
    ey_eh_df = pd.concat([
        time_org_df,
        addit_time_struc_df
    ], axis=1, sort=False)
    # fill blanks with NA
    ey_eh_df.fillna("NA", inplace=True)
    return ey_eh_df


def ey_play_based_learning_ss():
    kind_play_df = retrieve_data(kind_of_play, "kind_of_play")
    who_invol_df = retrieve_data(who_involved, "who_involved")
    play_foc_df = retrieve_data(play_focus, "play_focus")
    ey_pbl_df = pd.concat([
        kind_play_df,
        who_invol_df,
        play_foc_df
    ], axis=1, sort=False)
    # fill blanks with NA
    ey_pbl_df.fillna("NA", inplace=True)
    return ey_pbl_df


def feedback_ss():
    # get feedback source data
    feedb_source_df = retrieve_data(feedback_source_output, "feedback_Source")
    # Get feedback source highlighted text
    feedb_source_HT_df = retrieve_data(feedback_source_output, "feedback_Source_ht")
    # Get feedback source user comments
    feedb_source_Comments_df = retrieve_data(feedback_source_output, "feedback_Source_info")
    # FEEDBACK SOURCE COMPONENTS SPLIT
    # get feedback source teacher data
    fsource_teacher_df = retrieve_data(fsource_teacher, "fb_source_teacher")
    # get feedback source teaching assistant data
    fsource_ta_df = retrieve_data(fsource_ta, "fb_source_ta")
    # get feedback source volunteer data
    fsource_volunteer_df = retrieve_data(fsource_volunteer, "fb_source_volunteer")
    # get feedback source parent data
    fsource_parent_df = retrieve_data(fsource_parent, "fb_source_parent")
    # get feedback source researcher data
    fsource_researcher_df = retrieve_data(fsource_researcher, "fb_source_researcher")
    # get feedback source peer same age data
    fsource_peer_ssame_Age_df = retrieve_data(fsource_peer_sameage_class, "fb_source_peer_sameage")
    # get feedback source peer group data
    fsource_peer_group_df = retrieve_data(fsource_peer_group, "fb_source_peer_group")
    # get feedback source peer older data
    fsource_peer_older_df = retrieve_data(fsource_peer_older, "fb_source_peer_older")
    # get feedback source digital automated data
    fsource_digit_aut_df = retrieve_data(fsource_dig_aut, "fb_source_dig_aut")
    # get feedback source other non-human data
    fsource_non_human_df = retrieve_data(fsource_other_nonhuman, "fb_source_non_human")
    # get feedback source self data
    fsource_self_df = retrieve_data(fsource_self, "fb_source_self")
    # get feedback source other data
    fsource_other_df = retrieve_data(fsource_other, "fb_source_other")
    # FEEDBACK DIRECTED OUTPUT
    # get feedback directed data
    feedb_directed_df = retrieve_data(feedback_directed_output, "fb_directed")
    # Get feedback directed highlighted text
    feedb_directed_df_HT_df = retrieve_data(feedback_directed_output, "fb_directed_ht")
    # Get feedback directed user comments
    feedb_directed_Comments_df = retrieve_data(feedback_directed_output, "fb_directed_info")
    # FEEDBACK FORM OUTPUT
    # get feedback form data
    feedb_form_df = retrieve_data(feedback_form_output, "fb_form")
    # Get feedback form highlighted text
    feedb_form_HT_df = retrieve_data(feedback_form_output, "fb_form_ht")
    # Get feedback form user comments
    feedb_form_Comments_df = retrieve_data(feedback_form_output, "fb_form_info")
    # FEEDBACK WHEN OUTPUT
    # get feedback when data
    feedb_when_df = retrieve_data(feedback_when_output, "fb_when")
    # Get feedback when highlighted text
    feedb_when_HT_df = retrieve_data(feedback_when_output, "fb_when_ht")
    # Get feedback when user comments
    feedb_when_Comments_df = retrieve_data(feedback_when_output, "fb_when_info")
    # FEEDBACK KIND OUTPUT
    # get feedback kind data
    feedb_kind_df = retrieve_data(feedback_kind_output, "fb_kind")
    # get feedback kind "about the outcome" nested data (correct / incorrect"
    feedb_kind_abt_outcome_df = retrieve_data(feedback_about_outcome_output, "fb_kind_about_outcome")
    # Get feedback kind highlighted text
    feedb_kind_HT_df = retrieve_data(feedback_kind_output, "fb_kind_ht")
    # Get feedback kind user comments
    feedb_kind_Comments_df = retrieve_info(feedback_kind_output, "fbkind_info")
    # FEEDBACK EMOTIONAL TONE OUTPUT
    # get feedback emotional tone data
    feedb_emo_tone_df = retrieve_data(feedback_emo_tone, "fb_emo_tone")
    # Get feedback emotional tone highlighted text
    feedb_emo_tone_HT_df = retrieve_ht(feedback_emo_tone, "fb_emo_tone_ht")
    # Get feedback emotional tone user comments
    feedb_emo_tone_Comments_df = retrieve_info(feedback_emo_tone,"fb_emo_tone_info")
    # concatenate data frames
    feedback_ss_df = pd.concat([
        feedb_source_df,
        fsource_teacher_df,
        fsource_ta_df,
        fsource_volunteer_df,
        fsource_parent_df,
        fsource_researcher_df,
        fsource_peer_ssame_Age_df,
        fsource_peer_group_df,
        fsource_peer_older_df,
        fsource_digit_aut_df,
        fsource_non_human_df,
        fsource_self_df,
        fsource_other_df,
        feedb_directed_df,
        feedb_form_df,
        feedb_when_df,
        feedb_kind_df,
        feedb_kind_abt_outcome_df,
        feedb_emo_tone_df,
    ], axis=1, sort=False)
    # remove problematic text from outputs
    clean_up(feedback_ss_df)
    return feedback_ss_df


def homework_ss():
    hw_dur_df = retrieve_data(hw_dur_info_output, "hw_dur")
    # get hw duration information data
    hw_dur_info_df = retrieve_info(hw_dur_info_output, "hw_dur_info")
    # get hw duration total time data
    hw_dur_tot_time_df = retrieve_info(hw_total_time, "hw_dur_tot_time")
    # get hw who was involved data
    hw_who_invol_df = retrieve_data(hw_who_involved_output, "hw_who_involved")
    # get hw if parentes involved, describe role data
    hw_par_role_df = retrieve_data(hw_if_parents_describe_role_output, "hw_par_role")
    # get hw completed where data
    hw_where_df = retrieve_data(hw_completed_where_output, "hw_where")
    # get hw marking method data
    hw_mark_method_df = retrieve_data(hw_mark_method_info_output, "hw_mark_method_info")
    hw_ss_df = pd.concat([
        hw_dur_df,
        hw_dur_info_df,
        hw_dur_tot_time_df,
        hw_who_invol_df,
        hw_par_role_df,
        hw_where_df,
        hw_mark_method_df
    ], axis=1, sort=False)
    # fill blanks with NA
    hw_ss_df.fillna("NA", inplace=True)
    return hw_ss_df


def indiv_instr_ss():
    ii_approach_df = retrieve_data(ii_approach_output, "ii_approach_df")
    # get also included data
    ii_also_included_df = retrieve_data(ii_also_included_output, "ii_elements_included_df")
    # get also mentioned data
    ii_also_mentioned_df = retrieve_data(ii_also_mentioned_output, "ii_programmes_mentioned_df")
    ii_ss_df = pd.concat([
        ii_approach_df,
        ii_also_included_df,
        ii_also_mentioned_df,
    ], axis=1, sort=False)
    # fill blanks with NA
    ii_ss_df.fillna("NA", inplace=True)
    return ii_ss_df


def mentoring_ss():
    ment_ident_df = retrieve_data(mentor_identity, "m_identity_df")
    ment_ident_HT_df = retrieve_ht(mentor_identity, "m_identity_ht_df")
    ment_ident_Comments_df = retrieve_info(mentor_identity, "m_identity_info_df")
    ment_pay_df = retrieve_data(mentor_paid_or_compensated, "m_pay_df")
    ment_pay_HT_df = retrieve_ht(mentor_paid_or_compensated, "m_pay_ht_df")
    ment_pay_Comments_df = retrieve_info(mentor_paid_or_compensated, "m_pay_info_df")
    ment_org_df = retrieve_data(mentor_organisation, "m_org_df")
    ment_org_HT_df = retrieve_ht(mentor_organisation, "m_org_ht_df")
    ment_org_Comments_df = retrieve_info(mentor_organisation, "m_org_info_df")
    ment_training_df = retrieve_data(mentor_training, "m_training_df")
    ment_training_HT_df = retrieve_ht(mentor_training, "m_training_ht_df")
    ment_training_Comments_df = retrieve_info(mentor_training, "m_training_info_df")
    ment_meeting_freq_df = retrieve_data(mentor_meeting_frequency, "m_meeting_freq_df")
    ment_meeting_freq_HT_df = retrieve_ht(mentor_meeting_frequency, "m_meeting_freq_ht_df")
    ment_meeting_freq_Comments_df = retrieve_info(mentor_meeting_frequency, "m_meeting_freq_info_df")
    ment_meeting_details_df = retrieve_data(mentor_meeting_details_provided, "m_meeting_details_df")
    ment_meeting_details_HT_df = retrieve_ht(mentor_meeting_details_provided, "m_meeting_details_ht_df")
    ment_meeting_details_Comments_df = retrieve_info(mentor_meeting_details_provided, "m_meeting_details_info_df")
    ment_meeting_location_df = retrieve_data(mentor_meeting_location, "m_meeting_location_df")
    ment_meeting_location_HT_df = retrieve_ht(mentor_meeting_location, "m_meeting_location_ht_df")
    ment_meeting_location_Comments_df = retrieve_info(mentor_meeting_location, "m_meeting_location_info_df")
    ment_addit_exp_df = retrieve_data(mentoring_additional_experiences, "m_addit_exp_df")
    ment_addit_exp_HT_df = retrieve_ht(mentoring_additional_experiences, "m_addit_exp_ht_df")
    ment_addit_exp_Comments_df = retrieve_info(mentoring_additional_experiences, "m_addit_exp_info_df")
    ment_prog_focus_df = retrieve_data(mentoring_programme_focus, "m_prog_focus_df")
    ment_prog_focus_HT_df = retrieve_ht(mentoring_programme_focus, "m_prog_focus_ht_df")
    ment_prog_focus_Comments_df = retrieve_info(mentoring_programme_focus, "m_prog_focus_info_df")
    # concatenate data frames
    mentoring_ss_df = pd.concat([
        ment_ident_df,
        ment_pay_df,
        ment_org_df,
        ment_training_df,
        ment_meeting_freq_df,
        ment_meeting_details_df,
        ment_meeting_location_df,
        ment_addit_exp_df,
        ment_prog_focus_df,
    ], axis=1, sort=False)
    # fill blanks with NA
    mentoring_ss_df.fillna("NA", inplace=True)
    return mentoring_ss_df


def mastery_learning_ss():
    ml_theor_df = retrieve_data(ml_theor_output, "ml_theor")
    ml_age_grp_df = retrieve_data(ml_age_group_output, "ml_age_grp")
    ml_ability_grp_df = retrieve_data(ml_ability_group_output, "ml_ability_grp")
    ml_attain_group_type_df = retrieve_data(ml_if_attain_what_grouping_type_output, "ml_attain_grouping")
    ml_goal_level_df = retrieve_data(ml_goal_level, "ml_goal_level")
    ml_asess_det_df = retrieve_data(ml_assess_detail, "ml_assess_det")
    ml_fb_det_prov_df = retrieve_data(ml_fb_detail_prov, "ml_fb_detail_prov")
    ml_mast_lev_df = retrieve_data(ml_mastery_level, "ml_mastery_lev")
    ml_ss_df = pd.concat([
        ml_theor_df,
        ml_age_grp_df,
        ml_ability_grp_df,
        ml_attain_group_type_df,
        ml_goal_level_df,
        ml_asess_det_df,
        ml_fb_det_prov_df,
        ml_mast_lev_df
    ], axis=1, sort=False)
    # fill blanks with NA
    ml_ss_df.fillna("NA", inplace=True)
    return ml_ss_df


def metacog_self_reg_ss():
    msr_knowl_type_df = retrieve_data(msr_knowl_type_output, "msr_knowl_type")
    msr_task_stage_df = retrieve_data(msr_task_stage_output, "msr_task_stage")
    msr_strategy_df = retrieve_data(msr_strategy_type_output, "msr_strategy")
    msr_motiv_aspects_df = retrieve_data(msr_self_reg_mot_aspects_output, "msr_motiv_aspects")
    msr_teaching_approach_df = retrieve_data(msr_teaching_approach_output, "msr_teaching_approach")
    msr_digit_tech_df = retrieve_data(msr_digit_tech, "msr_digit_tech")
    msr_ss_df = pd.concat([
        msr_knowl_type_df,
        msr_task_stage_df,
        msr_strategy_df,
        msr_motiv_aspects_df,
        msr_teaching_approach_df,
        msr_digit_tech_df
    ], axis=1, sort=False)
    # fill blanks with NA
    msr_ss_df.fillna("NA", inplace=True)
    return msr_ss_df


def oral_lang_ss():
    ol_focus_df = retrieve_data(ol_focus, "ol_focus")
    ol_target_df = retrieve_data(ol_target, "ol_target")
    ol_target_comp_type_df = retrieve_data(ol_imp_comp_type, "ol_target_comp_type")
    ol_act_invol_df = retrieve_data(ol_activity_invol, "ol_activity_invol")
    ol_ss_df = pd.concat([
        ol_focus_df,
        ol_target_df,
        ol_target_comp_type_df,
        ol_act_invol_df,
    ], axis=1, sort=False)
    # fill blanks with NA
    ol_ss_df.fillna("NA", inplace=True)
    return ol_ss_df


def one_t_one_comp_ss():
    comp_avail_df = retrieve_data(comparisons_available, "1_1_comparisons_Available")
    comp_avail_HT_df = retrieve_ht(comparisons_available, "1_1_comparisons_Available_SS_ht")
    comp_avail_Comments_df = retrieve_info(comparisons_available, "1_1_comparisons_Available_SS_info")
    # concatenate data frames
    one_to_one_ss_df = pd.concat([
        comp_avail_df,
    ], axis=1, sort=False)
    # fill blanks with NA
    one_to_one_ss_df.fillna("NA", inplace=True)
    # remove problematic text from outputs
    clean_up(one_to_one_ss_df)
    return one_to_one_ss_df


def peer_tut():
    tut_desc_df = retrieve_data(tutor_age_output, "pt_tut_desc")
    tut_desc_same_age_df = retrieve_data(tutor_age_same, "pt_tut_desc_same_age")
    tut_desc_cross_age_df = retrieve_data(tutor_age_cross, "pt_tut_desc_cross_age")
    tut_same_age_df = retrieve_data(tutor_same_age_output, "pt_same_age_attainment")
    tut_cross_age_df = retrieve_data(tutor_cross_age_output, "pt_cross_age_attainment")
    tut_from_df = retrieve_data(tutor_from_output, "pt_tut_from")
    tut_role_df = retrieve_data(tutor_role_output, "pt_tut_role")
    tut_tutee_attain_lev_df = retrieve_data(tutee_attainment_output, "pt_tutee_attain_level")
    digit_tech_df = retrieve_data(digit_tech_output, "pt_digit_tech")
    tut_incentive_df = retrieve_data(tutor_tutee_incentive_output, "pt_incentive")
    peer_tut_ss_df = pd.concat([
        tut_desc_df,
        tut_desc_same_age_df,
        tut_desc_cross_age_df,
        tut_same_age_df,
        tut_cross_age_df,
        tut_from_df,
        tut_role_df,
        tut_tutee_attain_lev_df,
        digit_tech_df,
        tut_incentive_df,
    ], axis=1, sort=False)
    return peer_tut_ss_df


def phys_activity_ss():
    pha_when_df = retrieve_data(pha_when_output, "pa_when")
    pha_lessons_df = retrieve_data(pha_lessons_included_output, "pa_lessons")
    pha_act_type_df = retrieve_data(pha_activity_type_output, "pa_act_type")
    pha_exer_level_df = retrieve_data(pha_exercise_level_output, "pa_exer_level")
    pha_ss_df = pd.concat([
        pha_when_df,
        pha_lessons_df,
        pha_act_type_df,
        pha_exer_level_df,
    ], axis=1, sort=False)
    # fill blanks with NA
    pha_ss_df.fillna("NA", inplace=True)
    return pha_ss_df


def read_comprehension_ss():
    rc_comp_df = retrieve_data(rc_components_output, "rc_comp")
    # split rc components for ind col extraction
    # rc comp strat data
    rc_comp_strat_df = retrieve_data(rc_comp_strat_output, "rc_comp_strat")
    # rc comp vocab data
    rc_comp_vocab_df = retrieve_data(rc_comp_vocab_output, "rc_comp_vocab")
    # rc comp reading fluency data
    rc_comp_red_flu_df = retrieve_data(rc_comp_red_flu_output, "rc_comp_red_flu")
    # rc comp phonics fluency data
    rc_comp_phon_df = retrieve_data(rc_comp_phon_output, "rc_comp_phon")
    # rc comp writing data
    rc_comp_wri_df = retrieve_data(rc_comp_wri_output, "rc_comp_wri")
    # rc comp other data
    rc_comp_other_df = retrieve_data(rc_comp_other_output, "rc_comp_other")
    # rc comp unclear data
    rc_comp_unclear_df = retrieve_data(rc_comp_unclear_output, "rc_comp_unclear")
    # ^^ end of individual column extraction ^^*
    # get rc strategy instruction data
    rc_strat_instr_df = retrieve_data(rc_strat_instruct_type_output, "rc_strat_instruc")
    # get rc instructional components data
    rc_instruc_comp_df = retrieve_data(rc_comp_other_output, "rc_instruc_comp")
    # get rc text type / reading materials data
    rc_txt_type_df = retrieve_data(rc_txt_type_output, "rc_txt_type_red_mat")
    rc_ss_df = pd.concat([
        rc_comp_df,
        rc_comp_strat_df,
        rc_comp_vocab_df,
        rc_comp_red_flu_df,
        rc_comp_phon_df,
        rc_comp_wri_df,
        rc_comp_other_df,
        rc_comp_unclear_df,
        rc_strat_instr_df,
        rc_instruc_comp_df,
        rc_txt_type_df,
    ], axis=1, sort=False)
    return rc_ss_df


def red_class_size_ss():
    redc_avg_small_class_size_df = retrieve_info(redc_avg_small_class_size_output, "redc_avg_small_class_size_info")
    redc_avg_large_class_size_df = retrieve_info(redc_avg_large_class_size_output, "redc_avg_large_class_size_info")
    redc_small_class_teach_num_df = retrieve_data(redc_small_class_teacher_number_output, "redc_small_class_teach_num")
    redc_large_class_teach_num_df = retrieve_data(redc_large_class_teacher_number_output, "redc_large_class_teach_num")
    redc_large_class_adapt_df = retrieve_data(redc_large_class_adaption_output, "redc_large_class_adapt")
    redc_lim_num_subj_df = retrieve_data(redc_reduc_for_limited_num_sub_output, "redc_lim_num_subj")
    redc_impl_all_or_most_lessons_df = retrieve_data(redc_impl_for_all_or_most_output, "redc_impl_all_or_most_lessons")
    redc_ss_df = pd.concat([
        redc_avg_small_class_size_df,
        redc_avg_large_class_size_df,
        redc_small_class_teach_num_df,
        redc_large_class_teach_num_df,
        redc_large_class_adapt_df,
        redc_lim_num_subj_df,
        redc_impl_all_or_most_lessons_df,
    ], axis=1, sort=False)
    return redc_ss_df


def repeat_year_ss():
    ry_identify_ret_stu_df = retrieve_data(ry_ret_stu_identify_output, "ry_identify_ret_stu")
    ry_ret_stu_age_df = retrieve_data(ry_ret_stu_age_output, "ry_ret_stu_age")
    ry_ret_basis_df = retrieve_data(ry_ret_basis_output, "ry_ret_basis")
    ry_impact_meas_df = retrieve_data(ry_impact_measure_delay_output, "ry_impact_meas")
    ry_stu_ret_num_df = retrieve_data(ry_stu_ret_number_output, "ry_stu_ret_num")
    ry_ret_stu_comparison_df = retrieve_data(ry_ret_stud_compared_with_output, "ry_ret_stud_comp")
    ry_prom_count_char_df = retrieve_data(ry_prom_count_characteristics_output, "ry_matching_char")
    ry_comp_df = retrieve_data(ry_comparison, "ry_comp")
    ry_comp_grp_school_df = retrieve_data(ry_comp_grp_school, "ry_comp_grp_school")
    # concatenate data frames
    ry_ss_df = pd.concat([
        ry_identify_ret_stu_df,
        ry_ret_stu_age_df,
        ry_ret_basis_df,
        ry_impact_meas_df,
        ry_stu_ret_num_df,
        ry_ret_stu_comparison_df,
        ry_prom_count_char_df,
        ry_comp_df,
        ry_comp_grp_school_df,
    ], axis=1, sort=False)
    # remove problematic text from outputs
    clean_up(ry_ss_df)
    return ry_ss_df


def soc_emo_learning_ss():
    # get involvement data
    sel_involvement_df = retrieve_data(sel_involvement_output, "sel_involvement")
    # get involvement pupils data
    sel_invol_pupils_df = retrieve_data(sel_invol_all_pupils, "sel_invol_pupils")
    # get involvement target groups data
    sel_invol_targ_groups_df = retrieve_data(sel_invol_targ_grp, "sel_invol_targ_grps")
    # get involvement classes data
    sel_invol_classes_df = retrieve_data(sel_invol_classes, "sel_invol_classes")
    # get involvement whole schools data
    sel_invol_whole_school_df = retrieve_data(sel_invol_school, "sel_invol_whole_school")
    # get involvement classroom teachers data
    sel_invol_class_teachers_df = retrieve_data(sel_invol_teachers, "sel_invol_class_teachers")
    # get involvement other staff data
    sel_invol_oth_staff_df = retrieve_data(sel_invol_other_staff, "sel_invol_oth_staff")
    # get involvement outside experts data
    sel_invol_out_experts_df = retrieve_data(sel_invol_outside_experts, "sel_invol_out_experts")
    # get involvement other data
    sel_invol_other_df = retrieve_data(sel_invol_other, "sel_invol_other")
    # get focus data
    sel_focus_df = retrieve_data(sel_focus_output, "sel_focus")
    # get location data
    sel_location_df = retrieve_data(sel_location_output, "sel_location")
    sel_ss_df = pd.concat([
        sel_involvement_df,
        sel_invol_pupils_df,
        sel_invol_targ_groups_df,
        sel_invol_classes_df,
        sel_invol_whole_school_df,
        sel_invol_class_teachers_df,
        sel_invol_oth_staff_df,
        sel_invol_out_experts_df,
        sel_invol_other_df,
        sel_focus_df,
        sel_location_df
    ], axis=1, sort=False)
    # fill blanks with NA
    sel_ss_df.fillna("NA", inplace=True)
    return sel_ss_df


def setting_streaming_ss():
    # get grouping change data
    sets_dir_grp_change_df = retrieve_data(sets_dir_grouping_change, "sets_dir_grp_change")
    """ # get grouping type within attainment data
    sets_grp_type_within_attain = get_data(sets_dir_grouping_type_within_attain)
    sets_grp_type_within_attain_df = pd.DataFrame(sets_grp_type_within_attain)
    sets_grp_type_within_attain_df = sets_grp_type_within_attain_df.T
    sets_grp_type_within_attain_df.columns = ["sets_grp_type_within_attain"] """
    """ # nested within grp type within attain ^
    # get curriculum taight within attainment data
    sets_curr_taught_attain = get_data(sets_curr_taught_in_attain_grp)
    sets_curr_taught_attain_df = pd.DataFrame(sets_curr_taught_attain)
    sets_curr_taught_attain_df = sets_curr_taught_attain_df.T
    sets_curr_taught_attain_df.columns = ["sets_curr_taught_in_attain"] """
    # get grouping type regroup data
    sets_dir_grp_type_regroup_df = retrieve_data(sets_dir_grouping_type_regroup, "sets_dir_grp_type_regroup")
    # nested within grp type regroup ^
    # get curr taught in regroup data
    sets_curr_taught_regroup_df = retrieve_data(sets_curr_taught_in_regroup, "sets_curr_taught_in_regroup")
    # get dir grouping stream data
    sets_dir_grp_stream_df = retrieve_data(sets_dir_grouping_stream, "sets_dir_grp_type_streaming")
    # get dir grouping gifted data
    sets_dir_grp_gifted_df = retrieve_data(sets_dir_grouping_gifted, "sets_dir_grp_type_gifted")
    # get school groupings data
    sets_schl_groupings_df = retrieve_data(sets_school_groupings, "sets_school_groupings")
    # get attainment grouping levels data
    sets_attain_grp_levels_df = retrieve_data(sets_attain_grouping_level, "sets_attain_grouping_levels")
    # get attainment grouping levels data
    sets_foll_same_curr_df = retrieve_data(sets_follow_same_curr, "sets_follow_same_curr")
    # get approach name data
    sets_appr_name_df = retrieve_data(sets_approach_name, "sets_approach_name")
    # get pupil assignment data
    sets_pup_assignment_df = retrieve_data(sets_pupil_assignment, "sets_pup_assign")
    sets_ss_df = pd.concat([
        sets_dir_grp_change_df,
        sets_dir_grp_type_regroup_df,
        sets_curr_taught_regroup_df,
        sets_dir_grp_stream_df,
        sets_dir_grp_gifted_df,
        sets_schl_groupings_df,
        sets_attain_grp_levels_df,
        sets_foll_same_curr_df,
        sets_appr_name_df,
        sets_pup_assignment_df
    ], axis=1, sort=False)
    # fill blanks with NA
    sets_ss_df.fillna("NA", inplace=True)
    return sets_ss_df


def small_group_tuit_ss():
    # get group size data
    group_size_df = retrieve_data(group_size_output, "sgt_group_size")
    # Get group size highlighted text
    group_size_HT_df = retrieve_ht(group_size_output, "sgt_group_size_ht")
    # Get group size user comments
    group_size_info_df = retrieve_info(group_size_output, "sgt_group_size_info")
    # get group composition data
    group_composition_df = retrieve_data(group_composition_output, "sgt_group_composition")
    # Get group composition highlighted text
    group_composition_HT_df = retrieve_ht(group_composition_output, "sgt_group_composition_ht")
    # Get group composition user comments
    group_composition_info_df = retrieve_info(group_composition_output, "sgt_group_composition_info")
    # get group lead data
    group_lead_df = retrieve_data(group_teaching_lead_output, "sgt_group_lead")
    # Get group lead highlighted text
    group_lead_HT_df = retrieve_ht(group_teaching_lead_output, "sgt_group_lead_ht")
    # Get group lead user comments
    group_lead_info_df = retrieve_info(group_teaching_lead_output, "sgt_group_lead_info")
    sgt_ss_df = pd.concat([
        group_size_df,
        group_composition_df,
        group_lead_df,
    ], axis=1, sort=False)
    # fill blanks with NA
    sgt_ss_df.fillna("NA", inplace=True)
    return sgt_ss_df


def summer_school_ss():
    ss_aim_df = retrieve_data(ss_aim_output, "ss_aim")
    ss_aim_catch_up_df = retrieve_data(ss_aim_output_catch_up, "ss_aim_catch_up")
    ss_aim_enrich_df = retrieve_data(ss_aim_output_enrich, "ss_aim_enrich")
    ss_aim_trans_df = retrieve_data(ss_aim_output_school_trans, "ss_aim_trans")
    ss_aim_gifted_df = retrieve_data(ss_aim_output_gifted, "ss_aim_gifted")
    ss_aim_unclear_df = retrieve_data(ss_aim_output_unclear, "ss_aim_unclear")
    ss_pupil_part_df = retrieve_data(ss_pupil_part_output, "ss_pupil_part")
    ss_resid_comp_df = retrieve_data(ss_resid_comp_output, "ss_resid_comp")
    ss_grp_size_df = retrieve_data(ss_group_size_output, "ss_grp_size")
    ss_act_focus_df = retrieve_data(ss_activity_focus_output, "ss_act_focus")
    ss_staff_kind_df = retrieve_data(ss_staff_kind_output, "ss_staff_kind")
    ss_par_invol_df = retrieve_data(ss_parent_invol, "ss_par_invol")
    ss_dig_tech_df = retrieve_data(ss_digit_tech, "ss_dig_tech")
    ss_atten_df = retrieve_data(ss_attendance, "ss_attendance")
    SS_ss_df = pd.concat([
        ss_aim_df,
        ss_aim_catch_up_df,
        ss_aim_enrich_df,
        ss_aim_trans_df,
        ss_aim_gifted_df,
        ss_aim_unclear_df,
        ss_pupil_part_df,
        ss_resid_comp_df,
        ss_grp_size_df,
        ss_act_focus_df,
        ss_staff_kind_df,
        ss_par_invol_df,
        ss_dig_tech_df,
        ss_atten_df
    ], axis=1, sort=False)
    SS_ss_df.fillna("NA", inplace=True)
    return SS_ss_df


def teach_assistants_ss():
    # get teaching assistants description data
    ta_desc_df = retrieve_data(ta_description_output, "ta_desc")
    # Get teaching assistants description highlighted text
    ta_desc_HT_df = retrieve_ht(ta_description_output, "ta_desc_ht")
    # Get teaching assistants description user comments
    ta_desc_Comments_df = retrieve_info(ta_description_output, "ta_desc_info")
    # TEACHING ASSISTANTS ROLE
    # get teaching assistants description data
    ta_role_df = retrieve_data(ta_role_output, "ta_role")
    # Get teaching assistants description highlighted text
    ta_role_HT_df = retrieve_ht(ta_role_output, "ta_role_ht")
    # Get teaching assistants description user comments
    ta_role_Comments_df = retrieve_info(ta_role_output, "ta_role_info")
    # TEACHING GROUP SIZE
    # get teaching assistants group size data
    ta_group_size_df = retrieve_data(ta_group_size_output, "ta_group_size")
    # get teaching assistants group size highlighted text
    ta_group_size_HT_df = retrieve_ht(ta_group_size_output, "ta_group_size_ht")
    # get teaching assistants group size user comments
    ta_group_size_Comments_df = retrieve_info(ta_group_size_output, "ta_group_size_info")
    # concatenate data frames
    ta_ss_df = pd.concat([
        ta_desc_df,
        ta_role_df,
        ta_group_size_df,
    ], axis=1, sort=False)
    # remove problematic text from outputs
    clean_up(ta_ss_df)
    return ta_ss_df


def parental_engagement():
    pe_involved_df = retrieve_data(pe_involved_output, "pe_involved")
    pe_act_loc_df = retrieve_data(pe_activity_location_output, "pe_act_loc")
    pe_prog_train_df = retrieve_data(pe_prog_training_output, "pe_prog_training")
    pe_prog_support_df = retrieve_data(pe_prog_support_output, "pe_prog_support")
    pe_children_work_with_df = retrieve_data(pe_children_output, "pe_children")
    pe_focus_df = retrieve_data(pe_focus_output, "pe_focus")
    pe_ss_df = pd.concat([
        pe_involved_df,
        pe_act_loc_df,
        pe_prog_train_df,
        pe_prog_support_df,
        pe_children_work_with_df,
        pe_focus_df,
    ], axis=1, sort=False) 
    # fill blanks with NA
    pe_ss_df.fillna("NA", inplace=True)
    return pe_ss_df


def phonics():
    ph_tar_pop_df = retrieve_data(ph_targ_pop_output, "ph_targ_pop")
    ph_const_part_df = retrieve_data(ph_constit_part_approach_output, "ph_constit_part")
    ph_const_part_synth_df = retrieve_data(ph_constit_part_approach_synth_ph, "ph_constit_part_synth_phon")
    ph_const_part_sys_df = retrieve_data(ph_constit_part_approach_syst_ph, "ph_constit_part_sys_phon")
    ph_const_part_analyt_df = retrieve_data(ph_constit_part_approach_analyt_ph, "ph_constit_part_analyt_phon")
    ph_const_part_analog_df = retrieve_data(ph_constit_part_approach_analog_ph, "ph_constit_part_analog_phon")
    ph_const_part_emb_df = retrieve_data(ph_constit_part_approach_emb_ph, "ph_constit_part_emb_phon")
    ph_const_part_phon_aware_df = retrieve_data(ph_constit_part_approach_phon_aware, "ph_constit_part_phonem_aware")
    ph_const_part_phonol_aware_df = retrieve_data(ph_constit_part_approach_phonol_aware, "ph_constit_part_phonol_aware")
    ph_const_part_onset_rime_df = retrieve_data(ph_constit_part_approach_onset_rime, "ph_constit_part_onset_rime")
    ph_const_part_syll_instr_df = retrieve_data(ph_constit_part_approach_syll_instr, "ph_constit_part_syll_instr")
    ph_const_part_sight_vocab_df = retrieve_data(ph_constit_part_approach_sight_vocab, "ph_constit_part_sight_vocab")
    ph_const_part_whole_word_df = retrieve_data(ph_constit_part_approach_whole_word, "ph_constit_part_whole_word")
    ph_central_to_approach_df = retrieve_data(ph_central_teach_lit_output, "ph_central_to_approach")
    ph_par_invol_df = retrieve_data(ph_par_invol_output, "ph_par_invol")
    ph_dig_tech_df = retrieve_data(ph_digit_tech_output, "ph_dig_tech")
    ph_ss_df = pd.concat([
        ph_tar_pop_df,
        ph_const_part_df,
        ph_const_part_synth_df,
        ph_const_part_sys_df,
        ph_const_part_analyt_df,
        ph_const_part_analog_df,
        ph_const_part_emb_df,
        ph_const_part_phon_aware_df,
        ph_const_part_phonol_aware_df,
        ph_const_part_onset_rime_df,
        ph_const_part_syll_instr_df,
        ph_const_part_sight_vocab_df,
        ph_const_part_whole_word_df,
        ph_central_to_approach_df,
        ph_par_invol_df,
        ph_dig_tech_df
    ], axis=1, sort=False)
    # fill blanks with NA
    ph_ss_df.fillna("NA", inplace=True)
    return ph_ss_df


def performance_pay():
    pp_incent_crit_df = retrieve_data(pp_incentive_criteria_output, "pp_incent_criteria")
    pp_reward_recip_df = retrieve_data(pp_reward_recipient_output, "pp_reward_recip")
    pp_incent_timing_df = retrieve_data(pp_incentive_timing_output, "pp_incent_timing")
    pp_incent_type_df = retrieve_data(pp_incentive_type_output, "pp_incent_type")
    pp_incent_amount_df = retrieve_data(pp_incentive_amount_output, "pp_incent_amount")
    pp_teach_eval_per_df = retrieve_data(pp_teacher_eval_period_output, "pp_teach_eval_per")
    pp_ss_df = pd.concat([
        pp_incent_crit_df,
        pp_reward_recip_df,
        pp_incent_timing_df,
        pp_incent_type_df,
        pp_incent_amount_df,
        pp_teach_eval_per_df,
    ], axis=1, sort=False)
    # fill blanks with NA
    pp_ss_df.fillna("NA", inplace=True)
    return pp_ss_df


def within_class_grouping():
    wc_grp_dir_df = retrieve_data(wcg_dir_grouping_change_output, "wc_grp_dir")
    wc_curr_taught_att_grp_df = retrieve_data(wcg_curr_taught_attain_grp_output, "wc_curr_taught_att_grp")
    wc_pup_affected_df = retrieve_data(wcg_pupils_affected_by_wcg_output, "wc_pup_affected")
    wc_att_grping_levels_df = retrieve_data(wcg_attain_grouping_level, "wc_attn_grouping_levels")
    wc_follow_same_curr_df = retrieve_data(wcg_follow_same_curr, "wc_follow_same_curr")
    wc_approach_name_df = retrieve_data(wcg_approach_name, "wc_approach_name")
    wc_pup_assign_df = retrieve_data(wcg_pupil_assignment, "wc_pup_assign")
    # concatenate data frames
    wc_ss_df = pd.concat([
        wc_grp_dir_df,
        wc_curr_taught_att_grp_df,
        wc_pup_affected_df,
        wc_att_grping_levels_df,
        wc_follow_same_curr_df,
        wc_approach_name_df,
        wc_pup_assign_df,
    ], axis=1, sort=False)
    # remove problematic text from outputs
    clean_up(wc_ss_df)
    return wc_ss_df

#/*************************/
#/   COMMAND LINE TABLES   /
#/*************************/

def data_analysis_cl_table():
    """
    """
    console = Console()

    main_table = Table(title="\nStrand Specific Dataframe Selection",
                       show_header=True, 
                       box=box.HORIZONTALS,
                       highlight=False,                     
    )

    main_table.add_column("", style="bold white")
    main_table.add_column("Main Toolkit", header_style="bold magenta", style="white")

    main_table.add_row("1",  "Arts Participation")
    main_table.add_row("2",  "Behaviour Interventions")
    main_table.add_row("3",  "Collaborative Learning")
    main_table.add_row("4",  "Extending School Time")
    main_table.add_row("5",  "Feedback")
    main_table.add_row("6",  "Homework")
    main_table.add_row("7",  "Individualised Instruction")
    main_table.add_row("8",  "Mentoring")
    main_table.add_row("9",  "Mastery Learning")
    main_table.add_row("10",  "Metacognition & Self Regulation")
    main_table.add_row("11",  "One to One Tution")
    main_table.add_row("12",  "Oral Language")
    main_table.add_row("13",  "Physical Activity")
    main_table.add_row("14",  "Parentel Engagement")
    main_table.add_row("15",  "Phonics")
    main_table.add_row("16",  "Performance Pay")
    main_table.add_row("17",  "Peer Tutoring")
    main_table.add_row("18",  "Reading Comprehension")
    main_table.add_row("19",  "Reducing Class Size")
    main_table.add_row("20",  "Repeating a Year")
    main_table.add_row("21",  "Social & Emotional Learning")
    main_table.add_row("22",  "Setting/Streaming")
    main_table.add_row("23",  "Small Group Tuition")
    main_table.add_row("24",  "Summer Schools")
    main_table.add_row("25",  "Teaching Assistants")
    main_table.add_row("26",  "Within-Class Grouping")

    console.print(main_table)

     # Get user selection for strand specific dataframe (if needed)
    ss_user_input = int(input("Enter a number from the list corresponding to the a strand specific data option from the list above: "))
    return ss_user_input

def strand_specific_df_selection(user_input):
    match user_input:
        # MAIN TOOLKIT
        case 1: 
            print("- Strand specific datraframe selection: Arts Participation")
            ss_df = arts_participation_ss()
        case 2: 
            print("- Strand specific datraframe selection: Behaviour Interventions")
            ss_df = behaviour_int_ss()
        case 3:
            print("- Strand specific datraframe selection: Collaborative Learning")
            ss_df = collab_learning_ss()
        case 4: 
            print("- Strand specific datraframe selection: Extending School Time")
            ss_df = ext_school_time_ss()
        case 5: 
            print("- Strand specific datraframe selection: Feedback")
            ss_df = feedback_ss()
        case 6:
            print("- Strand specific datraframe selection: Homework")
            ss_df = homework_ss()
        case 7: 
            print("- Strand specific datraframe selection: Individualised Instruction")
            ss_df = indiv_instr_ss()
        case 8: 
            print("- Strand specific datraframe selection: Mentoring")
            ss_df = mentoring_ss()
        case 9:
            print("- Strand specific datraframe selection: Mastery Learning")
            ss_df = mastery_learning_ss()
        case 10: 
            print("- Strand specific datraframe selection: Metacognition & Self Regulation")
            ss_df = metacog_self_reg_ss()
        case 11:
            print("- Strand specific datraframe selection: One to One Tuition")
            ss_df = one_t_one_comp_ss()
        case 12: 
            print("- Strand specific datraframe selection: Oral Language")
            ss_df = oral_lang_ss()
        case 13:
            print("- Strand specific datraframe selection: Physical Activity")
            ss_df = phys_activity_ss()
        case 14: 
            print("- Strand specific datraframe selection: Parentel Engagement")
            ss_df = parental_engagement()
        case 15: 
            print("- Strand specific datraframe selection: Phonics")
            ss_df = phonics()
        case 16:
            print("- Strand specific datraframe selection: Performance Pay")
            ss_df = performance_pay()
        case 17: 
            print("- Strand specific datraframe selection: Peer Tutoring")
            ss_df = peer_tut()
        case 18: 
            print("- Strand specific datraframe selection: Reading Comprehension")
            ss_df = read_comprehension_ss()
        case 19:
            print("- Strand specific datraframe selection: Reducing Class Size")
            ss_df = red_class_size_ss()
        case 20: 
            print("- Strand specific datraframe selection: Repeating a Year")
            ss_df = repeat_year_ss()
        case 21: 
            print("- Strand specific datraframe selection: Social & Emotional Learning")
            ss_df = soc_emo_learning_ss()
        case 22: 
            print("- Strand specific datraframe selection: Setting/Streaming")
            ss_df = setting_streaming_ss()
        case 23: 
            print("- Strand specific datraframe selection: Small Group Tuition")
            ss_df = small_group_tuit_ss()
        case 24: 
            print("- Strand specific datraframe selection: Summer Schools")
            ss_df = summer_school_ss()
        case 25: 
            print("- Strand specific datraframe selection: Teaching Assistants")
            ss_df = teach_assistants_ss()
        case 26: 
            print("- Strand specific datraframe selection: Within-Class Grouping")
            ss_df = within_class_grouping()
        # EARLY YEARS
        case 27: 
            print("- Strand specific datraframe selection: Early Years - Early Literacy Approaches")
            ss_df = ey_early_lit_approaches_ss()
        case 28: 
            print("- Strand specific datraframe selection: Early Numeracy Approaches")
            ss_df = ey_early_num_approaches_ss()
        case 29: 
            print("- Strand specific datraframe selection: Earlier Starting Age")
            ss_df = ey_earlier_start_age_ss()
        case 30: 
            print("- Strand specific datraframe selection: Extra Hours")
            ss_df = ey_extra_hours_ss()
        case 31: 
            print("- Strand specific datraframe selection: Play Based Learning")
            ss_df = ey_play_based_learning_ss()
    return ss_df

def display_table_struct(funcs): 
            """
            """
            for num, func in track(enumerate(funcs), description="[green]Processing dataframes..\n[/green]"):
                func(save_file=True, clean_cols=True, verbose=False)

            table = Table(show_header=True, 
                          header_style="bold magenta",
                          title="Data Cleaning Dataframe Info Table",
                          safe_box=True,
                          box=box.MINIMAL)
                    
            table.add_column("", style="green")
            table.add_column("Dataframes", header_style="bold green")
            table.add_column("Selection", justify="center", header_style="bold red")
            table.add_column("Save dir", justify="left", header_style="white")

            return table

def data_cleaning_col_breakdown():

    from rich import print
    from rich import box
    from rich.console import Console
    from rich.table import Table
    from rich.progress import track
    console = Console()

    main_table = Table(show_header=True, 
                        box=box.HORIZONTALS,
                        highlight=False,                     
    )
    main_table.add_column("Dataframe 1", header_style="bold yellow", style="bold yellow")
    main_table.add_column("Dataframe 2", header_style="bold cyan", style="bold cyan")
    main_table.add_column("Dataframe 3", header_style="bold green", style="bold green")
    main_table.add_column("Dataframe 4", header_style="bold purple", style="bold purple")
    main_table.add_column("Dataframe 5", header_style="bold red", style="bold red")
    main_table.add_row("Study ID",  "Study ID",  "Study ID",  "Study ID",  "Study ID")
    main_table.add_row("Author",  "Author",  "Author",  "Author",  "Author")
    main_table.add_row("Year",  "Year",  "Year",  "Year",  "Year")
    main_table.add_row("Abstract",  "Strand",  "Strand",  "Strand",  "Strand")
    main_table.add_row("Admin Strand",  "Int Name",  "Gender",  "Desc Stats Prim Out",  "Outcome Type")
    main_table.add_row("Publication Type EPPI",  "Int Description",  "Sample Size",  "Int Treat Grp Number",  "Standard Mean Difference")
    main_table.add_row("Publication Type",  "Int Objective",  "SES/FSM",  "Int Treat Grp Pre-test Mean/SD",  "Standard Error")
    main_table.add_row("Educational Setting", "Int Organisatio Type",  "Int Treat Sample Size",  "Int Treat Grp Post-test Mean/SD",  "Confidence Interval (lb)")
    main_table.add_row("Ecological Validity", "Int Training",  "Int Cont Sample Size",  "Int Treat Grp Gain Score Mean/SD",  "Confidence Interval (ub)")
    main_table.add_row("Student Age",  "Int Focus",  "Int Treat Grp2 Sample Size",  "Int Treat Grp Any Other Info",  "Outcome")
    main_table.add_row("Number of Schools",  "Int Teaching Approach",  "Int Treat Grp3 Sample Size",  "Int Cont Grp Number",  "Sample")
    main_table.add_row("Number of Classes",  "Int Inclusion",  "Int Treat Sample Size Analyzed",  "Int Cont Grp Pre-test Mean/SD",  "Outcome Comparison")
    main_table.add_row("Treatment Group",  "Int Time",  "Int Cont Sample Size Analyzed",  "Int Cont Grp Post-test Mean/SD",  "Effect Size Type")
    main_table.add_row("Participant Assignment",  "Int Delivery",  "Int Treat Grp2 Sample Size Analyzed",  "Int Cont Grp Gain Score Mean/SD",  "Outcome Measure")
    main_table.add_row("Level of Assignment", "Int Duration",  "Int Cont Grp2 Sample Size Analyzed",  "Int Cont Grp Any Other Info",  "Outcome Title")
    main_table.add_row("Study Design", "Int Frequency",  "Attrition Reported",  "Int Treat Grp2 Number",  "Group1 N")
    main_table.add_row( "Randomisation",  "Int Session Length",  "Attrition Treat Grp",  "Int Treat Grp2 Pre-test Mean/SD",  "Group2 N")
    main_table.add_row("Other Outcomes",  "Int Detail",  "Attrition Total (%)",  "Int Treat Grp2 Post-test Mean/SD",  "Group1 Mean")
    main_table.add_row("Additional Outcomes",  "Int Costs", "", "Int Treat Grp2 Gain Score Mean/SD", "Group2 Mean")
    main_table.add_row("Other Participants Outcomes", "Int Evaluation",  "",   "Int Treat Grp2 Any Other Info", "Group1 SD")
    main_table.add_row("",  "Baseline Differences", "",  "Int Cont Grp2 Number",  "Group2 SD")
    main_table.add_row("", "Computational Analysis",  "", "Int Cont Grp2 Pre-test Mean/SD",  "Outcome Description")
    main_table.add_row("",  "Comparability Variables Reported",  "", "Int Cont Grp2 Post-test Mean/SD",  "Test Type Outcome")
    main_table.add_row("",  "Clustering",  "", "Int Cont Grp2 Gain Score Mean/SD", "")
    main_table.add_row("",  "", "",  "Int Cont Grp2 Any Other Info", "")
    main_table.add_row("",  "", "",  "Follow-up Information", "")

    console.print(main_table)