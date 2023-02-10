#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jonathan Reardon'

# Third party imports
import pandas as pd

# Local imports
from Main import load_json
from Main import get_metadata
from Main import comments
from Main import highlighted_text
from Main import get_data
from Main import get_outcome_lvl1
from Main import get_outcome_lvl2
from Main import clean_up


def process_data(output, data_col):
    # get data
    data = get_data(output)
    data_df = pd.DataFrame(data)
    data_df = data_df.T
    data_df.columns = [data_col]
    return data_df


def process_ht(output, ht_col):
    # get highlighted text
    ht = highlighted_text(output)
    ht_df = pd.DataFrame(ht)
    ht_df = ht_df.T
    ht_df.columns = [ht_col]
    return ht_df


def process_info(output, info_col):
    # get comments
    comms = comments(output)
    comments_df = pd.DataFrame(comms)
    comments_df = comments_df.T
    comments_df.columns = [info_col]
    return comments_df


def process_metadata(output, info_col):
    # get metadata
    metadata = get_metadata(output)
    metadata_df = pd.DataFrame(metadata)
    #metadata_df = metadata_df.T
    metadata_df.columns = [info_col]
    return metadata_df

load_json()

def get_abstract_data():
    """
    Retrieve abstract data and return it as a cleaned up DataFrame.

    Returns:
    -------
    abstract_df : pandas.DataFrame
        DataFrame containing abstract data.
    """
    # Get abstract data frame
    abstract_df = process_metadata("Abstract", "abstract")

    # Clean up data frame
    clean_up(abstract_df)
    abstract_df.fillna("NA", inplace=True)

    return abstract_df

def get_admin_strand_data():
    """
    Retrieve data about the admin strand and return it as a cleaned up DataFrame.

    Returns:
    -------
    df : pandas.DataFrame
        DataFrame containing the admin strand data and associated comments.
    """
    from AttributeIDList import admin_strand_output

    # Get admin strand data frame
    admin_strand_df = process_data(admin_strand_output,"strand_raw")

    # Get admin strand user comments
    admin_strand_df_com = process_info(admin_strand_output,"strand_info")

    # Concatenate data frames
    df = pd.concat([admin_strand_df, admin_strand_df_com], axis=1, sort=False)

    # Clean up data frame
    clean_up(df)
    df.fillna("NA", inplace=True)

    return df

def get_student_age_data():
    """
    Retrieve student age data and return it as a cleaned up DataFrame.

    Returns:
    -------
    df : pandas.DataFrame
        DataFrame containing student age data.
    """
    from AttributeIDList import student_age_output

    # Get student age data
    student_age_df = process_data(student_age_output, "part_age_raw")

    # Get student age highlighted text
    student_age_HT_df = process_ht(student_age_output, "part_age_ht")

    # Get student age user comments
    student_age_Comments_df = process_info(student_age_output, "part_age_info")

    # concatenate data frames
    dataframes = [student_age_df, student_age_HT_df, student_age_Comments_df]
    df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    clean_up(df)
    df.fillna("NA", inplace=True)

    return df

def get_attrition_data():
    """
    Retrieve attrition data and return it as a cleaned up DataFrame.

    Returns:
    -------
    df : pandas.DataFrame
        DataFrame containing attrition data.
    """
    from AttributeIDList import attr_dropout_rep_output
    from AttributeIDList import overall_perc_attr
    from AttributeIDList import treat_grp_attr

    #-----------------------------#
    # ATTRITION DROP OUT REPORTED #
    #-----------------------------#

    attr_dropout_rep_df = process_data(attr_dropout_rep_output, "attri_raw")
    attr_dropout_rep_HT_df = process_ht(attr_dropout_rep_output, "attri_ht")
    attr_dropout_rep_comments_df = process_info(attr_dropout_rep_output, "attri_info")

    #-----------------------------#
    #  TREATMENT GROUP ATTRITION  #
    #-----------------------------#

    treat_grp_attr_HT_df = process_ht(treat_grp_attr, "attri_treat_ht")
    treat_grp_attr_comments_df = process_info(treat_grp_attr, "attri_treat_info")

    #-----------------------------#
    #  OVERALL PERCENT ATTRITION  #
    #-----------------------------#

    overall_perc_attr_HT_df = process_ht(overall_perc_attr, "attri_perc_ht")
    overall_perc_attr_comments_df = process_info(overall_perc_attr, "attri_perc_info")

    # Concatenate dataframes
    dataframes = [attr_dropout_rep_df, 
                  attr_dropout_rep_HT_df, 
                  attr_dropout_rep_comments_df, 
                  treat_grp_attr_HT_df, 
                  treat_grp_attr_comments_df, 
                  overall_perc_attr_HT_df, 
                  overall_perc_attr_comments_df]
                  
    df = pd.concat(dataframes, axis=1, sort=False)

    return df

# get author data
def author():
    """
    Retrieve 'ShortTitle'' data and return it as a cleaned up DataFrame.

    Returns:
    -------
    author_df : pandas.DataFrame
        DataFrame containing publication author data.
    """
    # Get author metadata
    author_df = process_metadata("ShortTitle", "pub_author")

    # Clean up dataframe
    clean_up(author_df)
    author_df.fillna("NA", inplace=True)

    return author_df

def authors():
    """
    Retrieve Authors data and return it as a cleaned up DataFrame.

    Returns:
    -------
    author_df : pandas.DataFrame
        DataFrame containing publication author data.
    """
    # Get authors metadata
    authors_df = process_metadata("Authors", "pub_author")

    # Clean up data frame
    authors_df.fillna("NA", inplace=True)

    return authors_df

def baseline_diff():
    """
    Retrieve baseline differences data and return it as a cleaned up DataFrame.

    Returns:
    -------
    df : pandas.DataFrame
        DataFrame containing baseline differences data.
    """
    from AttributeIDList import baseline_diff_output

    # Get baseline differences data
    baseline_diff_df = process_data(baseline_diff_output, "base_diff_raw")

    # Get baseline differences highlighted text
    baseline_diff_ht_df = process_ht(baseline_diff_output, "base_diff_ht")

    # Get baseline differences comments
    baseline_diff_comments_df = process_info(baseline_diff_output, "base_diff_info")

    # Concatenate data frames
    dataframes = [baseline_diff_df,baseline_diff_ht_df, baseline_diff_comments_df]
    baseline_diff_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    baseline_diff_df.fillna("NA", inplace=True)

    return baseline_diff_df

def cilower():
    # extract confidence interval lower data
    cilowersmd_df = get_outcome_lvl1("CILowerSMD")
    cilowersmd_df = pd.DataFrame(cilowersmd_df)

    # round data to 4 decimal places
    cilowersmd_df = cilowersmd_df.applymap(
        lambda x: round(x, 4) if isinstance(x, (int, float)) else x)

    # name each column (number depends on outcome number)
    cilowersmd_df.columns=[
        "ci_lower_"+'{}'.format(column+1) for column in cilowersmd_df.columns
    ]

    # fill blanks with NA
    cilowersmd_df.fillna("NA", inplace=True)

    # replace problematic text
    cilowersmd_df = cilowersmd_df.replace(r'^\s*$', "NA", regex=True)

    return cilowersmd_df

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

def ciupper():
    """
    """
    # Extract confidence interval upper data
    ciuppersmd = get_outcome_lvl1("CIUpperSMD")
    ciuppersmd_df = pd.DataFrame(ciuppersmd)

    # Round data to 4 decimal places
    ciuppersmd_df = ciuppersmd_df.applymap(
        lambda x: round(x, 4) if isinstance(x, (int, float)) else x)

    # Name each column (number depends on outcome number)
    ciuppersmd_df.columns = [
        "ci_upper_"+'{}'.format(column+1) for column in ciuppersmd_df.columns]

    # Clean up data frame
    ciuppersmd_df.fillna("NA", inplace=True)
    ciuppersmd_df = ciuppersmd_df.replace(r'^\s*$', "NA", regex=True)

    return ciuppersmd_df

def clustering():
    """
    
    """
    from AttributeIDList import clustering_output

    # Get clustering data
    clustering_df = process_data(clustering_output, "clust_anal_raw")

    # Get clustering highlighted text
    clustering_ht_df = process_ht(clustering_output, "clust_anal_ht")

    # Get clustering user comments
    clustering_comments_df = process_info(clustering_output, "clust_anal_info")

    # Concatenate data frames
    dataframes = [clustering_df, clustering_ht_df, clustering_comments_df]
    df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    df.fillna("NA", inplace=True)

    return df

def com_var_rep():
    """
    
    """
    from AttributeIDList import comp_vars_rep
    from AttributeIDList import which_comp_vars_rep_output

    #====================================================#
    # Are the variables used for comparability reported? #
    #====================================================#

    # Get comparability variables reported data
    comp_vars_rep_df = process_data(comp_vars_rep, "comp_var_rep_raw")

    # Get Comparability Variables Reported highlighted text
    comp_vars_rep_ht_df = process_ht(comp_vars_rep, "comp_var_rep_ht")

    # Get Comparability Variables Reported comments
    comp_vars_rep_comments_df = process_info(comp_vars_rep, "comp_var_rep_info")

    #=====================================================#
    # If yes, which variables are used for comparability? #
    #=====================================================#

    # Get "which" variables are used for comparability data
    comp_vars_rep_df = process_data(which_comp_vars_rep_output, "comp_var_raw")

    # Get Comparability Variables Reported highlighted text
    comp_vars_rep_ht_df = process_ht(which_comp_vars_rep_output, "comp_var_ht")

    # Get Comparability Variables Reported comments
    comp_vars_rep_comments_df = process_info(which_comp_vars_rep_output, "comp_var_info")

    # Concatenate data frames
    dataframes = [comp_vars_rep_df, comp_vars_rep_ht_df,
                  comp_vars_rep_comments_df, comp_vars_rep_df,
                  comp_vars_rep_ht_df, comp_vars_rep_comments_df]

    comp_var_rep_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    comp_var_rep_df.fillna("NA", inplace=True)

    return comp_var_rep_df

def comparability():
    """

    """
    from AttributeIDList import comparability_output

    # get comparability data
    comparability_df = process_data(comparability_output, "comp_anal_raw")

    # Get Comparability highlighted text
    comparability_ht_df = process_ht(comparability_output, "comp_anal_ht")

    # Get Comparability user comments
    comparability_comments_df = process_info(comparability_output, "comp_anal_info")

    # Concatenate data frames
    dataframes = [comparability_df, comparability_ht_df, comparability_comments_df]
    comparability = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    comparability.fillna("NA", inplace=True)

    return comparability

def country():
    """
    
    """
    from AttributeIDList import countries

    # get country data
    country_df = process_data(countries, "loc_country_raw")

    # Get country highlighted text
    country_ht_df = process_ht(countries, "loc_country_ht")

    # Get country user comments
    country_Comments_df = process_info(countries, "loc_country_info")

    # concatenate data frames
    """ country_df = pd.concat(
        [country_df, country_ht_df, country_Comments_df], axis=1, sort=False) """

    # Clean up data frame
    country_df.fillna("NA", inplace=True)

    return country_df

def curr_sub():
    """
    
    """
    from AttributeIDList import curriculum_subjects
    from AttributeIDList import other_outcomes_output
    from AttributeIDList import which_other_outcomes_output
    from AttributeIDList import other_participants_output

    # Get curriculum subjects data
    curric_subjects_df = process_data(curriculum_subjects, "test_subject_raw")

    # Get Country highlighted text
    curric_subjects_ht_df = process_ht(curriculum_subjects, "test_subject_ht")

    # Get Country user comments
    curric_subjects_comments_df = process_info(curriculum_subjects, "test_subject_info")

    #-------------------------#
    # OTHER OUTCOMES REPORTED #
    #-------------------------#

    # Get other outcomes data
    other_outcomes_df = process_data(other_outcomes_output, "out_other_raw")

    # Get other outcomes highlighted text
    other_outcomes_ht_df = process_ht(other_outcomes_output, "out_other_ht")

    # Get other outcomes comments
    other_outcomes_comments_df = process_info(other_outcomes_output, "out_other_info")

    #-------------------------#
    #   WHICH OTHER OUTCOMES  #
    #-------------------------#

    # Get which other outcomes data
    which_outcomes_df = process_data(which_other_outcomes_output, "out_info_raw")

    # Get which other outcomes highlighted text
    which_outcomes_ht_df = process_ht(which_other_outcomes_output, "out_info_ht")

    # Get which other outcomes comments
    which_outcomes_comments_df = process_info(which_other_outcomes_output, "out_info_info")

    #-------------------------#
    #    OTHER PARTICIPANTS   #
    #-------------------------#

    # GSet other participants highlighted text
    other_participants_HT_df = process_ht(other_participants_output, "part_other_ht")

    # Get other participants comments
    other_participants_comments_df = process_info(other_participants_output, "part_other_info")

    dataframes = [curric_subjects_df, 
                  curric_subjects_ht_df, 
                  curric_subjects_comments_df, 
                  other_outcomes_df, 
                  other_outcomes_ht_df,
                  other_outcomes_comments_df,
                  which_outcomes_df, 
                  which_outcomes_ht_df, 
                  which_outcomes_comments_df, 
                  other_participants_HT_df,
                  other_participants_comments_df]

    curric_subj_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up dataframe
    curric_subj_df.fillna("NA", inplace=True)
    clean_up(curric_subj_df)

    return curric_subj_df

def date():
    # get year data
    year = get_metadata("Year")
    year = pd.DataFrame(year)
    year.columns = ["pub_year"]

    # add decade column
    """ year_df["decade"] = year_df.apply(decade_row, axis=1) """

    # fill blanks with NA
    year.fillna("NA", inplace=True)

    return year

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

