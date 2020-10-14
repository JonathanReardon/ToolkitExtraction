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

edusetting = get_data(edu_setting_output)

edusetting_df = pd.DataFrame(edusetting)
edusetting_df = edusetting_df.T
edusetting_df.columns=["int_setting_raw"]

""" edusetting_df["int_setting_primary/elementary_school"] = edusetting_df["int_setting_raw"].map(set(['Primary/elementary school']).issubset).astype(int)
edusetting_df["int_setting_middle_school"]             = edusetting_df["int_setting_raw"].map(set(['Middle school']).issubset).astype(int)
edusetting_df["int_setting_secondary/high_school"]     = edusetting_df["int_setting_raw"].map(set(['Secondary/High school']).issubset).astype(int) """

# Get Educational Setting highlighted text
edusetting_HT            = highlighted_text(edu_setting_output)
edusetting_HT_df         = pd.DataFrame(edusetting_HT)
edusetting_HT_df         = edusetting_HT_df.T
edusetting_HT_df.columns = ["int_setting_ht"]

# Get Educational Setting user comments
edusetting_Comments            = comments(edu_setting_output)
edusetting_Comments_df         = pd.DataFrame(edusetting_Comments)
edusetting_Comments_df         = edusetting_Comments_df.T
edusetting_Comments_df.columns = ["int_setting_info"]

# concatenate data frames
educational_setting_df = pd.concat([edusetting_df, edusetting_HT_df, edusetting_Comments_df], axis=1, sort=False)

educational_setting_df.fillna("NA", inplace=True)

educational_setting_df.to_csv("edusetting.csv", index=False)