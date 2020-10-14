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

studydesign = get_data(study_design_output)

studydesign_df = pd.DataFrame(studydesign)
studydesign_df = studydesign_df.T
studydesign_df.columns=["int_design_raw"]

""" studydesign_df["Individual RCT"]                               = studydesign_df["Study_Design_extract"].map(set(['Individual RCT']).issubset).astype(int)
studydesign_df["Cluster RCT"]                                  = studydesign_df["Study_Design_extract"].map(set(['Cluster RCT']).issubset).astype(int)
studydesign_df["Multisite RCT'"]                               = studydesign_df["Study_Design_extract"].map(set(['Multisite RCT']).issubset).astype(int)
studydesign_df["Prospective QED"]                              = studydesign_df["Study_Design_extract"].map(set(['Prospective QED']).issubset).astype(int)
studydesign_df["Retrospective QED"]                            = studydesign_df["Study_Design_extract"].map(set(['Retrospective QED']).issubset).astype(int)
studydesign_df["Interrupted time series QED"]                  = studydesign_df["Study_Design_extract"].map(set(['Interrupted time series QED']).issubset).astype(int)
studydesign_df["Regression Discontinuity with randomisation"]  = studydesign_df["Study_Design_extract"].map(set(['Regression Discontinuity with randomisation']).issubset).astype(int)
studydesign_df["Regression Discontinuity - not randomised"]    = studydesign_df["Study_Design_extract"].map(set(['Regression Discontinuity - not randomised']).issubset).astype(int)
studydesign_df["Regression Continuity  - naturally occurring"] = studydesign_df["Study_Design_extract"].map(set(['Regression Continuity  - naturally occurring']).issubset).astype(int) """

# Get Study Design highlighted text
studydesign_HT            = highlighted_text(study_design_output)
studydesign_HT_df         = pd.DataFrame(studydesign_HT)
studydesign_HT_df         = studydesign_HT_df.T
studydesign_HT_df.columns = ["int_design_ht"]

# Get Study Design user comments
studydesign_Comments            = comments(study_design_output)
studydesign_Comments_df         = pd.DataFrame(studydesign_Comments)
studydesign_Comments_df         = studydesign_Comments_df.T
studydesign_Comments_df.columns = ["int_design_info"]

# concatenate data frames
study_design_df = pd.concat([studydesign_df, studydesign_HT_df, studydesign_Comments_df], axis=1, sort=False)

study_design_df.fillna("NA", inplace=True)

study_design_df.to_csv("studydesign.csv", index=False)

