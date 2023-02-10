#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Jonathan Reardon
"""

import os
import sys

# Third party imports
import pandas as pd
from toolz import interleave

# Local imports
from Main import save_dataframe
from ind_var_functions import ind_var_Gen

data_files = sys.argv[1]

def make_outcomes_df(save_file=True):

    global outcome_num

    eppiid_df = ind_var_Gen.eppi()
    author_df = ind_var_Gen.author()
    outcometype_df = ind_var_Gen.out_type()
    outcome_df = ind_var_Gen.outcome()
    outcome_title_df =  ind_var_Gen.out_tit()

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
        save_dataframe(all_variables, "_Outcomes.csv")

make_outcomes_df(save_file=True)

