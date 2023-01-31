from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import study_loc
from AttributeIDList import study_loc_type

import pandas as pd

# load json file
load_json()

# get location info highlighted text
loc_HT = highlighted_text(study_loc)
loc_HT_df = pd.DataFrame(loc_HT)
loc_HT_df = loc_HT_df.T
loc_HT_df.columns = ["loc_ht"]

# get location type further info highlighted text
loc_type_HT = highlighted_text(study_loc_type)
loc_type_HT_df = pd.DataFrame(loc_type_HT)
loc_type_HT_df = loc_type_HT_df.T
loc_type_HT_df.columns = ["loc_type_ht"]

# concatenate datafeames
loc_info = pd.concat([
    loc_HT_df,
    loc_type_HT_df,
], axis=1, sort=False)