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

student_age=get_data(student_age_output)

student_age_df=pd.DataFrame(student_age)
student_age_df=student_age_df.T
student_age_df.columns=["part_age_raw"]

""" student_age_df["part_age_3"]=student_age_df["part_age_raw"].map(set(['3']).issubset).astype(int)
student_age_df["part_age_4"]=student_age_df["part_age_raw"].map(set(['4']).issubset).astype(int)
student_age_df["part_age_5"]=student_age_df["part_age_raw"].map(set(['5']).issubset).astype(int)
student_age_df["part_age_6"]=student_age_df["part_age_raw"].map(set(['6']).issubset).astype(int)
student_age_df["part_age_7"]=student_age_df["part_age_raw"].map(set(['7']).issubset).astype(int)
student_age_df["part_age_8"]=student_age_df["part_age_raw"].map(set(['8']).issubset).astype(int)
student_age_df["part_age_9"]=student_age_df["part_age_raw"].map(set(['9']).issubset).astype(int)
student_age_df["part_age_10"]=student_age_df["part_age_raw"].map(set(['10']).issubset).astype(int)
student_age_df["part_age_11"]=student_age_df["part_age_raw"].map(set(['11']).issubset).astype(int)
student_age_df["part_age_12"]=student_age_df["part_age_raw"].map(set(['12']).issubset).astype(int)
student_age_df["part_age_13"]=student_age_df["part_age_raw"].map(set(['13']).issubset).astype(int)
student_age_df["part_age_14"]=student_age_df["part_age_raw"].map(set(['14']).issubset).astype(int)
student_age_df["part_age_15"]=student_age_df["part_age_raw"].map(set(['15']).issubset).astype(int)
student_age_df["part_age_16"]=student_age_df["part_age_raw"].map(set(['16']).issubset).astype(int)
student_age_df["part_age_17"]=student_age_df["part_age_raw"].map(set(['17']).issubset).astype(int)
student_age_df["part_age_18"]=student_age_df["part_age_raw"].map(set(['18']).issubset).astype(int)

student_age_df["part_age_no_information_provided"]=student_age_df["part_age_raw"].map(set(['No information provided']).issubset).astype(int) """

# Get Student Age highlighted text
student_age_HT            = highlighted_text(student_age_output)
student_age_HT_df         = pd.DataFrame(student_age_HT)
student_age_HT_df         = student_age_HT_df.T
student_age_HT_df.columns = ["part_age_ht"]

# Get Student Age user comments
student_age_Comments            = comments(student_age_output)
student_age_Comments_df         = pd.DataFrame(student_age_Comments)
student_age_Comments_df         = student_age_Comments_df.T
student_age_Comments_df.columns = ["part_age_info"]

# concatenate data frames
student_age = pd.concat([student_age_df, student_age_HT_df, student_age_Comments_df], axis=1, sort=False)

student_age.replace('\r',' ', regex=True, inplace=True)
student_age.replace('\n',' ', regex=True, inplace=True)
student_age.replace(':',' ',  regex=True, inplace=True)
student_age.replace(';',' ',  regex=True, inplace=True)

student_age.fillna("NA", inplace=True)

student_age.to_csv("age.csv", index=False)
