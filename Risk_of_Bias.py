#!/usr/bin/env python3
import os
import sys

from ind_var_Gen.eppi_ID import eppiid_df
from ind_var_Gen.Author import author_df
from ind_var_Gen.Date import year_df
from ind_var_Gen.AdminStrand import admin_strand_df

from ind_var_Gen.PublicationType import publicationtype_df
from ind_var_Gen.ParticipantAssignment import participant_assignment_df
from ind_var_Gen.Randomisation import randomisation_df
from ind_var_Gen.StudyRealism import study_realism_df
from ind_var_Gen.NumberofSchools import number_of_schools_intervention_Comments_df
from ind_var_Gen.NumberofClasses import number_of_classes_total_Comments_df
from ind_var_Gen.InterventionDelivery import intervention_delivery_df
from ind_var_Gen.InterventionEvaluation import InterventionEvaluation_df
from ind_var_Gen.Comparability import comparability_df
from ind_var_Gen.SampleSize import sample_size_Comments_df
from ind_var_Gen.Attrition import overall_percent_attrition_Comments_df
from ind_var_Gen.Clustering import clustering_df

from DataFrame5 import toolkit_test_type
from DataFrame5 import toolkit_es_type

from DataFrame6 import df_all
import pandas as pd
import numpy as np

data_files = sys.argv[1]


###############
# ADMIN STRAND
###############

del admin_strand_df['strand_info']

##############
# DATE (Year)
##############

year_df["pub_year"] = year_df["pub_year"].apply(pd.to_numeric, errors='coerce').fillna(0)

def pub_year_risk(row):
    if row["pub_year"] < 1980:
        return 'High Risk'
    if row["pub_year"] > 1979 and row["pub_year"] < 2000:
        return 'Medium Risk'
    if row["pub_year"] > 1999:
        return 'Low Risk'
    return 'NA'


year_df["pub_year_raw_risk"] = year_df.apply(
    lambda row: pub_year_risk(row), axis=1)

conditions = [
    (year_df["pub_year_raw_risk"] == 'High Risk'),
    (year_df["pub_year_raw_risk"] == 'Medium Risk'),
    (year_df["pub_year_raw_risk"] == 'Low Risk'),
]
choices = [1, 2, 3]

year_df['pub_year_risk_value'] = np.select(conditions, choices, default="NA")

#######################
# ATTRITION PERCENTAGE
#######################

# imported and included in output dataframe (at end of file)
# no conditional columns necessary

overall_percent_attrition_Comments_df.replace('%', '', regex=True, inplace=True)

overall_percent_attrition_Comments_df["attri_perc_info"] = overall_percent_attrition_Comments_df["attri_perc_info"].apply(
    pd.to_numeric, errors='coerce').fillna(0)


def perc_attrit_risk(row):
    if row["attri_perc_info"] < 10:
        return 'Low Risk'
    if row["attri_perc_info"] > 10 and row["attri_perc_info"] < 20:
        return 'Medium Risk'
    if row["attri_perc_info"] > 19:
        return 'High Risk'
    return 'NA'


overall_percent_attrition_Comments_df["attri_perc_info_raw_risk"] = overall_percent_attrition_Comments_df.apply(
    lambda row: perc_attrit_risk(row), axis=1)

conditions = [
    (overall_percent_attrition_Comments_df["attri_perc_info_raw_risk"] == 'High Risk'),
    (overall_percent_attrition_Comments_df["attri_perc_info_raw_risk"] == 'Medium Risk'),
    (overall_percent_attrition_Comments_df["attri_perc_info_raw_risk"] == 'Low Risk'),
]
choices = [1, 2, 3]

overall_percent_attrition_Comments_df['attri_perc_info_risk_value'] = np.select(conditions, choices, default="NA")


######################
# CLUSTER IN ANALYSIS
######################

del clustering_df["clust_anal_ht"]
del clustering_df["clust_anal_info"]

# Medium/High risk for Yes/No – the difference is usually trivial(slightly wider confidence intervals), but reflects a less sophisticated analysis. """

clustering_df["clust_anal_raw"] = clustering_df["clust_anal_raw"].apply(
    lambda x: ",".join(x) if isinstance(x, list) else x)

conditions = [
    (clustering_df['clust_anal_raw'] == "Yes"),
    (clustering_df['clust_anal_raw'] == "No"),
]

# GET RISK LEVELS PER PUBLICATION TYPE
choices = ['Medium Risk', 'High Risk', ]

clustering_df["clust_anal_raw_risk"] = np.select(conditions, choices, default="NA")

conditions = [
    (clustering_df["clust_anal_raw_risk"] == 'Medium Risk'),
    (clustering_df["clust_anal_raw_risk"] == 'High Risk'),
]

choices = [2,1]

clustering_df["clust_anal_risk_value"] = np.select(
    conditions, choices, default="NA")

############################
# OUTCOME: EFFECT SIZE TYPE
############################

toolkit_es_type = pd.DataFrame(toolkit_es_type)

if len(toolkit_es_type.columns) > 1:
    del toolkit_es_type[1]

toolkit_es_type.columns = ["out_es_type"]
toolkit_es_type["out_es_type"] = toolkit_es_type["out_es_type"].apply(lambda x: ",".join(x) if isinstance(x, list) else x)

