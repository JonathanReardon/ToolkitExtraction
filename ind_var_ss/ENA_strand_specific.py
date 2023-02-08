from Main import load_json, get_data, highlighted_text

from AttributeIDList import ena_maths_included
from AttributeIDList import ena_prog_comp
from AttributeIDList import ena_prog_activities

import pandas as pd

load_json()

# EARLY NUMERACY APPROACHES

# maths included data
math_incl = get_data(ena_maths_included)
math_incl_df = pd.DataFrame(math_incl)
math_incl_df = math_incl_df.T
math_incl_df.columns = ["math_incl"]

# maths included highlighted text
math_incl_HT = highlighted_text(ena_maths_included)
math_incl_HT_df = pd.DataFrame(math_incl_HT)
math_incl_HT_df = math_incl_HT_df.T
math_incl_HT_df.columns = ["math_incl_ht"]

# how comprehensive was the data, data
prog_comp = get_data(ena_prog_comp)
prog_comp_df = pd.DataFrame(prog_comp)
prog_comp_df = prog_comp_df.T
prog_comp_df.columns = ["prog_comp"]

# how comprehensive activities, data
prog_act = get_data(ena_prog_activities)
prog_act_df = pd.DataFrame(prog_act)
prog_act_df = prog_act_df.T
prog_act_df.columns = ["prog_act"]

# concatenate data frames
ena_ss_df = pd.concat([
    math_incl_df,
    #math_incl_HT_df,
    prog_comp_df,
    prog_act_df,
], axis=1, sort=False)

# fill blanks with NA
ena_ss_df.fillna("NA", inplace=True)

# save to disk
# mentoring_ss_df.to_csv("mentoring_ss_df.csv", index=False)
