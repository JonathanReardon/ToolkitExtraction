from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import level_of_assignment_CEDIL
import pandas as pd

# load json file
load_json()

# get level of assignment data
levelofassignment = get_data(level_of_assignment_CEDIL)
levelofassignment_df = pd.DataFrame(levelofassignment)
levelofassignment_df = levelofassignment_df.T
levelofassignment_df.columns=["level_assig_raw"]

# remove square brackets
levelofassignment_df['level_assig_raw'] = levelofassignment_df['level_assig_raw'].str[0]

# Get Level of Assignment highlighted text
levelofassignment_HT = highlighted_text(level_of_assignment_CEDIL)
level_of_assignment_output_df = pd.DataFrame(levelofassignment_HT)
level_of_assignment_output_df = level_of_assignment_output_df.T
level_of_assignment_output_df.columns = ["level_assig_ht"]

# Get Level of Assignment user comments
levelofassignment_Comments = comments(level_of_assignment_CEDIL)
levelofassignment_Comments_df = pd.DataFrame(levelofassignment_Comments)
levelofassignment_Comments_df = levelofassignment_Comments_df.T
levelofassignment_Comments_df.columns = ["level_assig_info"]

# concatenate data frames
level_of_assignment_df = pd.concat([
    levelofassignment_df, 
    level_of_assignment_output_df, 
    levelofassignment_Comments_df
], axis=1, sort=False)

# fill blanks with NA
level_of_assignment_df.fillna("NA", inplace=True)

# save to disk
""" level_of_assignment_df.to_csv("levelofassignment.csv", index=False) """

print(level_of_assignment_df)