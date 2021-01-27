from eppi_ID import eppiid_df
from Author import author_df
from Date import year_df
from AdminStrand import admin_strand_df

from PublicationType import publicationtype_df
from ParticipantAssignment import participant_assignment_df
from Randomisation import randomisation_df
from StudyRealism import study_realism_df
from NumberofSchools import number_of_schools_intervention_df
from NumberofClasses import number_of_classes_total_df
from InterventionDelivery import intervention_delivery_df
from InterventionEvaluation import InterventionEvaluation_df

import pandas as pd
import numpy as np

#################################
# PUBLICATION TYPE RISK OF BIAS 
#################################

conditions = [
    (publicationtype_df['pub_type_raw'] == "Journal article"),
    (publicationtype_df['pub_type_raw'] == "Dissertation or thesis"),
    (publicationtype_df['pub_type_raw'] == "Technical report"),
    (publicationtype_df['pub_type_raw'] == "Book or book chapter"),
    (publicationtype_df['pub_type_raw'] == "Conference paper"),
    (publicationtype_df['pub_type_raw'] == "Other (Please specify)"),
]

# GET RISK LEVELS PER PUBLICATION TYPE
choices = ['Lower Risk', 'Medium Risk', 'Medium Risk',
           'Higher Risk', 'Medium Risk', 'Medium Risk']

publicationtype_df["pub_type_risk"] = np.select(
    conditions, choices, default="NA")

conditions = [
    (publicationtype_df["pub_type_risk"] == 'Higher Risk'),
    (publicationtype_df["pub_type_risk"] == 'Medium Risk'),
    (publicationtype_df["pub_type_risk"] == 'Lower Risk'),
]

choices = [1,2,3]

publicationtype_df["pub_type_risk_value"] = np.select(
    conditions, choices, default="NA")
    
######################################
# PARTICIPANT ASSIGNMENT RISK OF BIAS
######################################

del participant_assignment_df["part_assig_ht"]
del participant_assignment_df["part_assig_info"]

conditions = [
    (participant_assignment_df['part_assig_raw'] == 'Random (please specify)'),
    (participant_assignment_df['part_assig_raw'] == 'Non-random, but matched'),
    (participant_assignment_df['part_assig_raw'] == 'Non-random, not matched prior to treatment'),
    (participant_assignment_df['part_assig_raw'] == 'Unclear '),
    (participant_assignment_df['part_assig_raw'] == 'Not assigned - naturally occurring sample'),
    (participant_assignment_df['part_assig_raw'] == 'Retrospective Quasi Experimental Design (QED)'),
    (participant_assignment_df['part_assig_raw'] == 'Regression discontinuity '),
]
choices = ['Lower Risk', 'Medium Risk', 'Medium Risk',
           'Higher Risk', 'Medium Risk', 'Medium Risk', 'Medium Risk']

participant_assignment_df['part_assig_risk'] = np.select(
    conditions, choices, default="NA")

conditions = [
    (participant_assignment_df['part_assig_risk'] == 'Higher Risk'),
    (participant_assignment_df['part_assig_risk'] == 'Medium Risk'),
    (participant_assignment_df['part_assig_risk'] == 'Lower Risk'),
]
choices = [1, 2, 3]

participant_assignment_df['part_assig_risk_value'] = np.select(
    conditions, choices, default="NA")

#############################
# RANDOMISATION RISK OF BIAS
#############################

del randomisation_df['rand_ht']
del randomisation_df['rand_info']

conditions = [
    (randomisation_df['rand_raw'] == 'Yes'),
    (randomisation_df['rand_raw'] == 'Not applicable'),
    (randomisation_df['rand_raw'] == 'No/Unclear'),
]
choices = ['Lower Risk', 'N/A', 'Medium Risk']

randomisation_df['rand_risk'] = np.select(conditions, choices, default="NA")

conditions = [
    (randomisation_df['rand_risk'] == 'Lower Risk'),
    (randomisation_df['rand_risk'] == 'N/A'),
    (randomisation_df['rand_risk'] == 'Medium Risk'),
]
choices = [3, 3, 2]

randomisation_df['rand_risk_value'] = np.select(
    conditions, choices, default="NA")

#############################
# STUDY REALISM RISK OF BIAS
##############################

del study_realism_df['eco_valid_ht']
del study_realism_df['eco_valid_info']

conditions = [
    (study_realism_df['eco_valid_raw'] == 'High ecological validity'),
    (study_realism_df['eco_valid_raw'] == 'Low ecological validity'),
    (study_realism_df['eco_valid_raw'] == 'Unclear'),
]
choices = ['Lower Risk', 'Higher Risk', 'Higher Risk']

study_realism_df['eco_valid_risk'] = np.select(
    conditions, choices, default="NA")

conditions = [
    (study_realism_df['eco_valid_risk'] == 'Lower Risk'),
    (study_realism_df['eco_valid_risk'] == 'Higher Risk'),
]
choices = [3, 1]

study_realism_df['eco_valid_risk_value'] = np.select(
    conditions, choices, default="NA")

##############################################
# NUMBER OF SCHOOLS INTERVENTION RISK OF BIAS
##############################################

number_of_schools_intervention_df["school_treat_info_new"] = number_of_schools_intervention_df["school_treat_info"].apply(
    pd.to_numeric, errors='coerce').fillna(0)


def school_treat_risk(row):
    if row['school_treat_info_new'] == 1:
        return 'Higher Risk'
    if row['school_treat_info_new'] == 2 or row['school_treat_info'] == 3 or row['school_treat_info'] == 4 or row['school_treat_info'] == 5:
        return 'Medium Risk'
    if row['school_treat_info_new'] > 5:
        return 'Lower Risk'
    return 'NA'