def edu_setting():
    """
    
    """
    from AttributeIDList import edu_setting_output

    # Get educational setting data
    edu_setting_df = process_data(edu_setting_output, "int_setting_raw")
    # Get Educational Setting highlighted text
    edu_setting_ht_df = process_ht(edu_setting_output, "int_setting_ht")
    # Get Educational Setting comments
    edu_setting_comments_df = process_info(edu_setting_output, "int_setting_info")

    # Goncatenate data frames
    dataframes = [edu_setting_df, edu_setting_ht_df, edu_setting_comments_df]
    edu_setting_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    edu_setting_df.fillna("NA", inplace=True)

    return edu_setting_df

def es_type():
    """
    
    """
    from AttributeIDList import es_type_output

    # Get effect size type data
    es_type = get_outcome_lvl2(es_type_output)
    es_type_df = pd.DataFrame(es_type)

    # Name each column (number depends on outcome number)
    es_type_df.columns = [
        "out_es_type_" + str(column + 1) for column in es_type_df.columns
    ]

    # Clean up data frame
    es_type_df.fillna("NA", inplace=True)
    return es_type_df

# get eppiID data
def eppi():
    """

    """
    eppi_id = get_metadata("ItemId")
    eppi_id_df = pd.DataFrame(eppi_id)
    eppi_id_df.columns = ["id"]
    eppi_id_df.fillna("NA", inplace=True)
    return eppi_id_df

def gender():
    """
    
    """
    from AttributeIDList import student_gender

    # Get educational setting data
    gender_df = process_data(student_gender, "part_gen_raw")
    # Get Educational Setting highlighted text
    gender_ht_df = process_ht(student_gender, "part_gen_ht")
    # Get Educational Setting comments
    gender_comments_df = process_info(student_gender, "part_gen_info")

    # Concatenate data frames
    dataframes = [gender_df, gender_ht_df, gender_comments_df]
    gender_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    gender_df.fillna("NA", inplace=True)
    return gender_df

def gender_split():
    """
    
    """
    from AttributeIDList import gender_split_output

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

def int_costs():
    """
    """
    from AttributeIDList import int_costs_reported

    # Get Intervention Costs Reported data
    int_costs_df = process_data(int_costs_reported, "int_cost_raw")
    # Get Intervention Costs Reported highlighted text
    int_costs_HT_df = process_ht(int_costs_reported, "int_cost_ht")
    # Get Intervention Costs Reported comments
    int_costs_comments_df = process_info(int_costs_reported, "int_cost_info")

    # Concatenate data frames
    dataframes = [int_costs_df, int_costs_HT_df, int_costs_comments_df]
    int_costs_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    clean_up(int_costs_df)
    int_costs_df.fillna("NA", inplace=True)

    return int_costs_df

def int_delivery():
    """
    
    """
    from AttributeIDList import intervention_delivery_output

    # Get intervention delivery data
    int_deliv_df = process_data(intervention_delivery_output, "int_who_raw")
    # Get intervention delivery highlighted text
    Int_deliv_ht_df = process_ht(intervention_delivery_output, "int_who_ht")
    # Get intervention delivery comments
    Int_deliv_comments_df = process_info(intervention_delivery_output, "int_who_info")

    # Concatenate data frames
    dataframes = [int_deliv_df, Int_deliv_ht_df, Int_deliv_comments_df]
    int_deliv_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    clean_up(int_deliv_df)
    int_deliv_df.fillna("NA", inplace=True)

    return int_deliv_df

def intervention_desc():
    """
    
    """
    from AttributeIDList import intervention_description_output

    # get intervention description highlighted text
    int_desc_ht_df = process_ht(intervention_description_output, "int_desc_ht")
    # get intervention description user comments
    int_desc_comments_df = process_info(intervention_description_output, "int_desc_info")

    # Concatenate dataframes
    dataframes = [int_desc_ht_df, int_desc_comments_df]
    int_desc_df = pd.concat([dataframes], axis=1, sort=False)

    # Clean up data frame
    clean_up(int_desc_df)
    int_desc_df.fillna("NA", inplace=True)

    return int_desc_df

def int_detail():
    """
    
    """
    from AttributeIDList import int_impl_details

    # Get intervention implementation detail data
    int_detail_df = process_data(int_impl_details, "int_fidel_raw")

    # Get intervention implementation detail highlighted text
    int_detail_ht_df = process_ht(int_impl_details, "int_fidel_ht")

    # Get intervention implementation detail comments
    int_detail_comments_df = process_info(int_impl_details, "int_fidel_info")

    # Concatenate data frames
    dataframes = [int_detail_df, int_detail_ht_df, int_detail_comments_df]
    intervention_detail_df = pd.concat([dataframes], axis=1, sort=False)

    # Clean up data frame
    clean_up(intervention_detail_df)
    intervention_detail_df.fillna("NA", inplace=True)

    return intervention_detail_df

def int_duration():
    """
    """
    from AttributeIDList import int_dur_output

    # get intervention duration highlighted text
    int_dur_ht_df = process_ht(int_dur_output, "int_dur_ht")
    # get intervention duration user comments
    int_dur_comments_df = process_info(int_dur_output, "int_dur_info")

    # Concatenate data frames
    dataframes = [int_dur_ht_df, int_dur_comments_df]
    intervention_duration_df = pd.concat([dataframes], axis=1, sort=False)

    # Clean up data frame
    clean_up(intervention_duration_df)
    intervention_duration_df.fillna("NA", inplace=True)

    return intervention_duration_df

def int_duration_comm():
    """
    """
    from AttributeIDList import int_dur_output

    # get intervention duration user comments
    int_dur_comments_df = process_info(int_dur_output, "int_dur_info")

    # Remove problematic text (potential escape sequences) from text input
    clean_up(int_dur_comments_df)

    # Clean up data frame
    int_dur_comments_df.fillna("NA", inplace=True)

    return int_dur_comments_df

def int_eval():
    """
    """
    from AttributeIDList import int_eval

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
    int_eval_df = pd.concat([dataframes], axis=1, sort=False)

    int_eval_df=int_eval_df[[
        "out_eval_raw", 
        "out_eval_ht", 
        "out_eval_info", 
        "eef_eval_raw"
    ]]

    # Clean up data frame
    clean_up(int_eval_df)
    int_eval_df.fillna("NA", inplace=True)

    return int_eval_df

def intervention_focus():
    """
    
    """
    from AttributeIDList import int_focus_output

    # Get intervention focus data
    int_focus_df = process_data(int_focus_output, "int_part_raw")
    # Get intervention focus highlighted text
    int_focus_ht_df = process_ht(int_focus_output, "int_part_ht")
    # Get intervention focus comments
    int_focus_comments_df = process_info(int_focus_output, "int_part_info")

    # Voncatenate data frames
    dataframes = [int_focus_df, int_focus_ht_df, int_focus_comments_df]
    int_focus_df = pd.concat([dataframes], axis=1, sort=False)

    # Clean up data frame
    clean_up(int_focus_df)
    int_focus_df.fillna("NA", inplace=True)

    return int_focus_df

def int_frequency():
    """
    """
    from AttributeIDList import inte_freq_output

    # Get intervention frequency highlighted text
    int_freq_ht_df = process_ht(inte_freq_output, "int_freq_ht")

    # Get intervention frequency user comments
    int_freq_comments_df = process_info(inte_freq_output, "int_freq_info")

    # Concatenate data frames
    dataframes = [int_freq_ht_df, int_freq_comments_df]
    int_freq_df = pd.concat([dataframes], axis=1, sort=False)

    # Clean up dataframe
    clean_up(int_freq_df)
    int_freq_df.fillna("NA", inplace=True)

    return int_freq_df

def int_frequency_comms():
    """
    """
    from AttributeIDList import inte_freq_output

    # Get intervention frequency user comments
    int_freq_comments_df = process_info(inte_freq_output, "int_freq_info")

    # Clean up data frame
    clean_up(int_freq_comments_df)
    int_freq_comments_df.fillna("NA", inplace=True)

    return int_freq_comments_df


def int_inclusion():
    """
    """
    from AttributeIDList import int_appr_dig_tech
    from AttributeIDList import int_appr_par_or_comm_vol

    ###########################################
    # DIGITAL TECHNOLOGY INTERVENTION INCLUSION
    ###########################################

    # Get Digital Technology (inclusion) main data
    dig_tech_df = process_data(int_appr_dig_tech, "digit_tech_raw")

    # Get Digital Technology (inclusion) highlighted text
    dig_tech_ht_df = process_ht(int_appr_dig_tech, "digit_tech_ht")

    # Get Digital Technology (inclusion) user comments
    dig_tech_comments_df = process_info(int_appr_dig_tech, "digit_tech_info")
    
    ###########################################
    # PARENTS OR COMMUNITY VOLUNTEERS INCLUSION
    ###########################################

    # Get Parents/Community volunteers (inclusion) main data
    par_or_commu_vol_df = process_data(int_appr_par_or_comm_vol, "parent_partic_raw")

    # Get Parents/Community volunteers (inclusion) highlighted text
    par_or_comm_vol_ht_df = process_ht(int_appr_par_or_comm_vol, "parent_partic_ht")

    # Get Parents/Community volunteers (inclusion) user comments
    par_or_comm_vol_comments_df = process_info(int_appr_par_or_comm_vol, "parent_partic_info")

    # concatenate data frames
    dataframes = [
        dig_tech_df,
        dig_tech_ht_df,
        dig_tech_comments_df,
        par_or_commu_vol_df,
        par_or_comm_vol_ht_df,
        par_or_comm_vol_comments_df
    ]

    int_incl_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    clean_up(int_incl_df)
    int_incl_df.fillna("NA", inplace=True)

    return int_incl_df


def int_inclusion_digit_tech():
    """
    """
    from AttributeIDList import int_appr_dig_tech

    #===========================================#
    # DIGITAL TECHNOLOGY INTERVENTION INCLUSION #
    #===========================================#

    # Get Digital Technology (inclusion) main data
    dig_tech_df = process_data(int_appr_dig_tech, "digit_tech_raw")
    # Get Digital Technology (inclusion) highlighted text
    dig_tech_ht_df = process_ht(int_appr_dig_tech, "digit_tech_ht")
    # Get Digital Technology (inclusion) comments
    dig_tech_Comments_df = process_info(int_appr_dig_tech, "digit_tech_info")

    # Concatenate data frames
    dataframes = [dig_tech_df, dig_tech_ht_df, dig_tech_Comments_df]
    int_incl_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    clean_up(int_incl_df)
    int_incl_df.fillna("NA", inplace=True)

    return int_incl_df

def int_inclusion_par_vol():
    """
    """
    from AttributeIDList import int_appr_par_or_comm_vol

    #===========================================#
    # PARENTS OR COMMUNITY VOLUNTEERS INCLUSION #
    #===========================================#

    # Get Parents/Community volunteers (inclusion) main data
    par_or_comm_vol_df = process_data(int_appr_par_or_comm_vol, "parent_partic_raw")
    # Get Parents/Community volunteers (inclusion) highlighted text
    par_or_comm_vol_ht_df = process_ht(int_appr_par_or_comm_vol, "parent_partic_ht")
    # Get Parents/Community volunteers (inclusion) comments
    par_or_comm_vol_comments_df = process_info(int_appr_par_or_comm_vol, "parent_partic_info")

    # Concatenate data frames
    dataframes = [par_or_comm_vol_df, par_or_comm_vol_ht_df, par_or_comm_vol_comments_df]
    int_incl_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    clean_up(int_incl_df)
    int_incl_df.fillna("NA", inplace=True)

    return int_incl_df

def intervention_name():
    """
    """
    from AttributeIDList import int_name_output

    # Get intervention name highlighted text
    int_name_ht_df = process_ht(int_name_output, "int_name_ht")
    # Get intervention name user comments
    int_name_comments_df = process_info(int_name_output, "int_name_info")

    # Clean up data frame
    int_name_comments_df.replace('\r', ' ', regex=True, inplace=True)
    int_name_comments_df.replace('\n', ' ', regex=True, inplace=True)
    int_name_comments_df.replace(':', ' ', regex=True, inplace=True)
    int_name_comments_df.replace(';', ' ', regex=True, inplace=True)

    # Concatenate dataframes
    dataframes = [int_name_ht_df, int_name_comments_df]

    int_name_df = pd.concat(dataframes, axis=1, sort=False)

    # Cleanup data frame
    int_name_df.fillna("NA", inplace=True)

    return int_name_df

def intervention_objec():
    """
    """
    from AttributeIDList import intervention_objectives_output

    # Get Intervention Name highlighted text
    Intervention_ObjectivesHT = highlighted_text(intervention_objectives_output)
    Intervention_ObjectivesHT_df = pd.DataFrame(Intervention_ObjectivesHT)
    Intervention_ObjectivesHT_df = Intervention_ObjectivesHT_df.T
    Intervention_ObjectivesHT_df.columns=["int_objec_ht"]

    # Get Intervention Description user comments
    Intervention_Objectives_Comments = comments(intervention_objectives_output)
    Intervention_Objectives_Comments_df = pd.DataFrame(Intervention_Objectives_Comments)
    Intervention_Objectives_Comments_df = Intervention_Objectives_Comments_df.T
    Intervention_Objectives_Comments_df.columns = ["int_objec_info"]

    # concatenate data frames
    intervention_objectives_df = pd.concat([
        Intervention_ObjectivesHT_df, 
        Intervention_Objectives_Comments_df
    ], axis=1, sort=False)

    # remove problematic text
    clean_up(intervention_objectives_df)

    # fill blanks with NA
    intervention_objectives_df.fillna("NA", inplace=True)

    return intervention_objectives_df

def int_org_type():
    """
    """
    from AttributeIDList import int_org_type_output

    # Get intervention organisation type main data
    int_org_type_ht_df = process_data(int_org_type_output, "int_prov_raw")
    # Get intervention organisation type highlighted text
    int_org_type_ht_df = process_ht(int_org_type_output, "int_prov_ht")
    # Get intervention organisation type comments
    int_org_type_comments_df = process_info(int_org_type_output, "int_prov_info")

    # Concatenate data frames
    dataframes = [int_org_type_ht_df, int_org_type_ht_df, int_org_type_comments_df]
    int_org_type = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    clean_up(int_org_type)
    int_org_type.fillna("NA", inplace=True)

    return int_org_type

