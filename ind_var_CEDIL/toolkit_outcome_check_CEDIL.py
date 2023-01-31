from eppi_ID_CEDIL import eppiid_df
from OutcomeType_CEDIL import outcometype_df

import pandas as pd

all_variables = pd.concat([
    eppiid_df,
    outcometype_df
], axis=1, sort=False)

print(all_variables)
