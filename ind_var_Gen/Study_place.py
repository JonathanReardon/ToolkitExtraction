from Main import load_json, get_data, highlighted_text
from AttributeIDList import location_info
import pandas as pd

# load json file
load_json()

# get study place info data
study_place = get_data(location_info)
study_place_df = pd.DataFrame(study_place)
study_place_df = study_place_df.T
study_place_df.columns = ["study_place_info"]

# get study place ht data
study_place_ht = highlighted_text(location_info)
study_place_ht_df = pd.DataFrame(study_place_ht)
study_place_ht_df = study_place_ht_df.T
study_place_ht_df.columns = ["study_place_ht"]

# concatenate data frames
study_place_df = pd.concat([
    study_place_df,
    study_place_ht_df,
], axis=1, sort=False)

# fill blanks with NA
study_place_df.fillna("NA", inplace=True)

print(study_place_df)

# save to disk
""" source_all_df.to_csv("source.csv", index=False) """