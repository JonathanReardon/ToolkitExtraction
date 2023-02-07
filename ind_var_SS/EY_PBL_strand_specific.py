from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import kind_of_play
from AttributeIDList import who_involved
from AttributeIDList import play_focus

import pandas as pd
import os
import sys

load_json()

# get kind if play data
kind_play = get_data(kind_of_play)
kind_play_df = pd.DataFrame(kind_play)
kind_play_df = kind_play_df.T
kind_play_df.columns = ["kind_of_play"]

# get who involved data
who_invol = get_data(who_involved)
who_invol_df = pd.DataFrame(who_invol)
who_invol_df = who_invol_df.T
who_invol_df.columns = ["who_involved"]

# get play focus data
play_foc = get_data(play_focus)
play_foc_df = pd.DataFrame(play_foc)
play_foc_df = play_foc_df.T
play_foc_df.columns = ["play_focus"]

ey_pbl_df = pd.concat([
    kind_play_df,
    who_invol_df,
    play_foc_df
], axis=1, sort=False)

# fill blanks with NA
ey_pbl_df.fillna("NA", inplace=True)

# save to disk
#ey_pbl_df.to_csv("ey_pbl_ss_df.csv", index=False)