def int_sess_len():
    from AttributeIDList import intervention_session_length_output
    # get intervention session length highlighted text
    InterventionSessionLength_HT = highlighted_text(intervention_session_length_output)
    InterventionSessionLength_HT_df = pd.DataFrame(InterventionSessionLength_HT)
    InterventionSessionLength_HT_df = InterventionSessionLength_HT_df.T
    InterventionSessionLength_HT_df.columns = ["int_leng_ht"]

    # get intervention session length user comments
    InterventionSessionLength_Comments = comments(intervention_session_length_output)
    InterventionSessionLength_Comments_df = pd.DataFrame(InterventionSessionLength_Comments)
    InterventionSessionLength_Comments_df = InterventionSessionLength_Comments_df.T
    InterventionSessionLength_Comments_df.columns = ["int_leng_info"]

    # concatenate data frames
    intervention_session_length_df = pd.concat([
        InterventionSessionLength_HT_df, 
        InterventionSessionLength_Comments_df
    ], axis=1, sort=False)

    # remove problematic text
    clean_up(intervention_session_length_df)

    intervention_session_length_df.fillna("NA", inplace=True)

    return intervention_session_length_df

def int_sess_len_comm():
    from AttributeIDList import intervention_session_length_output

    # get intervention session length user comments
    InterventionSessionLength_Comments = comments(intervention_session_length_output)
    InterventionSessionLength_Comments_df = pd.DataFrame(InterventionSessionLength_Comments)
    InterventionSessionLength_Comments_df = InterventionSessionLength_Comments_df.T
    InterventionSessionLength_Comments_df.columns = ["int_leng_info"]

    # remove problematic text
    clean_up(InterventionSessionLength_Comments_df)

    InterventionSessionLength_Comments_df.fillna("NA", inplace=True)

    return InterventionSessionLength_Comments_df

def int_teach_appr():
    from AttributeIDList import intervention_teaching_approach
    # get intervention teaching approach data
    InterventionTeachingApproach = get_data(intervention_teaching_approach)
    InterventionTeachingApproach_df = pd.DataFrame(InterventionTeachingApproach)
    InterventionTeachingApproach_df = InterventionTeachingApproach_df.T
    InterventionTeachingApproach_df.columns = ["int_approach_raw"]

    # get intervention teaching approach highlighted text
    InterventionTeachingApproach_HT = highlighted_text(intervention_teaching_approach)
    InterventionTeachingApproach_HT_df = pd.DataFrame(InterventionTeachingApproach_HT)
    InterventionTeachingApproach_HT_df = InterventionTeachingApproach_HT_df.T
    InterventionTeachingApproach_HT_df.columns = ["int_approach_ht"]

    # get intervention teaching approach user comments
    InterventionTeachingApproach_Comments = comments(intervention_teaching_approach)
    InterventionTeachingApproach_Comments_df = pd.DataFrame(InterventionTeachingApproach_Comments)
    InterventionTeachingApproach_Comments_df = InterventionTeachingApproach_Comments_df.T
    InterventionTeachingApproach_Comments_df.columns = ["int_approach_info"]

    # concatenate data frames
    intervention_teaching_approach_df = pd.concat([
        InterventionTeachingApproach_df, 
        InterventionTeachingApproach_HT_df, 
        InterventionTeachingApproach_Comments_df
    ], axis=1, sort=False)

    # remove problematic text
    clean_up(intervention_teaching_approach_df)

    # fill blanks with NA
    intervention_teaching_approach_df.fillna("NA", inplace=True)

    return intervention_teaching_approach_df

def int_time():
    from AttributeIDList import intervention_time_output
    
    # Get Intervention Time main data
    InterventionTime = get_data(intervention_time_output)
    InterventionTime_df = pd.DataFrame(InterventionTime)
    InterventionTime_df = InterventionTime_df.T
    InterventionTime_df.columns = ["int_when_raw"]

    # Get Intervention Time highlighted text
    InterventionTime_HT = highlighted_text(intervention_time_output)
    InterventionTime_HT_df = pd.DataFrame(InterventionTime_HT)
    InterventionTime_HT_df = InterventionTime_HT_df.T
    InterventionTime_HT_df.columns = ["int_when_ht"]

    # Get Intervention Time user comments
    InterventionTime_Comments = comments(intervention_time_output)
    InterventionTime_Comments_df = pd.DataFrame(InterventionTime_Comments)
    InterventionTime_Comments_df = InterventionTime_Comments_df.T
    InterventionTime_Comments_df.columns = ["int_when_info"]

    # concatenate data frames
    intervention_time_df = pd.concat([
        InterventionTime_df, 
        InterventionTime_HT_df, 
        InterventionTime_Comments_df
    ], axis=1, sort=False)

    # Remove problematic text (potential escape sequences) from text input
    clean_up(intervention_time_df)

    # fill blanks with NA
    intervention_time_df.fillna("NA", inplace=True)

    return intervention_time_df

def int_train_prov():
    from AttributeIDList import intervention_training_provided_output
    # get intervention training provided data
    InterventionTrainingProvided = get_data(intervention_training_provided_output)
    InterventionTrainingProvided_df = pd.DataFrame(InterventionTrainingProvided)
    InterventionTrainingProvided_df = InterventionTrainingProvided_df.T
    InterventionTrainingProvided_df.columns = ["int_training_raw"]

    # get intervention training provided highlighted text
    InterventionTrainingProvided_HT = highlighted_text(intervention_training_provided_output)
    InterventionTrainingProvided_HT_df = pd.DataFrame(InterventionTrainingProvided_HT)
    InterventionTrainingProvided_HT_df = InterventionTrainingProvided_HT_df.T
    InterventionTrainingProvided_HT_df.columns = ["int_training_ht"]

    # get intervention training provided user comments
    InterventionTrainingProvided_Comments = comments(intervention_training_provided_output)
    InterventionTrainingProvided_Comments_df = pd.DataFrame(InterventionTrainingProvided_Comments)
    InterventionTrainingProvided_Comments_df = InterventionTrainingProvided_Comments_df.T
    InterventionTrainingProvided_Comments_df.columns = ["int_training_info"]

    # concatenate data frames
    intervention_training_provided_df = pd.concat([
        InterventionTrainingProvided_df, 
        InterventionTrainingProvided_HT_df, 
        InterventionTrainingProvided_Comments_df
    ], axis=1, sort=False)

    # Remove problematic text (potential escape sequences) from text input
    clean_up(intervention_training_provided_df)

    # fill blanks with NA
    intervention_training_provided_df.fillna("NA", inplace=True)

    return intervention_training_provided_df

def issue():
    # get issue data
    issue = get_metadata("Issue")
    issue_df = pd.DataFrame(issue)
    issue_df.columns = ["Issue"]
    issue_df.fillna("NA", inplace=True)

    return issue_df

def level_assign():
    from AttributeIDList import level_of_assignment_output
    # get level of assignment data
    levelofassignment = get_data(level_of_assignment_output)
    levelofassignment_df = pd.DataFrame(levelofassignment)
    levelofassignment_df = levelofassignment_df.T
    levelofassignment_df.columns=["level_assig_raw"]

    # remove square brackets
    levelofassignment_df['level_assig_raw'] = levelofassignment_df['level_assig_raw'].str[0]

    # Get Level of Assignment highlighted text
    levelofassignment_HT = highlighted_text(level_of_assignment_output)
    level_of_assignment_output_df = pd.DataFrame(levelofassignment_HT)
    level_of_assignment_output_df = level_of_assignment_output_df.T
    level_of_assignment_output_df.columns = ["level_assig_ht"]

    # Get Level of Assignment user comments
    levelofassignment_Comments = comments(level_of_assignment_output)
    levelofassignment_Comments_df = pd.DataFrame(levelofassignment_Comments)
    levelofassignment_Comments_df = levelofassignment_Comments_df.T
    levelofassignment_Comments_df.columns = ["level_assig_info"]

    # concatenate data frames
    level_of_assignment_df = pd.concat([
        levelofassignment_df, 
        level_of_assignment_output_df, 
        levelofassignment_Comments_df
    ], axis=1, sort=False)

    # fill blanks with NA
    level_of_assignment_df.fillna("NA", inplace=True)

    return level_of_assignment_df

def out_test_type():
    from AttributeIDList import test_type_output
    # get test type data
    testtype = get_outcome_lvl2(test_type_output)
    testtype_df = pd.DataFrame(testtype)

    # name each column (number depends on outcome number)
    testtype_df.columns = [
        "out_test_type_raw_"+'{}'.format(column+1) for column in testtype_df.columns]

    # fill blanks with NA
    testtype_df.fillna("NA", inplace=True)

    return testtype_df

def outcome():
    # get outcome data
    outcome = get_outcome_lvl1("OutcomeText")
    outcome_df = pd.DataFrame(outcome)

    # name each column (number depends on outcome number)
    outcome_df.columns = ["out_label_" +'{}'.format(column+1) for column in outcome_df.columns]

    # fill blanks with NA
    outcome_df.fillna("NA", inplace=True)

    return outcome_df

def out_comp():
    # get outcome comparison data
    out_comp = get_outcome_lvl1("ControlText")
    out_comp_df = pd.DataFrame(out_comp)

    # name each column (number depends on outcome number)
    out_comp_df.columns = [
        "out_comp_" +'{}'.format(column+1) for column in out_comp_df.columns]

    # fill blanks with NA
    out_comp_df.fillna("NA", inplace=True)

    return out_comp_df

def out_desc():
    """
    """
    # Get outcome description data
    out_desc = get_outcome_lvl1("OutcomeDescription")
    out_desc_df = pd.DataFrame(out_desc)

    # Name each column (number depends on outcome number)
    out_desc_df.columns = [
        "out_desc_"+'{}'.format(column+1) for column in out_desc_df.columns]

    """ outcome_description_df = outcome_description_df.fillna("NA") """

    # Clean up data frame
    out_desc_df = out_desc_df.replace(r'^\s*$', "NA", regex=True)

    out_desc_df.replace('\r', ' ', regex=True, inplace=True)
    out_desc_df.replace('\n', ' ', regex=True, inplace=True)
    out_desc_df.replace(':', ' ', regex=True, inplace=True)
    out_desc_df.replace(';', ' ', regex=True, inplace=True)

    return out_desc_df

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

def out_measure():
    # get outcome measure data
    outcome_measure = get_outcome_lvl1("InterventionText")
    outcome_measure_df = pd.DataFrame(outcome_measure)

    # name each column (number depends on outcome number)
    outcome_measure_df.columns = [
        "out_measure_"+'{}'.format(column+1) for column in outcome_measure_df.columns]

    # fill blanks with NA
    outcome_measure_df.fillna("NA", inplace=True)

    # remove problematic text
    outcome_measure_df = outcome_measure_df.replace(r'^\s*$', "NA", regex=True)

    return outcome_measure_df 

def out_text():
    # get outcome text data
    outcome_text = get_outcome_lvl1("OutcomeText")
    outcome_text_df = pd.DataFrame(outcome_text)

    # round data to 4 decimal places
    outcome_text_df = outcome_text_df.applymap(lambda x: round(
        x, 4) if isinstance(x, (int, float)) else x)

    # name each column (number depends on outcome number)
    outcome_text_df.columns = [
        "out_text_"+'{}'.format(column+1) for column in outcome_text_df.columns]

    # fill blanks with NA
    outcome_text_df.fillna("NA", inplace=True)

    # replace problematic text
    outcome_text_df = outcome_text_df.replace(r'^\s*$', "NA", regex=True)

    return outcome_text_df

def out_tit():
    # get outcome title data
    outcome_title = get_outcome_lvl1("Title")
    outcome_title_df = pd.DataFrame(outcome_title)

    # name each column (number depends on outcome number)
    outcome_title_df.columns = ["out_tit_"+'{}'.format(column+1) for column in outcome_title_df.columns]

    """ outcome_label_text_df.fillna("NA", inplace=True) """

    # replace problematic text
    outcome_title_df = outcome_title_df.replace(r'^\s*$', "NA", regex=True)

    return outcome_title_df

def out_type():
    from AttributeIDList import outcome_type_codes
    # get outcome type data
    outcome_type = get_outcome_lvl2(outcome_type_codes)
    outcometype_df = pd.DataFrame(outcome_type)

    # name each column (number depends on outcome number)
    outcometype_df.columns = ["out_type_"+'{}'.format(column+1) for column in outcometype_df.columns]

    # fill blanks with NA
    outcometype_df.fillna("NA", inplace=True)

    return outcometype_df

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

def part_assign():
    from AttributeIDList import participant_assignment_output
    # get participant assignment data
    participantassignment = get_data(participant_assignment_output)
    participantassignment_df = pd.DataFrame(participantassignment)
    participantassignment_df = participantassignment_df.T
    participantassignment_df.columns = ["part_assig_raw"]

    # remove square brackets
    participantassignment_df['part_assig_raw'] = participantassignment_df['part_assig_raw'].str[0]

    # Gget level of assignment highlighted text
    participantassignment_HT = highlighted_text(participant_assignment_output)
    participantassignment_HT_df = pd.DataFrame(participantassignment_HT)
    participantassignment_HT_df = participantassignment_HT_df.T
    participantassignment_HT_df.columns = ["part_assig_ht"]

    # get level of assignment user comments
    participantassignment_Comments = comments(participant_assignment_output)
    participantassignment_Comments_df = pd.DataFrame(participantassignment_Comments)
    participantassignment_Comments_df = participantassignment_Comments_df.T
    participantassignment_Comments_df.columns = ["part_assig_info"]

    # concatenate data frames
    participant_assignment_df = pd.concat([
        participantassignment_df, 
        participantassignment_HT_df, 
        participantassignment_Comments_df
    ], axis=1, sort=False)

    # fill blanks with NA
    participant_assignment_df.fillna("NA", inplace=True)

    # remove problematic text
    clean_up(participant_assignment_df)

    return participant_assignment_df

