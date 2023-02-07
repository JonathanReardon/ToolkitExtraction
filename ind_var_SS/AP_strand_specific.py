from Main import load_json, get_data
from AttributeIDList import ap_focus_output
from AttributeIDList import ap_who_output
from AttributeIDList import ap_where_output
import pandas as pd

load_json()

# ARTS PARTICIPATION

# get focus data
ap_focus = get_data(ap_focus_output)
ap_focus_df = pd.DataFrame(ap_focus)
ap_focus_df = ap_focus_df.T
ap_focus_df.columns = ["ap_focus"]

# get who involved data
ap_who_invol = get_data(ap_who_output)
ap_who_invol_df = pd.DataFrame(ap_who_invol)
ap_who_invol_df = ap_who_invol_df.T
ap_who_invol_df.columns = ["ap_involved"]

# get where data
ap_where = get_data(ap_where_output)
ap_where_df = pd.DataFrame(ap_where)
ap_where_df = ap_where_df.T
ap_where_df.columns = ["ap_where"]

ap_ss_df = pd.concat([
    ap_focus_df,
    ap_who_invol_df,
    ap_where_df,
], axis=1, sort=False)

# fill blanks with NA
ap_ss_df.fillna("NA", inplace=True)

# save to disk
""" ap_ss_df.to_csv("arts_participation_ss.csv", index=False) """