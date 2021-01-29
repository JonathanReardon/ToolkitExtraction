from Main import load_json, get_data, comments, highlighted_text
from CODES import intervention_evaluation
import pandas as pd

# load json file
load_json()

# get intervention costs reported main data
InterventionEvaluation = get_data(intervention_evaluation)
InterventionEvaluation_df = pd.DataFrame(InterventionEvaluation)
InterventionEvaluation_df = InterventionEvaluation_df.T
InterventionEvaluation_df.columns = ["out_eval_raw"]

InterventionEvaluation_df["eef_eval_raw"] = InterventionEvaluation_df["out_eval_raw"].map(set(["Is this an EEF evaluation?"]).issubset).astype(int)
InterventionEvaluation_df["eef_eval_raw"]=InterventionEvaluation_df["eef_eval_raw"].replace(to_replace=[0, 1], value=["No", "Yes"])

# get intervention costs reported highlighted text
InterventionEvaluation_HT = highlighted_text(intervention_evaluation)
InterventionEvaluation_HT_df = pd.DataFrame(InterventionEvaluation_HT)
InterventionEvaluation_HT_df  = InterventionEvaluation_HT_df.T
InterventionEvaluation_HT_df.columns = ["out_eval_ht"]

# get intervention costs reported user comments
InterventionEvaluation_Comments = comments(intervention_evaluation)
InterventionEvaluation_Comments_df = pd.DataFrame(InterventionEvaluation_Comments)
InterventionEvaluation_Comments_df = InterventionEvaluation_Comments_df.T
InterventionEvaluation_Comments_df.columns = ["out_eval_info"]

# concatenate data frames
intervention_evaluation_df = pd.concat([
    InterventionEvaluation_df, 
    InterventionEvaluation_HT_df, 
    InterventionEvaluation_Comments_df
], axis=1, sort=False)

intervention_evaluation_df=intervention_evaluation_df[[
    "out_eval_raw", 
    "out_eval_ht", 
    "out_eval_info", 
    "eef_eval_raw"
]]

# remove problematic text
intervention_evaluation_df.replace('\r',' ', regex=True, inplace=True)
intervention_evaluation_df.replace('\n',' ', regex=True, inplace=True)
intervention_evaluation_df.replace(':',' ',  regex=True, inplace=True)
intervention_evaluation_df.replace(';',' ',  regex=True, inplace=True)

intervention_evaluation_df.fillna("NA", inplace=True)

# Save to file (.csv)
""" intervention_evaluation_df.to_csv("InterventionEvaluation.csv", index=False) """