def desc_s_prim_out_rep_c_two():

    from AttributeIDList import control_group_two_number
    from AttributeIDList import control_group_two_pretest_mean
    from AttributeIDList import control_group_two_pretest_sd
    from AttributeIDList import control_group_two_posttest_mean
    from AttributeIDList import control_group_two_posttest_sd
    from AttributeIDList import control_group_two_gain_score_mean
    from AttributeIDList import control_group_two_gain_score_sd
    from AttributeIDList import control_group_two_any_other_info
    from AttributeIDList import follow_up_data_reported
    
    ###########################
    # CONTROL GROUP NUMBER
    ###########################

    # Get Control Group Number highlighted text
    ControlGroupNumber_HT = highlighted_text(control_group_two_number)
    ControlGroupNumber_HT_df = pd.DataFrame(ControlGroupNumber_HT)
    ControlGroupNumber_HT_df = ControlGroupNumber_HT_df.T
    ControlGroupNumber_HT_df.columns = ["n_cont2_ht"]

    # Get Control Group Number comments
    ControlGroupNumber_comments = comments(control_group_two_number)
    ControlGroupNumber_comments_df = pd.DataFrame(ControlGroupNumber_comments)
    ControlGroupNumber_comments_df = ControlGroupNumber_comments_df.T
    ControlGroupNumber_comments_df.columns = ["n_cont2_info"]

    #################################
    # Control GROUP PRE-TEST MEAN
    #################################

    # Get Control Group Pre-test Mean highlighted text
    ControlGroupPretestMean_HT = highlighted_text(control_group_two_pretest_mean)
    ControlGroupPretestMean_HT_df = pd.DataFrame(ControlGroupPretestMean_HT)
    ControlGroupPretestMean_HT_df = ControlGroupPretestMean_HT_df.T
    ControlGroupPretestMean_HT_df.columns = ["pre_c2_mean_ht"]

    # Get Control Group Pre-test Mean comments
    ControlGroupPretestMean_comments = comments(control_group_two_pretest_mean)
    ControlGroupPretestMean_comments_df = pd.DataFrame(ControlGroupPretestMean_comments)
    ControlGroupPretestMean_comments_df = ControlGroupPretestMean_comments_df.T
    ControlGroupPretestMean_comments_df.columns = ["pre_c2_mean_info"]

    ################################
    # Control GROUP PRE-TEST SD
    ################################

    # Get Control Group Pre-test SD highlighted text
    ControlGroupPretestSD_HT = highlighted_text(control_group_two_pretest_sd)
    ControlGroupPretestSD_HT_df = pd.DataFrame(ControlGroupPretestSD_HT)
    ControlGroupPretestSD_HT_df = ControlGroupPretestSD_HT_df.T
    ControlGroupPretestSD_HT_df.columns = ["pre_c2_sd_ht"]

    # Get Control Group Pre-test SD comments
    ControlGroupPretestSD_comments = comments(control_group_two_pretest_sd)
    ControlGroupPretestSD_comments_df = pd.DataFrame(ControlGroupPretestSD_comments)
    ControlGroupPretestSD_comments_df = ControlGroupPretestSD_comments_df.T
    ControlGroupPretestSD_comments_df.columns = ["pre_c2_sd_info"]

    ##################################
    # Control GROUP POST-TEST MEAN
    ###################################

    # Get Control Group Post-Test Mean highlighted text
    ControlGroupPostTestMean_HT = highlighted_text(control_group_two_posttest_mean)
    ControlGroupPostTestMean_HT_df = pd.DataFrame(ControlGroupPostTestMean_HT)
    ControlGroupPostTestMean_HT_df = ControlGroupPostTestMean_HT_df.T
    ControlGroupPostTestMean_HT_df.columns = ["post_c2_mean_ht"]

    # Get Control Group Post-Test Mean comments
    ControlGroupPostTestMean_comments = comments(control_group_two_posttest_mean)
    ControlGroupPostTestMean_comments_df = pd.DataFrame(ControlGroupPostTestMean_comments)
    ControlGroupPostTestMean_comments_df = ControlGroupPostTestMean_comments_df.T
    ControlGroupPostTestMean_comments_df.columns = ["post_c2_mean_info"]

    ##################################
    # Control GROUP POST-TEST SD
    ###################################

    # Get Control Group Post-test SD highlighted text
    ControlGroupPostTestSD_HT = highlighted_text(control_group_two_posttest_sd)
    ControlGroupPostTestSD_HT_df = pd.DataFrame(ControlGroupPostTestSD_HT)
    ControlGroupPostTestSD_HT_df = ControlGroupPostTestSD_HT_df.T
    ControlGroupPostTestSD_HT_df.columns = ["post_c2_sd_ht"]

    # Get Control Group Post-test SD comments
    ControlGroupPostTestSD_comments = comments(control_group_two_posttest_sd)
    ControlGroupPostTestSD_comments_df = pd.DataFrame(ControlGroupPostTestSD_comments)
    ControlGroupPostTestSD_comments_df = ControlGroupPostTestSD_comments_df.T
    ControlGroupPostTestSD_comments_df.columns = ["post_c2_sd_info"]

    ####################################
    # Control GROUP GAIN SCORE MEAN
    ####################################

    # Get Control Group Grain Score Mean highlighted text
    ControlGroupGainScoreMean_HT = highlighted_text(control_group_two_gain_score_mean)
    ControlGroupGainScoreMean_HT_df = pd.DataFrame(ControlGroupGainScoreMean_HT)
    ControlGroupGainScoreMean_HT_df = ControlGroupGainScoreMean_HT_df.T
    ControlGroupGainScoreMean_HT_df.columns = ["gain_c2_mean_ht"]

    # Get Control Group Gain Score Mean comments
    ControlGroupGainScoreMean_comments = comments(control_group_two_gain_score_mean)
    ControlGroupGainScoreMean_comments_df = pd.DataFrame(ControlGroupGainScoreMean_comments)
    ControlGroupGainScoreMean_comments_df = ControlGroupGainScoreMean_comments_df.T
    ControlGroupGainScoreMean_comments_df.columns = ["gain_c2_mean_info"]

    ##################################
    # Control GROUP GAIN SCORE SD
    ##################################

    # Get Control Group Grain Score SD highlighted text
    ControlGroupGainScoreSD_HT = highlighted_text(control_group_two_gain_score_sd)
    ControlGroupGainScoreSD_HT_df = pd.DataFrame(ControlGroupGainScoreSD_HT)
    ControlGroupGainScoreSD_HT_df = ControlGroupGainScoreSD_HT_df.T
    ControlGroupGainScoreSD_HT_df.columns = ["gain_c2_sd_ht"]

    # Get Control Group Gain Score SD comments
    ControlGroupGainScoreSD_comments = comments(control_group_two_gain_score_sd)
    ControlGroupGainScoreSD_comments_df = pd.DataFrame(ControlGroupGainScoreSD_comments)
    ControlGroupGainScoreSD_comments_df = ControlGroupGainScoreSD_comments_df.T
    ControlGroupGainScoreSD_comments_df.columns = ["gain_c2_sd_info"]

    ###############################
    # Control GROUP OTHER INFO
    ###############################

    # Get Control Group Other Information highlighted text
    ControlGroupOtherInfo_HT = highlighted_text(control_group_two_any_other_info)
    ControlGroupOtherInfo_HT_df = pd.DataFrame(ControlGroupOtherInfo_HT)
    ControlGroupOtherInfo_HT_df = ControlGroupOtherInfo_HT_df.T
    ControlGroupOtherInfo_HT_df.columns = ["out_c2_other_ht"]

    # Get Control Group Other Information comments
    ControlGroupOtherInfo_comments = comments(control_group_two_any_other_info)
    ControlGroupOtherInfo_comments_df = pd.DataFrame(ControlGroupOtherInfo_comments)
    ControlGroupOtherInfo_comments_df = ControlGroupOtherInfo_comments_df.T
    ControlGroupOtherInfo_comments_df.columns = ["out_c2_other_info"]

    ########################
    # Follow up data?
    ########################

    # Get Follow Up Data
    followupdata = get_data(follow_up_data_reported)
    followupdata_df = pd.DataFrame(followupdata)
    followupdata_df = followupdata_df.T
    followupdata_df.columns = ["follow_up_raw"]

    # Get Follow Up Data highlighted text
    followupdata_HT = highlighted_text(follow_up_data_reported)
    followupdata_HT_df = pd.DataFrame(followupdata_HT)
    followupdata_HT_df = followupdata_HT_df.T
    followupdata_HT_df.columns = ["follow_up_ht"]

    # Get Follow Up Data comments
    followupdata_comments = comments(follow_up_data_reported)
    followupdata_comments_df = pd.DataFrame(followupdata_comments)
    followupdata_comments_df = followupdata_comments_df.T
    followupdata_comments_df.columns = ["follow_up_info"]

    # concatenate data frames
    DescStatsPrimaryOutcomeReported_Control_TWO_df = pd.concat([
        ControlGroupNumber_HT_df, 
        ControlGroupNumber_comments_df,
        ControlGroupPretestMean_HT_df, 
        ControlGroupPretestMean_comments_df,
        ControlGroupPretestSD_HT_df, 
        ControlGroupPretestSD_comments_df,
        ControlGroupPostTestMean_HT_df, 
        ControlGroupPostTestMean_comments_df,
        ControlGroupPostTestSD_HT_df, 
        ControlGroupPostTestSD_comments_df,
        ControlGroupGainScoreMean_HT_df, 
        ControlGroupGainScoreMean_comments_df,
        ControlGroupGainScoreSD_HT_df, 
        ControlGroupGainScoreSD_comments_df,
        ControlGroupOtherInfo_HT_df, 
        ControlGroupOtherInfo_comments_df,
        followupdata_df, 
        followupdata_HT_df, 
        followupdata_comments_df
    ], axis=1, sort=False)

    return DescStatsPrimaryOutcomeReported_Control_TWO_df


def desc_s_p_out_rep_contr():

    from AttributeIDList import ctrl_grp_number
    from AttributeIDList import ctrl_grp_pretest_mean
    from AttributeIDList import ctrl_grp_pretest_sd
    from AttributeIDList import ctrl_grp_posttest_mean
    from AttributeIDList import ctrl_grp_posttest_sd
    from AttributeIDList import ctrl_grp_gain_score_mean
    from AttributeIDList import ctrl_grp_gain_score_sd
    from AttributeIDList import ctrl_grp_any_other_info
    #from AttributeIDList import follow_up_data_reported

    ###########################
    # CONTROL GROUP NUMBER
    ###########################

    # Get Control Group Number highlighted text
    ctrl_grp_num_ht_df = process_ht(ctrl_grp_number, "n_cont_ht")
    # Get Control Group Number comments
    ctrl_grp_num_comments_df = process_info(ctrl_grp_number, "n_cont_info")

    #################################
    # Control GROUP PRE-TEST MEAN
    #################################

    # Get Control Group Pre-test Mean highlighted text
    ctrl_grp_pretest_mean_ht_df = process_ht(ctrl_grp_pretest_mean, "pre_c_mean_ht")
    # Get Control Group Pre-test Mean comments
    ctrl_grp_pretest_mean_comments_df = process_info(ctrl_grp_pretest_mean, "pre_c_mean_info")

    ################################
    # Control GROUP PRE-TEST SD
    ################################

    # Get Control Group Pre-test SD highlighted text
    ctrl_grp_pretest_sd_ht_df = process_ht(ctrl_grp_pretest_sd, "pre_c_sd_ht")
    # Get Control Group Pre-test SD comments
    ctrl_grp_pretest_sd_comments_df = process_info(ctrl_grp_pretest_sd, "pre_c_sd_info")

    ##################################
    # Control GROUP POST-TEST MEAN
    ###################################

    # Get Control Group Post-Test Mean highlighted text
    ctrl_grp_post_test_mean_ht_df = process_ht(ctrl_grp_posttest_mean, "post_c_mean_ht")
    # Get Control Group Post-Test Mean comments
    ctrl_grp_post_test_mean_comments_df = process_info(ctrl_grp_posttest_mean, "post_c_mean_info")

    ##################################
    # Control GROUP POST-TEST SD
    ###################################

    # Get Control Group Post-test SD highlighted text
    ctrl_grp_post_test_sd_ht_df = process_ht(ctrl_grp_posttest_sd, "post_c_sd_ht")
    # Get Control Group Post-test SD comments
    ctrl_grp_post_test_sd_comments_df = process_info(ctrl_grp_posttest_sd, "post_c_sd_info")

    ####################################
    # Control GROUP GAIN SCORE MEAN
    ####################################

    # Get Control Group Gain Score Mean highlighted text
    Ctrl_grp_gain_score_mean_ht_df = process_ht(ctrl_grp_gain_score_mean, "gain_c_mean_ht")
    # Get Control Group Gain Score Mean comments
    ctrl_grp_gain_score_mean_comments_df = process_info(ctrl_grp_gain_score_mean, "gain_c_mean_info")

    ##################################
    # Control GROUP GAIN SCORE SD
    ##################################

    # Get Control Group Gain Score SD highlighted text
    ctrl_grp_gain_score_sd_ht_df = process_ht(ctrl_grp_gain_score_sd, "gain_c_sd_ht")
    # Get Control Group Gain Score SD comments
    ctrl_grp_gain_score_sd_comments_df = process_info(ctrl_grp_gain_score_sd, "gain_c_sd_info")

    ###############################
    # Control GROUP OTHER INFO
    ###############################

    # Get Control Group Other Information highlighted text
    ctrl_grp_other_info_ht_df = process_ht(ctrl_grp_any_other_info, "out_c_other_ht")
    # Get Control Group Other Information comments
    ctrl_grp_other_info_comments_df = process_info(ctrl_grp_any_other_info, "out_c_other_info")

    """ ########################
    # Follow up data?
    ########################
    followupdata = get_data(follow_up_data_reported)
    followupdata_df = pd.DataFrame(followupdata)
    followupdata_df = followupdata_df.T
    followupdata_df.columns=["Follow_Up_Data_Reported"]

    followupdata_df["Follow_Up_Data_Reported_YES"] = followupdata_df["Follow_Up_Data_Reported"].map(set(['Yes']).issubset).astype(int)
    followupdata_df["Follow_Up_Data_Reported_NO"] = followupdata_df["Follow_Up_Data_Reported"].map(set(['No']).issubset).astype(int)

    # Get Follow Up Data highlighted text
    followupdata_HT = highlighted_text(follow_up_data_reported)
    followupdata_HT_df = pd.DataFrame(followupdata_HT)
    followupdata_HT_df = followupdata_HT_df.T
    followupdata_HT_df.columns = ["Follow_Up_Data_Reported_HT"]

    # Get Follow Up Data comments
    followupdata_comments = comments(follow_up_data_reported)
    followupdata_comments_df = pd.DataFrame(followupdata_comments)
    followupdata_comments_df = followupdata_comments_df.T
    followupdata_comments_df.columns = ["Follow_Up_Data_Reported_comments"]

    print(followupdata_df)
    """

    # Concatenate data frames
    dataframes = [ctrl_grp_num_ht_df, 
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
                  ctrl_grp_gain_score_sd_ht_df, 
                  ctrl_grp_gain_score_sd_comments_df,
                  ctrl_grp_other_info_ht_df, 
                  ctrl_grp_other_info_comments_df]

    desc_stats_prim_out_rep_control_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up dataframe
    desc_stats_prim_out_rep_control_df.fillna("NA", inplace=True)

    return desc_stats_prim_out_rep_control_df

