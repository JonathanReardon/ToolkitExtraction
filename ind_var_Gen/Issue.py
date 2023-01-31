from Main import load_json, get_metadata
import pandas as pd

load_json()

# get author data
issue = get_metadata("Issue")
issue_df = pd.DataFrame(issue)
issue_df.columns = ["Issue"]
issue_df.fillna("NA", inplace=True)

# save to disk
#issue_df.to_csv("issue.csv", index=False)

""" print(issue_df)
 """