from Main import load_json, comments, highlighted_text
from AttributeIDList import intervention_frequency_output
import pandas as pd

# load json file
load_json()

# get intervention frequency highlighted text
InterventionFrequency_HT = highlighted_text(intervention_frequency_output)
InterventionFrequency_HT_df = pd.DataFrame(InterventionFrequency_HT)
InterventionFrequency_HT_df = InterventionFrequency_HT_df.T
InterventionFrequency_HT_df.columns = ["int_freq_ht"]

# get intervention frequency user comments
InterventionFrequency_Comments = comments(intervention_frequency_output)
InterventionFrequency_Comments_df = pd.DataFrame(InterventionFrequency_Comments)
InterventionFrequency_Comments_df = InterventionFrequency_Comments_df.T
InterventionFrequency_Comments_df.columns = ["int_freq_info"]

# concatenate data frames
intervention_frequency_df = pd.concat([
    InterventionFrequency_HT_df, 
    InterventionFrequency_Comments_df
], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_frequency_df.replace('\r',' ', regex=True, inplace=True)
intervention_frequency_df.replace('\n',' ', regex=True, inplace=True)
intervention_frequency_df.replace(':',' ',  regex=True, inplace=True)
intervention_frequency_df.replace(';',' ',  regex=True, inplace=True)

intervention_frequency_df.fillna("NA", inplace=True)

# Save to file (.csv)
""" intervention_frequency_df.to_csv("InterventionFrequency.csv", index=False) """