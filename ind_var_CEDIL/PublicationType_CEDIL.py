from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import publication_type_CEDIL
import pandas as pd

# load json file
load_json()

# get publication type data
publicationtype = get_data(publication_type_CEDIL)
publicationtype_df = pd.DataFrame(publicationtype)
publicationtype_df = publicationtype_df.T
publicationtype_df.columns = ["pub_type_raw"]

# Get Publication Type highlighted text
publicationtype_HT = highlighted_text(publication_type_CEDIL)
publicationtype_HT_df = pd.DataFrame(publicationtype_HT)
publicationtype_HT_df = publicationtype_HT_df.T
publicationtype_HT_df.columns = ["pubtype_ht"]

# Get Publication Type user comments
publicationtype_Comments = comments(publication_type_CEDIL)
publicationtype_Comments_df = pd.DataFrame(publicationtype_Comments)
publicationtype_Comments_df = publicationtype_Comments_df.T
publicationtype_Comments_df.columns = ["pubtype_info"]

# concatenate data frames
publication_type_df = pd.concat([
    publicationtype_df, 
    publicationtype_HT_df, 
    publicationtype_Comments_df
], axis=1, sort=False)

# fill blanks with NA
publication_type_df.fillna("NA", inplace=True)

# save to risk
""" publication_type_df.to_csv("publicationtype.csv", index=False) """

print(publication_type_df)
