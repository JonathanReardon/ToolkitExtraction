from Main import load_json, get_data, highlighted_text

from AttributeIDList import ela_literacy_activities
from AttributeIDList import ela_comprehensive
from AttributeIDList import ela_prog_desc

import pandas as pd

load_json()

# EARLY LITERACY APPROACHES

# literacy acticivities data
lit_act = get_data(ela_literacy_activities)
lit_act_df = pd.DataFrame(lit_act)
lit_act_df = lit_act_df.T
lit_act_df.columns = ["lit_activities"]

# literacy activities highlighted text
lit_act_HT = highlighted_text(ela_literacy_activities)
lit_act_HT_df = pd.DataFrame(lit_act_HT)
lit_act_HT_df = lit_act_HT_df.T
lit_act_HT_df.columns = ["lit_activities_HT"]

# comprehensive prog data
prog_comp = get_data(ela_comprehensive)
prog_comp_df = pd.DataFrame(prog_comp)
prog_comp_df = prog_comp_df.T
prog_comp_df.columns = ["prog_comp"]

# comprehensive prog highlighted text
prog_comp_HT = highlighted_text(ela_comprehensive)
prog_comp_HT_df = pd.DataFrame(prog_comp_HT)
prog_comp_HT_df = prog_comp_HT_df.T
prog_comp_HT_df.columns = ["prog_comp_HT"]

# comprehensive prog data
prog_desc = get_data(ela_prog_desc)
prog_desc_df = pd.DataFrame(prog_desc)
prog_desc_df = prog_desc_df.T
prog_desc_df.columns = ["prog_desc"]

# comprehensive prog highlighted text
prog_desc_HT = highlighted_text(ela_prog_desc)
prog_desc_HT_df = pd.DataFrame(prog_desc_HT)
prog_desc_HT_df = prog_desc_HT_df.T
prog_desc_HT_df.columns = ["prog_desc_HT"]


# concatenate data frames
ela_ss_df = pd.concat([
    lit_act_df,
    #lit_act_HT_df,
    prog_comp_df,
    #prog_comp_HT_df,
    prog_desc_df,
    #prog_desc_HT_df,
], axis=1, sort=False)