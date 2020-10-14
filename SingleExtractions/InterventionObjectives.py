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

# Get Intervention Name highlighted text
Intervention_ObjectivesHT = highlighted_text(intervention_objectives_output)
Intervention_ObjectivesHT_df = pd.DataFrame(Intervention_ObjectivesHT)
Intervention_ObjectivesHT_df = Intervention_ObjectivesHT_df.T
Intervention_ObjectivesHT_df.columns=["int_objec_ht"]

# Get Intervention Description user comments
Intervention_Objectives_Comments = comments(intervention_objectives_output)
Intervention_Objectives_Comments_df = pd.DataFrame(Intervention_Objectives_Comments)
Intervention_Objectives_Comments_df = Intervention_Objectives_Comments_df.T
Intervention_Objectives_Comments_df.columns=["int_objec_info"]

intervention_objectives_df = pd.concat([Intervention_ObjectivesHT_df, Intervention_Objectives_Comments_df], axis=1, sort=False)

intervention_objectives_df.replace('\r',' ', regex=True, inplace=True)
intervention_objectives_df.replace('\n',' ', regex=True, inplace=True)
intervention_objectives_df.replace(':',' ', regex=True, inplace=True)
intervention_objectives_df.replace(';',' ', regex=True, inplace=True)

intervention_objectives_df.fillna("NA", inplace=True)

intervention_objectives_df.to_csv("InterventionObjectives.csv", index=False)

print(intervention_objectives_df)