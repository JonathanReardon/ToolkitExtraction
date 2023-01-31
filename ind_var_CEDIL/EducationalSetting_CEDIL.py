from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import edu_setting_CEDIL
import pandas as pd

load_json()

# get educational setting data
edusetting = get_data(edu_setting_CEDIL)
edusetting_df = pd.DataFrame(edusetting)
edusetting_df = edusetting_df.T
edusetting_df.columns=["int_setting_raw"]

# Get Educational Setting highlighted text
edusetting_HT = highlighted_text(edu_setting_CEDIL)
edusetting_HT_df = pd.DataFrame(edusetting_HT)
edusetting_HT_df = edusetting_HT_df.T
edusetting_HT_df.columns = ["int_setting_ht"]

# Get Educational Setting user comments
edusetting_Comments = comments(edu_setting_CEDIL)
edusetting_Comments_df = pd.DataFrame(edusetting_Comments)
edusetting_Comments_df = edusetting_Comments_df.T
edusetting_Comments_df.columns = ["int_setting_info"]

# concatenate data frames
educational_setting_df = pd.concat([
    edusetting_df, 
    edusetting_HT_df, 
    edusetting_Comments_df
], axis=1, sort=False)

# replace blanks with NA
educational_setting_df.fillna("NA", inplace=True)

# save to disk
# educational_setting_df.to_csv("edusetting.csv", index=False)

print(educational_setting_df)