conditions = [
    (toolkit_es_type["out_es_type"] == "Post-test unadjusted (select one from this group)"),
    (toolkit_es_type["out_es_type"] == "Post-test adjusted for baseline attainment"),
    (toolkit_es_type["out_es_type"] == "Post-test adjusted for baseline attainment AND clustering"),
    (toolkit_es_type["out_es_type"] == "Pre-post gain"),
]

choices = ['High Risk', 'Low Risk', 'Low Risk', 'Medium Risk']

toolkit_es_type["out_es_type_raw_risk"] = np.select(conditions, choices, default="NA")

conditions = [
    (toolkit_es_type["out_es_type_raw_risk"] == 'High Risk'),
    (toolkit_es_type["out_es_type_raw_risk"] == 'Medium Risk'),
    (toolkit_es_type["out_es_type_raw_risk"] == 'Low Risk'),
]

choices = [1, 2, 3]

toolkit_es_type["out_es_type_risk_value"] = np.select(conditions, choices, default="NA")

#####################
# OUTCOME: TEST TYPE
#####################

toolkit_test_type = pd.DataFrame(toolkit_test_type)


if len(toolkit_test_type.columns) >1:
    del toolkit_test_type[1]

toolkit_test_type.columns = ["out_test_type_raw"]
toolkit_test_type["out_test_type_raw"] = toolkit_test_type["out_test_type_raw"].apply(
    lambda x: ",".join(x) if isinstance(x, list) else x)

conditions = [
    (toolkit_test_type["out_test_type_raw"] == "Test type: Standardised test "),
    (toolkit_test_type["out_test_type_raw"] == "Test type: Researcher developed test"),
    (toolkit_test_type["out_test_type_raw"] == "Test type: National test"),
    (toolkit_test_type["out_test_type_raw"] == "Test type: School-developed test"),
    (toolkit_test_type["out_test_type_raw"] == "Test type: International tests"),
]

# GET RISK LEVELS PER PUBLICATION TYPE
choices = ['Low Risk', 'High Risk', 'Low Risk', 'Medium Risk', 'Low Risk']

toolkit_test_type["out_test_type_raw_risk"] = np.select(conditions, choices, default="NA")

conditions = [
    (toolkit_test_type["out_test_type_raw_risk"] == 'High Risk'),
    (toolkit_test_type["out_test_type_raw_risk"] == 'Medium Risk'),
    (toolkit_test_type["out_test_type_raw_risk"] == 'Low Risk'),
]

choices = [1, 2, 3]

toolkit_test_type["out_test_type_raw_risk_value"] = np.select(
    conditions, choices, default="NA")

###############
# SAMPLE SIZE
###############

sample_size_Comments_df["sample_analysed_info"] = sample_size_Comments_df["sample_analysed_info"].apply(
    pd.to_numeric, errors='coerce').fillna(0)

def sample_size_risk(row):
    if row["sample_analysed_info"] <= 30: return 'High Risk'
    if row["sample_analysed_info"] > 30 and row["sample_analysed_info"] < 100: return 'Medium Risk'
    if row["sample_analysed_info"] > 100: return 'Low Risk'
    return 'NA'

sample_size_Comments_df["sample_size_risk"] = sample_size_Comments_df.apply(lambda row: sample_size_risk(row), axis=1)

conditions = [
    (sample_size_Comments_df["sample_size_risk"] == 'High Risk'),
    (sample_size_Comments_df["sample_size_risk"] == 'Medium Risk'),
    (sample_size_Comments_df["sample_size_risk"] == 'Low Risk'),
]
choices = [1, 2, 3]

sample_size_Comments_df['sample_size_risk_value'] = np.select(
    conditions, choices, default="NA")

###################
# PUBLICATION TYPE
###################

publicationtype_df["pub_type_raw"] = publicationtype_df["pub_type_raw"].apply(lambda x: ",".join(x) if isinstance(x, list) else x)

conditions = [
    (publicationtype_df['pub_type_raw'] == "Journal article"),
    (publicationtype_df['pub_type_raw'] == "Dissertation or thesis"),
    (publicationtype_df['pub_type_raw'] == "Technical report"),
    (publicationtype_df['pub_type_raw'] == "Book or book chapter"),
    (publicationtype_df['pub_type_raw'] == "Conference paper"),
    (publicationtype_df['pub_type_raw'] == "Other (Please specify)"),
]

# GET RISK LEVELS PER PUBLICATION TYPE
choices = ['Low Risk', 'Low Risk', 'Low Risk', 'Medium Risk', 'Medium Risk', 'Medium Risk']

publicationtype_df["pub_type_risk"] = np.select(conditions, choices, default="NA")

conditions = [
    (publicationtype_df["pub_type_risk"] == 'High Risk'),
    (publicationtype_df["pub_type_risk"] == 'Medium Risk'),
    (publicationtype_df["pub_type_risk"] == 'Low Risk'),
]

choices = [1, 2, 3]

publicationtype_df["pub_type_risk_value"] = np.select(conditions, choices, default="NA")

#########################
# PARTICIPANT ASSIGNMENT
#########################

del participant_assignment_df["part_assig_ht"]
del participant_assignment_df["part_assig_info"]

