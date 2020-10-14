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

levelofassignment = get_data(level_of_assignment_output)

levelofassignment_df = pd.DataFrame(levelofassignment)
levelofassignment_df = levelofassignment_df.T
levelofassignment_df.columns=["level_assig_raw"]

# remove square brackets
levelofassignment_df['level_assig_raw'] = levelofassignment_df['level_assig_raw'].str[0]

# convert each variable to binary
""" levelofassignment_df["level_assig_individual"]                 = levelofassignment_df['level_assig_raw'].isin(["Individual"]).astype(int)
levelofassignment_df["level_assig_class"]                      = levelofassignment_df['level_assig_raw'].isin(["Class"]).astype(int)
levelofassignment_df["level_assig_school_cluster"]             = levelofassignment_df['level_assig_raw'].isin(['School - cluster']).astype(int)
levelofassignment_df["level_assig_school_multi_site"]          = levelofassignment_df['level_assig_raw'].isin(['School - multi-site']).astype(int)
levelofassignment_df["level_assig_region_or_district"]         = levelofassignment_df['level_assig_raw'].isin(['Region or district']).astype(int)
levelofassignment_df["level_assig_not_provided_not_available"] = levelofassignment_df['level_assig_raw'].isin(['Not provided/ not available']).astype(int) """

# Get Level of Assignment highlighted text
levelofassignment_HT                  = highlighted_text(level_of_assignment_output)
level_of_assignment_output_df         = pd.DataFrame(levelofassignment_HT)
level_of_assignment_output_df         = level_of_assignment_output_df.T
level_of_assignment_output_df.columns = ["level_assig_ht"]

# Get Level of Assignment user comments
levelofassignment_Comments            = comments(level_of_assignment_output)
levelofassignment_Comments_df         = pd.DataFrame(levelofassignment_Comments)
levelofassignment_Comments_df         = levelofassignment_Comments_df.T
levelofassignment_Comments_df.columns = ["level_assig_info"]

# concatenate data frames
level_of_assignment_df = pd.concat([levelofassignment_df, level_of_assignment_output_df, levelofassignment_Comments_df], axis=1, sort=False)

level_of_assignment_df.fillna("NA", inplace=True)

print(level_of_assignment_df)

level_of_assignment_df.to_csv("levelofassignment.csv", index=False)