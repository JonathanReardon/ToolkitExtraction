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

# Get Intervention Teaching Approach main data
InterventionTeachingApproach            = get_data(intervention_teaching_approach)
InterventionTeachingApproach_df         = pd.DataFrame(InterventionTeachingApproach)
InterventionTeachingApproach_df         = InterventionTeachingApproach_df.T
InterventionTeachingApproach_df.columns = ["int_approach_raw"]

# Binarize main data
""" InterventionTeachingApproach_df["int_approach_large_group/class_teaching_(+6)"]     = InterventionTeachingApproach_df["int_approach_raw"].map(set(["Large group/class teaching (+6)"]).issubset).astype(int)
InterventionTeachingApproach_df["int_approach_small_group/intensive_support_(3-5)"] = InterventionTeachingApproach_df["int_approach_raw"].map(set(["Small group/intensive support (3-5)"]).issubset).astype(int)
InterventionTeachingApproach_df["int_approach_paired_learning"]                     = InterventionTeachingApproach_df["int_approach_raw"].map(set(["Paired learning"]).issubset).astype(int)
InterventionTeachingApproach_df["int_approach_one_to_one"]                          = InterventionTeachingApproach_df["int_approach_raw"].map(set(["One to one"]).issubset).astype(int)
InterventionTeachingApproach_df["int_approach_student_alone_(self-administered)"]   = InterventionTeachingApproach_df["int_approach_raw"].map(set(["Student alone (self-administered)"]).issubset).astype(int)
InterventionTeachingApproach_df["int_approach_other_(explain_in_notes)"]            = InterventionTeachingApproach_df["int_approach_raw"].map(set(["Other (Explain in notes)"]).issubset).astype(int) """

# Get Intervention Teaching Approachhighlighted text
InterventionTeachingApproach_HT            = highlighted_text(intervention_teaching_approach)
InterventionTeachingApproach_HT_df         = pd.DataFrame(InterventionTeachingApproach_HT)
InterventionTeachingApproach_HT_df         = InterventionTeachingApproach_HT_df.T
InterventionTeachingApproach_HT_df.columns = ["int_approach_ht"]

# Get Intervention Teaching Approach user comments
InterventionTeachingApproach_Comments            = comments(intervention_teaching_approach)
InterventionTeachingApproach_Comments_df         = pd.DataFrame(InterventionTeachingApproach_Comments)
InterventionTeachingApproach_Comments_df         = InterventionTeachingApproach_Comments_df.T
InterventionTeachingApproach_Comments_df.columns = ["int_approach_info"]

# concatenate data frames
intervention_teaching_approach_df = pd.concat([InterventionTeachingApproach_df, InterventionTeachingApproach_HT_df, InterventionTeachingApproach_Comments_df], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_teaching_approach_df.replace('\r',' ', regex=True, inplace=True)
intervention_teaching_approach_df.replace('\n',' ', regex=True, inplace=True)
intervention_teaching_approach_df.replace(':',' ',  regex=True, inplace=True)
intervention_teaching_approach_df.replace(';',' ',  regex=True, inplace=True)

intervention_teaching_approach_df.fillna("NA", inplace=True)

# Save to file (.csv)
intervention_teaching_approach_df.to_csv("InterventionTeachingApproach.csv", index=False)

print(intervention_teaching_approach_df)