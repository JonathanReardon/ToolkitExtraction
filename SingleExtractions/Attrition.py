import os
import json
import pandas as pd

from AttributeIDList import *
from DATAFILE import file

exclude="NA"

script_dir = os.path.dirname(__file__)
datafile = os.path.join(script_dir, file)

with open(datafile) as f:
    data=json.load(f)

def get_data(codes):
    df=[]
    for var in range(len(codes)):
        holder=[]
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                holderfind, holdervalue = [], []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            holderfind.append(value)
                if len(holderfind)==0:
                    holderfind=exclude
                holder.append(holderfind)
        df.append(holder)
    return df

def highlighted_text(codes):
    all_comments, highlighted_text = [], []
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
                                        user_highlighted_text.append(data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"][i]["Text"])
                if not user_highlighted_text:
                    highlighted_text.append(exclude)
                else:
                    highlighted_text.append(user_highlighted_text)
            else:
                highlighted_text.append(exclude)
        all_comments.append(highlighted_text)
        highlighted_text=[]
    return all_comments

def comments(codes):
    all_comments, comments= [], []
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
                    comments.append(exclude)
                else:
                    comments.append(user_comments)
            else:
                comments.append(exclude)
        all_comments.append(comments)
        comments=[]
    return all_comments

###############################
# ATTRITION DROP OUT REPORTED #
###############################
attrition_dropout_reported = get_data(attrition_dropout_reported_output)
attrition_dropout_reported_df = pd.DataFrame(attrition_dropout_reported)
attrition_dropout_reported_df = attrition_dropout_reported_df.T
attrition_dropout_reported_df.columns=["attri_raw"]

# highlighted text
attrition_dropout_reported_HT            = highlighted_text(attrition_dropout_reported_output)
attrition_dropout_reported_HT_df         = pd.DataFrame(attrition_dropout_reported_HT)
attrition_dropout_reported_HT_df         = attrition_dropout_reported_HT_df.T
attrition_dropout_reported_HT_df.columns = ["attri_ht"]

# comments
attrition_dropout_reported_Comments            = comments(attrition_dropout_reported_output)
attrition_dropout_reported_Comments_df         = pd.DataFrame(attrition_dropout_reported_Comments)
attrition_dropout_reported_Comments_df         = attrition_dropout_reported_Comments_df.T
attrition_dropout_reported_Comments_df.columns = ["attri_info"]

# binarize output options
""" attrition_dropout_reported_df["Attrition_Dropout_Reported_YES"] = attrition_dropout_reported_df["Attrition_Dopout_Reported_extract"].map(set(['Yes']).issubset).astype(int)
attrition_dropout_reported_df["Attrition_Dropout_Reported_NO"] = attrition_dropout_reported_df["Attrition_Dopout_Reported_extract"].map(set(['No']).issubset).astype(int)
attrition_dropout_reported_df["Attrition Unclear (please add notes)"] = attrition_dropout_reported_df["Attrition_Dopout_Reported_extract"].map(set(['Unclear (please add notes)']).issubset).astype(int) """

#############################
# TREATMENT GROUP ATTRITION #
#############################

# Get Treatment Attrition highlighted text
treatmentgroup_attrition_HT            = highlighted_text(treatment_group_attrition)
treatmentgroup_attrition_HT_df         = pd.DataFrame(treatmentgroup_attrition_HT)
treatmentgroup_attrition_HT_df         = treatmentgroup_attrition_HT_df.T
treatmentgroup_attrition_HT_df.columns = ["attri_treat_ht"]

# Get Treatment Attrition user comments
treatmentgroup_attrition_Comments            = comments(treatment_group_attrition)
treatmentgroup_attrition_Comments_df         = pd.DataFrame(treatmentgroup_attrition_Comments)
treatmentgroup_attrition_Comments_df         = treatmentgroup_attrition_Comments_df.T
treatmentgroup_attrition_Comments_df.columns = ["attri_treat_info"]

#############################
# OVERALL PERCENT ATTRITION #
#############################

# Get Overall Percent Attrition highlighted text
overall_percent_attrition_HT            = highlighted_text(overall_percent_attrition)
overall_percent_attrition_HT_df         = pd.DataFrame(overall_percent_attrition_HT)
overall_percent_attrition_HT_df         = overall_percent_attrition_HT_df.T
overall_percent_attrition_HT_df.columns = ["attri_perc_ht"]

# Get Overall Percent Attrition  user comments
overall_percent_attrition_Comments            = comments(overall_percent_attrition)
overall_percent_attrition_Comments_df         = pd.DataFrame(overall_percent_attrition_Comments)
overall_percent_attrition_Comments_df         = overall_percent_attrition_Comments_df.T
overall_percent_attrition_Comments_df.columns = ["attri_perc_info"]

# concatenate data frames
attrition_df = pd.concat([attrition_dropout_reported_df, attrition_dropout_reported_HT_df, attrition_dropout_reported_Comments_df,
                          treatmentgroup_attrition_HT_df, treatmentgroup_attrition_Comments_df,
                          overall_percent_attrition_HT_df, overall_percent_attrition_Comments_df], axis=1, sort=False)

attrition_df.fillna("NA", inplace=True)

attrition_df.to_csv("Attrition.csv", index=False)

