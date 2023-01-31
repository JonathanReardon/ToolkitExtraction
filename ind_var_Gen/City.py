from Main import load_json, get_metadata
import pandas as pd

load_json()

# get author data
city = get_metadata("City")
city_df = pd.DataFrame(city)
city_df.columns = ["City"]
city_df.fillna("NA", inplace=True)

# save to disk
#city_df.to_csv("city.csv", index=False)

""" print(city_df) """
