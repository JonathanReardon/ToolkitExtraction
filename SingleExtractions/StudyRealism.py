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

studyrealism = get_data(study_realism_output)

studyrealism_df = pd.DataFrame(studyrealism)
studyrealism_df = studyrealism_df.T
studyrealism_df.columns=["eco_valid_raw"]

""" studyrealism_df["eco_valid_raw_high_ecological_validity"] = studyrealism_df["eco_valid_raw"].map(set(['High ecological validity']).issubset).astype(int)
studyrealism_df["eco_valid_raw_low_ecological_validity"]  = studyrealism_df["eco_valid_raw"].map(set(['Low ecological validity']).issubset).astype(int)
studyrealism_df["eco_valid_raw_unclear"]                  = studyrealism_df["eco_valid_raw"].map(set(['Unclear']).issubset).astype(int) """

# Get Study Realism highlighted text
studyrealism_HT            = highlighted_text(study_realism_output)
studyrealism_HT_df         = pd.DataFrame(studyrealism_HT)
studyrealism_HT_df         = studyrealism_HT_df.T
studyrealism_HT_df.columns = ["eco_valid_ht"]

# Get Study Realism user comments
studyrealism_Comments            = comments(study_realism_output)
studyrealism_Comments_df         = pd.DataFrame(studyrealism_Comments)
studyrealism_Comments_df         = studyrealism_Comments_df.T
studyrealism_Comments_df.columns = ["eco_valid_info"]

# concatenate data frames
study_realism_df = pd.concat([studyrealism_df, studyrealism_HT_df, studyrealism_Comments_df], axis=1, sort=False)

study_realism_df.fillna("NA", inplace=True)

print(study_realism_df)

study_realism_df.to_csv("studyrealism.csv", index=False)