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

gender = get_data(student_gender)

gender_df = pd.DataFrame(gender)
gender_df = gender_df.T
gender_df.columns=["part_gen_raw"]

""" gender_df["part_gen_female_only"]      = gender_df["part_gen_raw"].map(set(['Female only']).issubset).astype(int)
gender_df["part_gen_male_only"]        = gender_df["part_gen_raw"].map(set(['Male only']).issubset).astype(int)
gender_df["part_gen_mixed_gender"]     = gender_df["part_gen_raw"].map(set(['Mixed gender']).issubset).astype(int)
gender_df["part_gen_no_info_provided"] = gender_df["part_gen_raw"].map(set(['No information provided']).issubset).astype(int) """

# Get Gender highlighted text
gender_HT            = highlighted_text(student_gender)
gender_HT_df         = pd.DataFrame(gender_HT)
gender_HT_df         = gender_HT_df.T
gender_HT_df.columns = ["part_gen_ht"]

# Get Gender user comments
gender_Comments            = comments(student_gender)
gender_Comments_df         = pd.DataFrame(gender_Comments)
gender_Comments_df         = gender_Comments_df.T
gender_Comments_df.columns = ["part_gen_info"]

# concatenate data frames
gender_df = pd.concat([gender_df, gender_HT_df, gender_Comments_df], axis=1, sort=False)

gender_df.fillna("NA", inplace=True)

print(gender_df)

gender_df.to_csv("gender.csv", index=False)