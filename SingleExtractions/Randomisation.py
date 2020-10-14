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

randomisation = get_data(randomisation_details)

randomisation_df = pd.DataFrame(randomisation)
randomisation_df = randomisation_df.T
randomisation_df.columns=["rand_raw"]

""" randomisation_df["rand_randomisation_yes"]            = randomisation_df["rand_raw"].map(set(['Yes']).issubset).astype(int)
randomisation_df["rand_randomisation_not_applicable"] = randomisation_df["rand_raw"].map(set(['Not applicable']).issubset).astype(int)
randomisation_df["rand_randomisation_no_unclear"]     = randomisation_df["rand_raw"].map(set(['No/Unclear']).issubset).astype(int) """

# Get Randomisation highlighted text
randomisation_HT                 = highlighted_text(randomisation_details)
randomisation_details_df         = pd.DataFrame(randomisation_HT)
randomisation_details_df         = randomisation_details_df.T
randomisation_details_df.columns = ["rand_ht"]

# Get Randomisation user comments
randomisation_Comments            = comments(randomisation_details)
randomisation_Comments_df         = pd.DataFrame(randomisation_Comments)
randomisation_Comments_df         = randomisation_Comments_df.T
randomisation_Comments_df.columns = ["rand_info"]

# concatenate data frames
randomisation_df = pd.concat([randomisation_df, randomisation_details_df, randomisation_Comments_df], axis=1, sort=False)

randomisation_df.fillna("NA", inplace=True)

print(randomisation_df)

randomisation_df.to_csv("randomisation.csv", index=False)