conditions = [
    (participant_assignment_df['part_assig_raw'] == 'Random (please specify)'),
    (participant_assignment_df['part_assig_raw'] == 'Non-random, but matched'),
    (participant_assignment_df['part_assig_raw'] == 'Non-random, not matched prior to treatment'),
    (participant_assignment_df['part_assig_raw'] == 'Unclear'),
    (participant_assignment_df['part_assig_raw'] == 'Not assigned - naturally occurring sample'),
    (participant_assignment_df['part_assig_raw'] == 'Retrospective Quasi Experimental Design (QED)'),
    (participant_assignment_df['part_assig_raw'] == 'Regression discontinuity'),
]
choices = ['Low Risk', 'Medium Risk', 'Medium Risk', 'Medium Risk', 'Medium Risk', 'Medium Risk', 'Medium Risk']

participant_assignment_df['part_assig_risk'] = np.select(conditions, choices, default="NA")

conditions = [
    (participant_assignment_df['part_assig_risk'] == 'High Risk'),
    (participant_assignment_df['part_assig_risk'] == 'Medium Risk'),
    (participant_assignment_df['part_assig_risk'] == 'Low Risk'),
]
choices = [1, 2, 3]

participant_assignment_df['part_assig_risk_value'] = np.select(conditions, choices, default="NA")

################
# RANDOMISATION
################

del randomisation_df['rand_ht']
del randomisation_df['rand_info']

conditions = [
    (randomisation_df['rand_raw'] == 'Yes'),
    (randomisation_df['rand_raw'] == 'Not applicable'),
    (randomisation_df['rand_raw'] == 'No/Unclear'),
]
choices = ['Low Risk', 'Medium Risk', 'Medium Risk']

randomisation_df['rand_risk'] = np.select(conditions, choices, default="NA")

conditions = [
    (randomisation_df['rand_risk'] == 'Low Risk'),
    (randomisation_df['rand_risk'] == 'Medium Risk'),
    (randomisation_df['rand_risk'] == 'Medium Risk'),
]
choices = [3, 2, 2]

randomisation_df['rand_risk_value'] = np.select(conditions, choices, default="NA")

################
# STUDY REALISM
################

del study_realism_df['eco_valid_ht']
del study_realism_df['eco_valid_info']

conditions = [
    (study_realism_df['eco_valid_raw'] == 'High ecological validity'),
    (study_realism_df['eco_valid_raw'] == 'Low ecological validity'),
    (study_realism_df['eco_valid_raw'] == 'Unclear'),
]
choices = ['Low Risk', 'High Risk', 'High Risk']

study_realism_df['eco_valid_risk'] = np.select(conditions, choices, default="NA")

conditions = [
    (study_realism_df['eco_valid_risk'] == 'Low Risk'),
    (study_realism_df['eco_valid_risk'] == 'High Risk'),
]
choices = [3, 1]

study_realism_df['eco_valid_risk_value'] = np.select(conditions, choices, default="NA")

#################################
# NUMBER OF SCHOOLS INTERVENTION
#################################

number_of_schools_intervention_Comments_df["school_treat_info_new"] = number_of_schools_intervention_Comments_df["school_treat_info"].apply(
    pd.to_numeric, errors='coerce').fillna(0)

def school_treat_risk(row):
    if row['school_treat_info_new'] == 1: return 'High Risk'
    if row['school_treat_info_new'] > 2 and row['school_treat_info_new'] < 6: return 'Medium Risk'
    if row['school_treat_info_new'] > 5: return 'Low Risk'
    return 'NA'

number_of_schools_intervention_Comments_df["school_treat_risk"] = number_of_schools_intervention_Comments_df.apply(
    lambda row: school_treat_risk(row), axis=1)

conditions = [
    (number_of_schools_intervention_Comments_df["school_treat_risk"] == 'High Risk'),
    (number_of_schools_intervention_Comments_df["school_treat_risk"] == 'Medium Risk'),
    (number_of_schools_intervention_Comments_df["school_treat_risk"] == 'Low Risk'),
]
choices = [1, 2, 3]

number_of_schools_intervention_Comments_df['school_treat_risk_value'] = np.select(conditions, choices, default="NA")

##########################
# NUMBER OF CLASSES TOTAL
##########################

number_of_classes_total_Comments_df["class_total_info_new"] = number_of_classes_total_Comments_df["class_total_info"].apply(
    pd.to_numeric, errors='coerce').fillna(0)

def class_total_risk1(row):
    if row['class_total_info_new'] == 1:
        return 'Higher Risk'
    if row['class_total_info_new'] > 2 and row['class_total_info_new'] < 6:
        return 'Medium Risk'
    if row['class_total_info_new'] > 5:
        return 'Low Risk'
    return 'NA'

number_of_classes_total_Comments_df["class_total_info_risk"] = number_of_classes_total_Comments_df.apply(
    lambda row: class_total_risk1(row), axis=1)

conditions = [
    (number_of_classes_total_Comments_df["class_total_info_risk"] == 'High Risk'),
    (number_of_classes_total_Comments_df["class_total_info_risk"] == 'Medium Risk'),
    (number_of_classes_total_Comments_df["class_total_info_risk"] == 'Low Risk'),
    (number_of_classes_total_Comments_df["class_total_info_risk"] == 'NA'),
]
choices = [1, 2, 3, np.nan]

number_of_classes_total_Comments_df['class_total_risk_value'] = np.select(conditions, choices, default="NA")

#############################
# INTERVENTION DELIVERY (WHO)
#############################

