from Main import get_metadata
import pandas as pd

# get author data
author = get_metadata("ShortTitle")
author_df = pd.DataFrame(author)
author_df.columns=["pub_author"]
author_df.fillna("NA", inplace=True)

# save to disk
author_df.to_csv("author.csv", index=False)
