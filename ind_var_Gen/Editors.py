from Main import load_json, get_metadata
import pandas as pd

load_json()

# get abstract data
editedby = get_metadata("EditedBy")
editedby_df = pd.DataFrame(editedby)
editedby_df.columns = ["Editor(s)"]
editedby_df.fillna("NA", inplace=True)

# save to disk
#editedby_df.to_csv("editors.csv", index=False)

""" print(editedby_df) """
