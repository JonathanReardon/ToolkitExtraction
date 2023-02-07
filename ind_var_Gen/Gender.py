from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import student_gender
import pandas as pd

load_json()

# get gender data
gender = get_data(student_gender)
gender_df = pd.DataFrame(gender)
gender_df = gender_df.T
gender_df.columns=["part_gen_raw"]

# Get Gender highlighted text
gender_HT = highlighted_text(student_gender)
gender_HT_df = pd.DataFrame(gender_HT)
gender_HT_df = gender_HT_df.T
gender_HT_df.columns = ["part_gen_ht"]

# Get Gender user comments
gender_Comments = comments(student_gender)
gender_Comments_df = pd.DataFrame(gender_Comments)
gender_Comments_df = gender_Comments_df.T
gender_Comments_df.columns = ["part_gen_info"]

# concatenate data frames
gender_df = pd.concat([gender_df, gender_HT_df, gender_Comments_df], axis=1, sort=False)

# fill blanks with NA
gender_df.fillna("NA", inplace=True)

# save to disk
#gender_df.to_csv("gender.csv", index=False)