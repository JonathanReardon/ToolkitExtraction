from Main import load_json, get_outcome_lvl2, comments
from AttributeIDList import toolkit_strand_codes
import pandas as pd

# load json file
load_json()

# get toolkit strand data
toolkitstrand = get_outcome_lvl2(toolkit_strand_codes)
toolkitstrand_df = pd.DataFrame(toolkitstrand)

# get toolkit strand comments
toolkitstrand_Comments = comments(toolkit_strand_codes)
toolkitstrand_Comments_df = pd.DataFrame(toolkitstrand_Comments)
toolkitstrand_Comments_df = toolkitstrand_Comments_df.T
toolkitstrand_Comments_df.columns = ["_info"]

# fill blanks with NA
toolkitstrand_df.fillna("NA", inplace=True)

# name each column (number depends on outcome number)
toolkitstrand_df.columns = [
    "out_strand_"+'{}'.format(column+1) for column in toolkitstrand_df.columns]

# save to disk
""" toolkitstrand_df.to_csv("toolkitstrand.csv", index=False) """

""" print(toolkitstrand_df) """
