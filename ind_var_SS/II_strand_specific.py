from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import ii_approach_output
from AttributeIDList import ii_also_included_output
from AttributeIDList import ii_also_mentioned_output

import pandas as pd

load_json()

# INDIVIDUALISED INSTRUCTION

# get approach data
ii_approach = get_data(ii_approach_output)
ii_approach_df = pd.DataFrame(ii_approach)
ii_approach_df = ii_approach_df.T
ii_approach_df.columns = ["ii_approach"]

# get also included data
ii_also_included = get_data(ii_also_included_output)
ii_also_included_df = pd.DataFrame(ii_also_included)
ii_also_included_df = ii_also_included_df.T
ii_also_included_df.columns = ["ii_elements_included"]

# get also mentioned data
ii_also_mentioned = get_data(ii_also_mentioned_output)
ii_also_mentioned_df = pd.DataFrame(ii_also_mentioned)
ii_also_mentioned_df = ii_also_mentioned_df.T
ii_also_mentioned_df.columns = ["ii_programmes_mentioned"]

ii_ss_df = pd.concat([
    ii_approach_df,
    ii_also_included_df,
    ii_also_mentioned_df,
], axis=1, sort=False)

# fill blanks with NA
ii_ss_df.fillna("NA", inplace=True)

# save to disk
ii_ss_df.to_csv("individualised_instruction_ss.csv", index=False)

print(ii_ss_df[0:50])