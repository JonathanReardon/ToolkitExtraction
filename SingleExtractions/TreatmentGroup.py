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

treatmentgroup = get_data(treatment_group)

treatmentgroup_df = pd.DataFrame(treatmentgroup)
treatmentgroup_df = treatmentgroup_df.T
treatmentgroup_df.columns=["treat_group_raw"]

""" treatmentgroup_df["treat_group_more_than_one_treatment_group_yes"] = treatmentgroup_df["treat_group_raw"].map(set(['Yes (Please specify)']).issubset).astype(int)
treatmentgroup_df["treat_group_more_than_one_treatment_group_no"]  = treatmentgroup_df["treat_group_raw"].map(set(['No']).issubset).astype(int)
treatmentgroup_df["treat_group_more_than_one_treatment_group_NA"]  = treatmentgroup_df["treat_group_raw"].map(set(['Not specified or N/A']).issubset).astype(int) """

# Get Study Realism highlighted text
treatmentgroup_HT            = highlighted_text(treatment_group)
treatmentgroup_HT_df         = pd.DataFrame(treatmentgroup_HT)
treatmentgroup_HT_df         = treatmentgroup_HT_df.T
treatmentgroup_HT_df.columns = ["treat_group_ht"]

# Get Study Realism user comments
treatmentgroup_Comments            = comments(treatment_group)
treatmentgroup_Comments_df         = pd.DataFrame(treatmentgroup_Comments)
treatmentgroup_Comments_df         = treatmentgroup_Comments_df.T
treatmentgroup_Comments_df.columns = ["treat_group_info"]

# concatenate data frames
treatment_group_df = pd.concat([treatmentgroup_df, treatmentgroup_HT_df, treatmentgroup_Comments_df], axis=1, sort=False)

treatment_group_df.fillna("NA", inplace=True)

treatment_group_df.to_csv("treatmentgroup.csv", index=False)