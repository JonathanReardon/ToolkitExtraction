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

# Get Intervention Organisation Type main data
InterventionOrgType=get_data(intervention_organisation_type_output)
InterventionOrgType_df=pd.DataFrame(InterventionOrgType)
InterventionOrgType_df=InterventionOrgType_df.T
InterventionOrgType_df.columns=["int_prov_raw"]

""" InterventionOrgType_df["int_prov_school_or_group_of_schools"]            =InterventionOrgType_df["int_prov_raw"].map(set(['School or group of schools']).issubset).astype(int)
InterventionOrgType_df["int_prov_charity or voluntary organisation"]     =InterventionOrgType_df["int_prov_raw"].map(set(['Charity or voluntary organisation']).issubset).astype(int)
InterventionOrgType_df["int_prov_uiversity_researcher_design"]           =InterventionOrgType_df["int_prov_raw"].map(set(['University/ researcher design']).issubset).astype(int)
InterventionOrgType_df["int_prov_local_education_authority_or_district"] =InterventionOrgType_df["int_prov_raw"].map(set(['Local education authority or district']).issubset).astype(int)
InterventionOrgType_df["int_prov_school_or_group_of_schools"]            =InterventionOrgType_df["int_prov_raw"].map(set(['School or group of schools']).issubset).astype(int)
InterventionOrgType_df["int_prov_other_(please_provide_details)"]        =InterventionOrgType_df["int_prov_raw"].map(set(['Other (please provide details)']).issubset).astype(int) """

# Get Intervention Organisation Type highlighted text
InterventionOrgType_HT = highlighted_text(intervention_organisation_type_output)
InterventionOrgType_HT_df = pd.DataFrame(InterventionOrgType_HT)
InterventionOrgType_HT_df = InterventionOrgType_HT_df.T
InterventionOrgType_HT_df.columns=["int_prov_ht"]

# Get Intervention Organisation Type user comments
InterventionOrgType_Comments = comments(intervention_organisation_type_output)
InterventionOrgType_Comments_df = pd.DataFrame(InterventionOrgType_Comments)
InterventionOrgType_Comments_df = InterventionOrgType_Comments_df.T
InterventionOrgType_Comments_df.columns=["int_prov_info"]

# concatenate data frames
intervention_org_type = pd.concat([InterventionOrgType_df, InterventionOrgType_HT_df, InterventionOrgType_Comments_df], axis=1, sort=False)

intervention_org_type.replace('\r',' ', regex=True, inplace=True)
intervention_org_type.replace('\n',' ', regex=True, inplace=True)
intervention_org_type.replace(':',' ', regex=True, inplace=True)
intervention_org_type.replace(';',' ', regex=True, inplace=True)

intervention_org_type.fillna("NA", inplace=True)

intervention_org_type.to_csv("InterventionOrgType.csv", index=False)