from Main import get_data, highlighted_text, comments
from AttributeIDList import clustering_output
import pandas as pd

# extract clustering data
clustering = get_data(clustering_output)
clustering_df = pd.DataFrame(clustering)
clustering_df = clustering_df.T
clustering_df.columns=["clust_anal_raw"]

# Get Baseline Differences highlighted text
clustering_HT = highlighted_text(clustering_output)
clustering_HT_df = pd.DataFrame(clustering_HT)
clustering_HT_df = clustering_HT_df.T
clustering_HT_df.columns = ["clust_anal_ht"]

# Get Educational Setting user comments
clustering_Comments = comments(clustering_output)
clustering_Comments_df = pd.DataFrame(clustering_Comments)
clustering_Comments_df = clustering_Comments_df.T
clustering_Comments_df.columns = ["clust_anal_info"]

# concatenate data frames
clustering_df = pd.concat([
    clustering_df, 
    clustering_HT_df, 
    clustering_Comments_df
], axis=1, sort=False)

# fill blanks with NA
clustering_df.fillna("NA", inplace=True)

# save to disk
clustering_df.to_csv("clustering.csv", index=False)