number_of_schools_intervention_df["school_treat_risk"] = number_of_schools_intervention_df.apply(
    lambda row: school_treat_risk(row), axis=1)

conditions = [
    (number_of_schools_intervention_df["school_treat_risk"] == 'Higher Risk'),
    (number_of_schools_intervention_df["school_treat_risk"] == 'Medium Risk'),
    (number_of_schools_intervention_df["school_treat_risk"] == 'Lower Risk'),
]
choices = [1, 2, 3]

number_of_schools_intervention_df['school_treat_risk_value'] = np.select(
    conditions, choices, default="NA")

###########################################
# INTERVENTION DELIVERY (WHO) RISK OF BIAS
###########################################

del intervention_delivery_df['int_who_info']
del intervention_delivery_df['int_who_ht']

research_staff_mask = intervention_delivery_df["int_who_raw"].apply(
    lambda x: 'Research staff' in x)

##########################
# NUMBER OF CLASSES TOTAL
##########################

number_of_classes_total_df["class_total_info_new"] = number_of_classes_total_df["class_total_info"].apply(
    pd.to_numeric, errors='coerce').fillna(0)


def class_total_risk(row):
    if row['class_total_info_new'] == 1:
        return 'Higher Risk'
    if row['class_total_info_new'] == 2 or row['class_total_info_new'] == 3 or row['class_total_info_new'] == 4 or row['class_total_info_new'] == 5:
        return 'Medium Risk'
    if row['class_total_info_new'] > 5:
        return 'Lower Risk'
    return 'NA'

number_of_classes_total_df["class_total_info_risk"] = number_of_classes_total_df.apply(
    lambda row: class_total_risk(row), axis=1)

conditions = [
    (number_of_classes_total_df["class_total_info_risk"] == 'Higher Risk'),
    (number_of_classes_total_df["class_total_info_risk"] == 'Medium Risk'),
    (number_of_classes_total_df["class_total_info_risk"] == 'Lower Risk'),
]
choices = [1, 2, 3]

number_of_classes_total_df['class_total_risk_value'] = np.select(
    conditions, choices, default="NA")

##################################
# OUTCOME EVALUATION RISK OF BIAS (figure out how to use np.select with data in square brackets)
##################################

conditions = [
    (InterventionEvaluation_df['out_eval_raw'] == "The developer"),
    (InterventionEvaluation_df['out_eval_raw'] == "A different organization paid by developer"),
    (InterventionEvaluation_df['out_eval_raw'] == "An organization commissioned independently to evaluate"),
    (InterventionEvaluation_df['out_eval_raw'] == "Unclear/not stated"),
]

# GET RISK LEVELS PER OUTCOME EVALUATION
choices = ['Lower Risk', 'Medium Risk', 'Medium Risk',
           'Higher Risk']

InterventionEvaluation_df["out_eval_risk"] = np.select(
    conditions, choices, default="NA")

conditions = [
    (InterventionEvaluation_df["out_eval_risk"] == 'Higher Risk'),
    (InterventionEvaluation_df["out_eval_risk"] == 'Medium Risk'),
    (InterventionEvaluation_df["out_eval_risk"] == 'Lower Risk'),
]

choices = [1,2,3]

InterventionEvaluation_df["out_eval_risk_value"] = np.select(
    conditions, choices, default="NA")


########################################################################################################################
########################################################################################################################

# CREATE COMPLETE RISK OF BIAS DATAFRAME
risk_of_bias_df = pd.concat([eppiid_df, author_df, year_df, admin_strand_df,
                             publicationtype_df,
                             participant_assignment_df,
                             randomisation_df,
                             study_realism_df,
                             number_of_schools_intervention_df,
                             intervention_delivery_df,
                             number_of_classes_total_df,
                             InterventionEvaluation_df], axis=1, sort=False)

# CONVERT OBJECT COLUMNS TO FLOAT (FOR ADDITION)
''' risk_of_bias_df["rand_risk_value"] = risk_of_bias_df["rand_risk_value"].apply(
    pd.to_numeric, errors='coerce').fillna(0)
risk_of_bias_df["part_assig_risk_value"] = risk_of_bias_df["part_assig_risk_value"].apply(
    pd.to_numeric, errors='coerce').fillna(0)
risk_of_bias_df["eco_valid_risk_value"] = risk_of_bias_df["eco_valid_risk_value"].apply(
    pd.to_numeric, errors='coerce').fillna(0)
risk_of_bias_df["school_treat_risk_value"] = risk_of_bias_df["school_treat_risk_value"].apply(
    pd.to_numeric, errors='coerce').fillna(0) '''

""" # RISK OF BIAS SCORE
risk_of_bias_df['risk_score'] = risk_of_bias_df.fillna(0)["part_assig_risk_value"] + risk_of_bias_df.fillna(
    0)["rand_risk_value"] + risk_of_bias_df.fillna(0)["eco_valid_risk_value"] + risk_of_bias_df.fillna(0)["school_treat_risk_value"] """

risk_of_bias_df.info()
risk_of_bias_df.fillna("NA", inplace=True)
risk_of_bias_df.to_csv("Risk_of_Bias_Security.csv", index=False)

""" # summary
Total = risk_of_bias_df['risk_score'].sum()
Study_Count = len(risk_of_bias_df.index)
Mean_Risk = Total/Study_Count

print("\nn = {}".format(Study_Count))
print("Risk Total: {}".format(int(Total)))
print("Mean Risk: {}".format(int(Mean_Risk))) """

print(risk_of_bias_df)
