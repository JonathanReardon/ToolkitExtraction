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

def var_comments(codes):
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

def var_highlighted_text(codes):
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

gender_split=var_comments(gender_split_output)

gender_split_df=pd.DataFrame(gender_split)
gender_split_df=gender_split_df.T
gender_split_df.columns=["Gender_Split_comments"]

gender_split_comments=var_highlighted_text(gender_split_output)

gender_split_comments_df=pd.DataFrame(gender_split_comments)
gender_split_comments_df=gender_split_comments_df.T
gender_split_comments_df.columns=["Gender_Split_HT"]

# CONCATENATE ALL DATAFREAMES
gender_split_df = pd.concat([gender_split_df, gender_split_comments_df], axis=1, sort=False)

# REPLACE (REMOVE) ESCAPE SEQUENCES FROM TEXT
gender_split_df.replace('\r',' ', regex=True, inplace=True)
gender_split_df.replace('\n',' ', regex=True, inplace=True)

gender_split_df.fillna("NA", inplace=True)

# SAVE DATAFRANE TO FILE
gender_split_df.to_csv("gender_split.csv", index=False)