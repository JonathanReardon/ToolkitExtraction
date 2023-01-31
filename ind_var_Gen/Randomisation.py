from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import randomisation_details
import pandas as pd

# load json file
load_json()

# get randomisation data
randomisation = get_data(randomisation_details)
randomisation_df = pd.DataFrame(randomisation)
randomisation_df = randomisation_df.T
randomisation_df.columns = ["rand_raw"]

# Get Randomisation highlighted text
randomisation_HT = highlighted_text(randomisation_details)
randomisation_details_df = pd.DataFrame(randomisation_HT)
randomisation_details_df = randomisation_details_df.T
randomisation_details_df.columns = ["rand_ht"]

# Get Randomisation user comments
randomisation_Comments = comments(randomisation_details)
randomisation_Comments_df = pd.DataFrame(randomisation_Comments)
randomisation_Comments_df = randomisation_Comments_df.T
randomisation_Comments_df.columns = ["rand_info"]

# concatenate data frames
randomisation_df = pd.concat([
    randomisation_df, 
    randomisation_details_df, 
    randomisation_Comments_df
], axis=1, sort=False)

# fill blanks with Na
randomisation_df.fillna("NA", inplace=True)

randomisation_df['rand_raw'] = randomisation_df['rand_raw'].apply(lambda x: ",".join(x) if isinstance(x, list) else x)

# save to disk
""" randomisation_df.to_csv("randomisation.csv", index=False) """

""" print(randomisation_df['rand_raw']) """
