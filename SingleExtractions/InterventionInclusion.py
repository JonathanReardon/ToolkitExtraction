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

###########################################
# DIGITAL TECHNOLOGY INTERVENTION INCLUSION
###########################################

# Get Digital Technology (inclusion) main data
DigitalTechnology            = get_data(intervention_approach_digital_technology)
DigitalTechnology_df         = pd.DataFrame(DigitalTechnology)
DigitalTechnology_df         = DigitalTechnology_df.T
DigitalTechnology_df.columns = ["digit_tech_raw"]

# Binarize Digital Technology (inclusion) data
""" DigitalTechnology_df["digit_tech_yes"] = DigitalTechnology_df["digit_tech_raw"].map(set(["Yes"]).issubset).astype(int)
DigitalTechnology_df["digit_tech_no"]  = DigitalTechnology_df["digit_tech_raw"].map(set(["No"]).issubset).astype(int) """


# Get Digital Technology (inclusion) highlighted text
DigitalTechnology_HT            = highlighted_text(intervention_approach_digital_technology)
DigitalTechnology_HT_df         = pd.DataFrame(DigitalTechnology_HT)
DigitalTechnology_HT_df         = DigitalTechnology_HT_df.T
DigitalTechnology_HT_df.columns = ["digit_tech_ht"]

# Get Digital Technology (inclusion) user comments
DigitalTechnology_Comments            = comments(intervention_approach_digital_technology)
DigitalTechnology_Comments_df         = pd.DataFrame(DigitalTechnology_Comments)
DigitalTechnology_Comments_df         = DigitalTechnology_Comments_df.T
DigitalTechnology_Comments_df.columns = ["digit_tech_info"]

###########################################
# PARENTS OR COMMUNITY VOLUNTEERS INCLUSION
###########################################

# Get Parents/Community volunteers (inclusion) main data
Parents_or_Community_Volunteers            = get_data(intervention_approach_parents_or_community_volunteers)
Parents_or_Community_Volunteers_df         = pd.DataFrame(Parents_or_Community_Volunteers)
Parents_or_Community_Volunteers_df         = Parents_or_Community_Volunteers_df.T
Parents_or_Community_Volunteers_df.columns = ["parent_partic_raw"]

# Binarize Parents/Community volunteers (inclusion) data
""" Parents_or_Community_Volunteers_df["parent_partic_yes"] = Parents_or_Community_Volunteers_df["parent_partic_raw"].map(set(["Yes"]).issubset).astype(int)
Parents_or_Community_Volunteers_df["parent_partic_no"]  = Parents_or_Community_Volunteers_df["parent_partic_raw"].map(set(["No"]).issubset).astype(int) """

# Get Parents/Community volunteers (inclusion) highlighted text
Parents_or_Community_Volunteers_HT            = highlighted_text(intervention_approach_digital_technology)
Parents_or_Community_Volunteers_HT_df         = pd.DataFrame(Parents_or_Community_Volunteers_HT)
Parents_or_Community_Volunteers_HT_df         = Parents_or_Community_Volunteers_HT_df.T
Parents_or_Community_Volunteers_HT_df.columns = ["parent_partic_ht"]

# Get Parents/Community volunteers (inclusion) user comments
Parents_or_Community_Volunteers                     = comments(intervention_approach_digital_technology)
Parents_or_Community_Volunteers_comments_df         = pd.DataFrame(Parents_or_Community_Volunteers)
Parents_or_Community_Volunteers_comments_df         = Parents_or_Community_Volunteers_comments_df.T
Parents_or_Community_Volunteers_comments_df.columns = ["parent_partic_info"]

# concatenate data frames
intervention_inclusion_df = pd.concat([DigitalTechnology_df, DigitalTechnology_HT_df, DigitalTechnology_Comments_df,
                                       Parents_or_Community_Volunteers_df, Parents_or_Community_Volunteers_HT_df, Parents_or_Community_Volunteers_comments_df], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_inclusion_df.replace('\r',' ', regex=True, inplace=True)
intervention_inclusion_df.replace('\n',' ', regex=True, inplace=True)
intervention_inclusion_df.replace(':',' ',  regex=True, inplace=True)
intervention_inclusion_df.replace(';',' ',  regex=True, inplace=True)

intervention_inclusion_df.fillna("NA", inplace=True)

# Save to file (.csv)
intervention_inclusion_df.to_csv("InterventionInclusion.csv", index=False)