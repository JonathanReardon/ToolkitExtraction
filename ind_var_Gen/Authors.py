from Main import load_json, get_metadata
import pandas as pd

load_json()

# get author data
authors = get_metadata("Authors")
authors_df = pd.DataFrame(authors)
authors_df.columns=["pub_author"]
authors_df.fillna("NA", inplace=True)

# save to disk
#authors_df.to_csv("authors.csv", index=False)

""" print(authors_df) """

""" authors_df.replace(';', ' ', regex=True, inplace=True) """
