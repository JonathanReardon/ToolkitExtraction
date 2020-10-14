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

baselinedifferences = get_data(baseline_differences_output)
baselinedifferences_df = pd.DataFrame(baselinedifferences)
baselinedifferences_df = baselinedifferences_df.T
baselinedifferences_df.columns=["base_diff_raw"]

# Get Baseline Differences highlighted text
baselinedifferences_HT            = highlighted_text(baseline_differences_output)
baselinedifferences_HT_df         = pd.DataFrame(baselinedifferences_HT)
baselinedifferences_HT_df         = baselinedifferences_HT_df.T
baselinedifferences_HT_df.columns = ["base_diff_ht"]

# Get Educational Setting user comments
baselinedifferences_Comments            = comments(baseline_differences_output)
baselinedifferences_Comments_df         = pd.DataFrame(baselinedifferences_Comments)
baselinedifferences_Comments_df         = baselinedifferences_Comments_df.T
baselinedifferences_Comments_df.columns = ["base_diff_info"]

# concatenate data frames
baseline_differences_df = pd.concat([baselinedifferences_df, baselinedifferences_HT_df, baselinedifferences_Comments_df], axis=1, sort=False)

baseline_differences_df.fillna("NA", inplace=True)

baseline_differences_df.to_csv("baselinedifferences.csv", index=False)