def desc_s_o_out_rep_interv_2():
    """
    
    """
    from AttributeIDList import int_grp_two_number
    from AttributeIDList import int_grp_two_pretest_mean
    from AttributeIDList import int_grp_two_pretest_sd
    from AttributeIDList import int_grp_two_posttest_mean
    from AttributeIDList import int_grp_two_posttest_sd
    from AttributeIDList import int_grp_two_gain_score_mean
    from AttributeIDList import int_grp_two_gain_score_sd
    from AttributeIDList import int_grp_two_any_other_info

    ###########################
    # INTERVENTION GROUP NUMBER
    ###########################

    # Get Intervention Group Number highlighted text
    int_grp_num_ht_df = process_ht(int_grp_two_number, "n_treat2_ht")
    # Get Intervention Group Number comments
    int_grp_num_comments_df = process_info(int_grp_two_number, "n_treat2_info")

    #################################
    # INTERVENTION GROUP PRE-TEST MEAN
    #################################

    # Get Intervention Group Pre-test Mean highlighted text
    int_grp_pretest_mean_ht_df = process_ht(int_grp_two_pretest_mean, "pre_t2_mean_ht")
    # Get Intervention Group Pre-test Mean comments
    int_grp_pretest_mean_comments_df = process_info(int_grp_two_pretest_mean, "pre_t2_mean_info")

    ################################
    # INTERVENTION GROUP PRE-TEST SD
    ################################

    # Get Intervention Group Pre-test SD highlighted text
    int_grp_pretest_sd_ht_df = process_ht(int_grp_two_pretest_sd, "pre_t2_sd_ht")
    # Get Intervention Group Pre-test SD comments
    int_grp_pretest_sd_comments_df = process_info(int_grp_two_pretest_sd, "pre_t2_sd_info")

    ##################################
    # INTERVENTION GROUP POST-TEST MEAN
    ###################################

    # Get Intervention Group Post-Test Mean highlighted text
    int_grp_post_test_mean_ht_df = process_ht(int_grp_two_posttest_mean, "post_t2_mean_ht")
    # Get Intervention Group Post-Test Mean comments
    int_grp_post_test_mean_comments_df = process_info(int_grp_two_posttest_mean, "post_t2_mean_info")

    ##################################
    # INTERVENTION GROUP POST-TEST SD
    ###################################

    # Get Intervention Group Post-test SD highlighted text
    int_grp_post_test_sd_ht_df = process_ht(int_grp_two_posttest_sd, "post_t2_sd_ht")
    # Get Intervention Group Post-test SD comments
    int_grp_post_test_sd_comments_df = process_info(int_grp_two_posttest_sd, "post_t2_sd_info")

    ####################################
    # INTERVENTION GROUP GAIN SCORE MEAN
    ####################################

    # Get Intervention Group Gain Score Mean highlighted text
    int_grp_gain_score_mean_ht_df = process_ht(int_grp_two_gain_score_mean, "gain_t2_mean_ht")
    # Get Intervention Group Gain Score Mean comments
    int_grp_gain_score_mean_comments_df = process_info(int_grp_two_gain_score_mean, "gain_t2_mean_info")

    ##################################
    # INTERVENTION GROUP GAIN SCORE SD
    ##################################

    # Get Intervention Group Grain Score SD highlighted text
    int_grp_gain_score_sd_ht_df = process_ht(int_grp_two_gain_score_sd, "gain_t2_sd_ht")
    # Get Intervention Group Gain Score SD comments
    int_grp_gain_score_sd_comments_df = process_info(int_grp_two_gain_score_sd, "gain_t2_sd_info")

    ###############################
    # INTERVENTION GROUP OTHER INFO
    ###############################

    # Get Intervention Group Other Information highlighted text
    int_grp_other_info_ht_df = process_ht(int_grp_two_any_other_info, "out_t2_other_ht")
    # Get Intervention Group Other Information comments
    int_grp_other_info_comments_df = process_info(int_grp_two_any_other_info, "out_t2_other_info")

    # Concatenate data frames
    dataframes = [int_grp_num_ht_df, 
                  int_grp_num_comments_df,
                  int_grp_pretest_mean_ht_df, 
                  int_grp_pretest_mean_comments_df,
                  int_grp_pretest_sd_ht_df,
                  int_grp_pretest_sd_comments_df,
                  int_grp_post_test_mean_ht_df, 
                  int_grp_post_test_mean_comments_df,
                  int_grp_post_test_sd_ht_df, 
                  int_grp_post_test_sd_comments_df,
                  int_grp_gain_score_mean_ht_df, 
                  int_grp_gain_score_mean_comments_df,
                  int_grp_gain_score_sd_ht_df, 
                  int_grp_gain_score_sd_comments_df,
                  int_grp_other_info_ht_df, 
                  int_grp_other_info_comments_df]

    desc_stats_prim_out_rep_int_two_df = pd.concat(dataframes, axis=1, sort=False)

    # Cleanup data frame
    desc_stats_prim_out_rep_int_two_df.fillna("NA", inplace=True)

    return desc_stats_prim_out_rep_int_two_df

def desc_s_p_out_rep_interv():
    """
    
    """
    from AttributeIDList import int_grp_number
    from AttributeIDList import int_grp_pretest_mean
    from AttributeIDList import int_grp_pretest_sd
    from AttributeIDList import intn_grp_posttest_mean
    from AttributeIDList import int_grp_posttest_sd
    from AttributeIDList import int_grp_gain_score_mean
    from AttributeIDList import int_grp_gain_score_sd
    from AttributeIDList import int_grp_any_other_info

    #---------------------------#
    # INTERVENTION GROUP NUMBER #
    #---------------------------#

    # Get Intervention Group Number highlighted text
    int_grp_num_ht_df = process_ht(int_grp_number, "n_treat_ht")
    # Get Intervention Group Number comments
    int_grp_number_comments_df = process_info(int_grp_number, "n_treat_info")

    #------------------------------------#
    #  INTERVENTION GROUP PRE-TEST MEAN  #
    #------------------------------------#

    # Get Intervention Group Pre-test Mean highlighted text
    int_grp_pretest_mean_ht_df = process_ht(int_grp_pretest_mean, "pre_t_mean_ht")
    # Get Intervention Group Pre-test Mean comments
    int_grp_pretest_mean_comments_df = process_info(int_grp_pretest_mean, "pre_t_mean_info")

    #--------------------------------#
    # INTERVENTION GROUP PRE-TEST SD #
    #--------------------------------#

    # Get Intervention Group Pre-test SD highlighted text
    int_group_pretest_sd_ht_df = process_ht(int_grp_pretest_sd, "pre_t_sd_ht")
    # Get Intervention Group Pre-test SD comments
    int_group_pretest_sd_comments_df = process_info(int_grp_pretest_sd, "pre_t_sd_info")

    #-----------------------------------#
    # INTERVENTION GROUP POST-TEST MEAN #
    #-----------------------------------#

    # Get Intervention Group Post-Test Mean highlighted text
    int_group_posttest_mean_ht_df = process_ht(intn_grp_posttest_mean, "prepost_t_mean_ht_t_sd_ht")
    # Get Intervention Group Post-Test Mean comments
    int_grp_posttest_mean_comments_df = process_info(intn_grp_posttest_mean, "post_t_mean_info")

    #---------------------------------#
    # INTERVENTION GROUP POST-TEST SD #
    #---------------------------------#

    # Get Intervention Group Post-test SD highlighted text
    int_grp_posttest_sd_ht_df = process_ht(int_grp_posttest_sd, "post_t_sd_ht")
    # Get Intervention Group Post-test SD comments
    int_grp_posttest_sd_comments_df = process_info(int_grp_posttest_sd, "post_t_sd_info")

    #------------------------------------#
    # INTERVENTION GROUP GAIN SCORE MEAN #
    #------------------------------------#

    # Get Intervention Group Grain Score Mean highlighted text
    int_group_gain_score_mean_ht_df = process_ht(int_grp_gain_score_mean, "gain_t_mean_ht")
    # Get Intervention Group Gain Score Mean comments
    int_group_gain_score_mean_comments_df = process_info(int_grp_gain_score_mean, "gain_t_mean_info")
    

    #----------------------------------#
    # INTERVENTION GROUP GAIN SCORE SD #
    #----------------------------------#

    # Get Intervention Group Grain Score SD highlighted text
    int_grp_gain_score_sd_ht_df = process_ht(int_grp_gain_score_sd, "gain_t_sd_ht")
    # Get Intervention Group Gain Score SD comments
    int_grp_gain_score_sd_comments_df = process_info(int_grp_gain_score_sd, "gain_t_sd_info")

    #-------------------------------#
    # INTERVENTION GROUP OTHER INFO #
    #-------------------------------#

    # Get Intervention Group Other Information highlighted text
    int_grp_other_info_ht_df = process_ht(int_grp_any_other_info, "out_t_other_ht")
    # Get Intervention Group Other Information comments
    int_grp_other_info_comments_df = process_info(int_grp_any_other_info, "out_t_other_info")

    # Concatenate data frames
    dataframes = [int_grp_num_ht_df, 
                  int_grp_number_comments_df,
                  int_grp_pretest_mean_ht_df, 
                  int_grp_pretest_mean_comments_df,
                  int_group_pretest_sd_ht_df, 
                  int_group_pretest_sd_comments_df,
                  int_group_posttest_mean_ht_df, 
                  int_grp_posttest_mean_comments_df,
                  int_grp_posttest_sd_ht_df, 
                  int_grp_posttest_sd_comments_df,
                  int_group_gain_score_mean_ht_df, 
                  int_group_gain_score_mean_comments_df,
                  int_grp_gain_score_sd_ht_df, 
                  int_grp_gain_score_sd_comments_df,
                  int_grp_other_info_ht_df, 
                  int_grp_other_info_comments_df]

    desc_stats_prim_outc_rep_int_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up dataframe
    desc_stats_prim_outc_rep_int_df.fillna("NA", inplace=True)

    return desc_stats_prim_outc_rep_int_df

def desc_s_out_rep():
    """
    """
    from AttributeIDList import desc_stats_primary_outcome

    #--------------------------#
    # PRIMARY OUTCOME REPORTED #
    #--------------------------#

    # Get Descriptive Stats (Primary Outcome) Reported data
    desc_stats_prim_out_rep_df = process_data(desc_stats_primary_outcome, "desc_stats_raw")
    # Get Descriptive Stats (Primary Outcome) Reported highlighted text
    desc_stats_prim_out_rep_ht_df = process_ht(desc_stats_primary_outcome, "desc_stats_ht")
    # Get Descriptive Stats (Primary Outcome) Reported comments
    descs_tats_prim_out_rep_comments_df = process_info(desc_stats_primary_outcome, "desc_stats_info")

    # Concatenate data frames
    dataframes = [desc_stats_prim_out_rep_df, 
                  desc_stats_prim_out_rep_ht_df, 
                  descs_tats_prim_out_rep_comments_df]

    desc_stats_out_rep_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean data frame
    desc_stats_out_rep_df.fillna("NA", inplace=True)

    return desc_stats_out_rep_df

def pubeppi():
    """
    """
    # Get pubtype eppi data
    pubtype_eppi = get_metadata("TypeName")
    pubtype_eppi_df = pd.DataFrame(pubtype_eppi)
    pubtype_eppi_df.columns = ["pub_eppi"]

    # Clean up data frame
    pubtype_eppi_df.fillna("NA", inplace=True)

    return pubtype_eppi_df

def pub_type():
    """
    """
    from AttributeIDList import publication_type_output

    # Get publication type data
    pub_type_df = process_data(publication_type_output, "pub_type_raw")
    # Get Publication Type highlighted text
    publ_type_ht_df = process_ht(publication_type_output, "pubtype_ht")
    # Get Publication Type comments
    pub_type_comments_df = process_info(publication_type_output, "pubtype_info")

    # Concatenate data frames
    dataframes = [pub_type_df, publ_type_ht_df, pub_type_comments_df]
    pub_type_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    pub_type_df.fillna("NA", inplace=True)

    return pub_type_df

