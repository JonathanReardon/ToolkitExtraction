from Main import load_json, highlighted_text, comments
from AttributeIDList import gender_split_output
import pandas as pd

load_json()
 
# get gender split data
gender_split = comments(gender_split_output)
gender_split_df = pd.DataFrame(gender_split)
gender_split_df = gender_split_df.T
gender_split_df.columns = ["Gender_Split_comments"]

# get gender split highlighted text
gender_split_comments = highlighted_text(gender_split_output)
gender_split_comments_df = pd.DataFrame(gender_split_comments)
gender_split_comments_df = gender_split_comments_df.T
gender_split_comments_df.columns = ["Gender_Split_HT"]

# concatenate all dataframes
gender_split_df = pd.concat([gender_split_df, gender_split_comments_df], axis=1, sort=False)

# remove problematic text
gender_split_df.replace('\r',' ', regex=True, inplace=True)
gender_split_df.replace('\n',' ', regex=True, inplace=True)

# fill blanks with NA
gender_split_df.fillna("NA", inplace=True)

# save to disk
#gender_split_df.to_csv("gender_split.csv", index=False)

""" print(gender_split_df) """
