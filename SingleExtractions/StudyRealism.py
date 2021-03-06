from Main import load_json, get_data, comments, highlighted_text
from CODES import study_realism_output
import pandas as pd

# load json file
load_json()

# get study realism data
studyrealism = get_data(study_realism_output)
studyrealism_df = pd.DataFrame(studyrealism)
studyrealism_df = studyrealism_df.T
studyrealism_df.columns = ["eco_valid_raw"]

# get study realism highlighted text
studyrealism_HT = highlighted_text(study_realism_output)
studyrealism_HT_df = pd.DataFrame(studyrealism_HT)
studyrealism_HT_df = studyrealism_HT_df.T
studyrealism_HT_df.columns = ["eco_valid_ht"]

# get study realism user comments
studyrealism_Comments = comments(study_realism_output)
studyrealism_Comments_df = pd.DataFrame(studyrealism_Comments)
studyrealism_Comments_df = studyrealism_Comments_df.T
studyrealism_Comments_df.columns = ["eco_valid_info"]

# concatenate data frames
study_realism_df = pd.concat([
    studyrealism_df, 
    studyrealism_HT_df, 
    studyrealism_Comments_df
], axis=1, sort=False)

# fill blanks with NA
study_realism_df.fillna("NA", inplace=True)

# remove square brackets [not for multiple input variables]
study_realism_df['eco_valid_raw'] = study_realism_df['eco_valid_raw'].str[0]

# save to disk
""" study_realism_df.to_csv("studyrealism.csv", index=False) """