del intervention_delivery_df['int_who_info']
del intervention_delivery_df['int_who_ht']

# originals
""" intervention_delivery_df["research staff"] = intervention_delivery_df["int_who_raw"].apply(lambda x: 'Research staff' in x) """
""" intervention_delivery_df["class teachers"]  = intervention_delivery_df["int_who_raw"].apply(lambda x: 'Class teachers' in x) """
""" intervention_delivery_df["other school staff"] = intervention_delivery_df["int_who_raw"].apply(lambda x: 'Other school staff' in x) """

intervention_delivery_df["peers"] = intervention_delivery_df["int_who_raw"].apply(lambda x: 'Peers' in x)
intervention_delivery_df["lay persons/volunteers"] = intervention_delivery_df["int_who_raw"].apply(lambda x: 'Lay persons/volunteers' in x)
intervention_delivery_df["digital technology"] = intervention_delivery_df["int_who_raw"].apply(lambda x: 'Digital technology' in x)
intervention_delivery_df["parents/carers"] = intervention_delivery_df["int_who_raw"].apply(lambda x: 'Parents/carers' in x)
intervention_delivery_df["external teachers"] = intervention_delivery_df["int_who_raw"].apply(lambda x: 'External teachers' in x)
intervention_delivery_df["teaching assistants"] = intervention_delivery_df["int_who_raw"].apply(lambda x: 'Teaching assistants' in x)
intervention_delivery_df["research staff"] = intervention_delivery_df["int_who_raw"].apply(lambda x: 'Research staff' in x)
intervention_delivery_df["class teachers"] = intervention_delivery_df["int_who_raw"].apply(lambda x: 'Class teachers' in x)
intervention_delivery_df["unclear/not specified"] = intervention_delivery_df["int_who_raw"].apply(lambda x: 'Unclear/not specified' in x)

intervention_delivery_df.columns = ["int_who_raw", "peers", "lay persons/volunteers", "digital technology", "parents/carers", "external teachers", "teaching assistants", "research staff", "class teachers", "unclear/not specified"]

intervention_delivery_df.loc[intervention_delivery_df['int_who_raw'].map(str).str.contains('Unclear/not specified'), 'int_who_raw_risk_value'] = 1
intervention_delivery_df.loc[intervention_delivery_df['int_who_raw'].map(str).str.contains('Peers'), 'int_who_raw_risk_value']   = 1
intervention_delivery_df.loc[intervention_delivery_df['int_who_raw'].map(str).str.contains('Lay persons/volunteers'), 'int_who_raw_risk_value']  = 2
intervention_delivery_df.loc[intervention_delivery_df['int_who_raw'].map(str).str.contains('Digital technology'), 'int_who_raw_risk_value']   = 1
intervention_delivery_df.loc[intervention_delivery_df['int_who_raw'].map(str).str.contains('Teaching assistants'), 'int_who_raw_risk_value'] = 2
intervention_delivery_df.loc[intervention_delivery_df['int_who_raw'].map(str).str.contains('Parents/carers'), 'int_who_raw_risk_value'] = 2
intervention_delivery_df.loc[intervention_delivery_df['int_who_raw'].map(str).str.contains('Research staff'), 'int_who_raw_risk_value'] = 2
intervention_delivery_df.loc[intervention_delivery_df['int_who_raw'].map(str).str.contains('Class teachers'), 'int_who_raw_risk_value'] = 3
intervention_delivery_df.loc[intervention_delivery_df['int_who_raw'].map(str).str.contains('External teachers'), 'int_who_raw_risk_value'] = 2

intervention_delivery_df['int_who_raw_risk_value'] = intervention_delivery_df['int_who_raw_risk_value']

print(intervention_delivery_df["research staff"][50:96])

#####################
# OUTCOME EVALUATION 
#####################

del InterventionEvaluation_df['eef_eval_raw']

InterventionEvaluation_df['out_eval_raw'] = InterventionEvaluation_df['out_eval_raw'].str[0]

conditions = [
    (InterventionEvaluation_df['out_eval_raw'] == "The developer"),
    (InterventionEvaluation_df['out_eval_raw'] == "A different organization paid by developer"),
    (InterventionEvaluation_df['out_eval_raw'] == "An organization commissioned independently to evaluate"),
    (InterventionEvaluation_df['out_eval_raw'] == "Unclear/not stated"),
]

# GET RISK LEVELS PER OUTCOME EVALUATION
choices = ['Medium Risk', 'Medium Risk', 'Low Risk', 'Medium Risk']

InterventionEvaluation_df["out_eval_risk"] = np.select(conditions, choices, default="NA")

conditions = [
    (InterventionEvaluation_df["out_eval_risk"] == 'High Risk'),
    (InterventionEvaluation_df["out_eval_risk"] == 'Medium Risk'),
    (InterventionEvaluation_df["out_eval_risk"] == 'Low Risk'),
]

choices = [1, 2, 3]

InterventionEvaluation_df["out_eval_risk_value"] = np.select(conditions, choices, default="NA")

################
# COMPARABILITY
################

del comparability_df["comp_anal_ht"]
del comparability_df["comp_anal_info"]

comparability_df['comp_anal_raw'] = comparability_df['comp_anal_raw'].apply(lambda x: ",".join(x) if isinstance(x, list) else x)