def publisher():
    """
    """
    # Get author data
    publisher = get_metadata("Publisher")
    publisher_df = pd.DataFrame(publisher)
    publisher_df.columns = ["Publisher"]
    publisher_df.fillna("NA", inplace=True)

    return publisher_df

def gender():
    """
    """
    from AttributeIDList import student_gender

    # Get gender data
    gender_df = process_data(student_gender, "part_gen_raw")
    # Get Gender highlighted text
    gender_ht_df = process_ht(student_gender, "part_gen_ht")
    # Get Gender comments
    gender_comments_df = process_info(student_gender, "part_gen_info")

    # Concatenate data frames
    dataframes = [gender_df, gender_ht_df, gender_comments_df]
    gender_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    gender_df.fillna("NA", inplace=True)

    return gender_df

def randomisation():
    """
    """
    from AttributeIDList import randomisation_details

    # Get randomisation data
    rand_df = process_data(randomisation_details, "rand_raw")
    # Get Randomisation highlighted text
    rand_details_df = process_ht(randomisation_details, "rand_ht")
    # Get Randomisation comments
    rand_comments_df = process_info(randomisation_details, "rand_info")

    # Concatenate data frames
    dataframes = [rand_df, rand_details_df, rand_comments_df]
    rand_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    rand_df.fillna("NA", inplace=True)

    rand_df['rand_raw'] = rand_df['rand_raw'].apply(lambda x: ",".join(x) if isinstance(x, list) else x)

    return rand_df

def samp_size_anal():

    from AttributeIDList import sample_size_analyzed_intervention_output
    from AttributeIDList import sample_size_analyzed_control_output
    from AttributeIDList import sample_size_analyzed_second_intervention_output
    from AttributeIDList import sample_size_analyzed_second_control_output
    
    #############################################
    # Analyzed sample size for intervention group
    #############################################

    # highlighted text
    sample_size_analyzed_intervention = highlighted_text(sample_size_analyzed_intervention_output)
    sample_size_analyzed_intervention_df = pd.DataFrame(sample_size_analyzed_intervention)
    sample_size_analyzed_intervention_df = sample_size_analyzed_intervention_df.T
    sample_size_analyzed_intervention_df.columns = ["n_treat_ht"]

    # comments
    sample_size_analyzed_intervention_Comments = comments(sample_size_analyzed_intervention_output)
    sample_size_analyzed_intervention_Comments_df = pd.DataFrame(sample_size_analyzed_intervention_Comments)
    sample_size_analyzed_intervention_Comments_df = sample_size_analyzed_intervention_Comments_df.T
    sample_size_analyzed_intervention_Comments_df.columns = ["n_treat_info"]

    ############################################
    # Analyzed sample size for the control group
    ############################################

    # highlighted text
    sample_size_analyzed_control = highlighted_text(sample_size_analyzed_control_output)
    sample_size_analyzed_control_df = pd.DataFrame(sample_size_analyzed_control)
    sample_size_analyzed_control_df = sample_size_analyzed_control_df.T
    sample_size_analyzed_control_df.columns = ["n_cont_ht"]

    # comments
    sample_size__anazlyed_control_Comments = comments(sample_size_analyzed_control_output)
    sample_size__anazlyed_control_Comments_df = pd.DataFrame(sample_size__anazlyed_control_Comments)
    sample_size__anazlyed_control_Comments_df = sample_size__anazlyed_control_Comments_df.T
    sample_size__anazlyed_control_Comments_df.columns = ["n_cont_info"]

    ########################################################
    # Analyzed sample size for the second intervention group
    ########################################################

    # highlighted text
    sample_size_analyzed_second_intervention = highlighted_text(sample_size_analyzed_second_intervention_output)
    sample_size_analyzed_second_intervention_df = pd.DataFrame(sample_size_analyzed_second_intervention)
    sample_size_analyzed_second_intervention_df = sample_size_analyzed_second_intervention_df.T
    sample_size_analyzed_second_intervention_df.columns = ["n_treat2_ht"]

    # comments
    sample_size_analyzed_second_intervention_Comments = comments(sample_size_analyzed_second_intervention_output)
    sample_size_analyzed_second_intervention_Comments_df = pd.DataFrame(sample_size_analyzed_second_intervention_Comments)
    sample_size_analyzed_second_intervention_Comments_df = sample_size_analyzed_second_intervention_Comments_df.T
    sample_size_analyzed_second_intervention_Comments_df.columns = ["n_treat2_info"]

    #######################################################
    # Analyzed sample size for the second control group
    #######################################################

    # highlighted text
    sample_size_analyzed_second_control = highlighted_text(sample_size_analyzed_second_control_output)
    sample_size_analyzed_second_control_df = pd.DataFrame(sample_size_analyzed_second_control)
    sample_size_analyzed_second_control_df = sample_size_analyzed_second_control_df.T
    sample_size_analyzed_second_control_df.columns = ["n_cont2_ht"]

    # comments
    sample_size_analyzed_second_control_Comments = comments(sample_size_analyzed_second_control_output)
    sample_size_analyzed_second_control_Comments_df = pd.DataFrame(sample_size_analyzed_second_control_Comments)
    sample_size_analyzed_second_control_Comments_df = sample_size_analyzed_second_control_Comments_df.T
    sample_size_analyzed_second_control_Comments_df.columns = ["n_cont2_info"]

    # concatenate dataframes
    analyzed_sample_size_df = pd.concat([
        sample_size_analyzed_intervention_df, 
        sample_size_analyzed_intervention_Comments_df,
        sample_size_analyzed_control_df, 
        sample_size__anazlyed_control_Comments_df,
        sample_size_analyzed_second_intervention_df, 
        sample_size_analyzed_second_intervention_Comments_df,
        sample_size_analyzed_second_control_df, 
        sample_size_analyzed_second_control_Comments_df
    ], axis=1, sort=False)

    # remover problematic text
    analyzed_sample_size_df.replace('\r', ' ', regex=True, inplace=True)
    analyzed_sample_size_df.replace('\n', ' ', regex=True, inplace=True)

    # fill blanks with NA
    analyzed_sample_size_df.fillna("NA", inplace=True)

    return analyzed_sample_size_df

def samp_size_init():

    from AttributeIDList import sample_size_intervention_output
    from AttributeIDList import sample_size_control_output
    from AttributeIDList import sample_size_second_intervention_output
    from AttributeIDList import sample_size_third_intervention_output

    #############################################
    # Initial sample size for intervention group
    #############################################

    # get sample size intervention highlighted text
    sample_size_intervention_HT = highlighted_text(sample_size_intervention_output)
    sample_size_intervention_HT_df = pd.DataFrame(sample_size_intervention_HT)
    sample_size_intervention_HT_df = sample_size_intervention_HT_df.T
    sample_size_intervention_HT_df.columns = ["base_n_treat_ht"]

    # get sample size intervention 
    sample_size_intervention_Comments = comments(sample_size_intervention_output)
    sample_size_intervention_Comments_df = pd.DataFrame(sample_size_intervention_Comments)
    sample_size_intervention_Comments_df = sample_size_intervention_Comments_df.T
    sample_size_intervention_Comments_df.columns = ["base_n_treat_info"]

    ############################################
    # Initial sample size for the control group
    ############################################

    # get sample size control highlighted text
    sample_size_control_HT = highlighted_text(sample_size_control_output)
    sample_size_control_HT_df = pd.DataFrame(sample_size_control_HT)
    sample_size_control_HT_df = sample_size_control_HT_df.T
    sample_size_control_HT_df.columns = ["base_n_cont_ht"]

    # get sample size control comments
    sample_size_control_Comments = comments(sample_size_control_output)
    sample_size_control_Comments_df = pd.DataFrame(sample_size_control_Comments)
    sample_size_control_Comments_df = sample_size_control_Comments_df.T
    sample_size_control_Comments_df.columns = ["base_n_cont_info"]

    ########################################################
    # Initial sample size for the second intervention group
    ########################################################

    # get sample size 2nd intervention highlighted text
    sample_size_second_intervention_HT = highlighted_text(sample_size_second_intervention_output)
    sample_size_second_intervention_HT_df = pd.DataFrame(sample_size_second_intervention_HT)
    sample_size_second_intervention_HT_df = sample_size_second_intervention_HT_df.T
    sample_size_second_intervention_HT_df.columns = ["base_n_treat2_ht"]

    # get sample size 2nd intervention comments
    sample_size_second_intervention_Comments = comments(sample_size_second_intervention_output)
    sample_size_second_intervention_Comments_df = pd.DataFrame(sample_size_second_intervention_Comments)
    sample_size_second_intervention_Comments_df = sample_size_second_intervention_Comments_df.T
    sample_size_second_intervention_Comments_df.columns = ["base_n_treat2_info"]

    #######################################################
    # Initial sample size for the third intervention group
    #######################################################

    # get sample size 3rd intervention highlighted text
    sample_size_third_intervention_HT = highlighted_text(sample_size_third_intervention_output)
    sample_size_third_intervention_HT_df = pd.DataFrame(sample_size_third_intervention_HT)
    sample_size_third_intervention_HT_df = sample_size_third_intervention_HT_df.T
    sample_size_third_intervention_HT_df.columns = ["base_n_treat3_ht"]

    # get sample size 3rd intervention comments
    sample_size_third_intervention_Comments = comments(sample_size_third_intervention_output)
    sample_size_third_intervention_Comments_df = pd.DataFrame(sample_size_third_intervention_Comments)
    sample_size_third_intervention_Comments_df = sample_size_third_intervention_Comments_df.T
    sample_size_third_intervention_Comments_df.columns = ["base_n_treat3_info"]

    # concatenate dataframes
    initial_sample_size_df = pd.concat([
        sample_size_intervention_HT_df, 
        sample_size_intervention_Comments_df,
        sample_size_control_HT_df, 
        sample_size_control_Comments_df,
        sample_size_second_intervention_HT_df,
        sample_size_second_intervention_Comments_df,
        sample_size_third_intervention_HT_df, 
        sample_size_third_intervention_Comments_df
    ], axis=1, sort=False)

    # remove problematic text
    initial_sample_size_df.replace('\r', ' ', regex=True, inplace=True)
    initial_sample_size_df.replace('\n', ' ', regex=True, inplace=True)

    # fill blanks with NA
    initial_sample_size_df.fillna("NA", inplace=True)

    return initial_sample_size_df

def sample():
    from AttributeIDList import sample_output
    # get sample data
    sample = get_outcome_lvl2(sample_output)
    sample_df = pd.DataFrame(sample)

    # name each column (number depends on outcome number)
    sample_df.columns = [
        "out_samp_" +'{}'.format(column+1) for column in sample_df.columns]

    # get sample main check data
    sample_main_check = get_data(sample_output)
    sample_main_check_df = pd.DataFrame(sample_main_check)
    sample_main_check_df = sample_main_check_df.T
    sample_main_check_df.columns = ["main_check"]

    # concatenate dataframes
    all_variables = pd.concat([ 
        sample_df, 
        sample_main_check_df
    ], axis=1, sort=False)

    # fill blanks with NA
    all_variables.fillna("NA", inplace=True)

    return all_variables

def samp_size():
    from AttributeIDList import sample_size_output
    # get sample size comments
    sample_size_Comments = comments(sample_size_output)
    sample_size_Comments_df = pd.DataFrame(sample_size_Comments)
    sample_size_Comments_df = sample_size_Comments_df.T
    sample_size_Comments_df.columns = ["sample_analysed_info"]

    # get sample size highlighted text
    sample_size_HT = highlighted_text(sample_size_output)
    sample_size_HT_df = pd.DataFrame(sample_size_HT)
    sample_size_HT_df = sample_size_HT_df.T
    sample_size_HT_df.columns = ["sample_analysed_ht"]

    # concatenate dataframes
    sample_size_df = pd.concat([
        sample_size_Comments_df,
        sample_size_HT_df
    ], axis=1, sort=False)

    # remove problematic text
    sample_size_df.replace('\r', ' ', regex=True, inplace=True)
    sample_size_df.replace('\n', ' ', regex=True, inplace=True)

    # fill blanks with NA
    sample_size_df.fillna("NA", inplace=True)

    return sample_size_df

def samp_size_comm():
    from AttributeIDList import sample_size_output
    # get sample size comments
    sample_size_Comments = comments(sample_size_output)
    sample_size_Comments_df = pd.DataFrame(sample_size_Comments)
    sample_size_Comments_df = sample_size_Comments_df.T
    sample_size_Comments_df.columns = ["sample_analysed_info"]

    # remove problematic text
    sample_size_Comments_df.replace('\r', ' ', regex=True, inplace=True)
    sample_size_Comments_df.replace('\n', ' ', regex=True, inplace=True)

    # fill blanks with NA
    sample_size_Comments_df.fillna("NA", inplace=True)

    return sample_size_Comments_df

