from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import study_design_output
import pandas as pd

# load json file
load_json()

# get study design data
studydesign = get_data(study_design_output)
studydesign_df = pd.DataFrame(studydesign)
studydesign_df = studydesign_df.T
studydesign_df.columns = ["int_desig_raw"]

# get study design highlighted text
studydesign_HT = highlighted_text(study_design_output)
studydesign_HT_df = pd.DataFrame(studydesign_HT)
studydesign_HT_df = studydesign_HT_df.T
studydesign_HT_df.columns = ["int_design_ht"]

# get study design user comments
studydesign_Comments = comments(study_design_output)
studydesign_Comments_df = pd.DataFrame(studydesign_Comments)
studydesign_Comments_df = studydesign_Comments_df.T
studydesign_Comments_df.columns = ["int_design_info"]

# concatenate data frames
study_design_df = pd.concat([
    studydesign_df, 
    studydesign_HT_df, 
    studydesign_Comments_df
], axis=1, sort=False)

# fill blanks with NA
study_design_df.fillna("NA", inplace=True)

# save to disk
""" study_design_df.to_csv("studydesign.csv", index=False) """