conditions = [
    (comparability_df['comp_anal_raw'] == "Yes"),
    (comparability_df['comp_anal_raw'] == "No"),
    (comparability_df['comp_anal_raw'] == "Unclear or details not provided"),
]

choices = ['Low Risk', 'Medium Risk', 'Medium Risk']

comparability_df["comp_anal_risk"] = np.select(conditions, choices, default="NA")

conditions = [
    (comparability_df['comp_anal_risk'] == 'Low Risk'),
    (comparability_df['comp_anal_risk'] == 'Medium Risk'),
    (comparability_df['comp_anal_risk'] == 'High Risk'),
]
choices = [3, 2, 1]

comparability_df["comp_anal_risk_value"] = np.select(conditions, choices, default="NA")

# TOOLKIT PRIMARY EFFECT SIZE AND STANDARD ERROR (FROM DATAFRAME 6 'MAIN ANALYSIS')

tool_prim_es = df_all["smd_tool"]
tool_prim_se = df_all["se_tool"]

########################################################################################################################
########################################################################################################################

risk_of_bias_df = pd.concat([
    eppiid_df, 
    author_df, 
    tool_prim_es,
    tool_prim_se,
    year_df, 
    admin_strand_df,
    publicationtype_df,
    participant_assignment_df,
    study_realism_df,
    number_of_schools_intervention_Comments_df,
    intervention_delivery_df,
    number_of_classes_total_Comments_df,
    InterventionEvaluation_df,
    comparability_df,
    sample_size_Comments_df,
    toolkit_test_type,
    toolkit_es_type,
    overall_percent_attrition_Comments_df,
    clustering_df,
    randomisation_df
], axis=1, sort=False)

# CONVERT OBJECT COLUMNS TO FLOAT (FOR ADDITION)
risk_of_bias_df["rand_risk_value"] = risk_of_bias_df["rand_risk_value"].apply(pd.to_numeric, errors='coerce')
risk_of_bias_df["part_assig_risk_value"] = risk_of_bias_df["part_assig_risk_value"].apply(pd.to_numeric, errors='coerce')
risk_of_bias_df["eco_valid_risk_value"] = risk_of_bias_df["eco_valid_risk_value"].apply(pd.to_numeric, errors='coerce')
risk_of_bias_df["school_treat_risk_value"] = risk_of_bias_df["school_treat_risk_value"].apply(pd.to_numeric, errors='coerce')
risk_of_bias_df["pub_type_risk_value"] = risk_of_bias_df["pub_type_risk_value"].apply(pd.to_numeric, errors='coerce')
risk_of_bias_df["class_total_risk_value"] = risk_of_bias_df["class_total_risk_value"].apply(pd.to_numeric, errors='coerce')
risk_of_bias_df["out_eval_risk_value"] = risk_of_bias_df["out_eval_risk_value"].apply(pd.to_numeric, errors='coerce')
risk_of_bias_df["comp_anal_risk_value"] = risk_of_bias_df["comp_anal_risk_value"].apply(pd.to_numeric, errors='coerce')
risk_of_bias_df["sample_size_risk_value"] = risk_of_bias_df["sample_size_risk_value"].apply(pd.to_numeric, errors='coerce')
risk_of_bias_df["out_test_type_raw_risk_value"] = risk_of_bias_df["out_test_type_raw_risk_value"].apply(pd.to_numeric, errors='coerce')
risk_of_bias_df["out_es_type_risk_value"] = risk_of_bias_df["out_es_type_risk_value"].apply(pd.to_numeric, errors='coerce')
risk_of_bias_df["int_who_raw_risk_value"] = risk_of_bias_df["int_who_raw_risk_value"].apply(pd.to_numeric, errors='coerce')
risk_of_bias_df["attri_perc_info_risk_value"] = risk_of_bias_df["attri_perc_info_risk_value"].apply(pd.to_numeric, errors='coerce')
risk_of_bias_df["clust_anal_risk_value"] = risk_of_bias_df["clust_anal_risk_value"].apply(pd.to_numeric, errors='coerce')
risk_of_bias_df["pub_year_risk_value"] = risk_of_bias_df["pub_year_risk_value"].apply(pd.to_numeric, errors='coerce')

risk_of_bias_df['raw_total'] = risk_of_bias_df[[
    'pub_year_risk_value',
    'pub_type_risk_value',
    'part_assig_risk_value',
    'rand_risk_value',
    'out_test_type_raw_risk_value',
    'eco_valid_risk_value',
    'int_who_raw_risk_value',
    'school_treat_risk_value',
    'sample_size_risk_value',
    'class_total_risk_value',
    'out_eval_risk_value',
    'out_es_type_risk_value',
    'comp_anal_risk_value',
    'attri_perc_info_risk_value',
    'clust_anal_risk_value',
    ]].iloc[:].sum(axis=1)

# concatanate risk values for mean calculation
mean_calc = pd.concat([
    risk_of_bias_df["pub_year_risk_value"],
    risk_of_bias_df["pub_type_risk_value"],
    risk_of_bias_df["part_assig_risk_value"],
    risk_of_bias_df["rand_risk_value"],
    risk_of_bias_df["out_test_type_raw_risk_value"],
    risk_of_bias_df["eco_valid_risk_value"],
    risk_of_bias_df["school_treat_risk_value"],
    risk_of_bias_df["sample_size_risk_value"],
    risk_of_bias_df["class_total_risk_value"],
    risk_of_bias_df["out_eval_risk_value"],
    risk_of_bias_df["out_es_type_risk_value"],
    risk_of_bias_df["comp_anal_risk_value"],
    risk_of_bias_df["attri_perc_info_risk_value"],
    risk_of_bias_df["clust_anal_risk_value"],
    risk_of_bias_df['int_who_raw_risk_value']
], axis=1, sort=False)

