from Main import get_data, highlighted_text, comments
from AttributeIDList import student_age_output
import pandas as pd

# get age data
student_age = get_data(student_age_output)
student_age_df = pd.DataFrame(student_age)
student_age_df = student_age_df.T
student_age_df.columns = ["part_age_raw"]

""" student_age_df["part_age_3"]=student_age_df["part_age_raw"].map(set(['3']).issubset).astype(int)
student_age_df["part_age_4"]=student_age_df["part_age_raw"].map(set(['4']).issubset).astype(int)
student_age_df["part_age_5"]=student_age_df["part_age_raw"].map(set(['5']).issubset).astype(int)
student_age_df["part_age_6"]=student_age_df["part_age_raw"].map(set(['6']).issubset).astype(int)
student_age_df["part_age_7"]=student_age_df["part_age_raw"].map(set(['7']).issubset).astype(int)
student_age_df["part_age_8"]=student_age_df["part_age_raw"].map(set(['8']).issubset).astype(int)
student_age_df["part_age_9"]=student_age_df["part_age_raw"].map(set(['9']).issubset).astype(int)
student_age_df["part_age_10"]=student_age_df["part_age_raw"].map(set(['10']).issubset).astype(int)
student_age_df["part_age_11"]=student_age_df["part_age_raw"].map(set(['11']).issubset).astype(int)
student_age_df["part_age_12"]=student_age_df["part_age_raw"].map(set(['12']).issubset).astype(int)
student_age_df["part_age_13"]=student_age_df["part_age_raw"].map(set(['13']).issubset).astype(int)
student_age_df["part_age_14"]=student_age_df["part_age_raw"].map(set(['14']).issubset).astype(int)
student_age_df["part_age_15"]=student_age_df["part_age_raw"].map(set(['15']).issubset).astype(int)
student_age_df["part_age_16"]=student_age_df["part_age_raw"].map(set(['16']).issubset).astype(int)
student_age_df["part_age_17"]=student_age_df["part_age_raw"].map(set(['17']).issubset).astype(int)
student_age_df["part_age_18"]=student_age_df["part_age_raw"].map(set(['18']).issubset).astype(int)

student_age_df["part_age_no_information_provided"]=student_age_df["part_age_raw"].map(set(['No information provided']).issubset).astype(int) """

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
student_age.to_csv("age.csv", index=False)
