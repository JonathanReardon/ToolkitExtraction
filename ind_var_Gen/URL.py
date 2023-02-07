from Main import load_json, get_metadata
import pandas as pd

load_json()

# get author data
url = get_metadata("URL")
url_df = pd.DataFrame(url)
url_df.columns = ["URL"]
url_df.fillna("NA", inplace=True)

# save to disk
#url_df.to_csv("url.csv", index=False)
