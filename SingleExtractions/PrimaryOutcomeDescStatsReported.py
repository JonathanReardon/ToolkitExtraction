from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import desc_stats_primary_outcome
import pandas as pd

# load json file
load_json()

###########################
# PRIMARY OUTCOME REPORTED
###########################

# Get Descriptive Stats (Primary Outcome) Reported main data
DescStatsPrimaryOutcomeReported = get_data(desc_stats_primary_outcome)
DescStatsPrimaryOutcomeReported_df = pd.DataFrame(DescStatsPrimaryOutcomeReported)
DescStatsPrimaryOutcomeReported_df = DescStatsPrimaryOutcomeReported_df.T
DescStatsPrimaryOutcomeReported_df.columns = ["desc_stats_raw"]

# Get Descriptive Stats (Primary Outcome) Reported highlighted text
DescStatsPrimaryOutcomeReported_HT = highlighted_text(desc_stats_primary_outcome)
DescStatsPrimaryOutcomeReported_HT_df = pd.DataFrame(DescStatsPrimaryOutcomeReported_HT)
DescStatsPrimaryOutcomeReported_HT_df = DescStatsPrimaryOutcomeReported_HT_df.T
DescStatsPrimaryOutcomeReported_HT_df.columns = ["desc_stats_ht"]

# Get Descriptive Stats (Primary Outcome) Reported user comments
DescStatsPrimaryOutcomeReported_Comments = comments(desc_stats_primary_outcome)
DescStatsPrimaryOutcomeReported_Comments_df = pd.DataFrame(DescStatsPrimaryOutcomeReported_Comments)
DescStatsPrimaryOutcomeReported_Comments_df = DescStatsPrimaryOutcomeReported_Comments_df.T
DescStatsPrimaryOutcomeReported_Comments_df.columns = ["desc_stats_info"]

# concatenate data frames
DescStatsOutcomeReported_df = pd.concat([
    DescStatsPrimaryOutcomeReported_df, 
    DescStatsPrimaryOutcomeReported_HT_df, 
    DescStatsPrimaryOutcomeReported_Comments_df
], axis=1, sort=False)

# fill blanks with NA
DescStatsOutcomeReported_df.fillna("NA", inplace=True)

# save to disk
""" DescStatsOutcomeReported_df.to_csv("DescStatsReported.csv", index=False) """