def ses_fm():

    from AttributeIDList import proportion_low_fsm_output
    from AttributeIDList import percentage_low_fsm_output
    from AttributeIDList import further_ses_fsm_info_output
    from AttributeIDList import no_ses_fsm_info_provided_output

    #######################################
    # PROPORTION OF LOW SES/FSM IN SAMPLE #
    #######################################

    # get low ses proportion comments
    low_ses_proportion_Comments = comments(proportion_low_fsm_output)
    low_ses_proportion_Comments_df = pd.DataFrame(low_ses_proportion_Comments)
    low_ses_proportion_Comments_df = low_ses_proportion_Comments_df.T
    low_ses_proportion_Comments_df.columns = ["fsm_prop_info"]

    # get low ses highlighted text
    low_ses_proportion_HT = highlighted_text(proportion_low_fsm_output)
    low_ses_proportion_HT_df = pd.DataFrame(low_ses_proportion_HT)
    low_ses_proportion_HT_df = low_ses_proportion_HT_df.T
    low_ses_proportion_HT_df.columns = ["fsm_prop_ht"]

    #######################################
    # PERCENTAGE OF LOW SES/FSM IN SAMPLE #
    #######################################

    # get low ses perc comments
    low_ses_percentage_Comments = comments(percentage_low_fsm_output)
    low_ses_percentage_Comments_df = pd.DataFrame(low_ses_percentage_Comments)
    low_ses_percentage_Comments_df = low_ses_percentage_Comments_df.T
    low_ses_percentage_Comments_df.columns = ["fsm_perc_info"]

    # get low ses perc highlighted text
    low_ses_percentage_HT = highlighted_text(percentage_low_fsm_output)
    low_ses_percentage_HT_df = pd.DataFrame(low_ses_percentage_HT)
    low_ses_percentage_HT_df = low_ses_percentage_HT_df.T
    low_ses_percentage_HT_df.columns = ["fsm_perc_ht"]

    #############################################
    # FURTHER LOW SES/FSM INFORMATION IN SAMPLE #
    #############################################

    # get further low ses info comments
    further_ses_info_Comments = comments(further_ses_fsm_info_output)
    further_ses_info_Comments_df = pd.DataFrame(further_ses_info_Comments)
    further_ses_info_Comments_df = further_ses_info_Comments_df.T
    further_ses_info_Comments_df.columns = ["fsm_info_info"]

    # get further low ses info highlighted text
    further_ses_fsm_info_HT = highlighted_text(further_ses_fsm_info_output)
    further_ses_fsm_info_HT_df = pd.DataFrame(further_ses_fsm_info_HT)
    further_ses_fsm_info_HT_df = further_ses_fsm_info_HT_df.T
    further_ses_fsm_info_HT_df.columns = ["fsm_info_ht"]

    #######################################
    # NO LOW SES/FSM INFORMATION PROVIDED #
    #######################################

    # get now low ses info data
    no_low_ses_fsm_info = get_data(no_ses_fsm_info_provided_output)
    no_low_ses_fsm_info_df = pd.DataFrame(no_low_ses_fsm_info)
    no_low_ses_fsm_info_df = no_low_ses_fsm_info_df.T
    no_low_ses_fsm_info_df.columns = ["fsm_na_raw"]

    # get no low ses info comments
    no_low_ses_fsm_info_comments = comments(no_ses_fsm_info_provided_output)
    no_low_ses_fsm_info_comments_df = pd.DataFrame(no_low_ses_fsm_info_comments)
    no_low_ses_fsm_info_comments_df = no_low_ses_fsm_info_comments_df.T
    no_low_ses_fsm_info_comments_df.columns = ["fsm_na_info"]


    # concatenate datafeames
    ses_fsm_df = pd.concat([
        low_ses_percentage_Comments_df, 
        low_ses_percentage_HT_df,
        further_ses_info_Comments_df, 
        further_ses_fsm_info_HT_df,
        no_low_ses_fsm_info_df, 
        no_low_ses_fsm_info_comments_df
    ], axis=1, sort=False)

    # remove problematic text
    clean_up(ses_fsm_df)

    # fill blanks with NA
    ses_fsm_df.fillna("NA", inplace=True)

    return ses_fsm_df

def low_ses_pc_comm():
    from AttributeIDList import percentage_low_fsm_output

    # get low ses perc info
    low_ses_percentage_ = comments(percentage_low_fsm_output)
    low_ses_percentage_df_info = pd.DataFrame(low_ses_percentage_)
    low_ses_percentage_df_info = low_ses_percentage_df_info.T
    low_ses_percentage_df_info.columns = ["fsm_perc_info"]

    # remove problematic text
    clean_up(low_ses_percentage_df_info)

    return low_ses_percentage_df_info

def ses_md():
    # get sesmd data
    sesmd = get_outcome_lvl1("SESMD")
    sesmd_df = pd.DataFrame(sesmd)

    # round data to 4 decimal places
    sesmd_df = sesmd_df.applymap(
        lambda x: round(x, 4) if isinstance(x, (int, float)) else x)

    # name each column (number depends on outcome number)
    sesmd_df.columns = [
        "se_"+'{}'.format(column+1) for column in sesmd_df.columns]

    # fill blanks with NA
    sesmd_df.fillna("NA", inplace=True)

    # replace problematic text
    sesmd_df = sesmd_df.replace(r'^\s*$', "NA", regex=True)

    return sesmd_df

def short_tit():
    # get eppiID data
    shorttitle = get_metadata("Title")
    shorttitle_df = pd.DataFrame(shorttitle)
    shorttitle_df.columns = ["title"]
    shorttitle_df.fillna("NA", inplace=True)

    return shorttitle_df

def smd():
    # get smd data
    smd = get_outcome_lvl1("SMD")
    smd_df = pd.DataFrame(smd)

    # round data to 4 decimal places
    smd_df = smd_df.applymap(lambda x: round(x, 4) if isinstance(x, (int, float)) else x)

    # name each column (number depends on outcome number)
    smd_df.columns = ["smd_"+'{}'.format(column+1) for column in smd_df.columns]

    # fill blanks with NA
    smd_df.fillna("NA", inplace=True)

    # replace problematic text
    smd_df = smd_df.replace(r'^\s*$', "NA", regex=True)

    return smd_df

def source():
    from AttributeIDList import source_output
    from AttributeIDList import source_EEF_Report_options
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
    from AttributeIDList import location_info
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

def study_design():
    from AttributeIDList import study_design_output
    # get study design data
    studydesign = get_data(study_design_output)
    studydesign_df = pd.DataFrame(studydesign)
    studydesign_df = studydesign_df.T
    studydesign_df.columns = ["int_desig_raw"]

    # get study design highlighted text
    studydesign_HT = highlighted_text(study_design_output)
    studydesign_HT_df = pd.DataFrame(studydesign_HT)
    studydesign_HT_df = studydesign_HT_df.T
    studydesign_HT_df.columns = ["int_design_ht"]

    # get study design user comments
    studydesign_Comments = comments(study_design_output)
    studydesign_Comments_df = pd.DataFrame(studydesign_Comments)
    studydesign_Comments_df = studydesign_Comments_df.T
    studydesign_Comments_df.columns = ["int_design_info"]

    # concatenate data frames
    study_design_df = pd.concat([
        studydesign_df, 
        studydesign_HT_df, 
        studydesign_Comments_df
    ], axis=1, sort=False)

    # fill blanks with NA
    study_design_df.fillna("NA", inplace=True)

    return study_design_df

def study_realism():
    from AttributeIDList import study_realism_output
    # get study realism data
    studyrealism = get_data(study_realism_output)
    studyrealism_df = pd.DataFrame(studyrealism)
    studyrealism_df = studyrealism_df.T
    studyrealism_df.columns = ["eco_valid_raw"]

    # get study realism highlighted text
    studyrealism_HT = highlighted_text(study_realism_output)
    studyrealism_HT_df = pd.DataFrame(studyrealism_HT)
    studyrealism_HT_df = studyrealism_HT_df.T
    studyrealism_HT_df.columns = ["eco_valid_ht"]

    # get study realism user comments
    studyrealism_Comments = comments(study_realism_output)
    studyrealism_Comments_df = pd.DataFrame(studyrealism_Comments)
    studyrealism_Comments_df = studyrealism_Comments_df.T
    studyrealism_Comments_df.columns = ["eco_valid_info"]

    # concatenate data frames
    study_realism_df = pd.concat([
        studyrealism_df, 
        studyrealism_HT_df, 
        studyrealism_Comments_df
    ], axis=1, sort=False)

    # fill blanks with NA
    study_realism_df.fillna("NA", inplace=True)

    # remove square brackets [not for multiple input variables]
    study_realism_df['eco_valid_raw'] = study_realism_df['eco_valid_raw'].str[0]
    return study_realism_df

def test_type():
    from AttributeIDList import test_type_main, test_type_output
    # get test type main extraction data
    test_type_main = get_data(test_type_main)
    test_type_main_df = pd.DataFrame(test_type_main)
    test_type_main_df = test_type_main_df.T
    test_type_main_df.columns = ["test_type_raw"]

    test_type_main_df["test_type_standardised_test"] = test_type_main_df["test_type_raw"].map(
        set(['Standardised test']).issubset).astype(int)
    test_type_main_df["test_type_researcher_developed_test"] = test_type_main_df["test_type_raw"].map(
        set(['Researcher developed test']).issubset).astype(int)
    test_type_main_df["test_type_school_developed_test"] = test_type_main_df["test_type_raw"].map(
        set(['School-developed test']).issubset).astype(int)
    test_type_main_df["test_type_normal_test_or_examination"] = test_type_main_df["test_type_raw"].map(
        set(['National test or examination']).issubset).astype(int)
    test_type_main_df["test_type_international_tests"] = test_type_main_df["test_type_raw"].map(
        set(['International tests']).issubset).astype(int)

    # get test type outcome data
    testtype_outcome = get_outcome_lvl2(test_type_output)
    testtype_outcome_df = pd.DataFrame(testtype_outcome)

    # name each column (number depends on outcome number)
    testtype_outcome_df.columns = [
        "out_test_type_raw_"+'{}'.format(column+1) for column in testtype_outcome_df.columns]

    # concatenate data frames
    """ testtype_df = pd.concat([test_type_main_df, testtype_outcome_df], axis=1, sort=False) """

    # fill blanks with NA
    testtype_outcome_df.fillna("NA", inplace=True)

    return testtype_outcome_df

def title():
    # get eppiID data
    title = get_metadata("Title")
    title_df = pd.DataFrame(title)
    title_df.columns = ["title"]
    title_df.fillna("NA", inplace=True)

    return title_df

def toolkit_strand():
    from AttributeIDList import toolkit_strand_codes
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

def treat_group():
    from AttributeIDList import treatment_group
    # get treatment group data
    treatmentgroup = get_data(treatment_group)
    treatmentgroup_df = pd.DataFrame(treatmentgroup)
    treatmentgroup_df = treatmentgroup_df.T
    treatmentgroup_df.columns = ["treat_group_raw"]

    # get treatment group highlighted text
    treatmentgroup_HT = highlighted_text(treatment_group)
    treatmentgroup_HT_df = pd.DataFrame(treatmentgroup_HT)
    treatmentgroup_HT_df = treatmentgroup_HT_df.T
    treatmentgroup_HT_df.columns = ["treat_group_ht"]

    # get treatment group user comments
    treatmentgroup_Comments = comments(treatment_group)
    treatmentgroup_Comments_df = pd.DataFrame(treatmentgroup_Comments)
    treatmentgroup_Comments_df = treatmentgroup_Comments_df.T
    treatmentgroup_Comments_df.columns = ["treat_group_info"]

    # concatenate data frames
    treatment_group_df = pd.concat(
        [treatmentgroup_df, treatmentgroup_HT_df, treatmentgroup_Comments_df], axis=1, sort=False)

    # fill blanks with NA
    treatment_group_df.fillna("NA", inplace=True)

    return treatment_group_df

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
    from AttributeIDList import study_loc
    from AttributeIDList import study_loc_type
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

def number_of_schools():

    from AttributeIDList import number_of_schools_intervention_output
    from AttributeIDList import number_of_schools_control_output
    from AttributeIDList import number_of_schools_total_output
    from AttributeIDList import number_of_schools_not_provided_output

    # get number of school intervention comments data
    number_of_schools_intervention_Comments = comments(number_of_schools_intervention_output)
    number_of_schools_intervention_Comments_df = pd.DataFrame(number_of_schools_intervention_Comments)
    number_of_schools_intervention_Comments_df = number_of_schools_intervention_Comments_df.T
    number_of_schools_intervention_Comments_df.columns = ["school_treat_info"]

    # get number of school intervention highlighted text data
    number_of_schools_intervention_HT = highlighted_text(number_of_schools_intervention_output)
    number_of_schools_intervention_HT_df = pd.DataFrame(number_of_schools_intervention_HT)
    number_of_schools_intervention_HT_df = number_of_schools_intervention_HT_df.T
    number_of_schools_intervention_HT_df.columns = ["school_treat_ht"]

    #############################
    # NUMBER OF SCHOOLS CONTROL #
    #############################

    # get number of school control comments data
    number_of_schools_control_Comments = comments(number_of_schools_control_output)
    number_of_schools_control_Comments_df = pd.DataFrame(number_of_schools_control_Comments)
    number_of_schools_control_Comments_df = number_of_schools_control_Comments_df.T
    number_of_schools_control_Comments_df.columns = ["school_cont_info"]

    # get number of school control highlighted text data
    number_of_schools_control_HT = highlighted_text(number_of_schools_control_output)
    number_of_schools_control_HT_df = pd.DataFrame(number_of_schools_control_HT)
    number_of_schools_control_HT_df = number_of_schools_control_HT_df.T
    number_of_schools_control_HT_df.columns = ["school_cont_ht"]

    ###########################
    # NUMBER OF SCHOOLS TOTAL #
    ###########################

    # get total nnumber of schools comments data
    number_of_schools_total_Comments = comments(number_of_schools_total_output)
    number_of_schools_total_Comments_df = pd.DataFrame(number_of_schools_total_Comments)
    number_of_schools_total_Comments_df = number_of_schools_total_Comments_df.T
    number_of_schools_total_Comments_df.columns = ["school_total_info"]

    # get total number of schools highlighted text data
    number_of_schools_total_HT = highlighted_text(number_of_schools_total_output)
    number_of_schools_total_HT_df = pd.DataFrame(number_of_schools_total_HT)
    number_of_schools_total_HT_df = number_of_schools_total_HT_df.T
    number_of_schools_total_HT_df.columns = ["school_total_ht"]

    #########################################################
    # NUMBER OF SCHOOLS NOT PROVIDED/UNCLEAR/NOT APPLICABLE #
    #########################################################

    # get number of schools not provided data
    number_of_schools_np = get_data(number_of_schools_not_provided_output)
    number_of_schools_np_df = pd.DataFrame(number_of_schools_np)
    number_of_schools_np_df = number_of_schools_np_df.T
    number_of_schools_np_df.columns = ["school_na_raw"]

    # get number of schools not provided comments data
    number_of_schools_np_Comments = comments(number_of_schools_not_provided_output)
    number_of_schools_np_Comments_df = pd.DataFrame(number_of_schools_np_Comments)
    number_of_schools_np_Comments_df = number_of_schools_np_Comments_df.T
    number_of_schools_np_Comments_df.columns = ["school_na_info"]

    # get number of schools not provided highlighted text data
    number_of_schools_np_HT = highlighted_text(number_of_schools_not_provided_output)
    number_of_schools_np_HT_df = pd.DataFrame(number_of_schools_np_HT)
    number_of_schools_np_HT_df = number_of_schools_np_HT_df.T
    number_of_schools_np_HT_df.columns = ["school_na_ht"]

    # concatenate dataframes
    number_of_schools_df = pd.concat([
        number_of_schools_intervention_Comments_df, 
        number_of_schools_intervention_HT_df,
        number_of_schools_control_Comments_df, 
        number_of_schools_control_HT_df,
        number_of_schools_total_Comments_df, 
        number_of_schools_total_HT_df,
        number_of_schools_np_df, 
        number_of_schools_np_Comments_df, 
        number_of_schools_np_HT_df
    ], axis=1, sort=False)

    # remove problematic text
    number_of_schools_df.replace('\r', ' ', regex=True, inplace=True)
    number_of_schools_df.replace('\n', ' ', regex=True, inplace=True)

    # fill blanks with NA
    number_of_schools_df.fillna("NA", inplace=True)

    return number_of_schools_df

