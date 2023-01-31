from Main import load_json, get_metadata
import pandas as pd

load_json()

# get author data
volume = get_metadata("Volume")
volume_df = pd.DataFrame(volume)
volume_df.columns = ["Volume"]
volume_df.fillna("NA", inplace=True)

# save to disk
#volume_df.to_csv("volume.csv", index=False)

""" print(volume_df) """
