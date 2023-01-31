from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import participant_assignment_CEDIL
import pandas as pd

# load json file
load_json()

# get participant assignment data
participantassignment = get_data(participant_assignment_CEDIL)
participantassignment_df = pd.DataFrame(participantassignment)
participantassignment_df = participantassignment_df.T
participantassignment_df.columns = ["part_assig_raw"]

# remove square brackets
participantassignment_df['part_assig_raw'] = participantassignment_df['part_assig_raw'].str[0]

# Gget level of assignment highlighted text
participantassignment_HT = highlighted_text(participant_assignment_CEDIL)
participantassignment_HT_df = pd.DataFrame(participantassignment_HT)
participantassignment_HT_df = participantassignment_HT_df.T
participantassignment_HT_df.columns = ["part_assig_ht"]

# get level of assignment user comments
participantassignment_Comments = comments(participant_assignment_CEDIL)
participantassignment_Comments_df = pd.DataFrame(participantassignment_Comments)
participantassignment_Comments_df = participantassignment_Comments_df.T
participantassignment_Comments_df.columns = ["part_assig_info"]

# concatenate data frames
participant_assignment_df = pd.concat([
    participantassignment_df, 
    participantassignment_HT_df, 
    participantassignment_Comments_df
], axis=1, sort=False)

# fill blanks with NA
participant_assignment_df.fillna("NA", inplace=True)

# remove problematic text
participant_assignment_df.replace('\r', ' ', regex=True, inplace=True)
participant_assignment_df.replace('\n', ' ', regex=True, inplace=True)
participant_assignment_df.replace(':', ' ',  regex=True, inplace=True)
participant_assignment_df.replace(';', ' ',  regex=True, inplace=True)

# save to disk
""" participant_assignment_df.to_csv("participantassignment.csv", index=False) """

print(participant_assignment_df)