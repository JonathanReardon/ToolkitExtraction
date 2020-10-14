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

# Get Intervention Implementation Detail main data
InterventionDetail            = get_data(intervention_implementation_details)
InterventionDetail_df         = pd.DataFrame(InterventionDetail)
InterventionDetail_df         = InterventionDetail_df.T
InterventionDetail_df.columns = ["int_fidel_raw"]

# Binarize Intervention Implementation Detail data
""" InterventionDetail_df["int_fidel_qualitative"]                         = InterventionDetail_df["int_fidel_raw"].map(set(["Qualitative"]).issubset).astype(int)
InterventionDetail_df["int_fidel_quantitative"]                        = InterventionDetail_df["int_fidel_raw"].map(set(["Quantitative"]).issubset).astype(int)
InterventionDetail_df["int_fidel_no_implementation_details_provided."] = InterventionDetail_df["int_fidel_raw"].map(set(["No implementation details provided."]).issubset).astype(int) """

# Get Intervention Implementation Detail highlighted text
InterventionDetail_HT            = highlighted_text(intervention_implementation_details)
InterventionDetail_HT_df         = pd.DataFrame(InterventionDetail_HT)
InterventionDetail_HT_df         = InterventionDetail_HT_df.T
InterventionDetail_HT_df.columns = ["int_fidel_ht"]

# Get Intervention Implementation Detail user comments
InterventionDetail_Comments            = comments(intervention_implementation_details)
InterventionDetail_Comments_df         = pd.DataFrame(InterventionDetail_Comments)
InterventionDetail_Comments_df         = InterventionDetail_Comments_df.T
InterventionDetail_Comments_df.columns = ["int_fidel_info"]

# concatenate data frames
intervention_detail_df = pd.concat([InterventionDetail_df, InterventionDetail_HT_df, InterventionDetail_Comments_df], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_detail_df.replace('\r',' ', regex=True, inplace=True)
intervention_detail_df.replace('\n',' ', regex=True, inplace=True)
intervention_detail_df.replace(':',' ',  regex=True, inplace=True)
intervention_detail_df.replace(';',' ',  regex=True, inplace=True)

intervention_detail_df.fillna("NA", inplace=True)

# Save to file (.csv)
intervention_detail_df.to_csv("InterventionDetail.csv", index=False)