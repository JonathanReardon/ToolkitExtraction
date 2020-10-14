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

# Get Intervention Delivery main data
InterventionDelivery             = get_data(intervention_delivery_output)
intervention_delivery_df         = pd.DataFrame(InterventionDelivery)
intervention_delivery_df         = intervention_delivery_df.T
intervention_delivery_df.columns = ["int_who_raw"]

# Binarize Intervention Delivery data
""" intervention_delivery_df["int_who_research_staff"]         = intervention_delivery_df["int_who_raw"].map(set(["Research staff"]).issubset).astype(int)
intervention_delivery_df["int_who_class_teachers"]         = intervention_delivery_df["int_who_raw"].map(set(["Class teachers"]).issubset).astype(int)
intervention_delivery_df["int_who_teaching_assistants"]    = intervention_delivery_df["int_who_raw"].map(set(["Teaching assistants"]).issubset).astype(int)
intervention_delivery_df["int_who_other_school_staff"]     = intervention_delivery_df["int_who_raw"].map(set(["Other school staff"]).issubset).astype(int)
intervention_delivery_df["int_who_external_teachers"]      = intervention_delivery_df["int_who_raw"].map(set(["External teachers"]).issubset).astype(int)
intervention_delivery_df["int_who_parents/carers"]         = intervention_delivery_df["int_who_raw"].map(set(["Parents/carers"]).issubset).astype(int)
intervention_delivery_df["int_who_lay_persons/volunteers"] = intervention_delivery_df["int_who_raw"].map(set(["Lay persons/volunteers"]).issubset).astype(int)
intervention_delivery_df["int_who_peers"]                  = intervention_delivery_df["int_who_raw"].map(set(["Peers"]).issubset).astype(int)
intervention_delivery_df["int_who_digital_technology"]     = intervention_delivery_df["int_who_raw"].map(set(["Digital technology"]).issubset).astype(int)
intervention_delivery_df["int_who_unclear/not specified"]  = intervention_delivery_df["int_who_raw"].map(set(["Unclear/not specified"]).issubset).astype(int) """

# Get Intervention Delivery highlighted text
InterventionDelivery_HT            = highlighted_text(intervention_delivery_output)
InterventionDelivery_HT_df         = pd.DataFrame(InterventionDelivery_HT)
InterventionDelivery_HT_df         = InterventionDelivery_HT_df.T
InterventionDelivery_HT_df.columns = ["int_who_ht"]

# Get Intervention Delivery user comments
InterventionDelivery_Comments            = comments(intervention_delivery_output)
InterventionDelivery_Comments_df         = pd.DataFrame(InterventionDelivery_Comments)
InterventionDelivery_Comments_df         = InterventionDelivery_Comments_df.T
InterventionDelivery_Comments_df.columns = ["int_who_info"]

# concatenate data frames
intervention_delivery_df = pd.concat([intervention_delivery_df, InterventionDelivery_HT_df, InterventionDelivery_Comments_df], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_delivery_df.replace('\r',' ', regex=True, inplace=True)
intervention_delivery_df.replace('\n',' ', regex=True, inplace=True)
intervention_delivery_df.replace(':',' ',  regex=True, inplace=True)
intervention_delivery_df.replace(';',' ',  regex=True, inplace=True)

intervention_delivery_df.fillna("NA", inplace=True)

# Save to file (.csv)
intervention_delivery_df.to_csv("InterventionDelivery.csv", index=False)