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

# Get Intervention Training Provided Type main data
InterventionTrainingProvided            = get_data(intervention_training_provided_output)
InterventionTrainingProvided_df         = pd.DataFrame(InterventionTrainingProvided)
InterventionTrainingProvided_df         = InterventionTrainingProvided_df.T
InterventionTrainingProvided_df.columns = ["int_training_raw"]

# Binarize main data
""" InterventionTrainingProvided_df["int_training_yes"]                   = InterventionTrainingProvided_df["int_training_raw"].map(set(['Yes (Please specify)']).issubset).astype(int)
InterventionTrainingProvided_df["int_training_no"]                    = InterventionTrainingProvided_df["int_training_raw"].map(set(["No"]).issubset).astype(int)
InterventionTrainingProvided_df["int_training_unclear/Not_specified"] = InterventionTrainingProvided_df["int_training_raw"].map(set(["Unclear/ Not specified"]).issubset).astype(int) """

# Get Intervention Training Provided highlighted text
InterventionTrainingProvided_HT            = highlighted_text(intervention_training_provided_output)
InterventionTrainingProvided_HT_df         = pd.DataFrame(InterventionTrainingProvided_HT)
InterventionTrainingProvided_HT_df         = InterventionTrainingProvided_HT_df.T
InterventionTrainingProvided_HT_df.columns = ["int_training_ht"]

# Get Intervention Training Provided user comments
InterventionTrainingProvided_Comments            = comments(intervention_training_provided_output)
InterventionTrainingProvided_Comments_df         = pd.DataFrame(InterventionTrainingProvided_Comments)
InterventionTrainingProvided_Comments_df         = InterventionTrainingProvided_Comments_df.T
InterventionTrainingProvided_Comments_df.columns = ["int_training_info"]

# concatenate data frames
intervention_training_provided_df = pd.concat([InterventionTrainingProvided_df, InterventionTrainingProvided_HT_df, InterventionTrainingProvided_Comments_df], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_training_provided_df.replace('\r',' ', regex=True, inplace=True)
intervention_training_provided_df.replace('\n',' ', regex=True, inplace=True)
intervention_training_provided_df.replace(':',' ', regex=True, inplace=True)
intervention_training_provided_df.replace(';',' ', regex=True, inplace=True)

intervention_training_provided_df.fillna("NA", inplace=True)

# Save to file (.csv)
intervention_training_provided_df.to_csv("InterventionTrainingProvided.csv", index=False)