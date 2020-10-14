import os
import json
import pandas as pd

from CODES import *
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

# Get Intervention Costs Reported main data
InterventionCosts            = get_data(intervention_costs_reported)
InterventionCosts_df         = pd.DataFrame(InterventionCosts)
InterventionCosts_df         = InterventionCosts_df.T
InterventionCosts_df.columns = ["int_cost_raw"]

# Binarize Intervention Costs Reported data
""" InterventionCosts_df["int_cost_yes"] = InterventionCosts_df["int_cost_raw"].map(set(["Yes (Please add details)"]).issubset).astype(int)
InterventionCosts_df["int_cost_no"]  = InterventionCosts_df["int_cost_raw"].map(set(["No"]).issubset).astype(int) """

# Get Intervention Costs Reported highlighted text
InterventionCosts_HT            = highlighted_text(intervention_costs_reported)
InterventionCosts_HT_df         = pd.DataFrame(InterventionCosts_HT)
InterventionCosts_HT_df         = InterventionCosts_HT_df.T
InterventionCosts_HT_df.columns = ["int_cost_ht"]

# Get Intervention Costs Reported user comments
InterventionCosts_Comments            = comments(intervention_costs_reported)
InterventionCosts_Comments_df         = pd.DataFrame(InterventionCosts_Comments)
InterventionCosts_Comments_df         = InterventionCosts_Comments_df.T
InterventionCosts_Comments_df.columns = ["int_cost_info"]

# concatenate data frames
intervention_costs_df = pd.concat([InterventionCosts_df, InterventionCosts_HT_df, InterventionCosts_Comments_df], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_costs_df.replace('\r',' ', regex=True, inplace=True)
intervention_costs_df.replace('\n',' ', regex=True, inplace=True)
intervention_costs_df.replace(':',' ',  regex=True, inplace=True)
intervention_costs_df.replace(';',' ',  regex=True, inplace=True)

intervention_costs_df.fillna("NA", inplace=True)

# Save to file (.csv)
intervention_costs_df.to_csv("InterventionCostsReported.csv", index=False)

print(intervention_costs_df)