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

# Get Intervention Focus main data
InterventionFocus            = get_data(intervention_focus_output)
InterventionFocus_df         = pd.DataFrame(InterventionFocus)
InterventionFocus_df         = InterventionFocus_df.T
InterventionFocus_df.columns = ["int_part_raw"]

# Binarize main data
""" InterventionFocus_df["int_part_students"]                      = InterventionFocus_df["int_part_raw"].map(set(["Students"]).issubset).astype(int)
InterventionFocus_df["int_part_teachers"]                      = InterventionFocus_df["int_part_raw"].map(set(["Teachers"]).issubset).astype(int)
InterventionFocus_df["int_part_teaching_assistants"]           = InterventionFocus_df["int_part_raw"].map(set(["Teaching assistants"]).issubset).astype(int)
InterventionFocus_df["int_part_other_education_practitioners"] = InterventionFocus_df["int_part_raw"].map(set(["Other education practitioners"]).issubset).astype(int)
InterventionFocus_df["int_part_non-teaching_staff"]            = InterventionFocus_df["int_part_raw"].map(set(["Non-teaching staff"]).issubset).astype(int)
InterventionFocus_df["int_part_senior_management"]             = InterventionFocus_df["int_part_raw"].map(set(["Senior management"]).issubset).astype(int)
InterventionFocus_df["int_part_parents"]                       = InterventionFocus_df["int_part_raw"].map(set(["Parents"]).issubset).astype(int)
InterventionFocus_df["int_part_other_(please specify)"]        = InterventionFocus_df["int_part_raw"].map(set(["Other (Please specify)"]).issubset).astype(int) """

# Get Intervention Focus highlighted text
InterventionFocus_HT            = highlighted_text(intervention_focus_output)
InterventionFocus_HT_df         = pd.DataFrame(InterventionFocus_HT)
InterventionFocus_HT_df         = InterventionFocus_HT_df.T
InterventionFocus_HT_df.columns = ["int_part_ht"]

# Get Intervention Focus user comments
InterventionFocus_Comments            = comments(intervention_focus_output)
InterventionFocus_Comments_df         = pd.DataFrame(InterventionFocus_Comments)
InterventionFocus_Comments_df         = InterventionFocus_Comments_df.T
InterventionFocus_Comments_df.columns = ["int_part_info"]

# concatenate data frames
intervention_focus_df = pd.concat([InterventionFocus_df, InterventionFocus_HT_df, InterventionFocus_Comments_df], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_focus_df.replace('\r',' ', regex=True, inplace=True)
intervention_focus_df.replace('\n',' ', regex=True, inplace=True)
intervention_focus_df.replace(':',' ', regex=True, inplace=True)
intervention_focus_df.replace(';',' ', regex=True, inplace=True)

intervention_focus_df.fillna("NA", inplace=True)

# Save to file (.csv)
intervention_focus_df.to_csv("InterventionFocus.csv", index=False)