import os
import json
import pandas as pd

from CODES import *
from DATAFILE import file

##############################################
# World Bank economy listing by country
# https://datahelpdesk.worldbank.org/knowledgebase/articles/906519-world-bank-country-and-lending-groups

low_income = ["Afghanistan",  "Guinea-Bissau", "Sierra Leone",
              "Burkina Faso", "Haiti", "Somalia",
              "Burundi", "Korea, Dem. People's Rep.", "South Sudan",
              "Central African Republic", "Liberia", "Sudan",
              "Chad", "Madagascar", "Syrian Arab Republic",
              "Congo, Dem. Rep", "Malawi", "Tajikistan",
              "Eritrea", "Mali", "Togo"
              "Ethiopia", "Mozambique", "Uganda"
              "Gambia, The","Niger", "Yemen, Rep.",
              "Guinea", "Rwanda"]

##############################################

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

country = get_data(countries)

country_df = pd.DataFrame(country)
country_df = country_df.T
country_df.columns=["loc_country_raw"]

# Get Country highlighted text
country_HT            = highlighted_text(countries)
country_HT_df         = pd.DataFrame(country_HT)
country_HT_df         = country_HT_df.T
country_HT_df.columns = ["loc_country_ht"]

# Get Country user comments
country_Comments            = comments(countries)
country_Comments_df         = pd.DataFrame(country_Comments)
country_Comments_df         = country_Comments_df.T
country_Comments_df.columns = ["loc_country_info"]

# concatenate data frames
country_df = pd.concat([country_df, country_HT_df, country_Comments_df], axis=1, sort=False)

country_df.fillna("NA", inplace=True)

print(country_df)

country_df.to_csv("Country.csv", index=False)