from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import intervention_training_provided_output
import pandas as pd

# load json file
load_json()

# get intervention training provided data
InterventionTrainingProvided = get_data(intervention_training_provided_output)
InterventionTrainingProvided_df = pd.DataFrame(InterventionTrainingProvided)
InterventionTrainingProvided_df = InterventionTrainingProvided_df.T
InterventionTrainingProvided_df.columns = ["int_training_raw"]

# get intervention training provided highlighted text
InterventionTrainingProvided_HT = highlighted_text(intervention_training_provided_output)
InterventionTrainingProvided_HT_df = pd.DataFrame(InterventionTrainingProvided_HT)
InterventionTrainingProvided_HT_df = InterventionTrainingProvided_HT_df.T
InterventionTrainingProvided_HT_df.columns = ["int_training_ht"]

# get intervention training provided user comments
InterventionTrainingProvided_Comments = comments(intervention_training_provided_output)
InterventionTrainingProvided_Comments_df = pd.DataFrame(InterventionTrainingProvided_Comments)
InterventionTrainingProvided_Comments_df = InterventionTrainingProvided_Comments_df.T
InterventionTrainingProvided_Comments_df.columns = ["int_training_info"]

# concatenate data frames
intervention_training_provided_df = pd.concat([
    InterventionTrainingProvided_df, 
    InterventionTrainingProvided_HT_df, 
    InterventionTrainingProvided_Comments_df
], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_training_provided_df.replace('\r',' ', regex=True, inplace=True)
intervention_training_provided_df.replace('\n',' ', regex=True, inplace=True)
intervention_training_provided_df.replace(':',' ', regex=True, inplace=True)
intervention_training_provided_df.replace(';',' ', regex=True, inplace=True)

# fill blanks with NA
intervention_training_provided_df.fillna("NA", inplace=True)

# Save to file (.csv)
""" intervention_training_provided_df.to_csv("InterventionTrainingProvided.csv", index=False) """