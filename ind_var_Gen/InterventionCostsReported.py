from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import intervention_costs_reported
import pandas as pd

# load json file
load_json()

# Get Intervention Costs Reported main data
InterventionCosts = get_data(intervention_costs_reported)
InterventionCosts_df = pd.DataFrame(InterventionCosts)
InterventionCosts_df = InterventionCosts_df.T
InterventionCosts_df.columns = ["int_cost_raw"]

# Get Intervention Costs Reported highlighted text
InterventionCosts_HT = highlighted_text(intervention_costs_reported)
InterventionCosts_HT_df = pd.DataFrame(InterventionCosts_HT)
InterventionCosts_HT_df = InterventionCosts_HT_df.T
InterventionCosts_HT_df.columns = ["int_cost_ht"]

# Get Intervention Costs Reported user comments
InterventionCosts_Comments = comments(intervention_costs_reported)
InterventionCosts_Comments_df = pd.DataFrame(InterventionCosts_Comments)
InterventionCosts_Comments_df = InterventionCosts_Comments_df.T
InterventionCosts_Comments_df.columns = ["int_cost_info"]

# concatenate data frames
intervention_costs_df = pd.concat([
    InterventionCosts_df, 
    InterventionCosts_HT_df, 
    InterventionCosts_Comments_df
], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_costs_df.replace('\r',' ', regex=True, inplace=True)
intervention_costs_df.replace('\n',' ', regex=True, inplace=True)
intervention_costs_df.replace(':',' ',  regex=True, inplace=True)
intervention_costs_df.replace(';',' ',  regex=True, inplace=True)

# fill blanks with NA
intervention_costs_df.fillna("NA", inplace=True)

# Save to file (.csv)
""" intervention_costs_df.to_csv("InterventionCostsReported.csv", index=False) """

""" print(intervention_costs_df) """