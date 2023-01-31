from Main import load_json, get_outcome_lvl1
import pandas as pd

# load json file
load_json()

# get outcome comparison data
out_comp = get_outcome_lvl1("ControlText")
out_comp_df = pd.DataFrame(out_comp)

# name each column (number depends on outcome number)
out_comp_df.columns = [
    "out_comp_" +'{}'.format(column+1) for column in out_comp_df.columns]

# fill blanks with NA
out_comp_df.fillna("NA", inplace=True)

# save to disk
""" out_comp_df.to_csv("out_compe.csv", index=False) """