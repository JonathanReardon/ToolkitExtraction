from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import source_output
from AttributeIDList import source_EEF_Report_options
import pandas as pd

# load json file
load_json()

# get source raw data
source = get_data(source_output)
source_df = pd.DataFrame(source)
source_df = source_df.T
source_df.columns = ["source_raw"]

# get source EED options (nested) data
eef_options = get_data(source_EEF_Report_options)
eef_options_df = pd.DataFrame(eef_options)
eef_options_df = eef_options_df.T
eef_options_df.columns = ["source_eef_reports"]

# concatenate data frames
source_all_df = pd.concat([
    source_df,
    eef_options_df,
], axis=1, sort=False)

# fill blanks with NA
source_all_df.fillna("NA", inplace=True)

""" print(source_all_df) """

# save to disk
""" source_all_df.to_csv("source.csv", index=False) """