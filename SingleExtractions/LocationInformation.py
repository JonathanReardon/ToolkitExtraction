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

""" # Get More Location Information highlighted text
more_location_info_HT            = highlighted_text(more_location_info)
more_location_info_HT_df         = pd.DataFrame(more_location_info_HT)
more_location_info_HT_df         = more_location_info_HT_df.T
more_location_info_HT_df.columns = ["More_Location_information_HT"]

# Get More Location Information comments
more_location_info_Comments            = comments(more_location_info)
more_location_info_Comments_df         = pd.DataFrame(more_location_info_Comments)
more_location_info_Comments_df         = more_location_info_Comments_df.T
more_location_info_Comments_df.columns = ["More_Location_Information_comments"] """

# Get Location Specific Information highlighted text
location_specific_info_HT            = highlighted_text(specific_to_location)
location_specific_info_HT_df         = pd.DataFrame(location_specific_info_HT)
location_specific_info_HT_df         = location_specific_info_HT_df.T
location_specific_info_HT_df.columns = ["loc_spec_ht"]

# Get Location Specific Information comments
location_specific_info_Comments            = comments(specific_to_location)
location_specific_info_Comments_df         = pd.DataFrame(location_specific_info_Comments)
location_specific_info_Comments_df         = location_specific_info_Comments_df.T
location_specific_info_Comments_df.columns = ["loc_spec_info"]

# Get Type of Location highlighted text
type_of_location_info_HT            = highlighted_text(type_of_location)
type_of_location_info_HT_df         = pd.DataFrame(type_of_location_info_HT)
type_of_location_info_HT_df         = type_of_location_info_HT_df.T
type_of_location_info_HT_df.columns = ["loc_type_ht"]

# Get Type of Location  comments
type_of_location_info_Comments            = comments(type_of_location)
type_of_location_info_Comments_df         = pd.DataFrame(type_of_location_info_Comments)
type_of_location_info_Comments_df         = type_of_location_info_Comments_df.T
type_of_location_info_Comments_df.columns = ["loc_type_info"]

# Get No Location Information highlighted text
no_location_info_HT            = highlighted_text(no_location_info)
no_location_info_HT_df         = pd.DataFrame(no_location_info_HT)
no_location_info_HT_df         = no_location_info_HT_df.T
no_location_info_HT_df.columns = ["loc_na_ht"]

# Get No Location Information comments
no_location_info_Comments            = comments(type_of_location)
no_location_info_Comments_df         = pd.DataFrame(no_location_info_Comments)
no_location_info_Comments_df         = no_location_info_Comments_df.T
no_location_info_Comments_df.columns = ["loc_na_info"]


# concatenate data frames
location_info_df = pd.concat([location_specific_info_HT_df, location_specific_info_Comments_df,
                              type_of_location_info_HT_df, type_of_location_info_Comments_df,
                              no_location_info_HT_df, no_location_info_Comments_df], axis=1, sort=False)

location_info_df.fillna("NA", inplace=True)

location_info_df.to_csv("location_information.csv", index=False)