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
InterventionEvaluation            = get_data(intervention_evaluation)
InterventionEvaluation_df         = pd.DataFrame(InterventionEvaluation)
InterventionEvaluation_df         = InterventionEvaluation_df.T
InterventionEvaluation_df.columns = ["out_eval_raw"]

# Binarize Intervention Costs Reported data
""" InterventionEvaluation_df["out_eval_the_developer"]                                          = InterventionEvaluation_df["out_eval_raw"].map(set(["The developer"]).issubset).astype(int)
InterventionEvaluation_df["out_eval_a_different_organization_paid_by_developer"]             = InterventionEvaluation_df["out_eval_raw"].map(set(["A different organization paid by developer"]).issubset).astype(int)
InterventionEvaluation_df["out_eval_an_organization_commissioned_independently_to_evaluate"] = InterventionEvaluation_df["out_eval_raw"].map(set(["An organization commissioned independently to evaluate"]).issubset).astype(int)
InterventionEvaluation_df["out_eval_unclear/not_stated"]                                     = InterventionEvaluation_df["out_eval_raw"].map(set(["Unclear/not stated"]).issubset).astype(int) """

InterventionEvaluation_df["eef_eval_raw"] = InterventionEvaluation_df["out_eval_raw"].map(set(["Is this an EEF evaluation?"]).issubset).astype(int)
InterventionEvaluation_df["eef_eval_raw"]=InterventionEvaluation_df["eef_eval_raw"].replace(to_replace=[0, 1], value=["No", "Yes"])

# Get Intervention Costs Reported highlighted text
InterventionEvaluation_HT            = highlighted_text(intervention_evaluation)
InterventionEvaluation_HT_df         = pd.DataFrame(InterventionEvaluation_HT)
InterventionEvaluation_HT_df         = InterventionEvaluation_HT_df.T
InterventionEvaluation_HT_df.columns = ["out_eval_ht"]

# Get Intervention Costs Reported user comments
InterventionEvaluation_Comments            = comments(intervention_evaluation)
InterventionEvaluation_Comments_df         = pd.DataFrame(InterventionEvaluation_Comments)
InterventionEvaluation_Comments_df         = InterventionEvaluation_Comments_df.T
InterventionEvaluation_Comments_df.columns = ["out_eval_info"]

# concatenate data frames
intervention_evaluation_df = pd.concat([InterventionEvaluation_df, InterventionEvaluation_HT_df, InterventionEvaluation_Comments_df], axis=1, sort=False)

intervention_evaluation_df=intervention_evaluation_df[["out_eval_raw", "out_eval_ht", "out_eval_info", "eef_eval_raw"]]

# Remove problematic text (potential escape sequences) from text input
intervention_evaluation_df.replace('\r',' ', regex=True, inplace=True)
intervention_evaluation_df.replace('\n',' ', regex=True, inplace=True)
intervention_evaluation_df.replace(':',' ',  regex=True, inplace=True)
intervention_evaluation_df.replace(';',' ',  regex=True, inplace=True)

intervention_evaluation_df.fillna("NA", inplace=True)

# Save to file (.csv)
intervention_evaluation_df.to_csv("InterventionEvaluation.csv", index=False)