def number_of_schools_total_comm():

    from AttributeIDList import number_of_schools_total_output

    ###########################
    # NUMBER OF SCHOOLS TOTAL #
    ###########################

    # get total nnumber of schools comments data
    number_of_schools_total_Comments = comments(number_of_schools_total_output)
    number_of_schools_total_Comments_df = pd.DataFrame(number_of_schools_total_Comments)
    number_of_schools_total_Comments_df = number_of_schools_total_Comments_df.T
    number_of_schools_total_Comments_df.columns = ["school_total_info"]

    # remove problematic text
    number_of_schools_total_Comments_df.replace('\r', ' ', regex=True, inplace=True)
    number_of_schools_total_Comments_df.replace('\n', ' ', regex=True, inplace=True)

    # fill blanks with NA
    number_of_schools_total_Comments_df.fillna("NA", inplace=True)

    return number_of_schools_total_Comments_df

def number_of_classes():
    """
    
    """
    from AttributeIDList import num_of_class_int_output
    from AttributeIDList import num_of_class_cont_output
    from AttributeIDList import num_of_class_tot_output
    from AttributeIDList import numb_of_class_np_output

    ##################################
    # NUMBER OF CLASSES INTERVENTION #
    ##################################

    # get number of classes intervention comments data
    num_of_class_int_Comments_df = process_info(num_of_class_int_output, "class_treat_info")
    # get number of classes intervention highlighted text data
    num_of_class_int_ht_df = process_ht(num_of_class_int_output, "class_treat_ht")

    #############################
    # NUMBER OF CLASSES CONTROL #
    #############################

    # get number of classes control comments data
    num_of_class_cont_comments_df = process_info(num_of_class_cont_output, "class_cont_info")
    # get number of classes control highlighted text data
    num_of_class_cont_ht_df = process_ht(num_of_class_cont_output, "class_cont_ht")

    ###########################
    # NUMBER OF CLASSES TOTAL #
    ###########################

    # get number of classes total comments data
    num_of_class_total_comments_df = process_info(num_of_class_tot_output, "class_total_info")
    # get number of classes total highlighted text data
    num_of_class_total_ht_df = process_ht(num_of_class_tot_output, "class_total_ht")

    #########################################################
    # NUMBER OF CLASSES NOT PROVIDED/UNCLEAR/NOT APPLICABLE #
    #########################################################

    # Get number of classes not provided data
    num_of_class_np_df = process_data(numb_of_class_np_output, "class_na_raw")
    # Get number of classes not provided comments data
    num_of_class_np_comments_df = process_info(numb_of_class_np_output, "class_na_info")
    # Get number of classes not provided highlighted text data
    num_of_class_np_ht_df = process_ht(numb_of_class_np_output, "class_na_ht")

    # Concatenate dataframes
    dataframes = [
        num_of_class_int_Comments_df,
        num_of_class_int_ht_df,
        num_of_class_cont_comments_df,
        num_of_class_cont_ht_df,
        num_of_class_total_comments_df,
        num_of_class_total_ht_df,
        num_of_class_np_df,
        num_of_class_np_comments_df,
        num_of_class_np_ht_df
    ]

    num_of_class_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    num_of_class_df.replace('\r', ' ', regex=True, inplace=True)
    num_of_class_df.replace('\n', ' ', regex=True, inplace=True)
    num_of_class_df.fillna("NA", inplace=True)

    return num_of_class_df

def number_of_classes_total_comm():
    """
    """
    from AttributeIDList import num_of_class_tot_output

    # Get number of classes total comments data
    num_of_class_total_comments_df = process_info(num_of_class_tot_output, "class_total_info")

    # Clean up data frame
    num_of_class_total_comments_df.replace('\r', ' ', regex=True, inplace=True)
    num_of_class_total_comments_df.replace('\n', ' ', regex=True, inplace=True)
    num_of_class_total_comments_df.fillna("NA", inplace=True)

    return num_of_class_total_comments_df


def other_outcomes():
    """
    """
    from AttributeIDList import other_out_output
    from AttributeIDList import addit_out_output
    from AttributeIDList import other_part_output

    #################
    # Other outcomes
    #################

    # get other outcomes data
    other_out_df = process_data(other_out_output, "out_other_raw")
    # Get other outcomes highlighted text
    other_out_HT_df = process_ht(other_out_output, "out_other_ht")
    # Get other outcomes comments
    other_out_info_df = process_info(other_out_output, "out_other_info")

    ######################
    # Additional outcomes
    ######################

    # Get additional outcomes data
    addit_out_df = process_data(addit_out_output, "out_info_raw")
    # Get additional outcomes highlighted text
    addit_out_ht_df = process_ht(addit_out_output, "out_info_ht")
    # Get additional outcomes comments
    addit_out_info_df = process_info(addit_out_output, "out_info_info")

    #####################
    # Other participants
    #####################

    # Get other participants highlighted text
    other_part_ht_df = process_ht(other_part_output, "part_other_ht")
    # Get other participants comments
    other_part_info_df = process_info(other_part_output, "part_other_info")

    # Concatenate data frames
    dataframes = [
        other_out_df,
        other_out_HT_df, 
        other_out_info_df,
        addit_out_df,
        addit_out_ht_df,
        addit_out_info_df,
        other_part_ht_df,
        other_part_info_df
    ]

    other_outcomes_df = pd.concat(dataframes, axis=1, sort=False)

    # Clean up data frame
    other_outcomes_df.fillna("NA", inplace=True)

    return other_outcomes_df

def group1_n():
    # get group 1 N data
    group1n = get_outcome_lvl1("Data1")
    group1N_df = pd.DataFrame(group1n)

    # name each column (number depends on outcome number)
    group1N_df.columns = [
        "out_g1_n_"+'{}'.format(column+1) for column in group1N_df.columns
    ]

    # fill blanks with NA  
    group1N_df.fillna("NA", inplace=True)
    group1N_df = group1N_df.replace(r'^\s*$', "NA", regex=True)

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
    for col in group1N_df.columns:
        group1N_df.loc[mask, col] = "NA"

    return group1N_df

def group2_n():
    # get group 1 N data
    group2n = get_outcome_lvl1("Data2")
    group2N_df = pd.DataFrame(group2n)

    # name each column (number depends on outcome number)
    group2N_df.columns = [
        "out_g2_n_"+'{}'.format(column+1) for column in group2N_df.columns
    ]

    # fill blanks with NA  
    group2N_df.fillna("NA", inplace=True)

    # remove problematic text
    group2N_df = group2N_df.replace(r'^\s*$', "NA", regex=True)

    # get outcometypeId data (to check)
    outcomeid = get_outcome_lvl1("OutcomeTypeId")
    outcometypeid_df = pd.DataFrame(outcomeid)

    # name each column (number depends on outcome number)
    outcometypeid_df.columns = [
        "outcometype_df_"+'{}'.format(column+1) for column in outcometypeid_df.columns
    ]

    mask = pd.DataFrame(outcometypeid_df["outcometype_df_1"] == 0)
    mask.columns = ["mask"]
    mask = mask.iloc[:, 0]

    # replace all 0 instances (null data) with "NA"
    for col in group2N_df.columns:
        group2N_df.loc[mask, col] = "NA"

    return group2N_df

def group1_mean():
    # get group1 mean data
    group1mean = get_outcome_lvl1("Data3")
    group1mean_df = pd.DataFrame(group1mean)

    # name each column (number depends on outcome number)
    group1mean_df.columns = [
        "out_g1_mean_"+'{}'.format(column+1) for column in group1mean_df.columns
    ]

    # fill blanks with NA   
    group1mean_df.fillna("NA", inplace=True)

    # remove problematic text
    group1mean_df = group1mean_df.replace(r'^\s*$', "NA", regex=True)

    # get outcometypeId data (to check)
    outcometypeid = get_outcome_lvl1("OutcomeTypeId")
    outcometypeid_df = pd.DataFrame(outcometypeid)

    # name each column (number depends on outcome number)
    outcometypeid_df.columns = [
        "outcometype_df_"+'{}'.format(column+1) for column in outcometypeid_df.columns
    ]

    mask = pd.DataFrame(outcometypeid_df["outcometype_df_1"] == 0)
    mask.columns=["mask"]
    mask = mask.iloc[:, 0]

    # replace all 0 instances (null data) with "NA"
    for col in group1mean_df.columns:
        group1mean_df.loc[mask, col] = "NA"

    return group1mean_df

def group2_mean():
    # get group2 mean data
    group2mean = get_outcome_lvl1("Data4")
    group2mean_df = pd.DataFrame(group2mean)

    # name each column (number depends on outcome number)
    group2mean_df.columns = [
        "out_g2_mean_"+'{}'.format(column+1) for column in group2mean_df.columns
    ]

    # fill blanks with NA
    group2mean_df.fillna("NA", inplace=True)

    # remove problematic text
    group2mean_df = group2mean_df.replace(r'^\s*$', "NA", regex=True)

    # get outcometypeId data 
    outcomeid = get_outcome_lvl1("OutcomeTypeId")
    outcometypeid_df = pd.DataFrame(outcomeid)

    # name each column (number depends on outcome number)
    outcometypeid_df.columns = [
        "outcometype_df_"+'{}'.format(column+1) for column in outcometypeid_df.columns
    ]

    mask = pd.DataFrame(outcometypeid_df["outcometype_df_1"] == 0)
    mask.columns=["mask"]
    mask = mask.iloc[:, 0]

    # replace all 0 instances (null data) with "NA"
    for col in group2mean_df.columns:
        group2mean_df.loc[mask, col] = "NA"

    return group2mean_df

def group1_sd():
    # get group1 sd data
    group1sd = get_outcome_lvl1("Data5")
    group1sd_df = pd.DataFrame(group1sd)

    # name each column (number depends on outcome number)
    group1sd_df.columns = [
        "out_g1_sd_"+'{}'.format(column+1) for column in group1sd_df.columns
    ]

    # fill blanks with NA  
    group1sd_df.fillna("NA", inplace=True)

    # remove problematic text
    group1sd_df = group1sd_df.replace(r'^\s*$', "NA", regex=True)

    # get outcometypeId data (to check)
    getoucomeid = get_outcome_lvl1("OutcomeTypeId")
    outcometypeid_df = pd.DataFrame(getoucomeid)

    # name each column (number depends on outcome number)
    outcometypeid_df.columns = [
        "outcometype_df_"+'{}'.format(column+1) for column in outcometypeid_df.columns
    ]

    mask = pd.DataFrame(outcometypeid_df["outcometype_df_1"] == 0)
    mask.columns=["mask"]
    mask = mask.iloc[:, 0]

    # replace all 0 instances (null data) with "NA"
    for col in group1sd_df.columns:
        group1sd_df.loc[mask, col] = "NA"

    return group1sd_df

def group2_sd():
    # get group2sd data
    groupd2sd = get_outcome_lvl1("Data6")
    group2sd_df = pd.DataFrame(groupd2sd)

    # name each column (number depends on outcome number)
    group2sd_df.columns = [
        "out_g2_sd_"+'{}'.format(column+1) for column in group2sd_df.columns
    ]

    # fill blanks with NA  
    group2sd_df.fillna("NA", inplace=True)

    # remove problematic text
    group2sd_df = group2sd_df.replace(r'^\s*$', "NA", regex=True)

    # get outcometypeId data (to check)
    outcomeid = get_outcome_lvl1("OutcomeTypeId")
    outcometypeid_df = pd.DataFrame(outcomeid)

    # name each column (number depends on outcome number)
    outcometypeid_df.columns = [
        "outcometype_df_"+'{}'.format(column+1) for column in outcometypeid_df.columns
    ]

    mask = pd.DataFrame(outcometypeid_df["outcometype_df_1"] == 0)
    mask.columns=["mask"]
    mask = mask.iloc[:, 0]

    # replace all 0 instances (null data) with "NA"
    for col in group2sd_df.columns:
        group2sd_df.loc[mask, col] = "NA"

    return group2sd_df