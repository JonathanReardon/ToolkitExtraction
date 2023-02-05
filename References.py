#!/usr/bin/env python3

from Main import get_metadata, get_data, get_outcome_lvl1, get_outcome_lvl2, data_files

from ind_var_Gen.eppi_ID import eppiid_df
from ind_var_Gen.AdminStrand import admin_strand_df
from ind_var_Gen.Author import author_df
from ind_var_Gen.Authors import authors_df
from ind_var_Gen.Date import year_df
from ind_var_Gen.Title import title_df
from ind_var_Gen.ParentTitle import parentittle_df
from ind_var_Gen.Parent_Authors import parentauthors_df
from ind_var_Gen.TypeName import typename_df
from ind_var_Gen.Abstract import abstract_df

from ind_var_Gen.Volume import volume_df
from ind_var_Gen.Issue import issue_df
from ind_var_Gen.Pages import pages_df
from ind_var_Gen.DOI import doi_df
from ind_var_Gen.URL import url_df
from ind_var_Gen.Publisher import publisher_df
from ind_var_Gen.City import city_df
from ind_var_Gen.Institution import institution_df
from ind_var_Gen.Editors import editedby_df

# standard imports
import os, sys
import pandas as pd

data_files = sys.argv[1]

# remove strand info column
del admin_strand_df["strand_info"]

def make_references_df(save_file=True):
    references = pd.concat([
        eppiid_df,
        admin_strand_df,
        author_df,
        authors_df,
        year_df,
        title_df,
        parentittle_df,
        parentauthors_df,
        typename_df,
        abstract_df,
        volume_df,
        issue_df,
        pages_df,
        doi_df,
        url_df,
        publisher_df,
        city_df,
        institution_df
    ], axis=1, sort=False)

    references.columns = [[
        "ID",
        "toolkit_strand",
        "short_title",
        "main_authors",
        "year",
        "main_title",
        "parent_title",
        "parent_authors",
        "type_name",
        "abstract",
        "volume",
        "issue",
        "pages",
        "doi",
        "url",
        "publisher",
        "city",
        "institution"
    ]]

    if save_file:
        # get current wd
        cw = os.getcwd()

        # get file name for output
        outfile_name_pre = data_files.rsplit('/')[-1]
        outfile_name_mid = outfile_name_pre.rsplit('.')[0]
        outfile_name = outfile_name_mid + "_References.csv"
        outfile = os.path.join(cw + "/" + outfile_name_mid, outfile_name)

        # create dir (filename)
        try:
            os.mkdir(outfile_name_mid)
        except OSError:
            print("Create {} dir fail, already exists or permission error".format(outfile_name_mid))
        else:
            print("Successfully created {} directory".format(outfile_name_mid))

        # write to disk
        print("Input file: {}".format(data_files))
        print("Saving extracted output to: {}".format(outfile))
        references.to_csv(outfile, index=False, header=True)

make_references_df(save_file=True)






