from Main import load_json

from eppi_ID import eppiid_df
from OutcomeType import outcometype_df
from Outcome import outcome_df

import pandas as pd
import os
import json

load_json()

# concatenate eppi ids with outcome types to check for missing outcome info
all_variables = pd.concat([eppiid_df, outcometype_df], axis=1, sort=False)

# save to disk
#all_variables.to_csv("PT_14jan21_Outcome_Info.csv", index=False)