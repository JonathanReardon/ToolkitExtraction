from Main import load_json, get_metadata
import pandas as pd

load_json()

# get author data
publisher = get_metadata("Publisher")
publisher_df = pd.DataFrame(publisher)
publisher_df.columns = ["Publisher"]
publisher_df.fillna("NA", inplace=True)

# save to disk
#publisher_df.to_csv("publisher.csv", index=False)