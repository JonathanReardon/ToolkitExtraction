from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import student_age_output
import pandas as pd

load_json()

# get age data
student_age = get_data(student_age_output)
student_age_df = pd.DataFrame(student_age)
student_age_df = student_age_df.T
student_age_df.columns = ["part_age_raw"]

# get student age highlighted text
student_age_HT = highlighted_text(student_age_output)
student_age_HT_df = pd.DataFrame(student_age_HT)
student_age_HT_df = student_age_HT_df.T
student_age_HT_df.columns = ["part_age_ht"]

# get student age user comments
student_age_Comments = comments(student_age_output)
student_age_Comments_df = pd.DataFrame(student_age_Comments)
student_age_Comments_df = student_age_Comments_df.T
student_age_Comments_df.columns = ["part_age_info"]

# concatenate data frames
student_age = pd.concat([
    student_age_df, 
    student_age_HT_df, 
    student_age_Comments_df
], axis=1, sort=False)

# replace problematic text
student_age.replace('\r', ' ', regex=True, inplace=True)
student_age.replace('\n', ' ', regex=True, inplace=True)
student_age.replace(':', ' ',  regex=True, inplace=True)
student_age.replace(';', ' ',  regex=True, inplace=True)

# fill blanks with NA
student_age.fillna("NA", inplace=True)

# save to disk
#student_age.to_csv("age.csv", index=False)

""" print(student_age) """