""" risk_of_bias_df["NA_values"]  = mean_calc.isnull().sum(axis=1)

# replace zero with np.nan
mean_calc = mean_calc.replace(0, np.nan)
risk_of_bias_df["Mean"] = mean_calc.mean(axis=1)

# CALCULATE MEDIAN
 
# get median and assign to 'median' column on a row by row basis
risk_of_bias_df["Median"] = mean_calc.median(axis=1) """



""" # on a row by row basis, replace all NaN with corresponding median
mean_calc = mean_calc.T.fillna(mean_calc['median']).T """

""" risk_of_bias_df["pub_year_risk_value"] = median_calc["pub_year_risk_value"].values
risk_of_bias_df["pub_type_risk_value"] = median_calc["pub_type_risk_value"].values
risk_of_bias_df["part_assig_risk_value"] = median_calc["part_assig_risk_value"].values
risk_of_bias_df["rand_risk_value"] = median_calc["rand_risk_value"].values
risk_of_bias_df["out_test_type_raw_risk_value"] = median_calc["out_test_type_raw_risk_value"].values
risk_of_bias_df["eco_valid_risk_value"] = median_calc["eco_valid_risk_value"].values
risk_of_bias_df["school_treat_risk_value"] = median_calc["school_treat_risk_value"].values
risk_of_bias_df["sample_size_risk_value"] = median_calc["sample_size_risk_value"].values
risk_of_bias_df["class_total_risk_value"] = median_calc["class_total_risk_value"].values
risk_of_bias_df["out_eval_risk_value"] = median_calc["out_eval_risk_value"].values
risk_of_bias_df["out_es_type_risk_value"] = median_calc["out_es_type_risk_value"].values
risk_of_bias_df["comp_anal_risk_value"] = median_calc["comp_anal_risk_value"].values
risk_of_bias_df["attri_perc_info_risk_value"] = median_calc["attri_perc_info_risk_value"].values
risk_of_bias_df["clust_anal_risk_value"] = median_calc["clust_anal_risk_value"].values
risk_of_bias_df["int_who_raw_risk_value"] = median_calc["int_who_raw_risk_value"].values """

""" print(type(risk_of_bias_df["strand_raw"]))

risk_of_bias_df['strand_raw'] = risk_of_bias_df['strand_raw'].str.join(', ')

risk_of_bias_df.replace('~', '', regex=True, inplace=True)
risk_of_bias_df.replace('<', '', regex=True, inplace=True)
risk_of_bias_df.replace('≤', '', regex=True, inplace=True)
risk_of_bias_df.replace(['NA'], 'NA', inplace=True)
risk_of_bias_df.replace(['N'], 'NA', inplace=True)

risk_of_bias_df.replace('\r', ' ', regex=True, inplace=True)
risk_of_bias_df.replace('\n', ' ', regex=True, inplace=True)
risk_of_bias_df.replace(':', ' ',  regex=True, inplace=True)
risk_of_bias_df.replace(';', ' ',  regex=True, inplace=True)

risk_of_bias_df.replace(r'^\s*$', "NA", regex=True)
risk_of_bias_df.fillna('NA', inplace=True)

final_score_col = risk_of_bias_df.pop('raw_total')
risk_of_bias_df.insert(63, 'raw_total', final_score_col) """

cw = os.getcwd()

""" # get file name for output
outfile_name_pre = data_files.rsplit('/')[-1]
outfile_name_mid = outfile_name_pre.rsplit('.')[0]
outfile_name = outfile_name_mid + "_ROB.csv"
outfile = os.path.join(cw + "/" + outfile_name_mid, outfile_name)

# create dir (filename)
try:
    os.mkdir(outfile_name_mid)
except OSError:
    print("Create {} dir fail, already exists or permission error".format(
        outfile_name_mid))
else:
    print("Successfully created {} directory".format(outfile_name_mid))

# write to disk
print("Input file: {}".format(data_files))
print("Saving extracted output to: {}".format(outfile))
df_all.to_csv(outfile, index=False) """














# % studies since year 2000 
number_of_studies = len(risk_of_bias_df)
risk_of_bias_df["pub_year"] = pd.to_numeric(risk_of_bias_df["pub_year"], errors='coerce')
recent_studies = len(risk_of_bias_df[risk_of_bias_df["pub_year"] > 2000])
perc_recent = recent_studies/number_of_studies*100

# summary padlock frame
number_of_studies = len(risk_of_bias_df)
total_pupil_number = risk_of_bias_df["sample_analysed_info"].sum().astype(int)

# percentage randomised
perc_randomised = risk_of_bias_df[risk_of_bias_df["rand_raw"] == 'Yes'].shape[0]/len(risk_of_bias_df)*100
perc_randomised = np.round(perc_randomised, 1)

# percentrage high ecological validity
perc_high_eco_valid = risk_of_bias_df[risk_of_bias_df["eco_valid_raw"] == 'High ecological validity'].shape[0]/len(risk_of_bias_df)*100
perc_high_eco_valid = np.round(perc_high_eco_valid, 1)

