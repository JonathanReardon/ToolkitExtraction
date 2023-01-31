from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import intervention_delivery_output
import pandas as pd

# load json file
load_json()

# get intervention delivery data
InterventionDelivery = get_data(intervention_delivery_output)
interventiondelivery_df = pd.DataFrame(InterventionDelivery)
interventiondelivery_df = interventiondelivery_df.T
interventiondelivery_df.columns = ["int_who_raw"]

# get intervention delivery highlighted text
InterventionDelivery_HT = highlighted_text(intervention_delivery_output)
InterventionDelivery_HT_df = pd.DataFrame(InterventionDelivery_HT)
InterventionDelivery_HT_df = InterventionDelivery_HT_df.T
InterventionDelivery_HT_df.columns = ["int_who_ht"]

# get intervention delivery user comments
InterventionDelivery_Comments = comments(intervention_delivery_output)
InterventionDelivery_Comments_df = pd.DataFrame(InterventionDelivery_Comments)
InterventionDelivery_Comments_df = InterventionDelivery_Comments_df.T
InterventionDelivery_Comments_df.columns = ["int_who_info"]

# concatenate data frames
intervention_delivery_df = pd.concat([
    interventiondelivery_df, 
    InterventionDelivery_HT_df, 
    InterventionDelivery_Comments_df
], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_delivery_df.replace('\r',' ', regex=True, inplace=True)
intervention_delivery_df.replace('\n',' ', regex=True, inplace=True)
intervention_delivery_df.replace(':',' ',  regex=True, inplace=True)
intervention_delivery_df.replace(';',' ',  regex=True, inplace=True)

# fill blanks with NA
intervention_delivery_df.fillna("NA", inplace=True)

# Save to file (.csv)
intervention_delivery_df.to_csv("InterventionDelivery.csv", index=False)

""" print(intervention_delivery_df[10:22]) """
