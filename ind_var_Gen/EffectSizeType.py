from Main import load_json, get_outcome_lvl2
from AttributeIDList import effect_size_type_output
import pandas as pd

load_json()

# get effect size type data
effectsizetype = get_outcome_lvl2(effect_size_type_output)
effectsizetype_df = pd.DataFrame(effectsizetype)

# name each column (number depends on outcome number)
effectsizetype_df.columns = [
    "out_es_type_"+'{}'.format(column+1) for column in effectsizetype_df.columns]

# fill blanks with NA
effectsizetype_df.fillna("NA", inplace=True)

# save to disk
#effectsizetype_df.to_csv("effectsizetype.csv", index=False)