# mean ecological validity risk value
risk_of_bias_df["eco_valid_risk_value"] = pd.to_numeric(risk_of_bias_df["eco_valid_risk_value"], errors='coerce')
mean_eco_valid_risk = risk_of_bias_df["eco_valid_risk_value"].mean()
mean_eco_valid_risk = np.round(mean_eco_valid_risk, 2)

# median school treatment number
risk_of_bias_df["school_treat_info"] = pd.to_numeric(risk_of_bias_df["school_treat_info"], errors='coerce')
median_school_number = risk_of_bias_df["school_treat_info"].median(skipna=True)
median_school_number = np.round(median_school_number, 2)

# mean number of schools risk value
risk_of_bias_df["school_treat_risk_value"] = pd.to_numeric(risk_of_bias_df["school_treat_risk_value"], errors='coerce')
mean_number_schools_risk = risk_of_bias_df["school_treat_risk_value"].mean()
mean_number_schools_risk = np.round(mean_number_schools_risk, 2)

# mean randomisation risk value
participant_assignment_df['part_assig_risk_value'] = pd.to_numeric(participant_assignment_df['part_assig_risk_value'], errors='coerce')
mean_randomisation_risk = participant_assignment_df['part_assig_risk_value'].mean()
""" mean_randomisation_risk.round(2) """

# Percentage taught by research staff only (int_who_raw)
risk_of_bias_df["class_total_info"] = pd.to_numeric(risk_of_bias_df["class_total_info"], errors='coerce')
median_class_number = risk_of_bias_df["class_total_info"].median()
median_class_number = np.round(median_class_number, 2)

# mean class number risk value
risk_of_bias_df["class_total_risk_value"] = pd.to_numeric(risk_of_bias_df["class_total_risk_value"], errors='coerce')
mean_class_risk = risk_of_bias_df["class_total_risk_value"].mean()
mean_class_risk = np.round(mean_class_risk, 2)

# percentage independently evaluated
perc_indep_eval = risk_of_bias_df[risk_of_bias_df["out_eval_raw"] == 'An organization commissioned independently to evaluate'].shape[0]/len(risk_of_bias_df)*100
perc_indep_eval = np.round(perc_indep_eval, 1)

# median percent attrition reported
overall_percent_attrition_Comments_df["attri_perc_info"] = pd.to_numeric(overall_percent_attrition_Comments_df["attri_perc_info"], errors='coerce')
median_perc_attrit_reported = overall_percent_attrition_Comments_df["attri_perc_info"].median(skipna=True)
median_perc_attrit_reported = np.round(median_perc_attrit_reported, 2)


# percentage taught by research staff only
conditions = [
    (intervention_delivery_df['research staff'] == True) &
    (intervention_delivery_df["class teachers"] == False) &
    (intervention_delivery_df["external teachers"] == False),
]
values = ['1']
intervention_delivery_df['research_staff_only'] = np.select(conditions, values)
research_staff_only = (intervention_delivery_df["research_staff_only"] == "1").sum()/len(intervention_delivery_df*100)


print(intervention_delivery_df['research staff'])


strand = admin_strand_df.iloc[0, 0]

df = pd.DataFrame([[
    strand,
    number_of_studies, 
    perc_recent,
    total_pupil_number, 
    perc_randomised, 
    perc_high_eco_valid, 
    mean_eco_valid_risk,
    median_school_number,
    mean_number_schools_risk,
    median_class_number,
    mean_class_risk,
    perc_indep_eval,
    mean_randomisation_risk,
    research_staff_only,
    median_perc_attrit_reported
]])

df.columns = [
    "strand",
    "number_of_studies",
    "%_since_2000",
    "total_pupil_number",
    "%_randomised",
    "%_high_eco_valid",
    "mean_eco_valid_risk",
    "median_school_number",
    "mean_number_Schools_risk",
    "median_class_number",
    "mean_class_risk",
    "%_indep_eval",
    "mean_rand_risk",
    "%_taught_res_staff_only",
    "%_median_attrit_reported"
]

########################################
# % studies since 2000 padlock scale
########################################

# convert %_since_2000 data to numeric
df["%_since_2000"] = pd.to_numeric(df["%_since_2000"], errors='coerce').fillna(0)

def perc_recent_risk(row):
    if row["%_since_2000"] > 49:
        return 'L'
    if row["%_since_2000"] > 25 and row["%_since_2000"] < 50:
        return 'M'
    if row["%_since_2000"] < 25:
        return 'H'
    return 'NA'

# apply padlock function to number of studies column
df["%_since_2000_padlock_scale"] = df.apply(lambda row: perc_recent_risk(row), axis=1)

########################################
# _median_attrit_reported padlock scale
########################################

# convert median attrition data to numeric
df["%_median_attrit_reported"] = pd.to_numeric(df["%_median_attrit_reported"], errors='coerce').fillna(0)

def median_attrit_report_risk(row):
    if row["%_median_attrit_reported"] < 15:
        return 'L'
    if row["%_median_attrit_reported"] > 14 and row["%_median_attrit_reported"] < 30:
        return 'M'
    if row["%_median_attrit_reported"] >29:
        return 'H'
    return 'NA'

