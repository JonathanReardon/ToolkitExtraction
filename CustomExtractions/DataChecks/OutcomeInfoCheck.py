from eppi_ID import eppiid_df
from OutcomeType import outcometype_df
from Outcome import outcome_df

import pandas as pd
import os
import json

from DATAFILE import file

exclude = "NA"

script_dir = os.path.dirname(__file__)
datafile = os.path.join(script_dir, file)

with open(datafile) as f:
    data = json.load(f)

# concatenate eppi ids with outcome types to check for missing outcome info
all_variables = pd.concat([eppiid_df, outcometype_df], axis=1, sort=False)

# save to disk
all_variables.to_csv("PT_14jan21_Outcome_Info.csv", index=False)