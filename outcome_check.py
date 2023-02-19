#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__Author__ = "Jonathan Reardon"

# System imports
import os
import sys

# Third party imports
import pandas as pd
from toolz import interleave

# Local imports
from src.funcs import *

data_files = sys.argv[1]

def make_outcomes_df(save_file=True):

    global outcome_num

    eppiid_df = retrieve_metadata("ItemId", "id")
    author_df = retrieve_metadata("ShortTitle", "pub_author")
    outcometype_df = get_outcome_data_lvl2(outcome_type_codes, "out_type_")
    outcome_df = get_outcome_data_lvl1("OutcomeText", "out_label_")
    outcome_title_df = get_outcome_data_lvl1("Title", "out_tit_")

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

