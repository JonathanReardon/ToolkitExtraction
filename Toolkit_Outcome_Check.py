from ind_var.eppi_ID import eppiid_df
from ind_var.Author import author_df
from ind_var.OutcomeType import outcometype_df
from ind_var.Outcome import outcome_df
from ind_var.OutcomeTitle import outcome_title_df

import pandas as pd
from toolz import interleave

import os, sys

data_files = sys.argv[1]

def make_outcomes_df(save_file=True):

    global outcome_num

    df = pd.concat([
        outcometype_df,
        outcome_df,
        outcome_title_df
    ], axis=1)[list(interleave([
        outcometype_df,
        outcome_df,
        outcome_title_df
    ]))]

    all_variables = pd.concat([
        eppiid_df,
        author_df,
        df
    ], axis=1, sort=False)

    # get number of outcomes from last column name
    colname = all_variables.columns[-1]
    split = colname.split("_")
    outcome_num = split[-1]
    outcome_num = int(outcome_num)

    if save_file:
        # get current wd
        cw = os.getcwd()

        # get file name for output
        outfile_name_pre = data_files.rsplit('/')[-1]
        outfile_name_mid = outfile_name_pre.rsplit('.')[0]
        outfile_name = outfile_name_mid + "_Outcomes.csv"
        outfile = os.path.join(cw + "/" + outfile_name_mid, outfile_name)

        # create dir (filename)
        """ try:
            os.mkdir(outfile_name_mid)
        except OSError:
            print("Create {} dir fail, already exists or permission error".format(outfile_name_mid))
        else:
            print("Successfully created {} directory".format(outfile_name_mid))

        # write to disk
        print("Input file: {}".format(data_files))
        print("Saving extracted output to: {}".format(outfile))
        all_variables.to_csv(outfile, index=False, header=True) """

make_outcomes_df(save_file=True)

