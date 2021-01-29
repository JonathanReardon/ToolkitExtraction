from Main import load_json, comments, highlighted_text
from AttributeIDList import specific_to_location
from AttributeIDList import type_of_location
from AttributeIDList import no_location_info
import pandas as pd

# load json file
load_json()

""" # Get More Location Information highlighted text
more_location_info_HT = highlighted_text(more_location_info)
more_location_info_HT_df = pd.DataFrame(more_location_info_HT)
more_location_info_HT_df = more_location_info_HT_df.T
more_location_info_HT_df.columns = ["More_Location_information_HT"]

# Get More Location Information comments
more_location_info_Comments = comments(more_location_info)
more_location_info_Comments_df = pd.DataFrame(more_location_info_Comments)
more_location_info_Comments_df = more_location_info_Comments_df.T
more_location_info_Comments_df.columns = ["More_Location_Information_comments"] """

# Get Location Specific Information highlighted text
location_specific_info_HT = highlighted_text(specific_to_location)
location_specific_info_HT_df = pd.DataFrame(location_specific_info_HT)
location_specific_info_HT_df = location_specific_info_HT_df.T
location_specific_info_HT_df.columns = ["loc_spec_ht"]

# Get Location Specific Information comments
location_specific_info_Comments = comments(specific_to_location)
location_specific_info_Comments_df = pd.DataFrame(location_specific_info_Comments)
location_specific_info_Comments_df = location_specific_info_Comments_df.T
location_specific_info_Comments_df.columns = ["loc_spec_info"]

# Get Type of Location highlighted text
type_of_location_info_HT = highlighted_text(type_of_location)
type_of_location_info_HT_df = pd.DataFrame(type_of_location_info_HT)
type_of_location_info_HT_df = type_of_location_info_HT_df.T
type_of_location_info_HT_df.columns = ["loc_type_ht"]

# Get Type of Location  comments
type_of_location_info_Comments = comments(type_of_location)
type_of_location_info_Comments_df = pd.DataFrame(type_of_location_info_Comments)
type_of_location_info_Comments_df = type_of_location_info_Comments_df.T
type_of_location_info_Comments_df.columns = ["loc_type_info"]

# Get No Location Information highlighted text
no_location_info_HT = highlighted_text(no_location_info)
no_location_info_HT_df = pd.DataFrame(no_location_info_HT)
no_location_info_HT_df = no_location_info_HT_df.T
no_location_info_HT_df.columns = ["loc_na_ht"]

# Get No Location Information comments
no_location_info_Comments = comments(type_of_location)
no_location_info_Comments_df = pd.DataFrame(no_location_info_Comments)
no_location_info_Comments_df = no_location_info_Comments_df.T
no_location_info_Comments_df.columns = ["loc_na_info"]

# concatenate data frames
location_info_df = pd.concat([
    location_specific_info_HT_df, 
    location_specific_info_Comments_df,
    type_of_location_info_HT_df, 
    type_of_location_info_Comments_df,
    no_location_info_HT_df, 
    no_location_info_Comments_df
], axis=1, sort=False)

# fill blanks with NA
location_info_df.fillna("NA", inplace=True)

# savce to disk
""" location_info_df.to_csv("further_location_information.csv", index=False) """