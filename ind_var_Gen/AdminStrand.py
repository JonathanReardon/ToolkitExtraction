from Main import load_json, get_data, comments
from AttributeIDList import admin_strand_output
import pandas as pd
from IPython.display import display

load_json()

# get admin strand data
admin_strand = get_data(admin_strand_output)
adminstrand_df = pd.DataFrame(admin_strand)
adminstrand_df = adminstrand_df.T
adminstrand_df.columns = ["strand_raw"]

# Get Strand comment data
admin_strand_comments = comments(admin_strand_output)
admin_strand_comments_df = pd.DataFrame(admin_strand_comments)
admin_strand_comments_df = admin_strand_comments_df.T
admin_strand_comments_df.columns = ["strand_info"]

# concatenate data frames
admin_strand_df = pd.concat([
    adminstrand_df, 
    admin_strand_comments_df
], axis=1, sort=False)

# remove problematic text
admin_strand_df.replace('\r', ' ', regex=True, inplace=True)
admin_strand_df.replace('\n', ' ', regex=True, inplace=True)
admin_strand_df.replace(':', ' ',  regex=True, inplace=True)
admin_strand_df.replace(';', ' ',  regex=True, inplace=True)

# fill blanks with NA
admin_strand_df.fillna("NA", inplace=True)

""" # save to disk
admin_strand_df.to_csv("adminstrand.csv", index=False) """