# apply padlock function to number of studies column
df["%_median_attrit_reported_padlock_scale"] = df.apply(lambda row: median_attrit_report_risk(row), axis=1)

########################################
# make number of studies padlock scale
########################################

# convert number of studies data to numeric
df["number_of_studies"] = pd.to_numeric(df["number_of_studies"], errors='coerce').fillna(0)

def num_studies_risk(row):
    if row["number_of_studies"] < 10:
        return '0'
    if row["number_of_studies"] > 9 and row["number_of_studies"] < 25:
        return '1'
    if row["number_of_studies"] > 24 and row["number_of_studies"] < 35:
        return '2'
    if row["number_of_studies"] > 34 and row["number_of_studies"] < 60:
        return '3'
    if row["number_of_studies"] > 59 and row["number_of_studies"] < 90:
        return '4'
    if row["number_of_studies"] > 89:
        return '5'
    return 'NA'

# apply padlock function to number of studies column
df["number_of_studies_padlock_scale"] = df.apply(lambda row: num_studies_risk(row), axis=1)

########################################
# make % randomised padlock scale
########################################

# convert number of studies data to numeric
df["%_randomised"] = pd.to_numeric(df["%_randomised"], errors='coerce').fillna(0)

def perc_randomised_risk(row):
    if row["%_randomised"] < 30:
        return 'H'
    if row["%_randomised"] > 29 and row["%_randomised"] < 60:
        return 'M'
    if row["%_randomised"] > 59:
        return 'L'
    return 'NA'

df["%_randomised_padlock_scale"] = df.apply(lambda row: perc_randomised_risk(row), axis=1)

########################################
# make ecological validity padlock scale
########################################

# convert number of studies data to numeric
df["%_high_eco_valid"] = pd.to_numeric(df["%_high_eco_valid"], errors='coerce').fillna(0)

def eco_valid_risk(row):
    if row["%_high_eco_valid"] < 50:
        return 'H'
    if row["%_high_eco_valid"] > 49 and row["%_high_eco_valid"] < 75:
        return 'M'
    if row["%_high_eco_valid"] > 74:
        return 'L'
    return 'NA'

df["%_high_eco_valid_padlock_scale"] = df.apply(lambda row: eco_valid_risk(row), axis=1)

########################################
# make % indep eval padlock scale
########################################

# convert number of studies data to numeric
df["%_indep_eval"] = pd.to_numeric(df["%_indep_eval"], errors='coerce').fillna(0)


def perc_indep_eval_risk(row):
    if row["%_indep_eval"] < 10:
        return 'H'
    if row["%_indep_eval"] > 10 and row["%_indep_eval"] < 30:
        return 'M'
    if row["%_indep_eval"] > 29:
        return 'L'
    return 'NA'

df["%_indep_eval_padlock_scale"] = df.apply(lambda row: perc_indep_eval_risk(row), axis=1)

####################################################
# reduce padlock if any key ratings are High risk
####################################################

df["number_of_studies_padlock_scale"] = pd.to_numeric(df["number_of_studies_padlock_scale"], errors='coerce').fillna(0)
df["New_padlock"] = df["number_of_studies_padlock_scale"]

def risk_impact(row):
    if row["%_randomised_padlock_scale"] == "H": 
        df["New_padlock"] = df["New_padlock"] - 1
    if row["%_high_eco_valid_padlock_scale"] == "H":
        df["New_padlock"] = df["New_padlock"] - 1
    if row["%_indep_eval_padlock_scale"] == "H":
        df["New_padlock"] = df["New_padlock"] - 1
    if row["%_since_2000_padlock_scale"] == "H":
        df["New_padlock"] = df["New_padlock"] - 1
    if row["%_median_attrit_reported_padlock_scale"] == "H":
        df["New_padlock"] = df["New_padlock"] - 1
    return df["New_padlock"]

df["New_padlock"] = df.apply(lambda row: risk_impact(row), axis=1)

df = df[[
    "strand",
    "number_of_studies",
    "%_since_2000",
    "%_since_2000_padlock_scale",
    "number_of_studies_padlock_scale",
    "total_pupil_number",
    "%_randomised",
    "%_randomised_padlock_scale",
    "%_high_eco_valid",
    "mean_eco_valid_risk",
    "%_high_eco_valid_padlock_scale",
    "median_school_number",
    "mean_number_Schools_risk",
    "median_class_number",
    "mean_class_risk",
    "%_indep_eval",
    "%_indep_eval_padlock_scale",
    "mean_rand_risk",
    "%_taught_res_staff_only",
    "%_median_attrit_reported",
    "%_median_attrit_reported_padlock_scale",
    "New_padlock"
]]

#################################################################
# make more than 10 studies checker (has received meta-analysis)
#################################################################

number_of_studies_check = len(risk_of_bias_df)

if number_of_studies_check > 9 and df["New_padlock"][0] < 1:
    df["New_padlock"][0] = 1
    df["MA_floor"] = True
else:
    print("default padlock floor of zero")
    df["MA_floor"] = False

df["filename"] = data_files.rsplit('/')[-1]




# get file name for output
outfile_name = data_files.rsplit('/')[-1]
outfile_name = outfile_name.rsplit('.')[0]
outfile_name = "padlock_data/" + outfile_name + "_padlock_summary.csv"

# write to disk
print("saving {}".format(outfile_name))
df.to_csv(outfile_name, index=False, header=True)




