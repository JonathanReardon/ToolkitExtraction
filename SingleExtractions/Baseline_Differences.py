from Main import get_data, highlighted_text, comments
from AttributeIDList import baseline_differences_output
import pandas as pd

# extract baseline differences data
baselinedifferences = get_data(baseline_differences_output)
baselinedifferences_df = pd.DataFrame(baselinedifferences)
baselinedifferences_df = baselinedifferences_df.T
baselinedifferences_df.columns=["base_diff_raw"]

# Get Baseline Differences highlighted text
baselinedifferences_HT = highlighted_text(baseline_differences_output)
baselinedifferences_HT_df = pd.DataFrame(baselinedifferences_HT)
baselinedifferences_HT_df = baselinedifferences_HT_df.T
baselinedifferences_HT_df.columns = ["base_diff_ht"]

# Get Educational Setting user comments
baselinedifferences_Comments = comments(baseline_differences_output)
baselinedifferences_Comments_df = pd.DataFrame(baselinedifferences_Comments)
baselinedifferences_Comments_df = baselinedifferences_Comments_df.T
baselinedifferences_Comments_df.columns = ["base_diff_info"]

# concatenate data frames
baseline_differences_df = pd.concat([
    baselinedifferences_df, 
    baselinedifferences_HT_df, 
    baselinedifferences_Comments_df
], axis=1, sort=False)

# fill blanks with NA
baseline_differences_df.fillna("NA", inplace=True)

# save to disk
baseline_differences_df.to_csv("baselinedifferences.csv", index=False)