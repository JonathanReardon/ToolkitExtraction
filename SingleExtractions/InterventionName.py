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
Intervention_NameHT = highlighted_text(intervention_name_output)
Intervention_NameHT_df = pd.DataFrame(Intervention_NameHT)
Intervention_NameHT_df = Intervention_NameHT_df.T
Intervention_NameHT_df.columns=["int_name_ht"]

# Get Intervention Name user comments
Intervention_Name_Comments = comments(intervention_name_output)
Intervention_Name_Comments_df = pd.DataFrame(Intervention_Name_Comments)
Intervention_Name_Comments_df = Intervention_Name_Comments_df.T
Intervention_Name_Comments_df.columns=["int_name_info"]

intervention_name_df = pd.concat([Intervention_NameHT_df, Intervention_Name_Comments_df], axis=1, sort=False)

intervention_name_df.replace('\r',' ', regex=True, inplace=True)
intervention_name_df.replace('\n',' ', regex=True, inplace=True)
intervention_name_df.replace(':',' ', regex=True, inplace=True)
intervention_name_df.replace(';',' ', regex=True, inplace=True)

intervention_name_df.fillna("NA", inplace=True)

intervention_name_df.to_csv("InterventionName.csv", index=False)

print(intervention_name_df)


