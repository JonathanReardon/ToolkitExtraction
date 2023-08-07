#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__Author__ = "Jonathan Reardon"

# Standard library imports
import json
import os

# Third-party imports
from numba import jit
import numpy as np
import pandas as pd
import warnings
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from rich.console import Console
from rich.progress import track
from rich.style import Style
from rich.table import Table
from rich.columns import Columns
from rich.panel import Panel
from rich import box
from rich import print
from toolz import interleave

from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.style import Style
from rich.table import Table
from rich.columns import Columns

# Local imports
from eefdata.src.attributeIDs import *

# Filter out all warnings
warnings.filterwarnings('ignore')

GREY="#37474f"
WHITE="#FFFFFF"

class JSONDataExtractor:
    def __init__(self, data_file):
        self.data_file = data_file
        self.data = None
        self.load_json()


    def load_json(self):
        datafile = os.path.join(os.getcwd(), self.data_file)
        with open(datafile) as f:
            self.data = json.load(f)


    def get_metadata(self, var):
        ''' """ 
        Extracts study-level metadata. """
        Params: Variable name e.g. "Year", "ShortTitle".
        Returns: A list of extracted data. One datapoint per study.
        '''
        varlist = []
        for section in range(len(self.data["References"])):
            if self.data["References"][section][var]:
                varlist.append(self.data["References"][section][var])
            else:
                varlist.append("NA")
        return varlist


    def get_data(self, codes):
        df = []
        references = self.data["References"]
        references_length = len(references)
        for code in codes:
            holder = []
            for section in range(references_length):
                if "Codes" in references[section]:
                    codes_section = references[section]["Codes"]
                    code_keys = set(code.keys())
                    holderfind = [code[attribute["AttributeId"]] for attribute in codes_section if attribute["AttributeId"] in code_keys]
                    holder.append(holderfind if holderfind else "NA")
            df.append(holder)
        return df


    def comments(self, codes):
        ''' 
        Extracts study level "comment" data.
        Params: List/dict [{..}] of one or more AttributeID's and Attribute labels.
        Returns: A list of extracted data. One or more datapoints per study.
        '''
        all_comments = []
        references = self.data["References"]
        references_length = len(references)
        for code in codes:
            comments = []
            code_keys = set(code.keys())
            for section in range(references_length):
                if "Codes" in references[section]:
                    user_comments = []
                    codes_section = references[section]["Codes"]
                    for study_code in codes_section:
                        if study_code["AttributeId"] in code_keys and "AdditionalText" in study_code:
                            user_comments = study_code["AdditionalText"]
                    comments.append(user_comments if user_comments else "NA")
                else:
                    comments.append("NA")
            all_comments.append(comments)
        return all_comments


    def highlighted_text(self, codes):
        all_highlighted_text = []
        references = self.data["References"]
        references_length = len(references)
        for code in codes:
            highlighted_text = []
            code_keys = set(code.keys())
            for section in range(references_length):
                if "Codes" in references[section]:
                    user_highlighted_text = []
                    codes_section = references[section]["Codes"]
                    for study_code in codes_section:
                        if study_code["AttributeId"] in code_keys and "ItemAttributeFullTextDetails" in study_code:
                            user_highlighted_text.extend(item["Text"] for item in study_code["ItemAttributeFullTextDetails"])
                    highlighted_text.append(user_highlighted_text if user_highlighted_text else "NA")
                else:
                    highlighted_text.append("NA")
            all_highlighted_text.append(highlighted_text)
        return all_highlighted_text
    

    def get_outcome_lvl1(self, var):
        references = self.data["References"]
        references_length = len(references)
        outcome_number = [
            len(reference.get("Outcomes", [])) 
            for reference in references
        ]
        max_outcome_number = max(outcome_number, default=0)

        varlist = []
        for section in range(references_length):
            holder = []
            outcomes = references[section].get("Outcomes", [])
            for subsection in range(max_outcome_number):
                if subsection < len(outcomes):
                    holder.append(outcomes[subsection].get(var, "NA"))
                else:
                    holder.append("NA")
            varlist.append(holder)
        return varlist
    

    def get_outcome_lvl2(self, var):
        varlist = []
        references = self.data["References"]
        references_length = len(references)
        for variable in range(len(var)):
            var_items = var[variable].items()
            for study in range(references_length):
                reference_study = references[study]
                outerholder = "NA"
                if "Codes" in reference_study and "Outcomes" in reference_study:
                    outerholder = []
                    for item in range(len(reference_study["Outcomes"])):
                        outcome_item = reference_study["Outcomes"][item]
                        innerholderholder = "NA"
                        if "OutcomeCodes" in outcome_item:
                            innerholderholder = []
                            outcome_item_attributes = outcome_item["OutcomeCodes"]["OutcomeItemAttributesList"]
                            for subsection in range(len(outcome_item_attributes)):
                                attribute_id = outcome_item_attributes[subsection]["AttributeId"]
                                for key, value in var_items:
                                    if key == attribute_id:
                                        innerholderholder.append(outcome_item_attributes[subsection]["AttributeName"])
                            if len(innerholderholder) == 0:
                                innerholderholder = "NA"
                        outerholder.append(innerholderholder)
                varlist.append(outerholder)
        return varlist


    def getOutcomeData(self, dataframe, out_label, out_container, var_names):
        '''
        Extract strand level outcome data for main analysis dataframe
        '''
        eppiid_df = json_extractor.retrieve_metadata("ItemId", "id")
        author_df = json_extractor.retrieve_metadata("ShortTitle", "pub_author")
        outcometype_df = json_extractor.get_outcome_data_lvl2(outcome_type_codes, "out_type_")
        outcome_df = json_extractor.get_outcome_data_lvl1("OutcomeText", "out_label_")
        outcome_title_df = json_extractor.get_outcome_data_lvl1("Title", "out_tit_")

        df = pd.concat([outcometype_df, outcome_df, outcome_title_df
        ], axis=1)[list(interleave([
            outcometype_df, outcome_df, outcome_title_df
        ]))]

        all_variables = pd.concat([eppiid_df, author_df, df], axis=1, sort=False)

        # get number of outcomes from last column name
        colname = all_variables.columns[-1]
        split = colname.split("_")
        outcome_num = split[-1]
        outcome_num = int(outcome_num)       

        for counter, row in enumerate(dataframe['out_type_1']):
                found = False
                for outcome_n in range(1, outcome_num + 1):
                    if out_label in dataframe[f'out_type_{outcome_n}'][counter]:
                        found = True
                        for counter2, holder in enumerate(out_container):
                            holder.append(dataframe[var_names[counter2] + f"{outcome_n}"][counter])
                        break
                if not found:
                    for holder in out_container:
                        holder.append("NA")
        return out_container


    def get_outcome_data_lvl1(self, attribute_text, column_prefix):
        outcome_data = self.get_outcome_lvl1(attribute_text)
        outcome_df = pd.DataFrame(outcome_data)
        # round data to 4 decimal places
        outcome_df = outcome_df.applymap(lambda x: round(x, 4) if isinstance(x, (int, float)) else x)
        # name each column (number depends on outcome number)
        outcome_df.columns = [column_prefix+'{}'.format(column+1) for column in outcome_df.columns]

        #outcome_df.fillna("NA", inplace=True)
        #outcome_df = outcom_df.replace(r'^\s*$', "NA", regex=True)
        #outcome_df.replace('\r', ' ', regex=True, inplace=True)
        #outcome_df.replace('\n', ' ', regex=True, inplace=True)
        self.clean_up(outcome_df)
        return outcome_df


    def get_outcome_data_lvl2(self, attribute_codes, column_prefix):
        # get outcome data
        outcome_data = self.get_outcome_lvl2(attribute_codes)
        outcome_df = pd.DataFrame(outcome_data)
        # name each column (number depends on outcome number)
        outcome_df.columns = [column_prefix+'{}'.format(column+1) for column in outcome_df.columns]
        # fill blanks with NA
        outcome_df.fillna("NA", inplace=True)
        return outcome_df


    def process_data(self, output, data_col):
        data = self.get_data(output)
        data_df = pd.DataFrame(data)
        data_df = data_df.T
        data_df.columns = [data_col]
        self.clean_up(data_df)
        return data_df


    def process_ht(self, output, ht_col):
        ht = self.highlighted_text(output)
        ht_df = pd.DataFrame(ht)
        ht_df = ht_df.T
        ht_df.columns = [ht_col]
        self.clean_up(ht_df)
        return ht_df


    def process_info(self, output, info_col):
        comment = self.comments(output)
        comments_df = pd.DataFrame(comment)
        comments_df = comments_df.T
        comments_df.columns = [info_col]
        self.clean_up(comments_df)
        return comments_df


    def process_metadata(self, output, info_col):
        # get metadata
        metadata = self.get_metadata(output)
        metadata_df = pd.DataFrame(metadata)
        #metadata_df = metadata_df.T
        metadata_df.columns = [info_col]
        return metadata_df


    def retrieve_metadata(self, metadata_type, metadata_value):
        metadata_df = self.process_metadata(metadata_type, metadata_value)
        self.clean_up(metadata_df)
        metadata_df.fillna("NA", inplace=True)
        return metadata_df


    def retrieve_data(self,id, col_name):
        data = self.get_data(id)
        data_df = pd.DataFrame(data)
        data_df = data_df.T
        data_df.columns = [col_name]
        self.clean_up(data_df)
        return data_df


    def retrieve_ht(self,id, col_name):
        ht = self.highlighted_text(id)
        ht_df = pd.DataFrame(ht)
        ht_df = ht_df.T
        ht_df.columns = [col_name]
        self.clean_up(ht_df)
        return ht_df


    def retrieve_info(self,id, col_name):
        info = self.comments(id)
        info_df = pd.DataFrame(info)
        info_df = info_df.T
        info_df.columns = [col_name]
        self.clean_up(info_df)
        return info_df

    @staticmethod
    def clean_up(df):
        """
        """
        df.replace('\r', ' ', regex=True, inplace=True)
        df.replace('\n', ' ', regex=True, inplace=True)
        df.replace(':', ' ',  regex=True, inplace=True)
        df.replace(';', ' ',  regex=True, inplace=True)


    def get_outfile_dir(self, df, df_name):
        '''
        Gets output file directory
        '''
        # Get current working dir
        cw = os.getcwd() + "/output"
        # get file name for output
        outfile_name_pre = self.data_file.rsplit('/')[-1] # 
        outfile_name_mid = outfile_name_pre.rsplit('.')[0]  # use for dir name
        outfile_name = outfile_name_mid + df_name
        outfile = os.path.join(cw + "/" + outfile_name_mid, outfile_name)  
        return outfile


    def save_dataframe(self, df, df_name, standard_info=False, custom_info=False):
        '''
        Saves a .csv of the dataframe to output/
        '''
        # Get current working dir
        import datetime
        current_datetime = datetime.datetime.now()
        cw = os.getcwd()
        # get file name for output
        outfile_name_pre = data_file.rsplit('/')[-1] # 
        outfile_name_mid = outfile_name_pre.rsplit('.')[0]  # use for dir name
        outfile_name = outfile_name_mid + df_name
        outfile = os.path.join(cw + "/" + outfile_name)

        df.to_csv(outfile, index=False)

        if standard_info==True:
            pass

        if custom_info==True:
            pass

        return outfile

    
    def verbose_display(self, df):
        '''
        Displays further info
        '''
        # print dataframe
        print(df)
        print("\n")
        # list column names and position
        for counter, i in enumerate(df):
            print(counter, i)
        print("\n")
        # print dataframe info
        print("Columns: {}".format(df.shape[1]))
        print("Rows: {}".format(df.shape[0]))
        print("Datapoints: {}".format(df.shape[0] * df.shape[1]))
        print("\n")


    def make_outcomes_df(self, save_file=True):

        eppiid_df = json_extractor.retrieve_metadata("ItemId", "id")
        author_df = json_extractor.retrieve_metadata("ShortTitle", "pub_author")
        outcometype_df = json_extractor.get_outcome_data_lvl2(outcome_type_codes, "out_type_")
        outcome_df = json_extractor.get_outcome_data_lvl1("OutcomeText", "out_label_")
        outcome_title_df = json_extractor.get_outcome_data_lvl1("Title", "out_tit_")

        df = pd.concat([
            outcometype_df, outcome_df, outcome_title_df
        ], axis=1)[list(interleave([
            outcometype_df, outcome_df, outcome_title_df
        ]))]

        all_variables = pd.concat([eppiid_df, author_df, df], axis=1, sort=False)

        # get number of outcomes from last column name
        colname = all_variables.columns[-1]
        split = colname.split("_")
        outcome_num = split[-1]
        outcome_num = int(outcome_num)

        if save_file:
            self.save_dataframe(all_variables, "_Outcomes.csv", standard_info=True)


    #/***********************************************/
    #/   COMPILE DATA FRAMES FOR CHECKING/CLEANING   /
    #/***********************************************/
    

class DataFrameCompilation:
    def __init__(self, data_extractor):
        self.data_extraction = data_extractor

    def make_dataframe_1(self, save_file=True, clean_cols=False, verbose=True):
        """
        Extracts data from the sources defined in the current instance of the 
        DataExtraction class, and returns a pandas DataFrame with the relevant 
        variables for further cleaning and analysis. 

        Args:
        - save_file (bool): Whether or not to save the resulting dataframe to a file.
        - clean_cols (bool): Whether or not to add empty columns per variable
          for data checkers to log changes.
        - verbose (bool): Whether or not to display information about the extraction process.

        Returns:
        - all_variables: a pandas DataFrame with the relevant variables included.
        - outfile1 (str or None): the name of the output CSV file, 
          if `save_file=True`. If `save_file=False`, returns `None`.
        """
        eppiid_df = self.data_extraction.retrieve_metadata("ItemId", "id")
        author_df = self.data_extraction.retrieve_metadata("ShortTitle", "pub_author")
        year_df = self.data_extraction.retrieve_metadata("Year", "pub_year")
        abstract_df = self.data_extraction.retrieve_metadata("Abstract", "abstract")
        admin_strand_data = self.data_extraction.retrieve_data(admin_strand_output, "strand_raw")
        admin_strand_info = self.data_extraction.retrieve_info(admin_strand_output, "strand_info")
        toolkit_version_data = self.data_extraction.retrieve_data(toolkit_versions, "toolkit_version")
        pubtype_eppi_df = self.data_extraction.retrieve_metadata("TypeName", "pub_eppi")
        pub_type_data = self.data_extraction.retrieve_data(publication_type_output, "pub_type_raw")
        pub_type_ht = self.data_extraction.retrieve_ht(publication_type_output, "pubtype_ht")
        pub_type_info = self.data_extraction.retrieve_info(publication_type_output, "pubtype_info")
        country_df = self.data_extraction.retrieve_data(countries, "loc_country_raw")
        edu_setting_data = self.data_extraction.retrieve_data(edu_setting_output, "int_setting_raw")
        edu_setting_ht = self.data_extraction.retrieve_ht(edu_setting_output, "int_setting_ht")
        edu_setting_info = self.data_extraction.retrieve_info(edu_setting_output, "int_setting_info")
        study_realism_data = self.data_extraction.retrieve_data(study_realism_output, "eco_valid_raw")
        study_realism_ht = self.data_extraction.retrieve_ht(study_realism_output, "eco_valid_ht")
        study_realism_info = self.data_extraction.retrieve_info(study_realism_output, "eco_valid_info")
        student_age_data = self.data_extraction.retrieve_data(student_age_output, "part_age_raw")
        student_age_ht = self.data_extraction.retrieve_ht(student_age_output, "part_age_ht")
        student_age_info = self.data_extraction.retrieve_info(student_age_output, "part_age_info")
        number_of_school_int_info = self.data_extraction.retrieve_info(number_of_schools_intervention_output, "school_treat_info")
        number_of_school_int_ht = self.data_extraction.retrieve_ht(number_of_schools_intervention_output, "school_treat_ht")
        number_of_school_control_info = self.data_extraction.retrieve_info(number_of_schools_control_output, "school_cont_info")
        number_of_school_control_ht = self.data_extraction.retrieve_ht(number_of_schools_control_output, "school_cont_ht")
        number_of_school_total_info = self.data_extraction.retrieve_info(number_of_schools_total_output, "school_total_info")
        number_of_school_total_ht = self.data_extraction.retrieve_ht(number_of_schools_total_output, "school_total_ht")
        number_of_school_na_data = self.data_extraction.retrieve_data(number_of_schools_not_provided_output, "school_na_raw")
        number_of_school_na_info = self.data_extraction.retrieve_info(number_of_schools_not_provided_output, "school_na_info")
        number_of_school_na_ht = self.data_extraction.retrieve_ht(number_of_schools_not_provided_output, "school_na_ht")
        number_of_classes_int_info = self.data_extraction.retrieve_info(num_of_class_int_output, "class_treat_info")
        number_of_classes_int_ht = self.data_extraction.retrieve_ht(num_of_class_int_output, "class_treat_ht")
        number_of_classes_control_info = self.data_extraction.retrieve_info(num_of_class_cont_output, "class_cont_info")
        number_of_classes_control_ht = self.data_extraction.retrieve_ht(num_of_class_cont_output, "class_cont_ht")
        number_of_classes_total_info = self.data_extraction.retrieve_info(num_of_class_tot_output, "class_total_info")
        number_of_classes_total_ht = self.data_extraction.retrieve_ht(num_of_class_tot_output, "class_total_ht")
        number_of_classes_na_data = self.data_extraction.retrieve_data(numb_of_class_np_output, "class_na_raw")
        number_of_classes_na_info = self.data_extraction.retrieve_info(numb_of_class_np_output, "class_na_info")
        number_of_classes_na_ht = self.data_extraction.retrieve_ht(numb_of_class_np_output, "class_na_ht")
        treatment_group_data = self.data_extraction.retrieve_data(treatment_group, "treat_group_raw")
        treatment_group_ht = self.data_extraction.retrieve_ht(treatment_group, "treat_group_ht")
        treatment_group_info = self.data_extraction.retrieve_info(treatment_group, "treat_group_info")
        part_assig_data = self.data_extraction.retrieve_data(part_assign_output, "part_assig_raw")
        part_assig_ht = self.data_extraction.retrieve_ht(part_assign_output, "part_assig_ht")
        part_assig_info = self.data_extraction.retrieve_info(part_assign_output, "part_assig_info")
        level_of_assign_data = self.data_extraction.retrieve_data(level_of_assignment_output, "level_assig_raw")
        level_of_assign_ht = self.data_extraction.retrieve_ht(level_of_assignment_output, "level_assig_ht")
        level_of_assign_info = self.data_extraction.retrieve_info(level_of_assignment_output, "level_assig_info")
        study_design_data = self.data_extraction.retrieve_data(study_design_output, "int_desig_raw")
        study_design_ht = self.data_extraction.retrieve_ht(study_design_output, "int_design_ht")
        study_design_info = self.data_extraction.retrieve_info(study_design_output, "int_design_info")
        rand_data = self.data_extraction.retrieve_data(randomisation_details, "rand_raw")
        rand_ht = self.data_extraction.retrieve_ht(randomisation_details, "rand_ht")
        rand_info = self.data_extraction.retrieve_info(randomisation_details, "rand_info")
        other_outcomes_data = self.data_extraction.retrieve_data(other_out_output, "out_other_raw")
        other_outcomes_ht = self.data_extraction.retrieve_ht(other_out_output, "out_other_ht")
        other_outcomes_info = self.data_extraction.retrieve_info(other_out_output, "out_other_info")
        addit_out_data = self.data_extraction.retrieve_data(addit_out_output, "out_info_raw")
        addit_out_ht = self.data_extraction.retrieve_ht(addit_out_output, "out_info_ht")
        addit_out_info = self.data_extraction.retrieve_info(addit_out_output, "out_info_info")
        other_part_ht = self.data_extraction.retrieve_ht(other_part_output, "part_other_ht")
        other_part_info = self.data_extraction.retrieve_info(other_part_output, "part_other_info")
        
        all_variables = pd.concat([
            eppiid_df,
            author_df,
            year_df,
            abstract_df,
            admin_strand_data,
            admin_strand_info,
            toolkit_version_data,
            pubtype_eppi_df,
            pub_type_data,
            pub_type_ht,
            pub_type_info,
            country_df,
            edu_setting_data,
            edu_setting_ht,
            edu_setting_info,
            study_realism_data,
            study_realism_ht,
            study_realism_info,
            student_age_data,
            student_age_ht,
            student_age_info,
            number_of_school_int_info,
            number_of_school_int_ht,
            number_of_school_control_info,
            number_of_school_control_ht,
            number_of_school_total_info,
            number_of_school_total_ht,
            number_of_school_na_data,
            number_of_school_na_info,
            number_of_school_na_ht,
            number_of_classes_int_info,
            number_of_classes_int_ht,
            number_of_classes_control_info,
            number_of_classes_control_ht,
            number_of_classes_total_info,
            number_of_classes_total_ht,
            number_of_classes_na_data,
            number_of_classes_na_info,
            number_of_classes_na_ht,
            treatment_group_data,
            treatment_group_ht,
            treatment_group_info,
            part_assig_data,
            part_assig_ht,
            part_assig_info,
            level_of_assign_data,
            level_of_assign_ht,
            level_of_assign_info,
            study_design_data,
            study_design_ht,
            study_design_info,
            rand_data,
            rand_ht,
            rand_info,
            other_outcomes_data,
            other_outcomes_ht,
            other_outcomes_info,
            addit_out_data,
            addit_out_ht,
            addit_out_info,
            other_part_ht,
            other_part_info,
        ], axis=1, sort=False)

        all_variables['part_assig_raw'] = all_variables['part_assig_raw'].str[0]
        all_variables['level_assig_raw'] = all_variables['level_assig_raw'].str[0]
        all_variables['rand_raw'] = all_variables['rand_raw'].apply(lambda x: ",".join(x) if isinstance(x, list) else x)
        all_variables['eco_valid_raw'] = all_variables['eco_valid_raw'].str[0]
        
        if clean_cols == True:
            # Insert empty columns for each variable for data 
            # checkers to log errors prior to main analysis
            cols_to_insert = {
                'strand_CLEAN': 6,
                'pub_eppi_CLEAN': 9,
                'pub_type_CLEAN': 13,
                'loc_country_CLEAN': 15,
                'int_Setting_CLEAN': 19,
                'eco_valid_CLEAN': 23,
                'part_age_CLEAN': 27,
                'school_treat_CLEAN': 30,
                'school_cont_CLEAN': 33,
                'school_total_CLEAN': 36,
                'school_na_CLEAN': 40,
                'class_treat_CLEAN': 43,
                'class_cont_CLEAN': 46,
                'class_total_CLEAN': 49,
                'class_na_CLEAN': 53,
                'treat_group_CLEAN': 57,
                'part_assig_CLEAN': 61,
                'level_assig_CLEAN': 65,
                'int_design_CLEAN': 69,
                'rand_CLEAN': 73,
                'out_other_CLEAN': 77,
                'out_info_CLEAN': 81,
                'part_other_CLEAN': 84
            }
            # Insert empty columns at specified locations
            for col_name, col_idx in cols_to_insert.items():
                all_variables.insert(col_idx, col_name, '')
        
        # Remove problematic text from outputs
        self.data_extraction.clean_up(all_variables)
       
        if verbose:
            self.data_extraction.verbose_display(all_variables)
        
        if save_file:
            outfile1 = self.data_extraction.save_dataframe(all_variables, "_DataFrame1.csv", standard_info=True)
        
        return all_variables, outfile1


    def make_dataframe_2(self, save_file=True, clean_cols=False, verbose=True):
        """
        Extracts data from the sources defined in the current instance of the 
        DataExtraction class, and returns a pandas DataFrame with the relevant 
        variables for further cleaning and analysis.

        Args:
        - save_file (bool): Whether or not to save the resulting dataframe to a file.
        - clean_cols (bool): Whether or not to add empty columns per variable for data checkers to log changes.
        - verbose (bool): Whether or not to display information about the extraction process.

        Returns:
        - all_variables: a pandas DataFrame with the relevant variables included.
        - outfile2 (str or None): the name of the output CSV file, 
          if `save_file=True`. If `save_file=False`, returns `None`.
        """
        eppiid_df = self.data_extraction.retrieve_metadata("ItemId", "id")
        author_df = self.data_extraction.retrieve_metadata("ShortTitle", "pub_author")
        year_df = self.data_extraction.retrieve_metadata("Year", "pub_year")
        admin_strand_data = self.data_extraction.retrieve_data(admin_strand_output, "strand_raw")
        admin_strand_info = self.data_extraction.retrieve_info(admin_strand_output, "strand_info")
        toolkit_version_data = self.data_extraction.retrieve_data(toolkit_versions, "toolkit_version")
        intervention_name_ht = self.data_extraction.retrieve_ht(int_name_output, "int_name_ht")
        intervention_name_info = self.data_extraction.retrieve_info(int_name_output, "int_name_info")
        intervention_desc_ht = self.data_extraction.retrieve_ht(intervention_description_output, "int_desc_ht")
        intervention_desc_info = self.data_extraction.retrieve_info(intervention_description_output, "int_desc_info")
        intervention_objec_ht = self.data_extraction.retrieve_ht(intervention_objectives_output, "int_objec_ht")
        intervention_objec_info = self.data_extraction.retrieve_info(intervention_objectives_output, "int_objec_info")
        intervention_org_type_data = self.data_extraction.retrieve_data(int_org_type_output, "int_prov_raw")
        intervention_org_type_ht = self.data_extraction.retrieve_ht(int_org_type_output, "int_prov_ht")
        intervention_org_type_info = self.data_extraction.retrieve_info(int_org_type_output, "int_prov_info")
        intervention_training_prov_data = self.data_extraction.retrieve_data(int_training_provided_output, "int_training_raw")
        intervention_training_prov_ht = self.data_extraction.retrieve_ht(int_training_provided_output, "int_training_ht")
        intervention_training_prov_info = self.data_extraction.retrieve_info(int_training_provided_output, "int_training_info")
        intervention_focus_data = self.data_extraction.retrieve_data(int_focus_output, "int_part_raw")
        intervention_focus_ht = self.data_extraction.retrieve_ht(int_focus_output, "int_part_ht")
        intervention_focus_info= self.data_extraction.retrieve_info(int_focus_output, "int_part_info")
        intervention_teaching_app_data = self.data_extraction.retrieve_data(intervention_teaching_approach, "int_approach_raw")
        intervention_teaching_app_ht = self.data_extraction.retrieve_ht(intervention_teaching_approach, "int_approach_ht")
        intervention_teaching_app_info = self.data_extraction.retrieve_info(intervention_teaching_approach, "int_approach_info")
        digit_tech_data = self.data_extraction.retrieve_data(int_appr_dig_tech, "digit_tech_raw")
        digit_tech_ht = self.data_extraction.retrieve_ht(int_appr_dig_tech, "digit_tech_ht")
        digit_tech_info = self.data_extraction.retrieve_info(int_appr_dig_tech, "digit_tech_info")
        par_eng_data = self.data_extraction.retrieve_data(int_appr_par_or_comm_vol, "parent_partic_raw")
        par_eng_ht= self.data_extraction.retrieve_ht(int_appr_par_or_comm_vol, "parent_partic_ht")
        par_eng_info = self.data_extraction.retrieve_info(int_appr_par_or_comm_vol, "parent_partic_info")
        intervention_time_data = self.data_extraction.retrieve_data(intervention_time_output, "int_when_raw")
        intervention_time_ht = self.data_extraction.retrieve_ht(intervention_time_output, "int_when_ht")
        intervention_time_info = self.data_extraction.retrieve_info(intervention_time_output, "int_when_info")
        intervention_delivery_data = self.data_extraction.retrieve_data(intervention_delivery_output, "int_who_raw")
        intervention_delivery_ht = self.data_extraction.retrieve_ht(intervention_delivery_output, "int_who_ht")
        intervention_delivery_info = self.data_extraction.retrieve_info(intervention_delivery_output, "int_who_info")
        intervention_duration_ht = self.data_extraction.retrieve_ht(int_dur_output, "int_dur_ht")
        intervention_duration_info = self.data_extraction.retrieve_info(int_dur_output, "int_dur_info")
        intervention_frequency_ht = self.data_extraction.retrieve_ht(inte_freq_output, "int_freq_ht")
        intervention_frequency_info = self.data_extraction.retrieve_info(inte_freq_output, "int_freq_info")
        intervention_sess_length_ht = self.data_extraction.retrieve_ht(intervention_session_length_output, "int_leng_ht")
        intervention_sess_length_info = self.data_extraction.retrieve_info(intervention_session_length_output, "int_leng_info")
        intervention_detail_data = self.data_extraction.retrieve_data(int_impl_details, "int_fidel_raw")
        intervention_detail_ht = self.data_extraction.retrieve_ht(int_impl_details, "int_fidel_ht")
        intervention_detail_info = self.data_extraction.retrieve_info(int_impl_details, "int_fidel_info")
        intervention_costs_data = self.data_extraction.retrieve_data(int_costs_reported, "int_cost_raw")
        intervention_costs_ht = self.data_extraction.retrieve_ht(int_costs_reported, "int_cost_ht")
        intervention_costs_info = self.data_extraction.retrieve_info(int_costs_reported, "int_cost_info")
        #int_evaluation = self.data_extraction.retrieve_data(int_eval_output, "out_eval_raw")    
        #int_evaluation_ht = self.data_extraction.retrieve_ht(int_eval, "out_eval_ht")
        #int_evaluation_info = self.data_extraction.retrieve_info(int_eval, "out_eval_info")
        int_evaluation = int_eval()
        baseline_diff_data = self.data_extraction.retrieve_data(baseline_diff_output, "base_diff_raw")    
        baseline_diff_ht = self.data_extraction.retrieve_ht(baseline_diff_output, "base_diff_ht")
        baseline_diff_info = self.data_extraction.retrieve_info(baseline_diff_output, "base_diff_info")
        comp_anal_data = self.data_extraction.retrieve_data(comparability_output, "comp_anal_raw")    
        comp_anal_ht = self.data_extraction.retrieve_ht(comparability_output, "comp_anal_ht")
        comp_anal_info = self.data_extraction.retrieve_info(comparability_output, "comp_anal_info")
        comp_var_rep_data = self.data_extraction.retrieve_data(comp_vars_rep, "comp_var__raw")    
        comp_var_rep_ht = self.data_extraction.retrieve_ht(comp_vars_rep, "comp_var__ht")
        comp_var_rep_info = self.data_extraction.retrieve_info(comp_vars_rep, "comp_var__info")
        comp_var_rep_which_data = self.data_extraction.retrieve_data(which_comp_vars_rep_output, "comp_var_rep_raw")    
        comp_var_rep_which_ht = self.data_extraction.retrieve_ht(which_comp_vars_rep_output, "comp_var_rep_ht")
        comp_var_rep_which_info = self.data_extraction.retrieve_info(which_comp_vars_rep_output, "comp_var_rep_info")
        clustering_data = self.data_extraction.retrieve_data(clustering_output, "clust_anal_raw")    
        clustering_ht = self.data_extraction.retrieve_ht(clustering_output, "clust_anal_ht")
        clustering_info = self.data_extraction.retrieve_info(clustering_output, "clust_anal_info")
        
        all_variables = pd.concat([
            eppiid_df,
            author_df,
            year_df,
            admin_strand_data,
            admin_strand_info,
            toolkit_version_data,
            intervention_name_ht,
            intervention_name_info,
            intervention_desc_ht,
            intervention_desc_info,
            intervention_objec_ht,
            intervention_objec_info,
            intervention_org_type_data,
            intervention_org_type_ht,
            intervention_org_type_info,
            intervention_training_prov_data,
            intervention_training_prov_ht,
            intervention_training_prov_info,
            intervention_focus_data,
            intervention_focus_ht,
            intervention_focus_info,
            intervention_teaching_app_data,
            intervention_teaching_app_ht,
            intervention_teaching_app_info,
            digit_tech_data,
            digit_tech_ht,
            digit_tech_info,
            par_eng_data,
            par_eng_ht,
            par_eng_info,
            intervention_time_data,
            intervention_time_ht,
            intervention_time_info,
            intervention_delivery_data,
            intervention_delivery_ht,
            intervention_delivery_info,
            intervention_duration_ht,
            intervention_duration_info,
            intervention_frequency_ht,
            intervention_frequency_info,
            intervention_sess_length_ht,
            intervention_sess_length_info, 
            intervention_detail_data,
            intervention_detail_ht,
            intervention_detail_info,
            intervention_costs_data,
            intervention_costs_ht,
            intervention_costs_info,
            int_evaluation,
            #int_evaluation,
            #int_evaluation_ht,
            #int_evaluation_info,
            baseline_diff_data,
            baseline_diff_ht,
            baseline_diff_info,
            comp_anal_data,
            comp_anal_ht,
            comp_anal_info,
            comp_var_rep_data, 
            comp_var_rep_ht,
            comp_var_rep_info,
            comp_var_rep_which_data,   
            comp_var_rep_which_ht,
            comp_var_rep_which_info,
            clustering_data,    
            clustering_ht,
            clustering_info,
        ], axis=1, sort=False)
        all_variables["eef_eval_raw"] = all_variables["out_eval_raw"].map(
                    set(["Is this an EEF evaluation?"]).issubset).astype(int)
        all_variables["eef_eval_raw"] = all_variables["eef_eval_raw"].replace(
                    to_replace=[0, 1], value=["No", "Yes"])
        
        if clean_cols:
            cols_to_insert = {
                'strand_CLEAN': 5,
                'int_name_CLEAN': 9,
                'int_desc_CLEAN': 12,
                'int_objec_CLEAN': 15,
                'int_prov_CLEAN': 19,
                'int_training_CLEAN': 23,
                'int_part_CLEAN': 27,
                'int_approach_CLEAN': 31,
                'digital_tech_CLEAN': 35,
                'parent_partic_CLEAN': 39,
                'int_when_CLEAN': 43,
                'int_who_CLEAN': 47,
                'int_dur_CLEAN': 50,
                'int_freq_CLEAN': 53,
                'int_leng_CLEAN': 56,
                'int_fidel_CLEAN': 60,
                'int_cost_CLEAN': 64,
                'out_eval_CLEAN': 68,
                'eef_eval_CLEAN': 70,
                'base_diff_CLEAN': 74,
                'comp_anal_CLEAN': 78,
                'comp_var_CLEAN': 82,
                'comp_var_rep_CLEAN': 86,
                'clust_anal_CLEAN': 90
            }
            for col_name, col_idx in cols_to_insert.items():
                all_variables.insert(col_idx, col_name, '')
        
        self.data_extraction.clean_up(all_variables)
        all_variables.replace(r'^\s*$', "NA", regex=True)
        
        if verbose:
            self.data_extraction.verbose_display(all_variables)
        
        if save_file:
            outfile2 = self.data_extraction.save_dataframe(all_variables, "_DataFrame2.csv", standard_info=True)
        
        return all_variables, outfile2


    def make_dataframe_3(self, save_file=True, clean_cols=False, verbose=False):
        """
        Extracts data from the sources defined in the current instance of the 
        DataExtraction class, and returns a pandas DataFrame with the relevant 
        variables for further cleaning and analysis.

        Args:
        - save_file (bool): Whether or not to save the resulting dataframe to a file.
        - clean_cols (bool): Whether or not to add empty columns per variable 
          for data checkers to log changes.
        - verbose (bool): Whether or not to display information about the extraction process.

        Returns:
        - all_variables: a pandas DataFrame with the relevant variables included.
        - outfile3 (str or None): the name of the output CSV file, 
          if `save_file=True`. If `save_file=False`, returns `None`.
        """
        eppiid_df = self.data_extraction.retrieve_metadata("ItemId", "id")
        author_df = self.data_extraction.retrieve_metadata("ShortTitle", "pub_author")
        year_df = self.data_extraction.retrieve_metadata("Year", "pub_year")
        admin_strand_data = self.data_extraction.retrieve_data(admin_strand_output, "strand_raw")
        admin_strand_info = self.data_extraction.retrieve_info(admin_strand_output, "strand_info")
        toolkit_version_data = self.data_extraction.retrieve_data(toolkit_versions, "toolkit_version")
        gender_df = self.data_extraction.retrieve_data(student_gender, "part_gen_raw")
        gender_ht_df = self.data_extraction.retrieve_ht(student_gender, "part_gen_ht")
        gender_comments_df = self.data_extraction.retrieve_info(student_gender, "part_gen_info")
        sample_size_comments_df = self.data_extraction.retrieve_info(sample_size_output, "sample_analysed_info")
        sample_size_ht_df = self.data_extraction.retrieve_ht(sample_size_output, "sample_analysed_ht")
        low_ses_percentage_Comments_df = self.data_extraction.retrieve_info(percentage_low_fsm_output, "fsm_perc_info")
        low_ses_percentage_HT_df = self.data_extraction.retrieve_ht(percentage_low_fsm_output, "fsm_perc_ht")
        further_ses_info_Comments_df = self.data_extraction.retrieve_info(further_ses_fsm_info_output, "fsm_info_info")
        further_ses_fsm_info_HT_df = self.data_extraction.retrieve_ht(further_ses_fsm_info_output, "fsm_info_ht")
        no_low_ses_fsm_info_df = self.data_extraction.retrieve_data(no_ses_fsm_info_provided_output, "fsm_na_raw")
        no_low_ses_fsm_info_comments_df = self.data_extraction.retrieve_info(no_ses_fsm_info_provided_output, "fsm_na_info")
        sample_size_intervention_HT_df = self.data_extraction.retrieve_ht(sample_size_intervention_output, "base_n_treat_ht")
        sample_size_intervention_Comments_df = self.data_extraction.retrieve_info(sample_size_intervention_output, "base_n_treat_info")
        sample_size_control_HT_df = self.data_extraction.retrieve_ht(sample_size_control_output,"base_n_cont_ht")
        sample_size_control_Comments_df = self.data_extraction.retrieve_info(sample_size_control_output,"base_n_cont_info")
        sample_size_second_intervention_HT_df = self.data_extraction.retrieve_ht(sample_size_second_intervention_output, "base_n_treat2_ht")
        sample_size_second_intervention_Comments_df = self.data_extraction.retrieve_info(sample_size_second_intervention_output, "base_n_treat2_info")
        sample_size_third_intervention_HT_df = self.data_extraction.retrieve_ht(sample_size_third_intervention_output, "base_n_treat3_ht")
        sample_size_third_intervention_Comments_df = self.data_extraction.retrieve_info(sample_size_third_intervention_output, "base_n_treat3_info")
        sample_size_anal_int_df = self.data_extraction.retrieve_ht(samp_size_anal_int_output, "n_treat_ht")
        sample_size_anal_int_comments_df = self.data_extraction.retrieve_info(samp_size_anal_int_output, "n_treat_info")
        sample_size_anal_cont_df = self.data_extraction.retrieve_ht(samp_size_anal_cont_output, "n_cont_ht")
        sample_size_anal_cont_comments_df = self.data_extraction.retrieve_info(samp_size_anal_cont_output, "n_cont_info")
        sample_size_anal_sec_int_df = self.data_extraction.retrieve_ht(samp_size_anal_sec_int_output, "n_treat2_ht")
        sample_size_anal_sec_int_comments_df = self.data_extraction.retrieve_info(samp_size_anal_sec_int_output, "n_treat2_info")
        sample_size_anal_sec_cont_df = self.data_extraction.retrieve_ht(samp_size_anal_sec_cont_output, "n_cont2_ht")
        sample_size_anal_sec_cont_comments_df = self.data_extraction.retrieve_info(samp_size_anal_sec_cont_output, "n_cont2_info")
        attr_dropout_rep_df = self.data_extraction.retrieve_data(attr_dropout_rep_output, "attri_raw")
        attr_dropout_rep_HT_df = self.data_extraction.retrieve_ht(attr_dropout_rep_output, "attri_ht")
        attr_dropout_rep_comments_df = self.data_extraction.retrieve_info(attr_dropout_rep_output, "attri_info")
        treat_grp_attr_HT_df = self.data_extraction.retrieve_ht(treat_grp_attr, "attri_treat_ht")
        treat_grp_attr_comments_df = self.data_extraction.retrieve_info(treat_grp_attr, "attri_treat_info")
        overall_perc_attr_HT_df = self.data_extraction.retrieve_ht(overall_perc_attr, "attri_perc_ht")
        overall_perc_attr_comments_df = self.data_extraction.retrieve_info(overall_perc_attr, "attri_perc_info")
        all_variables = pd.concat([
            eppiid_df,
            author_df,
            year_df,
            admin_strand_data,
            admin_strand_info,
            toolkit_version_data,
            sample_size_comments_df,
            sample_size_ht_df,
            gender_df,
            gender_ht_df,
            gender_comments_df,
            low_ses_percentage_Comments_df,
            low_ses_percentage_HT_df,
            further_ses_info_Comments_df,
            further_ses_fsm_info_HT_df,
            no_low_ses_fsm_info_df,
            no_low_ses_fsm_info_comments_df,
            sample_size_intervention_HT_df,
            sample_size_intervention_Comments_df,
            sample_size_control_HT_df,
            sample_size_control_Comments_df,
            sample_size_second_intervention_HT_df,
            sample_size_second_intervention_Comments_df,
            sample_size_third_intervention_HT_df,
            sample_size_third_intervention_Comments_df,
            sample_size_anal_int_df,
            sample_size_anal_int_comments_df,
            sample_size_anal_cont_df,
            sample_size_anal_cont_comments_df,
            sample_size_anal_sec_int_df,
            sample_size_anal_sec_int_comments_df,
            sample_size_anal_sec_cont_df,
            sample_size_anal_sec_cont_comments_df,
            attr_dropout_rep_df,
            attr_dropout_rep_HT_df,
            attr_dropout_rep_comments_df,
            treat_grp_attr_HT_df,
            treat_grp_attr_comments_df,
            overall_perc_attr_HT_df,
            overall_perc_attr_comments_df,
        ], axis=1, sort=False)
        
        if clean_cols:
            # Insert empty columns per variable for data checkers to log changes
            cols_to_insert = {
                'strand_CLEAN': 5,
                'sample_analysed_CLEAN': 9,
                'part_gen_CLEAN': 13,
                'fsm_perc_CLEAN': 16,
                'fsm_info_CLEAN': 19,
                'fsm_na_CLEAN': 22,
                'base_n_treat_CLEAN': 25,
                'base_n_cont_CLEAN': 28,
                'base_n_treat2_CLEAN': 31,
                'base_n_treat3_CLEAN': 34,
                'n_treat_CLEAN': 37,
                'n_cont_CLEAN': 40,
                'n_treat2_CLEAN': 43,
                'n_cont2_CLEAN': 46,
                'attri_CLEAN': 50,
                'attri_treat_CLEAN': 53,
                'attri_perc_CLEAN': 56,
            }

            # Insert empty columns at specified locations
            for col_name, col_idx in cols_to_insert.items():
                all_variables.insert(col_idx, col_name, '')
        
        all_variables.replace('\r', ' ', regex=True, inplace=True)
        all_variables.replace('\n', ' ', regex=True, inplace=True)
        all_variables.replace(':', ' ',  regex=True, inplace=True)
        all_variables.replace(';', ' ',  regex=True, inplace=True)
        
        if verbose:
            self.data_extraction.verbose_display(all_variables)
        
        if save_file:
            outfile3 = self.data_extraction.save_dataframe(all_variables, "_DataFrame3_Sample_Size.csv", standard_info=True)
        
        return all_variables, outfile3


    def make_dataframe_4(self, save_file=True, clean_cols=True, verbose=True):
        """
        Extracts data from the sources defined in the current instance of the 
        DataExtraction class, and returns a pandas DataFrame with the relevant 
        variables for further cleaning and analysis.

        Args:
        - save_file (bool): Whether or not to save the resulting dataframe to a file.
        - clean_cols (bool): Whether or not to add empty columns per variable for 
          data checkers to log changes.
        - verbose (bool): Whether or not to display information about the extraction process.

        Returns:
        - all_variables: a pandas DataFrame with the relevant variables included.
        - outfile4 (str or None): the name of the output CSV file, 
          if `save_file=True`. If `save_file=False`, returns `None`.

        Notes:
            The returned DataFrame has 85 columns.
        """
        try:
            eppiid_df = self.data_extraction.retrieve_metadata("ItemId", "id")
            author_df = self.data_extraction.retrieve_metadata("ShortTitle", "pub_author")
            year_df = self.data_extraction.retrieve_metadata("Year", "pub_year")
            admin_strand_data = self.data_extraction.retrieve_data(admin_strand_output, "strand_raw")
            admin_strand_info = self.data_extraction.retrieve_info(admin_strand_output, "strand_info") 
            toolkit_version_data = self.data_extraction.retrieve_data(toolkit_versions, "toolkit_version")
            desc_stats_prim_out_rep_df = self.data_extraction.retrieve_data(desc_stats_primary_outcome, "desc_stats_raw")
            desc_stats_prim_out_rep_ht_df = self.data_extraction.retrieve_ht(desc_stats_primary_outcome, "desc_stats_ht")
            descs_tats_prim_out_rep_comments_df = self.data_extraction.retrieve_info(desc_stats_primary_outcome, "desc_stats_info")
            int_grp_num_ht_df = self.data_extraction.retrieve_ht(int_grp_number, "n_treat_ht")
            int_grp_num_comments_df = self.data_extraction.process_info(int_grp_number, "n_treat_info")
            int_grp_pretest_mean_ht_df = self.data_extraction.retrieve_ht(int_grp_pretest_mean, "pre_t_mean_ht")
            int_grp_pretest_mean_comments_df = self.data_extraction.retrieve_info(int_grp_pretest_mean, "pre_t_mean_info")
            int_grp_pretest_sd_ht_df = self.data_extraction.retrieve_ht(int_grp_pretest_sd, "pre_t_sd_ht")
            int_grp_pretest_sd_comments_df = self.data_extraction.retrieve_info(int_grp_pretest_sd, "pre_t_sd_info")
            int_grp_posttest_mean_ht_df = self.data_extraction.retrieve_ht(intn_grp_posttest_mean, "post_t_mean_ht_t_sd_ht")
            int_grp_posttest_mean_comments_df = self.data_extraction.retrieve_info(intn_grp_posttest_mean, "post_t_mean_info")
            int_grp_posttest_sd_ht_df = self.data_extraction.retrieve_ht(int_grp_posttest_sd, "post_t_sd_ht")
            int_grp_posttest_sd_comments_df = self.data_extraction.retrieve_info(int_grp_posttest_sd, "post_t_sd_info")
            int_grp_gain_score_mean_ht_df = self.data_extraction.retrieve_ht(int_grp_gain_score_mean, "gain_t_mean_ht")
            int_grp_gain_score_mean_comments_df = self.data_extraction.retrieve_info(int_grp_gain_score_mean, "gain_t_mean_info")
            int_grp_gain_score_sd_ht_df = self.data_extraction.retrieve_ht(int_grp_gain_score_sd, "gain_t_sd_ht")
            int_grp_gain_score_sd_comments_df = self.data_extraction.retrieve_info(int_grp_gain_score_sd, "gain_t_sd_info")
            int_grp_other_info_ht_df = self.data_extraction.retrieve_ht(int_grp_any_other_info, "out_t_other_ht")
            int_grp_other_info_comments_df = self.data_extraction.retrieve_info(int_grp_any_other_info, "out_t_other_info")
            ctrl_grp_num_ht_df = self.data_extraction.retrieve_ht(ctrl_grp_number, "n_cont_ht")
            ctrl_grp_num_comments_df = self.data_extraction.retrieve_info(ctrl_grp_number, "n_cont_info")
            ctrl_grp_pretest_mean_ht_df = self.data_extraction.retrieve_ht(ctrl_grp_pretest_mean, "pre_c_mean_ht")
            ctrl_grp_pretest_mean_comments_df = self.data_extraction.retrieve_info(ctrl_grp_pretest_mean, "pre_c_mean_info")
            ctrl_grp_pretest_sd_ht_df = self.data_extraction.retrieve_ht(ctrl_grp_pretest_sd, "pre_c_sd_ht")
            ctrl_grp_pretest_sd_comments_df = self.data_extraction.retrieve_info(ctrl_grp_pretest_sd, "pre_c_sd_info")
            ctrl_grp_post_test_mean_ht_df = self.data_extraction.retrieve_ht(ctrl_grp_posttest_mean, "post_c_mean_ht")
            ctrl_grp_post_test_mean_comments_df = self.data_extraction.retrieve_info(ctrl_grp_posttest_mean, "post_c_mean_info")
            ctrl_grp_post_test_sd_ht_df = self.data_extraction.retrieve_ht(ctrl_grp_posttest_sd, "post_c_sd_ht")
            ctrl_grp_post_test_sd_comments_df = self.data_extraction.retrieve_info(ctrl_grp_posttest_sd, "post_c_sd_info")
            Ctrl_grp_gain_score_mean_ht_df = self.data_extraction.retrieve_ht(ctrl_grp_gain_score_mean, "gain_c_mean_ht")
            ctrl_grp_gain_score_mean_comments_df = self.data_extraction.retrieve_info(ctrl_grp_gain_score_mean, "gain_c_mean_info")
            ctrl_grp_gain_score_sd_ht_df = self.data_extraction.retrieve_ht(ctrl_grp_gain_score_sd, "gain_c_sd_ht")
            ctrl_grp_gain_score_sd_comments_df = self.data_extraction.retrieve_info(ctrl_grp_gain_score_sd, "gain_c_sd_info")
            ctrl_grp_other_info_ht_df = self.data_extraction.retrieve_ht(ctrl_grp_any_other_info, "out_c_other_ht")
            ctrl_grp_other_info_comments_df = self.data_extraction.retrieve_info(ctrl_grp_any_other_info, "out_c_other_info")
            int_grp_num2_ht_df = self.data_extraction.retrieve_ht(int_grp_two_number, "n_treat2_ht")
            int_grp_num2_comments_df = self.data_extraction.retrieve_info(int_grp_two_number, "n_treat2_info")
            int_grp_pretest2_mean_ht_df = self.data_extraction.retrieve_ht(int_grp_two_pretest_mean, "pre_t2_mean_ht")
            int_grp_pretest2_mean_comments_df = self.data_extraction.retrieve_info(int_grp_two_pretest_mean, "pre_t2_mean_info")
            int_grp_pretest2_sd_ht_df = self.data_extraction.retrieve_ht(int_grp_two_pretest_sd, "pre_t2_sd_ht")
            int_grp_pretest2_sd_comments_df = self.data_extraction.retrieve_info(int_grp_two_pretest_sd, "pre_t2_sd_info")
            int_grp_post2_test_mean_ht_df = self.data_extraction.retrieve_ht(int_grp_two_posttest_mean, "post_t2_mean_ht")
            int_grp_post2_test_mean_comments_df = self.data_extraction.retrieve_info(int_grp_two_posttest_mean, "post_t2_mean_info")
            int_grp_post2_test_sd_ht_df = self.data_extraction.retrieve_ht(int_grp_two_posttest_sd, "post_t2_sd_ht")
            int_grp_post2_test_sd_comments_df = self.data_extraction.retrieve_info(int_grp_two_posttest_sd, "post_t2_sd_info")
            int_grp_gain2_score_mean_ht_df = self.data_extraction.retrieve_ht(int_grp_two_gain_score_mean, "gain_t2_mean_ht")
            int_grp_gain2_score_mean_comments_df = self.data_extraction.retrieve_info(int_grp_two_gain_score_mean, "gain_t2_mean_info")
            int_grp_gain2_score_sd_ht_df = self.data_extraction.retrieve_ht(int_grp_two_gain_score_sd, "gain_t2_sd_ht")
            int_grp_gain2_score_sd_comments_df = self.data_extraction.retrieve_info(int_grp_two_gain_score_sd, "gain_t2_sd_info")
            int_grp_other2_info_ht_df = self.data_extraction.retrieve_ht(int_grp_two_any_other_info, "out_t2_other_ht")
            int_grp_other2_info_comments_df = self.data_extraction.retrieve_info(int_grp_two_any_other_info, "out_t2_other_info")
            ctrl_grp_num2_ht_df = self.data_extraction.retrieve_ht(control_group_two_number, "n_cont2_ht")
            ctrl_grp_num2_comments_df = self.data_extraction.retrieve_info(control_group_two_number, "n_cont2_info")
            ctrl_grp_pretest2_mean_ht_df = self.data_extraction.retrieve_ht(control_group_two_pretest_mean, "pre_c2_mean_ht")
            ctrl_grp_pretest2_mean_comments_df = self.data_extraction.retrieve_info(control_group_two_pretest_mean, "pre_c2_mean_info")
            ctrl_grp_pretest2_sd_ht_df = self.data_extraction.retrieve_ht(control_group_two_pretest_sd, "pre_c2_sd_ht")
            ctrl_grp_pretest2_sd_comments_df = self.data_extraction.retrieve_info(control_group_two_pretest_sd, "pre_c2_sd_info")
            ctrl_grp_post2_test_mean_ht_df = self.data_extraction.retrieve_ht(control_group_two_posttest_mean, "post_c2_mean_ht")
            ctrl_grp_post2_test_mean_comments_df = self.data_extraction.retrieve_info(control_group_two_posttest_mean, "post_c2_mean_info")
            ctrl_grp_post2_test_sd_ht_df = self.data_extraction.retrieve_ht(control_group_two_posttest_sd, "post_c2_sd_ht")
            ctrl_grp_post2_test_sd_comments_df = self.data_extraction.retrieve_info(control_group_two_posttest_sd, "post_c2_sd_info")
            Ctrl_grp_gain2_score_mean_ht_df = self.data_extraction.retrieve_ht(control_group_two_gain_score_mean, "gain_c2_mean_ht")
            ctrl_grp_gain2_score_mean_comments_df = self.data_extraction.retrieve_info(control_group_two_gain_score_mean, "gain_c2_mean_info")
            ctrl_grp_gain2_score_sd_ht_df = self.data_extraction.retrieve_ht(control_group_two_gain_score_sd, "gain_c2_sd_ht")
            ctrl_grp_gain2_score_sd_comments_df = self.data_extraction.retrieve_info(control_group_two_gain_score_sd, "gain_c2_sd_info")
            ctrl_grp_other2_info_ht_df = self.data_extraction.retrieve_ht(control_group_two_any_other_info, "out_c2_other_ht")
            ctrl_grp_other2_info_comments_df = self.data_extraction.retrieve_info(control_group_two_any_other_info, "out_c2_other_info")
            followupdata = self.data_extraction.retrieve_data(follow_up_data_reported, "follow_up_raw")
            followupdata_HT = self.data_extraction.retrieve_ht(follow_up_data_reported, "follow_up_ht")
            followupdata_comments = self.data_extraction.retrieve_info(follow_up_data_reported, "follow_up_info")
            
            all_variables = pd.concat([
                eppiid_df,
                author_df,
                year_df,
                admin_strand_data,
                admin_strand_info,
                toolkit_version_data,
                desc_stats_prim_out_rep_df,
                desc_stats_prim_out_rep_ht_df,
                descs_tats_prim_out_rep_comments_df,
                int_grp_num_ht_df,
                int_grp_num_comments_df,
                int_grp_pretest_mean_ht_df,
                int_grp_pretest_mean_comments_df,
                int_grp_pretest_sd_ht_df,
                int_grp_pretest_sd_comments_df,
                int_grp_posttest_mean_ht_df,
                int_grp_posttest_mean_comments_df,
                int_grp_posttest_sd_ht_df,
                int_grp_posttest_sd_comments_df,
                int_grp_gain_score_mean_ht_df,
                int_grp_gain_score_mean_comments_df,
                int_grp_gain_score_sd_ht_df,
                int_grp_gain_score_sd_comments_df,
                int_grp_other_info_ht_df,
                int_grp_other_info_comments_df,
                ctrl_grp_num_ht_df,
                ctrl_grp_num_comments_df,
                ctrl_grp_pretest_mean_ht_df,
                ctrl_grp_pretest_mean_comments_df,
                ctrl_grp_pretest_sd_ht_df,
                ctrl_grp_pretest_sd_comments_df,
                ctrl_grp_post_test_mean_ht_df,
                ctrl_grp_post_test_mean_comments_df,
                ctrl_grp_post_test_sd_ht_df,
                ctrl_grp_post_test_sd_comments_df,
                Ctrl_grp_gain_score_mean_ht_df,
                ctrl_grp_gain_score_mean_comments_df,
                ctrl_grp_gain_score_sd_ht_df,
                ctrl_grp_gain_score_sd_comments_df,
                ctrl_grp_other_info_ht_df,
                ctrl_grp_other_info_comments_df,
                int_grp_num2_ht_df,
                int_grp_num2_comments_df,
                int_grp_pretest2_mean_ht_df,
                int_grp_pretest2_mean_comments_df,
                int_grp_pretest2_sd_ht_df,
                int_grp_pretest2_sd_comments_df,
                int_grp_post2_test_mean_ht_df,
                int_grp_post2_test_mean_comments_df,
                int_grp_post2_test_sd_ht_df,
                int_grp_post2_test_sd_comments_df,
                int_grp_gain2_score_mean_ht_df,
                int_grp_gain2_score_mean_comments_df,
                int_grp_gain2_score_sd_ht_df,
                int_grp_gain2_score_sd_comments_df,
                int_grp_other2_info_ht_df,
                int_grp_other2_info_comments_df,
                ctrl_grp_num2_ht_df,
                ctrl_grp_num2_comments_df,
                ctrl_grp_pretest2_mean_ht_df,
                ctrl_grp_pretest2_mean_comments_df,
                ctrl_grp_pretest2_sd_ht_df,
                ctrl_grp_pretest2_sd_comments_df,
                ctrl_grp_post2_test_mean_ht_df,
                ctrl_grp_post2_test_mean_comments_df,
                ctrl_grp_post2_test_sd_ht_df,
                ctrl_grp_post2_test_sd_comments_df,
                Ctrl_grp_gain2_score_mean_ht_df,
                ctrl_grp_gain2_score_mean_comments_df,
                ctrl_grp_gain2_score_sd_ht_df,
                ctrl_grp_gain2_score_sd_comments_df,
                ctrl_grp_other2_info_ht_df,
                ctrl_grp_other2_info_comments_df,
                followupdata,
                followupdata_HT,
                followupdata_comments,
            ], axis=1, sort=False)
            
            if clean_cols:
                # Define columns to insert and their corresponding indices
                cols_to_insert = {
                    'desc_stats_CLEAN': 9,
                    'n_treat_CLEAN': 12,
                    'pre_t_mean_CLEAN': 15,
                    'pre_t_sd_CLEAN': 18,
                    'post_t_mean_CLEAN': 21,
                    'post_t_sd_CLEAN': 24,
                    'gain_t_mean_CLEAN': 27,
                    'gain_t_sd_CLEAN': 30,
                    'out_t_other_CLEAN': 33,
                    'n_cont_ht_CLEAN': 36,
                    'pre_c_mean_CLEAN': 39,
                    'pre_c_sd_CLEAN': 42,
                    'post_c_mean_CLEAN': 45,
                    'post_c_sd_CLEAN': 48,
                    'gain_c_mean_CLEAN': 51,
                    'gain_c_sd_CLEAN': 54,
                    'out_c_other_CLEAN': 57,
                    'n_treat2_CLEAN': 60,
                    'pre_t2_mean_CLEAN': 63,
                    'pre_t2_sd_CLEAN': 66,
                    'post_t2_mean_CLEAN': 69,
                    'post_t2_sd_CLEAN': 72,
                    'gain_t2_mean_CLEAN': 75,
                    'gain_t2_sd_CLEAN': 78,
                    'out_t2_other_CLEAN': 81,
                    'n_cont2_CLEAN': 84,
                    'pre_c2_mean_CLEAN': 87,
                    'pre_c2_sd_CLEAN': 90,
                    'post_c2_mean_CLEAN': 93,
                    'post_c2_sd_CLEAN': 96,
                    'gain_c2_mean_CLEAN': 99,
                    'gain_c2_sd_CLEAN': 102,
                    'out_c2_other_CLEAN': 105,
                    'follow_up_CLEAN': 109
                }

                # Insert empty columns at specified locations
                for col_name, col_idx in cols_to_insert.items():
                    all_variables.insert(col_idx, col_name, '')
                
                """ # Create a new dataframe with the inserted columns
                new_columns = {col_name: pd.Series('', index=all_variables.index) for col_name in cols_to_insert.keys()}
                new_dataframe = all_variables.assign(**new_columns)

                # Reorder the columns to preserve the original order
                all_variables = new_dataframe.reindex(columns=list(all_variables.columns) + list(cols_to_insert.keys())) """
                    
                #self.data_extraction.clean_up(all_variables)

            all_variables.replace('\r', ' ', regex=True, inplace=True)
            all_variables.replace('\n', ' ', regex=True, inplace=True)
            all_variables.replace(':', ' ',  regex=True, inplace=True)
            all_variables.replace(';', ' ',  regex=True, inplace=True)

            if verbose:
                self.data_extraction.verbose_display(all_variables)
            if save_file:
                outfile4 = self.data_extraction.save_dataframe(all_variables, "_DataFrame4_Effect_Size_A.csv", standard_info=True)
            
            return all_variables, outfile4
        except:
            pass


    def make_dataframe_5(self, save_file=True, clean_cols=True, verbose=True):
        """
        Extracts data from various sources and returns a pandas DataFrame with 
        relevant variables for further cleaning and analysis.
        
        Args:
        - self (object): An instance of the DataExtraction class.
        - save_file (bool, optional): Whether or not to save the resulting 
          DataFrame to a file. Defaults to True.
        - clean_cols (bool, optional): Whether or not to add empty columns per 
          variable for data checkers to log changes. Defaults to True.
        - verbose (bool, optional): Whether or not to display information 
          about the extraction process. Defaults to True.
            
        Returns:
        - tuple: A tuple containing the resulting DataFrame and the name of the 
          output CSV file, if `save_file=True`.
            
        Notes:
            The returned DataFrame contains 85 columns.
        """
        OUTCOME_VARS = (
            "out_type_",
            "smd_",
            "se_",
            "ci_lower_",
            "ci_upper_",
            "out_label_",
            "out_samp_",
            "out_comp_",
            "out_es_type_",
            "out_measure_",
            "out_tit_",
            "out_g1_n_",
            "out_g2_n_",
            "out_g1_mean_",
            "out_g2_mean_",
            "out_g1_sd_",
            "out_g2_sd_",
            "out_desc_",
            "out_test_type_raw_"
        )
       
        eppiid_df = self.data_extraction.retrieve_metadata("ItemId", "id")
        author_df = self.data_extraction.retrieve_metadata("ShortTitle", "pub_author")
        year_df = self.data_extraction.retrieve_metadata("Year", "pub_year")
        admin_strand_data = self.data_extraction.retrieve_data(admin_strand_output, "strand_raw")
        admin_strand_info = self.data_extraction.retrieve_info(admin_strand_output, "strand_info")
        toolkit_version_data = self.data_extraction.retrieve_data(toolkit_versions, "toolkit_version")
        outcometype_df = self.data_extraction.get_outcome_data_lvl2(outcome_type_codes, "out_type_")
        smd_df = self.data_extraction.get_outcome_data_lvl1("SMD", "smd_")
        sesmd_df = self.data_extraction.get_outcome_data_lvl1("SESMD", "se_")
        cilowersmd_df = self.data_extraction.get_outcome_data_lvl1("CILowerSMD", "ci_lower_")
        ciuppersmd_df = self.data_extraction.get_outcome_data_lvl1("CIUpperSMD", "ci_upper_")
        outcome_df = self.data_extraction.get_outcome_data_lvl1("OutcomeText", "out_label_")
        sample_df = self.data_extraction.get_outcome_data_lvl2(sample_output, "out_samp_")
        sample_check = sample_main_check()
        out_comp_df = self.data_extraction.get_outcome_data_lvl1("ControlText", "out_comp_")
        effectsizetype_df = self.data_extraction.get_outcome_data_lvl2(es_type_output, "out_es_type_")
        outcome_measure_df = self.data_extraction.get_outcome_data_lvl1("InterventionText", "out_measure_")
        outcome_title_df = self.data_extraction.get_outcome_data_lvl1("Title", "out_tit_")
        group1N_df = group_desc_stats("Data1", "out_g1_n_")
        group2N_df = group_desc_stats("Data2", "out_g2_n_")
        group1mean_df = group_desc_stats("Data3", "out_g1_mean_")
        group2mean_df = group_desc_stats("Data4", "out_g2_mean_")
        group1sd_df = group_desc_stats("Data5", "out_g1_sd_")
        group2sd_df = group_desc_stats("Data6", "out_g2_sd_")
        outcome_description_df = self.data_extraction.get_outcome_data_lvl1("OutcomeDescription", "out_desc_")
        testtype_outcome_df = self.data_extraction.get_outcome_data_lvl2(test_type_output, "out_test_type_raw_")
        
        # Concatenate record detail data frames
        record_details_df = pd.concat([
            eppiid_df,
            author_df,
            year_df,
            admin_strand_data,
            admin_strand_info,
            toolkit_version_data,
        ], axis=1)
        
        # Concatenate all main dataframes
        df = pd.concat([
            outcometype_df,
            smd_df,
            sesmd_df,
            cilowersmd_df,
            ciuppersmd_df,
            outcome_df,
            sample_df,
            sample_check,
            out_comp_df,
            effectsizetype_df,
            outcome_measure_df,
            outcome_title_df,
            group1N_df,
            group2N_df,
            group1mean_df,
            group2mean_df,
            group1sd_df,
            group2sd_df,
            outcome_description_df,
            testtype_outcome_df
        ], axis=1)[list(interleave([
            outcometype_df,
            smd_df,
            sesmd_df,
            cilowersmd_df,
            ciuppersmd_df,
            outcome_df,
            sample_df,
            sample_check,
            out_comp_df,
            effectsizetype_df,
            outcome_measure_df,
            outcome_title_df,
            group1N_df,
            group2N_df,
            group1mean_df,
            group2mean_df,
            group1sd_df,
            group2sd_df,
            outcome_description_df,
            testtype_outcome_df
        ]))]
        
        # Initialize empty lists to hold data
        toolkit_lists = [[] for _ in range(19)]
        
        (toolkit_prim,
        toolkit_prim_smd,
        toolkit_prim_se,
        toolkit_prim_ci_lower,
        toolkit_prim_ci_upper,
        toolkit_prim_outcome,
        toolkit_prim_sample,
        toolkit_prim_outcomp,
        toolkit_es_type,
        toolkit_out_measure,
        toolkit_out_tit,
        toolkit_g1_n,
        toolkit_g2_n,
        toolkit_g1_mean,
        toolkit_g2_mean,
        toolkit_g1_sd,
        toolkit_g2_sd,
        toolkit_out_desc,
        toolkit_test_type) = toolkit_lists
        
        toolkit_lists = self.data_extraction.getOutcomeData(df, 'Toolkit primary outcome', toolkit_lists, OUTCOME_VARS)
        
        reading_lists = [[] for _ in range(19)]
        
        (reading_prim,
        reading_prim_smd,
        reading_prim_se,
        reading_prim_ci_lower,
        reading_prim_ci_upper,
        reading_prim_outcome,
        reading_prim_sample,
        reading_prim_outcomp,
        reading_prim_es_type,
        reading_prim_out_measure,
        reading_prim_out_tit,
        reading_prim_g1_n,
        reading_prim_g2_n,
        reading_prim_g1_mean,
        reading_prim_g2_mean,
        reading_prim_g1_sd,
        reading_prim_g2_sd,
        reading_prim_out_desc,
        reading_test_type) = reading_lists
        
        reading_lists = self.data_extraction.getOutcomeData(df, 'Reading primary outcome', reading_lists, OUTCOME_VARS)
        
        writing_and_spelling_lists = [[] for _ in range(19)]
        
        (Writing_and_spelling_prim,
        Writing_and_spelling_prim_smd,
        Writing_and_spelling_prim_se,
        Writing_and_spelling_prim_ci_lower,
        Writing_and_spelling_prim_ci_upper,
        Writing_and_spelling_prim_outcome,
        Writing_and_spelling_prim_sample,
        Writing_and_spelling_prim_outcomp,
        Writing_and_spelling_prim_es_type,
        Writing_and_spelling_prim_out_measure,
        Writing_and_spelling_prim_out_tit,
        Writing_and_spelling_prim_g1_n,
        Writing_and_spelling_prim_g2_n,
        Writing_and_spelling_prim_g1_mean,
        Writing_and_spelling_prim_g2_mean,
        Writing_and_spelling_prim_g1_sd,
        Writing_and_spelling_prim_g2_sd,
        Writing_and_spelling_prim_out_desc,
        Writing_and_spelling_test_type) = writing_and_spelling_lists
        
        writing_and_spelling_lists = self.data_extraction.getOutcomeData(df, 'Writing and spelling primary outcome', writing_and_spelling_lists, OUTCOME_VARS)
        
        mathematics_lists = [[] for _ in range(19)]
        
        (Mathematics_prim,
        Mathematics_prim_smd,
        Mathematics_prim_se,
        Mathematics_prim_ci_lower,
        Mathematics_prim_ci_upper,
        Mathematics_prim_outcome,
        Mathematics_prim_sample,
        Mathematics_prim_outcomp,
        Mathematics_prim_es_type,
        Mathematics_prim_out_measure,
        Mathematics_prim_out_tit,
        Mathematics_prim_g1_n,
        Mathematics_prim_g2_n,
        Mathematics_prim_g1_mean,
        Mathematics_prim_g2_mean,
        Mathematics_prim_g1_sd,
        Mathematics_prim_g2_sd,
        Mathematics_prim_out_desc,
        Mathematics_test_type) = mathematics_lists
        
        mathematics_lists = self.data_extraction.getOutcomeData(df, 'Mathematics primary outcome', mathematics_lists, OUTCOME_VARS)
        
        science_lists = [[] for _ in range(19)]
        
        (Science_prim,
        Science_prim_smd,
        Science_prim_se,
        Science_prim_ci_lower,
        Science_prim_ci_upper,
        Science_prim_outcome,
        Science_prim_sample,
        Science_prim_outcomp,
        Science_prim_es_type,
        Science_prim_out_measure,
        Science_prim_out_tit,
        Science_prim_g1_n,
        Science_prim_g2_n,
        Science_prim_g1_mean,
        Science_prim_g2_mean,
        Science_prim_g1_sd,
        Science_prim_g2_sd,
        Science_prim_out_desc,
        Science_test_type) = science_lists
        
        science_lists = self.data_extraction.getOutcomeData(df, 'Science primary outcome', science_lists, OUTCOME_VARS)
        
        fsm_lists = [[] for _ in range(19)]
        
        (FSM_prim,
        FSM_prim_smd,
        FSM_prim_se,
        FSM_prim_ci_lower,
        FSM_prim_ci_upper,
        FSM_prim_outcome,
        FSM_prim_sample,
        FSM_prim_outcomp,
        FSM_prim_es_type,
        FSM_prim_out_measure,
        FSM_prim_out_tit,
        FSM_prim_g1_n,
        FSM_prim_g2_n,
        FSM_prim_g1_mean,
        FSM_prim_g2_mean,
        FSM_prim_g1_sd,
        FSM_prim_g2_sd,
        FSM_prim_out_desc,
        FSM_test_type) = fsm_lists
        
        science_lists = self.data_extraction.getOutcomeData(df, 'SES/FSM primary outcome', fsm_lists, OUTCOME_VARS)
        
        df_zip = list(zip(
            toolkit_out_tit,
            toolkit_out_desc,
            toolkit_prim,
            toolkit_prim_smd,
            toolkit_prim_se,
            toolkit_out_measure,
            toolkit_g1_n,
            toolkit_g1_mean,
            toolkit_g1_sd,
            toolkit_g2_n,
            toolkit_g2_mean,
            toolkit_g2_sd,
            toolkit_prim_ci_lower,
            toolkit_prim_ci_upper,
            toolkit_prim_outcome,
            toolkit_prim_sample,
            toolkit_prim_outcomp,
            toolkit_es_type,
            toolkit_test_type,
            reading_prim_out_tit,
            reading_prim_out_desc,
            reading_prim,
            reading_prim_smd,
            reading_prim_se,
            reading_prim_out_measure,
            reading_prim_g1_n,
            reading_prim_g1_mean,
            reading_prim_g1_sd,
            reading_prim_g2_n,
            reading_prim_g2_mean,
            reading_prim_g2_sd,
            reading_prim_ci_lower,
            reading_prim_ci_upper,
            reading_prim_outcome,
            reading_prim_sample,
            reading_prim_outcomp,
            reading_prim_es_type,
            reading_test_type,
            Writing_and_spelling_prim_out_tit,
            Writing_and_spelling_prim_out_desc,
            Writing_and_spelling_prim,
            Writing_and_spelling_prim_smd,
            Writing_and_spelling_prim_se,
            Writing_and_spelling_prim_out_measure,
            Writing_and_spelling_prim_g1_n,
            Writing_and_spelling_prim_g1_mean,
            Writing_and_spelling_prim_g1_sd,
            Writing_and_spelling_prim_g2_n,
            Writing_and_spelling_prim_g2_mean,
            Writing_and_spelling_prim_g2_sd,
            Writing_and_spelling_prim_ci_lower,
            Writing_and_spelling_prim_ci_upper,
            Writing_and_spelling_prim_outcome,
            Writing_and_spelling_prim_sample,
            Writing_and_spelling_prim_outcomp,
            Writing_and_spelling_prim_es_type,
            Writing_and_spelling_test_type,
            Mathematics_prim_out_tit,
            Mathematics_prim_out_desc,
            Mathematics_prim,
            Mathematics_prim_smd,
            Mathematics_prim_se,
            Mathematics_prim_out_measure,
            Mathematics_prim_g1_n,
            Mathematics_prim_g1_mean,
            Mathematics_prim_g1_sd,
            Mathematics_prim_g2_n,
            Mathematics_prim_g2_mean,
            Mathematics_prim_g2_sd,
            Mathematics_prim_ci_lower,
            Mathematics_prim_ci_upper,
            Mathematics_prim_outcome,
            Mathematics_prim_sample,
            Mathematics_prim_outcomp,
            Mathematics_prim_es_type,
            Mathematics_test_type,
            Science_prim_out_tit,
            Science_prim_out_desc,
            Science_prim,
            Science_prim_smd,
            Science_prim_se,
            Science_prim_out_measure,
            Science_prim_g1_n,
            Science_prim_g1_mean,
            Science_prim_g1_sd,
            Science_prim_g2_n,
            Science_prim_g2_mean,
            Science_prim_g2_sd,
            Science_prim_ci_lower,
            Science_prim_ci_upper,
            Science_prim_outcome,
            Science_prim_sample,
            Science_prim_outcomp,
            Science_prim_es_type,
            Science_test_type,
            FSM_prim_out_tit,
            FSM_prim_out_desc,
            FSM_prim,
            FSM_prim_smd,
            FSM_prim_se,
            FSM_prim_out_measure,
            FSM_prim_g1_n,
            FSM_prim_g1_mean,
            FSM_prim_g1_sd,
            FSM_prim_g2_n,
            FSM_prim_g2_mean,
            FSM_prim_g2_sd,
            FSM_prim_ci_lower,
            FSM_prim_ci_upper,
            FSM_prim_outcome,
            FSM_prim_sample,
            FSM_prim_outcomp,
            FSM_prim_es_type,
            FSM_test_type
        ))
        
        df = pd.DataFrame(df_zip)
        
        df.rename(columns={
            0: "out_tit_tool",
            1: "out_desc_tool",
            2: "out_type_tool",
            3: "smd_tool",
            4: "se_tool",
            5: "out_measure_tool",
            6: "out_g1_n_tool",
            7: "out_g1_mean_tool",
            8: "out_g1_sd_tool",
            9: "out_g2_n_tool",
            10: "out_g2_mean_tool",
            11: "out_g2_sd_tool",
            12: "ci_lower_tool",
            13: "ci_upper_tool",
            14: "out_label_tool",
            15: "out_samp_tool",
            16: "out_comp_tool",
            17: "out_es_type_tool",
            18: "out_test_type_raw_tool",



            19: "out_tit_red",
            20: "out_desc_red",
            21: "out_type_red",
            22: "smd_red",
            23: "se_red",
            24: "out_measure_red",
            25: "out_g1_n_red",
            26: "out_g1_mean_red",
            27: "out_g1_sd_red",
            28: "out_g2_n_red",
            29: "out_g2_mean_red",
            30: "out_g2_sd_red",
            31: "ci_lower_red",
            32: "ci_upper_red",
            33: "out_label_red",
            34: "out_samp_red",
            35: "out_comp_red",
            36: "out_es_type_red",
            37: "out_test_type_raw_red",

            
            38: "out_tit_wri",
            39: "out_desc_wri",
            40: "out_type_wri",
            41: "smd_wri",
            42: "se_wri",
            43: "out_measure_wri",
            44: "out_g1_n_wri",
            45: "out_g1_mean_wri",
            46: "out_g1_sd_wri",
            47: "out_g2_n_wri",
            48: "out_g2_mean_wri",
            49: "out_g2_sd_wri",
            50: "ci_lower_wri",
            51: "ci_upper_wri",
            52: "out_label_wri",
            53: "out_samp_wri",
            54: "out_comp_wri",
            55: "out_es_type_wri",
            56: "out_test_type_raw_wri",
            57: "out_tit_math",
            58: "out_desc_math",
            59: "out_type_math",
            60: "smd_math",
            61: "se_math",
            62: "out_measure_math",
            63: "out_g1_n_math",
            64: "out_g1_mean_math",
            65: "out_g1_sd_math",
            66: "out_g2_n_math",
            67: "out_g2_mean_math",
            68: "out_g2_sd_math",
            69: "ci_lower_math",
            70: "ci_upper_math",
            71: "out_label_math",
            72: "out_samp_math",
            73: "out_comp_math",
            74: "out_es_type_math",
            75: "out_test_type_raw_math",
            76: "out_tit_sci",
            77: "out_desc_sci",
            78: "out_type_sci",
            79: "smd_sci",
            80: "se_sci",
            81: "out_measure_sci",
            82: "out_g1_n_sci",
            83: "out_g1_mean_sci",
            84: "out_g1_sd_sci",
            85: "out_g2_n_sci",
            86: "out_g2_mean_sci",
            87: "out_g2_sd_sci",
            88: "ci_lower_sci",
            89: "ci_upper_sci",
            90: "out_label_sci",
            91: "out_samp_sci",
            92: "out_comp_sci",
            93: "out_es_type_sci",
            94: "out_test_type_raw_sci",
            95: "out_tit_fsm",
            96: "out_desc_fsm",
            97: "out_type_fsm",
            98: "smd_fsm",
            99: "se_fsm",
            100: "out_measure_fsm",
            101: "out_g1_n_fsm",
            102: "out_g1_mean_fsm",
            103: "out_g1_sd_fsm",
            104: "out_g2_n_fsm",
            105: "out_g2_mean_fsm",
            106: "out_g2_sd_fsm",
            107: "ci_lower_fsm",
            108: "ci_upper_fsm",
            109: "out_label_fsm",
            110: "out_samp_fsm",
            111: "out_comp_fsm",
            112: "out_es_type_fsm",
            113: "out_test_type_raw_fsm"
        }, inplace=True)
        
        # Concatenate record details and main dataframes
        all_variables = pd.concat([record_details_df, df], axis=1, sort=False)
        
        if clean_cols:
            new_cols = [
                "out_tit_tool",
                'out_tit_tool_CLEAN',
                "out_desc_tool",
                'out_desc_tool_CLEAN', 
                "out_type_tool",
                'out_type_tool_CLEAN',
                "smd_tool",
                'smd_tool_CLEAN',
                "se_tool",
                'se_tool_CLEAN',
                "out_measure_tool",
                'out_measure_tool_CLEAN',
                "out_g1_n_tool",
                'out_g1_n_tool_CLEAN',
                "out_g1_mean_tool",
                'out_g1_mean_tool_CLEAN',
                "out_g1_sd_tool",
                'out_g1_sd_tool_CLEAN',
                "out_g2_n_tool",
                'out_g2_n_tool_CLEAN',
                "out_g2_mean_tool",
                'out_g2_mean_tool_CLEAN',
                "out_g2_sd_tool",
                'out_g2_sd_tool_CLEAN',
                "ci_lower_tool",
                'ci_lower_tool_CLEAN', 
                "ci_upper_tool",
                'ci_upper_tool_CLEAN',
                "out_label_tool",
                'out_label_tool_CLEAN',
                "out_samp_tool",
                'out_samp_tool_CLEAN',
                "out_comp_tool",
                'out_comp_tool_CLEAN', 
                "out_es_type_tool",
                'out_es_type_tool_CLEAN',
                "out_test_type_raw_tool",
                'out_test_type_raw_tool_CLEAN'
            ]
            all_variables = df.reindex(columns=new_cols, fill_value='')
            all_variables = pd.concat([record_details_df, all_variables], axis=1, sort=False)
        
        if verbose:
            self.data_extraction.verbose_display(all_variables)
        
        if save_file:
            outfile5 = self.data_extraction.save_dataframe(all_variables, "_DataFrame5_Effect_Size_B.csv", standard_info=True)
        else:
            outfile5=None
        
        return all_variables, outfile5


    def make_dataframe_6(self, ss_df, save_file=True, verbose=False):
        """
        Extracts data from sources defined in the current instance of the 
        DataExtraction class, cleans it, and combines it into a pandas DataFrame 
        for further analysis. The resulting DataFrame is saved to a file if 
        `save_file` is True.

        Args:
        - ss_df (pandas DataFrame): DataFrame containing data on study sample sizes.
        - save_file (bool, optional): Whether or not to save the resulting DataFrame 
          to a file. Default is True.
        - verbose (bool, optional): Whether or not to display information about the 
          extraction process. Default is False.

        Returns:
        - df_all_SS (pandas DataFrame): DataFrame containing cleaned and combined 
          data for analysis.
        - outfile6 (str): Name of the output CSV file, if `save_file` is True.

        Note:
        - Outcome data is extracted using `getOutcomeData()` and concatenated with other data.
        - `fsm_50` column is added to indicate whether a study has more or less 
          than 50% of participants eligiblefor free school meals.
        """
        eppiid_df = self.data_extraction.retrieve_metadata("ItemId", "id")
        author_df = self.data_extraction.retrieve_metadata("ShortTitle", "pub_author")
        year_df = self.data_extraction.retrieve_metadata("Year", "pub_year")
        pub_type_data = self.data_extraction.retrieve_data(publication_type_output, "pub_type_raw")
        toolkitstrand_df = self.data_extraction.get_outcome_data_lvl2(toolkit_strand_codes, "out_strand_")
        smd_df = self.data_extraction.get_outcome_data_lvl1("SMD", "smd_")
        sesmd_df = self.data_extraction.get_outcome_data_lvl1("SESMD", "se_")
        out_title_df = self.data_extraction.get_outcome_data_lvl1("Title", "out_tit_")
        out_type_df = self.data_extraction.get_outcome_data_lvl2(outcome_type_codes, "out_type_")
        sample_df = self.data_extraction.get_outcome_data_lvl2(sample_output, "out_samp_")
        out_comp_df = self.data_extraction.get_outcome_data_lvl1("ControlText", "out_comp_")
        effectsizetype_df = self.data_extraction.get_outcome_data_lvl2(es_type_output, "out_es_type_")
        out_measure_df = self.data_extraction.get_outcome_data_lvl1("InterventionText", "out_measure_")
        testtype_df = self.data_extraction.get_outcome_data_lvl2(test_type_output, "out_test_type_raw_")
        admin_strand_data = self.data_extraction.retrieve_data(admin_strand_output, "strand_raw")
        admin_strand_info = self.data_extraction.retrieve_info(admin_strand_output, "strand_info")
        country_df = self.data_extraction.retrieve_data(countries, "loc_country_raw")
        intervention_training_prov_data = self.data_extraction.retrieve_data(int_training_provided_output, "int_training_raw")
        intervention_training_prov_ht = self.data_extraction.retrieve_ht(int_training_provided_output, "int_training_ht")
        intervention_training_prov_info = self.data_extraction.retrieve_info(int_training_provided_output, "int_training_info")
        intervention_teaching_app_data = self.data_extraction.retrieve_data(intervention_teaching_approach, "int_approach_raw")
        intervention_teaching_app_ht = self.data_extraction.retrieve_ht(intervention_teaching_approach, "int_approach_ht")
        intervention_teaching_app_info = self.data_extraction.retrieve_info(intervention_teaching_approach, "int_approach_info")
        digit_tech_data = self.data_extraction.retrieve_data(int_appr_dig_tech, "digit_tech_raw")
        digit_tech_ht = self.data_extraction.retrieve_ht(int_appr_dig_tech, "digit_tech_ht")
        digit_tech_info = self.data_extraction.retrieve_info(int_appr_dig_tech, "digit_tech_info")
        par_eng_data = self.data_extraction.retrieve_data(int_appr_par_or_comm_vol, "parent_partic_raw")
        par_eng_ht= self.data_extraction.retrieve_ht(int_appr_par_or_comm_vol, "parent_partic_ht")
        par_eng_info = self.data_extraction.retrieve_info(int_appr_par_or_comm_vol, "parent_partic_info")
        intervention_time_data = self.data_extraction.retrieve_data(intervention_time_output, "int_when_raw")
        intervention_time_ht = self.data_extraction.retrieve_ht(intervention_time_output, "int_when_ht")
        intervention_time_info = self.data_extraction.retrieve_info(intervention_time_output, "int_when_info")
        intervention_delivery_data = self.data_extraction.retrieve_data(intervention_delivery_output, "int_who_raw")
        intervention_delivery_ht = self.data_extraction.retrieve_ht(intervention_delivery_output, "int_who_ht")
        intervention_delivery_info = self.data_extraction.retrieve_info(intervention_delivery_output, "int_who_info")
        intervention_duration_info = self.data_extraction.retrieve_info(int_dur_output, "int_dur_info")
        intervention_frequency_info = self.data_extraction.retrieve_info(inte_freq_output, "int_freq_info")
        intervention_sess_length_info = self.data_extraction.retrieve_info(intervention_session_length_output, "int_leng_info")
        edu_setting_data = self.data_extraction.retrieve_data(edu_setting_output, "int_setting_raw")
        edu_setting_ht = self.data_extraction.retrieve_ht(edu_setting_output, "int_setting_ht")
        edu_setting_info = self.data_extraction.retrieve_info(edu_setting_output, "int_setting_info")
        student_age_data = self.data_extraction.retrieve_data(student_age_output, "part_age_raw")
        student_age_ht = self.data_extraction.retrieve_ht(student_age_output, "part_age_ht")
        student_age_info = self.data_extraction.retrieve_info(student_age_output, "part_age_info")
        number_of_school_total_info = self.data_extraction.retrieve_info(number_of_schools_total_output, "school_total_info")
        number_of_classes_total_info = self.data_extraction.retrieve_info(num_of_class_tot_output, "class_total_info")
        study_design_data = self.data_extraction.retrieve_data(study_design_output, "int_desig_raw")
        study_design_ht = self.data_extraction.retrieve_ht(study_design_output, "int_design_ht")
        study_design_info = self.data_extraction.retrieve_info(study_design_output, "int_design_info")
        sample_size_comments_df = self.data_extraction.retrieve_info(sample_size_output, "sample_analysed_info")
        toolkit_version_data = self.data_extraction.retrieve_data(toolkit_versions, "toolkit_version")
        low_ses_percentage_Comments_df = self.data_extraction.retrieve_info(percentage_low_fsm_output, "fsm_perc_info")

        record_details_df = pd.concat([
            eppiid_df,
            toolkit_version_data,
            author_df,
            year_df,
            pub_type_data,
        ], axis=1)

        df = pd.concat([
            toolkitstrand_df,
            smd_df,
            sesmd_df,
            out_title_df,
            out_type_df,
            sample_df,
            out_comp_df,
            effectsizetype_df,
            out_measure_df,
            testtype_df
        ], axis=1, sort=False)

        df = df[list(interleave([
            toolkitstrand_df,
            smd_df,
            sesmd_df,
            out_title_df,
            out_type_df,
            sample_df,
            out_comp_df,
            effectsizetype_df,
            out_measure_df,
            testtype_df
        ]))]

        general_df = pd.concat([
            admin_strand_data,
            admin_strand_info,
            country_df,
            intervention_training_prov_data,
            intervention_training_prov_ht,
            intervention_training_prov_info,
            intervention_teaching_app_data,
            intervention_teaching_app_ht,
            intervention_teaching_app_info,
            digit_tech_data,
            digit_tech_ht,
            digit_tech_info,
            par_eng_data,
            par_eng_ht,
            par_eng_info,
            intervention_time_data,
            intervention_time_ht,
            intervention_time_info,
            intervention_delivery_data,
            intervention_delivery_ht,
            intervention_delivery_info,
            intervention_duration_info,
            intervention_frequency_info,
            intervention_sess_length_info,
            edu_setting_data,
            edu_setting_ht,
            edu_setting_info,
            student_age_data,
            student_age_ht,
            student_age_info,
            number_of_school_total_info,
            number_of_classes_total_info,
            study_design_data,
            study_design_ht,
            study_design_info,
            sample_size_comments_df,
            low_ses_percentage_Comments_df
        ], axis=1)

        toolkit_lists = [[] for _ in range(10)]

        (toolkit_prim, 
         toolkit_prim_smd, 
         toolkit_prim_se, 
         toolkit_out_tit, 
         toolkit_prim_sample, 
         toolkit_prim_outcomp, 
         toolkit_es_type, 
         toolkit_out_measure, 
         toolkit_out_testtype, 
         toolkit_out_strand) = toolkit_lists

        outcome_vars = (
            "out_type_",
            "smd_",
            "se_",
            "out_tit_",
            "out_samp_",
            "out_comp_",
            "out_es_type_",
            "out_measure_",
            "out_test_type_raw_",
            "out_strand_",
        )

        self.data_extraction.getOutcomeData(df, 'Toolkit primary outcome', toolkit_lists, outcome_vars)

        reading_lists = [[] for _ in range(3)]
        (reading_prim,  reading_prim_smd,  reading_prim_se) = reading_lists

        self.data_extraction.getOutcomeData(df, 'Reading primary outcome', reading_lists, outcome_vars)

        writing_lists = [[] for _ in range(3)]
        (Writing_and_spelling_prim, Writing_and_spelling_prim_smd, Writing_and_spelling_prim_se) = writing_lists

        self.data_extraction.getOutcomeData(df, 'Writing and spelling primary outcome', writing_lists, outcome_vars)

        mathematics_lists = [[] for _ in range(3)]
        (Mathematics_prim, Mathematics_prim_smd, Mathematics_prim_se) = mathematics_lists

        self.data_extraction.getOutcomeData(df, 'Mathematics primary outcome', mathematics_lists, outcome_vars)

        science_lists = [[] for _ in range(3)]
        (Science_prim, Science_prim_smd, Science_prim_se) = science_lists

        self.data_extraction.getOutcomeData(df, 'Science primary outcome', science_lists, outcome_vars)

        fsm_lists = [[] for _ in range(3)]
        (fsm_prim, fsm_prim_smd, fsm_prim_se) = fsm_lists

        self.data_extraction.getOutcomeData(df, 'FSM primary outcome', fsm_lists, outcome_vars)

        df_zip = list(zip(
            toolkit_out_strand,
            toolkit_prim_smd,
            toolkit_prim_se,
            toolkit_out_tit,
            toolkit_prim,
            toolkit_prim_sample,
            toolkit_prim_outcomp,
            toolkit_es_type,
            toolkit_out_measure,
            toolkit_out_testtype,
            reading_prim,
            reading_prim_smd,
            reading_prim_se,
            Writing_and_spelling_prim,
            Writing_and_spelling_prim_smd,
            Writing_and_spelling_prim_se,
            Mathematics_prim,
            Mathematics_prim_smd,
            Mathematics_prim_se,
            Science_prim,
            Science_prim_smd,
            Science_prim_se,
            fsm_prim,
            fsm_prim_smd,
            fsm_prim_se
        ))

        df = pd.DataFrame(df_zip)

        df = df.rename(columns={
            0: "out_strand",
            1: "smd_tool",
            2: "se_tool",
            3: "out_tit",
            4: "out_out_type_tool",
            5: "out_samp",
            6: "out_comp",
            7: "out_es_type",
            8: "out_measure",
            9: "out_test_type_raw",
            10: "out_out_type_red",
            11: "smd_red",
            12: "se_red",
            13: "out_out_type_wri",
            14: "smd_wri",
            15: "se_wri",
            16: "out_out_type_math",
            17: "smd_math",
            18: "se_math",
            19: "out_out_type_sci",
            20: "smd_sci",
            21: "se_sci",
            22: "out_out_type_fsm",
            23: "smd_fsm",
            24: "se_fsm"
        })

        df_all = pd.concat([record_details_df, df, general_df], axis=1, sort=False)

        # add fsm_50 TRUE/FALSE column
        df_all["fsm_perc_info"] = (df_all["fsm_perc_info"].str.strip('%'))
        df_all["fsm_perc_info"] = pd.to_numeric(df_all["fsm_perc_info"], errors='coerce')

        conditions = [
            df_all["fsm_perc_info"] > 49,
            df_all["fsm_perc_info"] < 50,
        ]
        values = ['TRUE', 'FALSE']

        df_all['fsm_50'] = np.select(conditions, values)

        df_all["fsm_perc_info"] = df_all["fsm_perc_info"].replace(
            to_replace=np.nan, value="NA", regex=True
        )

        df_all['fsm_50'] = df_all['fsm_50'].replace("0", "NA", regex=True)

        df_all = df_all[[
            'id',
            'pub_author',
            'pub_year',
            'pub_type_raw',
            'strand_raw',
            'toolkit_version',
            'out_out_type_tool',
            'smd_tool',
            'se_tool',
            'out_es_type',
            'out_tit',
            'out_comp',
            'out_samp',
            'out_measure',
            'out_test_type_raw',
            'out_out_type_red',
            'smd_red',
            'se_red',
            'out_out_type_wri',
            'smd_wri',
            'se_wri',
            'out_out_type_math',
            'smd_math',
            'se_math',
            'out_out_type_sci',
            'smd_sci',
            'se_sci',
            'out_out_type_fsm',
            'smd_fsm',
            'se_fsm',
            'sample_analysed_info',
            'school_total_info',
            'class_total_info',
            'int_setting_raw',
            'part_age_raw',
            'fsm_50',
            'fsm_perc_info',
            'loc_country_raw',
            'int_desig_raw',
            'int_approach_raw',
            'int_training_raw',
            'digit_tech_raw',
            'parent_partic_raw',
            'int_when_raw',
            'int_who_raw',
            'int_dur_info',
            'int_freq_info',
            'int_leng_info',
            'out_strand'
        ]]

        df_all_SS = pd.concat([df_all, ss_df], axis=1, sort=False)

        replacements = [('\r', ' '), ('\n', ' '), (':', ' '), (';', ' ')]
        for old, new in replacements:
            df_all_SS.replace(old, new, regex=True, inplace=True)

        if verbose:
            self.data_extraction.verbose_display(df_all_SS)

        if save_file:
            outfile6 = self.data_extraction.save_dataframe(df_all_SS, "_Main_Analysis.csv", standard_info=True)

        return df_all_SS, outfile6


    def getOutcomeData(self, save_file=True):
        '''
        Extract strand level outcome data for main analysis dataframe
        '''
        eppiid_df = json_extractor.retrieve_metadata("ItemId", "id")
        author_df = json_extractor.retrieve_metadata("ShortTitle", "pub_author")
        outcometype_df = json_extractor.get_outcome_data_lvl2(outcome_type_codes, "out_type_")
        outcome_df = json_extractor.get_outcome_data_lvl1("OutcomeText", "out_label_")
        outcome_title_df = json_extractor.get_outcome_data_lvl1("Title", "out_tit_")

        df = pd.concat([outcometype_df, outcome_df, outcome_title_df
        ], axis=1)[list(interleave([
            outcometype_df, outcome_df, outcome_title_df
        ]))]

        all_variables = pd.concat([eppiid_df, author_df, df], axis=1, sort=False)

        if save_file:
            #all_variables = self.data_extraction.save_dataframe("Toolkit_Outcome_Check.csv")

            all_variables = self.data_extraction.save_dataframe(all_variables, "_Outcomes.csv", standard_info=True)

        return all_variables
    
    
    def make_references(self, save_file=True):
        """
        """
        eppiid_df = self.data_extraction.retrieve_metadata("ItemId", "id")
        admin_strand_df = self.data_extraction.retrieve_data(admin_strand_output, "toolkit_strand")
        author_df = self.data_extraction.retrieve_metadata("ShortTitle", "short_title")
        authors_df = self.data_extraction.retrieve_metadata("Authors", "main_authors")
        year_df = self.data_extraction.retrieve_metadata("Year", "year")
        title_df = self.data_extraction.retrieve_metadata("Title", "main_title")
        parentittle_df = self.data_extraction.retrieve_metadata("ParentTitle", "parent_title")
        parentauthors_df = self.data_extraction.retrieve_metadata("ParentAuthors", "parent_authors")
        typename_df = self.data_extraction.retrieve_metadata("TypeName", "type_name")
        abstract_df = self.data_extraction.retrieve_metadata("Abstract", "abstract")
        volume_df = self.data_extraction.retrieve_metadata("Volume", "volume")
        issue_df = self.data_extraction.retrieve_metadata("Issue", "issue")
        pages_df = self.data_extraction.retrieve_metadata("Pages", "pages")
        doi_df = self.data_extraction.retrieve_metadata("DOI", "doi")
        url_df = self.data_extraction.retrieve_metadata("URL", "url")
        publisher_df = self.data_extraction.retrieve_metadata("Publisher", "publisher")
        city_df = self.data_extraction.retrieve_metadata("City", "city")
        institution_df = self.data_extraction.retrieve_metadata("Institution", "institution")
        #editedby_df = self.data_extraction.retrieve_metadata("EditedBy", "editor(s)")

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
            institution_df,
        ], axis=1)

        if save_file:
            outfile_9 = self.data_extraction.save_dataframe(references, "_References.csv", standard_info=True)

        return references, outfile_9
        

class StrandSpecificFrames:
    """
    A class for retrieving strand-specific data.

    Attributes:
    data_extractor: an instance of a data extractor class for retrieving the necessary data.
    """
    def __init__(self, data_extractor):
        self.data_extraction = data_extractor
        
    def arts_participation_ss(self):
        """
        Retrieves strand-specific data related to arts participation.

        Returns:
            A pandas DataFrame containing the following data:
                - ap_focus: focus data
                - ap_who_invol: who involved data
                - ap_where: where data

            If data is missing for any of these columns, it will be filled with "NA".
        """
        ap_focus_df = self.data_extraction.retrieve_data(ap_focus_output, "ap_focus")
        ap_who_invol_df = self.data_extraction.retrieve_data(ap_who_output, "ap_involved")
        ap_where_df = self.data_extraction.retrieve_data(ap_where_output, "ap_where")
        
        ap_ss_df = pd.concat([ap_focus_df, ap_who_invol_df, ap_where_df], axis=1, sort=False)
        
        ap_ss_df.fillna("NA", inplace=True)
        return ap_ss_df


    def behaviour_int_ss(self):
        """
        Retrieves strand-specific data related to behavior intervention.

        Returns:
            A pandas DataFrame containing the following data:
                - bi_target_group: target group data
                - bi_int_approach: intervention approach data
                - bi_int_components: intervention components data
                - bi_components_counselling: counseling data
                - bi_components_monitoring: monitoring data
                - bi_components_self: self-management data
                - bi_components_roleplay: role-play data
                - bi_components_parentalinv: parental involvement data
                - bi_academic: academic focus data
                - bi_components_digital: digital technology data

            If data is missing for any of these columns, it will be filled with "NA".
        """
        bi_target_group_df = self.data_extraction.retrieve_data(bi_target_group_output, "bi_targ_group")
        bi_target_group_HT_df = self.data_extraction.retrieve_ht(bi_intervention_approach_output, "bi_targ_group_ht")
        bi_target_group_Comments_df = self.data_extraction.retrieve_info(bi_intervention_components_output, "bi_targ_group_info")
        bi_int_approach_df = self.data_extraction.retrieve_data(bi_intervention_approach_output, "bi_int_approach")
        bi_int_approach_HT_df = self.data_extraction.retrieve_ht(bi_intervention_approach_output, "bi_int_approach_ht")
        bi_int_approach_Comments_df = self.data_extraction.retrieve_info(bi_intervention_approach_output, "bi_int_approach_info")
        bi_int_components_df = self.data_extraction.retrieve_data(bi_intervention_components_output, "bi_int_components")
        bi_int_components_HT_df = self.data_extraction.retrieve_ht(bi_intervention_components_output, "bi_int_components_ht")
        bi_int_components_Comments_df = self.data_extraction.retrieve_info(bi_intervention_components_output, "bi_int_components_info")
        bi_int_comp_counselling_df = self.data_extraction.retrieve_data(ind_comp_counselling, "bi_components_counselling")
        bi_int_comp_monitoring_df = self.data_extraction.retrieve_data(ind_comp_monitoring, "bi_components_monitoring")
        bi_int_comp_self_man_df = self.data_extraction.retrieve_data(ind_comp_self_management, "bi_components_self")
        bi_int_comp_role_play_df = self.data_extraction.retrieve_data(ind_comp_role_play, "bi_components_roleplay")
        bi_int_comp_par_invol_df = self.data_extraction.retrieve_data(ind_comp_parental_involv, "bi_components_parentalinv")
        bi_int_comp_ac_focus_df = self.data_extraction.retrieve_data(ind_comp_academic_focus, "bi_academic")
        bi_int_comp_dig_tech_df = self.data_extraction.retrieve_data(ind_comp_digit_tech, "bi_components_digital")
        
        bi_ss_df = pd.concat([
            bi_target_group_df,
            bi_int_approach_df,
            bi_int_components_df,
            bi_int_comp_counselling_df,
            bi_int_comp_monitoring_df,
            bi_int_comp_self_man_df,
            bi_int_comp_role_play_df,
            bi_int_comp_par_invol_df,
            bi_int_comp_ac_focus_df,
            bi_int_comp_dig_tech_df
        ], axis=1, sort=False)
        
        bi_ss_df.fillna("NA", inplace=True)
        return bi_ss_df


    def collab_learning_ss(self):
        """
        Retrieves strand-specific data related to collaborative learning.

        Returns:
            A pandas DataFrame containing the following data:
                - cl_approach_spec: approach specification data
                - cl_grp_size: group size data
                - cl_collab_kind: collaboration kind data
                - cl_stud_collab: student collaboration data
                - cl_extr_rewards: extrinsic rewards data
                - cl_if_yes_rewards: if yes rewards data
                - cl_comp_elem: component elements data
                - cl_teach_role_info: teacher role info data
                - cl_pup_feedback: pupil feedback data
                - cl_pup_feedback_who: pupil feedback who data

            If data is missing for any of these columns, it will be filled with "NA".
        """
        cl_approach_spec_df = self.data_extraction.retrieve_data(cl_approach_spec_output, "cl_approach_spec")
        cl_grp_size_df = self.data_extraction.retrieve_data(cl_group_size_output, "cl_grp_size")
        cl_collab_kind_df = self.data_extraction.retrieve_data(cl_collab_kind_output, "cl_collab_kind")
        cl_stud_collab_df = self.data_extraction.retrieve_data(cl_stud_collab_output, "cl_stud_collab")
        cl_stud_collab_HT_df = self.data_extraction.retrieve_ht(cl_stud_collab_output, "cl_stud_collab_HT")
        cl_extr_rewards_df = self.data_extraction.retrieve_data(cl_extr_rewards_output, "cl_extr_rewards")
        cl_extr_rewards_HT_df = self.data_extraction.retrieve_ht(cl_extr_rewards_output, "cl_extr_rewards_HT")
        cl_if_yes_rewards_df = self.data_extraction.retrieve_data(cl_if_yes_rewards_output, "cl_what_rewards")
        cl_if_yes_rewards_HT_df = self.data_extraction.retrieve_ht(cl_if_yes_rewards_output, "cl_what_rewards_HT")
        cl_comp_elem_df = self.data_extraction.retrieve_data(cl_comp_elem_output, "cl_comp_elem")
        cl_comp_elem_HT_df = self.data_extraction.retrieve_ht(cl_comp_elem_output, "cl_comp_elem_HT")
        cl_teach_role_info_df = self.data_extraction.retrieve_data(cl_teacher_role_info_output, "cl_teacher_role_info")
        cl_teach_role_info_HT_df = self.data_extraction.retrieve_ht(cl_teacher_role_info_output, "cl_teacher_role_info_HT")
        cl_pup_feedback_df = self.data_extraction.retrieve_data(cl_pupil_feedback_output, "cl_pup_feedback")
        cl_pup_feedback_HT_df = self.data_extraction.retrieve_ht(cl_pupil_feedback_output, "cl_pup_feedback_HT")
        cl_pup_feedback_who_df = self.data_extraction.retrieve_data(cl_pupil_feedback_who_output, "cl_pup_feedback_who")
        cl_pup_feedback_who_HT_df = self.data_extraction.retrieve_ht(cl_pupil_feedback_who_output, "cl_pup_feedback_who_HT")
        
        cl_ss_df = pd.concat([
            cl_approach_spec_df,
            cl_grp_size_df,
            cl_collab_kind_df,
            cl_stud_collab_df,
            cl_extr_rewards_df,
            cl_if_yes_rewards_df,
            cl_comp_elem_df,
            cl_teach_role_info_df,
            cl_pup_feedback_df,
            cl_pup_feedback_who_df,
        ], axis=1, sort=False)
        
        cl_ss_df.fillna("NA", inplace=True)
        return cl_ss_df


    def ey_early_lit_approaches_ss(self):
        """
        Retrieves strand-specific data related to early literacy approaches.

        Returns:
            A pandas DataFrame containing the following data:
                - lit_activities: literacy activities data
                - prog_comp: program comprehensiveness data
                - prog_desc: program description data

            If data is missing for any of these columns, it will be filled with "NA".
        """
        lit_act_df = self.data_extraction.retrieve_data(ela_literacy_activities, "lit_activities")
        lit_act_HT_df = self.data_extraction.retrieve_ht(ela_literacy_activities, "lit_activities_HT")
        prog_comp_df = self.data_extraction.retrieve_data(ela_comprehensive, "prog_comp")
        prog_comp_HT_df = self.data_extraction.retrieve_ht(ela_comprehensive, "prog_comp_HT")
        prog_desc_df = self.data_extraction.retrieve_data(ela_prog_desc, "prog_desc")
        prog_desc_HT_df = self.data_extraction.retrieve_ht(ela_prog_desc, "prog_desc_HT")
        
        # concatenate data frames
        ela_ss_df = pd.concat([
            lit_act_df,
            #lit_act_HT_df,
            prog_comp_df,
            #prog_comp_HT_df,
            prog_desc_df,
            #prog_desc_HT_df,
        ], axis=1, sort=False)
        
        return ela_ss_df


    def ey_early_num_approaches_ss(self):
        """
        Retrieves strand-specific data related to early numeracy approaches.

        Returns:
            A pandas DataFrame containing the following data:
                - math_incl: math included data
                - prog_comp: program comprehensiveness data
                - prog_act: program activities data

            If data is missing for any of these columns, it will be filled with "NA".
        """
        math_incl_df = self.data_extraction.retrieve_data(ena_maths_included, "math_incl")
        math_incl_HT_df = self.data_extraction.retrieve_ht(ena_maths_included, "math_incl_ht")
        prog_comp_df = self.data_extraction.retrieve_data(ena_prog_comp, "prog_comp")
        prog_act_df = self.data_extraction.retrieve_data(ena_prog_activities, "prog_act")
        
        ena_ss_df = pd.concat([
            math_incl_df,
            #math_incl_HT_df,
            prog_comp_df,
            prog_act_df,
        ], axis=1, sort=False)
        
        ena_ss_df.fillna("NA", inplace=True)
        return ena_ss_df


    def ext_school_time_ss(self):
        """
        Retrieves strand-specific data related to extended school time.

        Returns:
            A pandas DataFrame containing the following data:
                - est_how: extended school time data
                - est_time_added: estimated time added data
                - est_time_added_info: estimated time added comments data
                - est_purpose: estimated purpose data
                - est_target_group: estimated target group data
                - est_pupil_participation: estimated pupil participation data
                - est_activity_focus: estimated activity focus data
                - est_staff_kind: estimated staff kind data
                - est_parental_involvement: estimated parental involvement data
                - est_digital_tech: estimated digital technology data
                - est_attend_monitored: estimated attendance monitored data

            If data is missing for any of these columns, it will be filled with "NA".
        """
        extended_how = self.data_extraction.get_data(extended_how_output)
        extended_how_df = self.data_extraction.retrieve_data(extended_how_output, "est_how")
        extended_how_HT_df = self.data_extraction.retrieve_ht(extended_how_output, "est_how_ht")
        extended_how_Comments_df = self.data_extraction.retrieve_info(extended_how_output, "est_how_info")
        time_added_df = self.data_extraction.retrieve_data(time_Added_output, "est_time_added")
        time_added_HT_df = self.data_extraction.retrieve_ht(time_Added_output, "est_time_added_ht")
        time_added_Comments_df = self.data_extraction.retrieve_info(time_Added_output, "est_time_added_info")
        purpose_df = self.data_extraction.retrieve_data(purpose_or_aim_output, "est_purpose")
        purpose_HT_df = self.data_extraction.retrieve_ht(purpose_or_aim_output, "est_purpose_ht")
        purpose_Comments_df = self.data_extraction.retrieve_info(purpose_or_aim_output, "est_purpose_info")
        target_group_df = self.data_extraction.retrieve_data(target_group_output, "est_target_group")
        target_group_HT_df = self.data_extraction.retrieve_ht(target_group_output, "est_target_group_ht")
        target_group_Comments_df = self.data_extraction.retrieve_info(target_group_output, "est_target_group_info")
        pupil_participation_df = self.data_extraction.retrieve_data(pupil_participation_output, "est_pupil_participation")
        pupil_participation_HT_df = self.data_extraction.retrieve_ht(pupil_participation_output, "est_pupil_participation_ht")
        pupil_participation_Comments_df = self.data_extraction.retrieve_info(pupil_participation_output, "est_pupil_participation_info")
        activity_focus_df = self.data_extraction.retrieve_data(activity_focus_output, "est_activity_focus")
        activity_focus_HT_df = self.data_extraction.retrieve_ht(activity_focus_output, "est_activity_focus_ht")
        activity_focus_Comments_df = self.data_extraction.retrieve_info(activity_focus_output, "est_activity_focus_info")
        staff_kind_df = self.data_extraction.retrieve_data(staff_kind_output, "est_staff_kind")
        staff_kind_HT_df = self.data_extraction.retrieve_ht(staff_kind_output, "est_staff_kind_ht")
        staff_kind_Comments_df = self.data_extraction.retrieve_info(staff_kind_output, "est_staff_kind_info")
        parent_involved_df = self.data_extraction.retrieve_data(parental_involvement_output, "est_parental_involvement")
        parent_involved_HT_df = self.data_extraction.retrieve_ht(parental_involvement_output, "est_parental_involvement_ht")
        parent_involved_Comments_df = self.data_extraction.retrieve_info(parental_involvement_output, "est_parental_involvement_info")
        digit_tech_df = self.data_extraction.retrieve_data(digital_tech_output, "est_digital_tech")
        digit_tech_HT_df = self.data_extraction.retrieve_ht(digital_tech_output, "est_digital_tech_ht")
        digit_tech_Comments_df = self.data_extraction.retrieve_info(digital_tech_output, "est_digital_tech_info")
        attend_mon_df = self.data_extraction.retrieve_data(attendance_monitored_output, "est_attend_monitored")
        attend_mon_HT_df = self.data_extraction.retrieve_ht(attendance_monitored_output, "est_attend_monitored_ht")
        attend_mon_Comments_df = self.data_extraction.retrieve_info(attendance_monitored_output, "est_attendance_monitored_info")
        
        est_ss_df = pd.concat([
            extended_how_df,
            time_added_df,
            time_added_Comments_df,
            purpose_df,
            target_group_df,
            pupil_participation_df,
            activity_focus_df,
            staff_kind_df,
            parent_involved_df,
            digit_tech_df,
            attend_mon_df,
        ], axis=1, sort=False)
        
        self.data_extraction.clean_up(est_ss_df)
        return est_ss_df


    def ey_earlier_start_age_ss(self):
        """
        Retrieves strand-specific data related to changes in the starting age of early years education.

        Returns:
            A pandas DataFrame containing the following data:
                - prev_start_age: previous starting age data
                - new_start_age: new starting age data
                - addit_time_f_pt: additional time for part-time children data
                - addit_time_struct: additional time for structured sessions data
                - early_child_addit_time: earlier children additional time data
                - early_child_addit_time_info: information about earlier children additional time data
                - setting_type: type of setting data

            If data is missing for any of these columns, it will be filled with "NA".
        """
        prev_start_age_df = self.data_extraction.retrieve_data(ey_esa_prev_starting_age, "prev_start_age")
        new_start_age_df = self.data_extraction.retrieve_data(ey_esa_new_starting_age, "new_start_age")
        addit_time_f_pt_df = self.data_extraction.retrieve_data(ey_esa_addit_time_f_pt, "addit_time_f_pt")
        add_time_struct_df = self.data_extraction.retrieve_data(ey_esa_addit_time_struct, "addit_time_struct")
        earl_child_addit_time_df = self.data_extraction.retrieve_data(ey_esa_earlier_child_addit_time, "early_child_addit_time")
        earl_child_addit_time_info_df = self.data_extraction.retrieve_info(ey_esa_earlier_child_addit_time_other, "early_child_addit_time_info")
        setting_type_df = self.data_extraction.retrieve_data(ey_esa_setting_type, "setting_type")
        
        ey_esa_df = pd.concat([
            prev_start_age_df,
            new_start_age_df,
            addit_time_f_pt_df,
            add_time_struct_df,
            earl_child_addit_time_df,
            earl_child_addit_time_info_df,
            setting_type_df,
        ], axis=1, sort=False)
        
        ey_esa_df.fillna("NA", inplace=True)
        return ey_esa_df


    def ey_extra_hours_ss(self):
        """
        Retrieves strand-specific data related to extra hours in early years education.

        Returns:
            A pandas DataFrame containing the following data:
                - time_org: time organised data
                - addit_time_struc: additional time structure data

            If data is missing for any of these columns, it will be filled with "NA".
        """
        time_org_df = self.data_extraction.retrieve_data(time_organsised, "time_org")
        addit_time_struc_df = self.data_extraction.retrieve_data(addit_time_struct, "addit_time_struct")
        
        ey_eh_df = pd.concat([time_org_df,addit_time_struc_df], axis=1, sort=False)
        
        ey_eh_df.fillna("NA", inplace=True)
        
        return ey_eh_df


    def ey_play_based_learning_ss(self):
        """
        Retrieves strand-specific data related to play-based learning in Early Years education.

        Returns:
            A pandas DataFrame containing the following data:
                - kind_of_play: the kind of play used in the learning process
                - who_involved: who is involved in the play-based learning process
                - play_focus: the focus of the play-based learning process

            If data is missing for any of these columns, it will be filled with "NA".
        """
        kind_play_df = self.data_extraction.retrieve_data(kind_of_play, "kind_of_play")
        who_invol_df = self.data_extraction.retrieve_data(who_involved, "who_involved")
        play_foc_df = self.data_extraction.retrieve_data(play_focus, "play_focus")
        
        ey_pbl_df = pd.concat([
            kind_play_df,
            who_invol_df,
            play_foc_df
        ], axis=1, sort=False)
        
        ey_pbl_df.fillna("NA", inplace=True)
        return ey_pbl_df


    def feedback_ss(self):
        """
        Retrieves strand-specific data related to feedback.

        Returns:
            A pandas DataFrame containing the following data:
                - feedback source data
                - feedback source highlighted text
                - feedback source user comments
                - feedback source teacher data
                - feedback source teaching assistant data
                - feedback source volunteer data
                - feedback source parent data
                - feedback source researcher data
                - feedback source peer same age data
                - feedback source peer group data
                - feedback source peer older data
                - feedback source digital automated data
                - feedback source other non-human data
                - feedback source self data
                - feedback source other data
                - feedback directed data
                - feedback directed highlighted text
                - feedback directed user comments
                - feedback form data
                - feedback form highlighted text
                - feedback form user comments
                - feedback when data
                - feedback when highlighted text
                - feedback when user comments
                - feedback kind data
                - feedback kind "about the outcome" nested data (correct / incorrect)
                - feedback kind highlighted text
                - feedback kind user comments
                - feedback emotional tone data
                - feedback emotional tone highlighted text
                - feedback emotional tone user comments

            If data is missing for any of these columns, it will be filled with "NA".
        """
        feedb_source_df = self.data_extraction.retrieve_data(feedback_source_output, "feedback_Source")
        feedb_source_HT_df = self.data_extraction.retrieve_data(feedback_source_output, "feedback_Source_ht")
        feedb_source_Comments_df = self.data_extraction.retrieve_data(feedback_source_output, "feedback_Source_info")
        fsource_teacher_df = self.data_extraction.retrieve_data(fsource_teacher, "fb_source_teacher")
        fsource_ta_df = self.data_extraction.retrieve_data(fsource_ta, "fb_source_ta")
        fsource_volunteer_df = self.data_extraction.retrieve_data(fsource_volunteer, "fb_source_volunteer")
        fsource_parent_df = self.data_extraction.retrieve_data(fsource_parent, "fb_source_parent")
        fsource_researcher_df = self.data_extraction.retrieve_data(fsource_researcher, "fb_source_researcher")
        fsource_peer_ssame_Age_df = self.data_extraction.retrieve_data(fsource_peer_sameage_class, "fb_source_peer_sameage")
        fsource_peer_group_df = self.data_extraction.retrieve_data(fsource_peer_group, "fb_source_peer_group")
        fsource_peer_older_df = self.data_extraction.retrieve_data(fsource_peer_older, "fb_source_peer_older")
        fsource_digit_aut_df = self.data_extraction.retrieve_data(fsource_dig_aut, "fb_source_dig_aut")
        fsource_non_human_df = self.data_extraction.retrieve_data(fsource_other_nonhuman, "fb_source_non_human")
        fsource_self_df = self.data_extraction.retrieve_data(fsource_self, "fb_source_self")
        fsource_other_df = self.data_extraction.retrieve_data(fsource_other, "fb_source_other")
        feedb_directed_df = self.data_extraction.retrieve_data(feedback_directed_output, "fb_directed")
        feedb_directed_df_HT_df = self.data_extraction.retrieve_data(feedback_directed_output, "fb_directed_ht")
        feedb_directed_Comments_df = self.data_extraction.retrieve_data(feedback_directed_output, "fb_directed_info")
        feedb_form_df = self.data_extraction.retrieve_data(feedback_form_output, "fb_form")
        feedb_form_HT_df = self.data_extraction.retrieve_data(feedback_form_output, "fb_form_ht")
        feedb_form_Comments_df = self.data_extraction.retrieve_data(feedback_form_output, "fb_form_info")
        feedb_when_df = self.data_extraction.retrieve_data(feedback_when_output, "fb_when")
        feedb_when_HT_df = self.data_extraction.retrieve_data(feedback_when_output, "fb_when_ht")
        feedb_when_Comments_df = self.data_extraction.retrieve_data(feedback_when_output, "fb_when_info")
        feedb_kind_df = self.data_extraction.retrieve_data(feedback_kind_output, "fb_kind")
        feedb_kind_abt_outcome_df = self.data_extraction.retrieve_data(feedback_about_outcome_output, "fb_kind_about_outcome")
        feedb_kind_HT_df = self.data_extraction.retrieve_data(feedback_kind_output, "fb_kind_ht")
        feedb_kind_Comments_df = self.data_extraction.retrieve_info(feedback_kind_output, "fbkind_info")
        feedb_emo_tone_df = self.data_extraction.retrieve_data(feedback_emo_tone, "fb_emo_tone")
        feedb_emo_tone_HT_df = self.data_extraction.retrieve_ht(feedback_emo_tone, "fb_emo_tone_ht")
        feedb_emo_tone_Comments_df = self.data_extraction.retrieve_info(feedback_emo_tone,"fb_emo_tone_info")
        
        feedback_ss_df = pd.concat([
            feedb_source_df,
            fsource_teacher_df,
            fsource_ta_df,
            fsource_volunteer_df,
            fsource_parent_df,
            fsource_researcher_df,
            fsource_peer_ssame_Age_df,
            fsource_peer_group_df,
            fsource_peer_older_df,
            fsource_digit_aut_df,
            fsource_non_human_df,
            fsource_self_df,
            fsource_other_df,
            feedb_directed_df,
            feedb_form_df,
            feedb_when_df,
            feedb_kind_df,
            feedb_kind_abt_outcome_df,
            feedb_emo_tone_df,
        ], axis=1, sort=False)
        
        self.data_extraction.clean_up(feedback_ss_df)
        return feedback_ss_df


    def homework_ss(self):
        """
        Retrieves data related to homework.

        Returns:
            pandas.DataFrame: A data frame containing the following columns:
                - hw_dur: homework duration in minutes
                - hw_dur_info: information about how homework duration was measured
                - hw_dur_tot_time: total time spent on homework, if available
                - hw_who_involved: who was involved in homework completion (parent, teacher, student, etc.)
                - hw_par_role: if parents were involved, what was their role
                - hw_where: where the homework was completed (at home, school, etc.)
                - hw_mark_method_info: information about the method of marking

            Any missing values are filled with "NA".
        """
        hw_dur_df = self.data_extraction.retrieve_data(hw_dur_info_output, "hw_dur")
        # get hw duration information data
        hw_dur_info_df = self.data_extraction.retrieve_info(hw_dur_info_output, "hw_dur_info")
        # get hw duration total time data
        hw_dur_tot_time_df = self.data_extraction.retrieve_info(hw_total_time, "hw_dur_tot_time")
        # get hw who was involved data
        hw_who_invol_df = self.data_extraction.retrieve_data(hw_who_involved_output, "hw_who_involved")
        # get hw if parentes involved, describe role data
        hw_par_role_df = self.data_extraction.retrieve_data(hw_if_parents_describe_role_output, "hw_par_role")
        # get hw completed where data
        hw_where_df = self.data_extraction.retrieve_data(hw_completed_where_output, "hw_where")
        # get hw marking method data
        hw_mark_method_df = self.data_extraction.retrieve_data(hw_mark_method_info_output, "hw_mark_method_info")
        
        hw_ss_df = pd.concat([
            hw_dur_df,
            hw_dur_info_df,
            hw_dur_tot_time_df,
            hw_who_invol_df,
            hw_par_role_df,
            hw_where_df,
            hw_mark_method_df
        ], axis=1, sort=False)
        
        # fill blanks with NA
        hw_ss_df.fillna("NA", inplace=True)
        
        return hw_ss_df


    def indiv_instr_ss(self):
        """
        Retrieves data related to individual instruction.

        Returns:
            pandas.DataFrame: A DataFrame with the following columns:
                - 'ii_approach_df': Data on the approach used for individual instruction.
                - 'ii_elements_included_df': Data on other elements included in the instruction.
                - 'ii_programmes_mentioned_df': Data on other instruction programmes mentioned in the instruction.

            If data is missing for any of these columns, it will be filled with "NA".
        """
        ii_approach_df = self.data_extraction.retrieve_data(ii_approach_output, "ii_approach_df")
        ii_also_included_df = self.data_extraction.retrieve_data(ii_also_included_output, "ii_elements_included_df")
        ii_also_mentioned_df = self.data_extraction.retrieve_data(ii_also_mentioned_output, "ii_programmes_mentioned_df")
        
        ii_ss_df = pd.concat([ii_approach_df, ii_also_included_df, ii_also_mentioned_df,
        ], axis=1, sort=False)

        ii_ss_df.fillna("NA", inplace=True)
        return ii_ss_df


    def mentoring_ss(self):
        """
        Retrieves data related to the mentoring program.

        Returns:
            pandas.DataFrame: A data frame containing the following columns:
                - m_identity_df: Mentor's identity
                - m_identity_ht_df: Highlighted text for mentor's identity
                - m_identity_info_df: User comments on mentor's identity
                - m_pay_df: Whether the mentor was paid or compensated
                - m_pay_ht_df: Highlighted text for payment information
                - m_pay_info_df: User comments on payment information
                - m_org_df: Mentor's organization
                - m_org_ht_df: Highlighted text for mentor's organization
                - m_org_info_df: User comments on mentor's organization
                - m_training_df: Whether the mentor received training
                - m_training_ht_df: Highlighted text for training information
                - m_training_info_df: User comments on training information
                - m_meeting_freq_df: Meeting frequency between mentor and mentee
                - m_meeting_freq_ht_df: Highlighted text for meeting frequency
                - m_meeting_freq_info_df: User comments on meeting frequency
                - m_meeting_details_df: Details of mentor-mentee meetings
                - m_meeting_details_ht_df: Highlighted text for meeting details
                - m_meeting_details_info_df: User comments on meeting details
                - m_meeting_location_df: Location of mentor-mentee meetings
                - m_meeting_location_ht_df: Highlighted text for meeting location
                - m_meeting_location_info_df: User comments on meeting location
                - m_addit_nd_df: Additional experiences of the mentor
                - m_addit_exp_ht_df: Highlighted text for additional experiences
                - m_addit_exp_info_df: User comments on additional experiences
                - m_prog_focus_df: Focus of the mentoring program
                - m_prog_focus_ht_df: Highlighted text for program focus
                - m_prog_focus_info_df: User comments on program focus

            If data is missing for any of these columns, it will be filled with "NA".
        """
        ment_ident_df = self.data_extraction.retrieve_data(mentor_identity, "m_identity_df")
        ment_ident_HT_df = self.data_extraction.retrieve_ht(mentor_identity, "m_identity_ht_df")
        ment_ident_Comments_df = self.data_extraction.retrieve_info(mentor_identity, "m_identity_info_df")
        ment_pay_df = self.data_extraction.retrieve_data(mentor_paid_or_compensated, "m_pay_df")
        ment_pay_HT_df = self.data_extraction.retrieve_ht(mentor_paid_or_compensated, "m_pay_ht_df")
        ment_pay_Comments_df = self.data_extraction.retrieve_info(mentor_paid_or_compensated, "m_pay_info_df")
        ment_org_df = self.data_extraction.retrieve_data(mentor_organisation, "m_org_df")
        ment_org_HT_df = self.data_extraction.retrieve_ht(mentor_organisation, "m_org_ht_df")
        ment_org_Comments_df = self.data_extraction.retrieve_info(mentor_organisation, "m_org_info_df")
        ment_training_df = self.data_extraction.retrieve_data(mentor_training, "m_training_df")
        ment_training_HT_df = self.data_extraction.retrieve_ht(mentor_training, "m_training_ht_df")
        ment_training_Comments_df = self.data_extraction.retrieve_info(mentor_training, "m_training_info_df")
        ment_meeting_freq_df = self.data_extraction.retrieve_data(mentor_meeting_frequency, "m_meeting_freq_df")
        ment_meeting_freq_HT_df = self.data_extraction.retrieve_ht(mentor_meeting_frequency, "m_meeting_freq_ht_df")
        ment_meeting_freq_Comments_df = self.data_extraction.retrieve_info(mentor_meeting_frequency, "m_meeting_freq_info_df")
        ment_meeting_details_df = self.data_extraction.retrieve_data(mentor_meeting_details_provided, "m_meeting_details_df")
        ment_meeting_details_HT_df = self.data_extraction.retrieve_ht(mentor_meeting_details_provided, "m_meeting_details_ht_df")
        ment_meeting_details_Comments_df = self.data_extraction.retrieve_info(mentor_meeting_details_provided, "m_meeting_details_info_df")
        ment_meeting_location_df = self.data_extraction.retrieve_data(mentor_meeting_location, "m_meeting_location_df")
        ment_meeting_location_HT_df = self.data_extraction.retrieve_ht(mentor_meeting_location, "m_meeting_location_ht_df")
        ment_meeting_location_Comments_df = self.data_extraction.retrieve_info(mentor_meeting_location, "m_meeting_location_info_df")
        ment_addit_exp_df = self.data_extraction.retrieve_data(mentoring_additional_experiences, "m_addit_exp_df")
        ment_addit_exp_HT_df = self.data_extraction.retrieve_ht(mentoring_additional_experiences, "m_addit_exp_ht_df")
        ment_addit_exp_Comments_df = self.data_extraction.retrieve_info(mentoring_additional_experiences, "m_addit_exp_info_df")
        ment_prog_focus_df = self.data_extraction.retrieve_data(mentoring_programme_focus, "m_prog_focus_df")
        ment_prog_focus_HT_df = self.data_extraction.retrieve_ht(mentoring_programme_focus, "m_prog_focus_ht_df")
        ment_prog_focus_Comments_df = self.data_extraction.retrieve_info(mentoring_programme_focus, "m_prog_focus_info_df")
        
        mentoring_ss_df = pd.concat([
            ment_ident_df,
            ment_pay_df,
            ment_org_df,
            ment_training_df,
            ment_meeting_freq_df,
            ment_meeting_details_df,
            ment_meeting_location_df,
            ment_addit_exp_df,
            ment_prog_focus_df,
        ], axis=1, sort=False)
        
        mentoring_ss_df.fillna("NA", inplace=True)
        return mentoring_ss_df


    def mastery_learning_ss(self):
        """
        Retrieves data related to mastery learning.
        
        Returns:
            pandas.DataFrame: A data frame containing the following columns:
                - ml_theor: Theoretical approach used in the mastery learning program
                - ml_age_grp: Age group of the students participating in the mastery learning program
                - ml_ability_grp: Ability groupings used in the mastery learning program
                - ml_attain_grouping: Grouping method used to determine attainment level
                - ml_goal_level: The level of the goals set for students in the mastery learning program
                - ml_assess_det: Details on how student performance is assessed in the mastery learning program
                - ml_fb_detail_prov: Details on how feedback is provided to students in the mastery learning program
                - ml_mastery_lev: The level of mastery required for students to attain the set goals in the mastery learning program

            If data is missing for any of these columns, it will be filled with "NA".
        """
        ml_theor_df = self.data_extraction.retrieve_data(ml_theor_output, "ml_theor")
        ml_age_grp_df = self.data_extraction.retrieve_data(ml_age_group_output, "ml_age_grp")
        ml_ability_grp_df = self.data_extraction.retrieve_data(ml_ability_group_output, "ml_ability_grp")
        ml_attain_group_type_df = self.data_extraction.retrieve_data(ml_if_attain_what_grouping_type_output, "ml_attain_grouping")
        ml_goal_level_df = self.data_extraction.retrieve_data(ml_goal_level, "ml_goal_level")
        ml_asess_det_df = self.data_extraction.retrieve_data(ml_assess_detail, "ml_assess_det")
        ml_fb_det_prov_df = self.data_extraction.retrieve_data(ml_fb_detail_prov, "ml_fb_detail_prov")
        ml_mast_lev_df = self.data_extraction.retrieve_data(ml_mastery_level, "ml_mastery_lev")
        
        ml_ss_df = pd.concat([
            ml_theor_df,
            ml_age_grp_df,
            ml_ability_grp_df,
            ml_attain_group_type_df,
            ml_goal_level_df,
            ml_asess_det_df,
            ml_fb_det_prov_df,
            ml_mast_lev_df
        ], axis=1, sort=False)
        
        ml_ss_df.fillna("NA", inplace=True)
        return ml_ss_df


    def metacog_self_reg_ss(self):
        """
        Retrieves data related to metacognition and self-regulated learning.

        Returns:
            pandas.DataFrame: A data frame containing the following columns:
                - msr_knowl_type: Type of knowledge in the task
                - msr_task_stage: Stage of the task at which self-regulated learning occurred
                - msr_strategy: Type of self-regulated learning strategy used
                - msr_motiv_aspects: Motivational aspects related to self-regulated learning
                - msr_teaching_approach: Teaching approach that encourages self-regulated learning
                - msr_digit_tech: Digital technologies used for self-regulated learning

            If data is missing for any of these columns, it will be filled with "NA".
        """
        msr_knowl_type_df = self.data_extraction.retrieve_data(msr_knowl_type_output, "msr_knowl_type")
        msr_task_stage_df = self.data_extraction.retrieve_data(msr_task_stage_output, "msr_task_stage")
        msr_strategy_df = self.data_extraction.retrieve_data(msr_strategy_type_output, "msr_strategy")
        msr_motiv_aspects_df = self.data_extraction.retrieve_data(msr_self_reg_mot_aspects_output, "msr_motiv_aspects")
        msr_teaching_approach_df = self.data_extraction.retrieve_data(msr_teaching_approach_output, "msr_teaching_approach")
        msr_digit_tech_df = self.data_extraction.retrieve_data(msr_digit_tech, "msr_digit_tech")
        
        msr_ss_df = pd.concat([
            msr_knowl_type_df,
            msr_task_stage_df,
            msr_strategy_df,
            msr_motiv_aspects_df,
            msr_teaching_approach_df,
            msr_digit_tech_df
        ], axis=1, sort=False)
        
        msr_ss_df.fillna("NA", inplace=True)
        return msr_ss_df


    def oral_lang_ss(self):
        """Retrieves data related to oral language activities.

        Returns:
            pandas.DataFrame: A data frame containing the following columns:
                - ol_focus: Focus of the oral language activities
                - ol_target: Target of the oral language activities
                - ol_target_comp_type: Type of component targeted by the oral language activities
                - ol_activity_invol: Involvement of the students in the oral language activities

            If data is missing for any of these columns, it will be filled with "NA".
        """
        ol_focus_df = self.data_extraction.retrieve_data(ol_focus, "ol_focus")
        ol_target_df = self.data_extraction.retrieve_data(ol_target, "ol_target")
        ol_target_comp_type_df = self.data_extraction.retrieve_data(ol_imp_comp_type, "ol_target_comp_type")
        ol_act_invol_df = self.data_extraction.retrieve_data(ol_activity_invol, "ol_activity_invol")
        
        ol_ss_df = pd.concat([
            ol_focus_df,
            ol_target_df,
            ol_target_comp_type_df,
            ol_act_invol_df,
        ], axis=1, sort=False)
        
        ol_ss_df.fillna("NA", inplace=True)
        return ol_ss_df


    def one_t_one_comp_ss(self):
        """Extracts data related to one-to-one comparisons.

        Returns:
            pandas.DataFrame: A data frame containing the following columns:
                - 1_1_comparisons_Available: Whether one-to-one comparisons were available
                - 1_1_comparisons_Available_SS_ht: Highlighted text for one-to-one comparison availability
                - 1_1_comparisons_Available_SS_info: User comments on one-to-one comparison availability
        """
        comp_avail_df = self.data_extraction.retrieve_data(comparisons_available, "1_1_comparisons_Available")
        comp_avail_HT_df = self.data_extraction.retrieve_ht(comparisons_available, "1_1_comparisons_Available_SS_ht")
        comp_avail_Comments_df = self.data_extraction.retrieve_info(comparisons_available, "1_1_comparisons_Available_SS_info")
        
        one_to_one_ss_df = pd.concat([comp_avail_df,], axis=1, sort=False)
        one_to_one_ss_df.fillna("NA", inplace=True)
        
        self.data_extraction.clean_up(one_to_one_ss_df)
        return one_to_one_ss_df


    def peer_tut(self):
        """
        Retrieves data related to peer tutoring.

        Returns:
            pandas.DataFrame: A data frame containing the following columns:
                - pt_tut_desc: Description of the peer tutoring program
                - pt_tut_desc_same_age: Description of the peer tutoring program for same-age peers
                - pt_tut_desc_cross_age: Description of the peer tutoring program for cross-age peers
                - pt_same_age_attainment: Peer tutoring's effect on same-age peers' academic attainment
                - pt_cross_age_attainment: Peer tutoring's effect on cross-age peers' academic attainment
                - pt_tut_from: Where the peer tutors came from (e.g. same school, different school)
                - pt_tut_role: Role of the peer tutors in the program
                - pt_tutee_attain_level: Level of academic attainment of the tutees
                - pt_digit_tech: Use of digital technology in the program
                - pt_incentive: Incentives offered to peer tutors or tutees

            If data is missing for any of these columns, it will be filled with "NA".
        """
        tut_desc_df = self.data_extraction.retrieve_data(tutor_age_output, "pt_tut_desc")
        tut_desc_same_age_df = self.data_extraction.retrieve_data(tutor_age_same, "pt_tut_desc_same_age")
        tut_desc_cross_age_df = self.data_extraction.retrieve_data(tutor_age_cross, "pt_tut_desc_cross_age")
        tut_same_age_df = self.data_extraction.retrieve_data(tutor_same_age_output, "pt_same_age_attainment")
        tut_cross_age_df = self.data_extraction.retrieve_data(tutor_cross_age_output, "pt_cross_age_attainment")
        tut_from_df = self.data_extraction.retrieve_data(tutor_from_output, "pt_tut_from")
        tut_role_df = self.data_extraction.retrieve_data(tutor_role_output, "pt_tut_role")
        tut_tutee_attain_lev_df = self.data_extraction.retrieve_data(tutee_attainment_output, "pt_tutee_attain_level")
        digit_tech_df = self.data_extraction.retrieve_data(digit_tech_output, "pt_digit_tech")
        tut_incentive_df = self.data_extraction.retrieve_data(tutor_tutee_incentive_output, "pt_incentive")
        
        peer_tut_ss_df = pd.concat([
            tut_desc_df,
            tut_desc_same_age_df,
            tut_desc_cross_age_df,
            tut_same_age_df,
            tut_cross_age_df,
            tut_from_df,
            tut_role_df,
            tut_tutee_attain_lev_df,
            digit_tech_df,
            tut_incentive_df,
        ], axis=1, sort=False)
        
        return peer_tut_ss_df


    def phys_activity_ss(self):
        """
        Retrieves data related to physical activity.

        Returns:
            pandas.DataFrame: A data frame containing the following columns:
                - pa_when: When physical activity took place
                - pa_lessons: Lessons included physical activity
                - pa_act_type: Type of physical activity
                - pa_exer_level: Level of exercise involved

            If data is missing for any of these columns, it will be filled with "NA".
        """
        pha_when_df = self.data_extraction.retrieve_data(pha_when_output, "pa_when")
        pha_lessons_df = self.data_extraction.retrieve_data(pha_lessons_included_output, "pa_lessons")
        pha_act_type_df = self.data_extraction.retrieve_data(pha_activity_type_output, "pa_act_type")
        pha_exer_level_df = self.data_extraction.retrieve_data(pha_exercise_level_output, "pa_exer_level")
        
        pha_ss_df = pd.concat([
            pha_when_df,
            pha_lessons_df,
            pha_act_type_df,
            pha_exer_level_df,
        ], axis=1, sort=False)
        
        pha_ss_df.fillna("NA", inplace=True)
        return pha_ss_df


    def read_comprehension_ss(self):
        """
        Retrieves data related to reading comprehension.

        Returns:
            pandas.DataFrame: A data frame containing the following columns:
                - rc_comp: Comprehension components assessed
                - rc_comp_strat: Comprehension strategies assessed
                - rc_comp_vocab: Vocabulary instruction provided
                - rc_comp_red_flu: Instruction on reading fluency provided
                - rc_comp_phon: Instruction on phonics provided
                - rc_comp_wri: Writing instruction provided
                - rc_comp_other: Other forms of instruction provided
                - rc_comp_unclear: Unclear forms of instruction provided
                - rc_strat_instruc: Type of instruction provided for comprehension strategies
                - rc_instruc_comp: Components of instruction provided for reading comprehension
                - rc_txt_type_red_mat: Text type or material used for reading comprehension

            If data is missing for any of these columns, it will be filled with "NA".
        """
        rc_comp_df = self.data_extraction.retrieve_data(rc_components_output, "rc_comp")
        rc_comp_strat_df = self.data_extraction.retrieve_data(rc_comp_strat_output, "rc_comp_strat")
        rc_comp_vocab_df = self.data_extraction.retrieve_data(rc_comp_vocab_output, "rc_comp_vocab")
        rc_comp_red_flu_df = self.data_extraction.retrieve_data(rc_comp_red_flu_output, "rc_comp_red_flu")
        rc_comp_phon_df = self.data_extraction.retrieve_data(rc_comp_phon_output, "rc_comp_phon")
        rc_comp_wri_df = self.data_extraction.retrieve_data(rc_comp_wri_output, "rc_comp_wri")
        rc_comp_other_df = self.data_extraction.retrieve_data(rc_comp_other_output, "rc_comp_other")
        rc_comp_unclear_df = self.data_extraction.retrieve_data(rc_comp_unclear_output, "rc_comp_unclear")
        rc_strat_instr_df = self.data_extraction.retrieve_data(rc_strat_instruct_type_output, "rc_strat_instruc")
        rc_instruc_comp_df = self.data_extraction.retrieve_data(rc_comp_other_output, "rc_instruc_comp")
        rc_txt_type_df = self.data_extraction.retrieve_data(rc_txt_type_output, "rc_txt_type_red_mat")
        
        rc_ss_df = pd.concat([
            rc_comp_df,
            rc_comp_strat_df,
            rc_comp_vocab_df,
            rc_comp_red_flu_df,
            rc_comp_phon_df,
            rc_comp_wri_df,
            rc_comp_other_df,
            rc_comp_unclear_df,
            rc_strat_instr_df,
            rc_instruc_comp_df,
            rc_txt_type_df,
        ], axis=1, sort=False)
        
        return rc_ss_df


    def red_class_size_ss(self):
        """
        Retrieves data related to reducing class sizes.

        Returns:
            pandas.DataFrame: A data frame containing the following columns:
                - redc_avg_small_class_size_info: The average size of small classes.
                - redc_avg_large_class_size_info: The average size of large classes.
                - redc_small_class_teach_num: The number of teachers in small classes.
                - redc_large_class_teach_num: The number of teachers in large classes.
                - redc_large_class_adapt: Adaptations made for large classes.
                - redc_lim_num_subj: Reduced class size for limited number of subjects.
                - redc_impl_all_or_most_lessons: Implementation of reduced class sizes for all or most lessons.

            If data is missing for any of these columns, it will be filled with "NA".
        """
        redc_avg_small_class_size_df = self.data_extraction.retrieve_info(redc_avg_small_class_size_output, "redc_avg_small_class_size_info")
        redc_avg_large_class_size_df = self.data_extraction.retrieve_info(redc_avg_large_class_size_output, "redc_avg_large_class_size_info")
        redc_small_class_teach_num_df = self.data_extraction.retrieve_data(redc_small_class_teacher_number_output, "redc_small_class_teach_num")
        redc_large_class_teach_num_df = self.data_extraction.retrieve_data(redc_large_class_teacher_number_output, "redc_large_class_teach_num")
        redc_large_class_adapt_df = self.data_extraction.retrieve_data(redc_large_class_adaption_output, "redc_large_class_adapt")
        redc_lim_num_subj_df = self.data_extraction.retrieve_data(redc_reduc_for_limited_num_sub_output, "redc_lim_num_subj")
        redc_impl_all_or_most_lessons_df = self.data_extraction.retrieve_data(redc_impl_for_all_or_most_output, "redc_impl_all_or_most_lessons")
        
        redc_ss_df = pd.concat([
            redc_avg_small_class_size_df,
            redc_avg_large_class_size_df,
            redc_small_class_teach_num_df,
            redc_large_class_teach_num_df,
            redc_large_class_adapt_df,
            redc_lim_num_subj_df,
            redc_impl_all_or_most_lessons_df,
        ], axis=1, sort=False)
        
        return redc_ss_df


    def repeat_year_ss(self):
        """
        Retrieves data related to the practice of students repeating a year.

        Returns:
            pandas.DataFrame: A data frame containing the following columns:
                - ry_identify_ret_stu_df: How students are identified for repeating a year
                - ry_ret_stu_age_df: Age of students who repeat a year
                - ry_ret_basis_df: Basis for students repeating a year
                - ry_impact_meas_df: How the impact of repeating a year is measured
                - ry_stu_ret_num_df: Number of students who repeat a year
                - ry_ret_stu_comparison_df: How students who repeat a year are compared with other students
                - ry_prom_count_char_df: Characteristics of students who are promoted or retained
                - ry_comp_df: Comparison between students who repeat a year and those who don't
                - ry_comp_grp_school_df: Comparison between students in the same school who repeat a year and those who don't

            If data is missing for any of these columns, it will be filled with "NA".
        """
        ry_identify_ret_stu_df = self.data_extraction.retrieve_data(ry_ret_stu_identify_output, "ry_identify_ret_stu")
        ry_ret_stu_age_df = self.data_extraction.retrieve_data(ry_ret_stu_age_output, "ry_ret_stu_age")
        ry_ret_basis_df = self.data_extraction.retrieve_data(ry_ret_basis_output, "ry_ret_basis")
        ry_impact_meas_df = self.data_extraction.retrieve_data(ry_impact_measure_delay_output, "ry_impact_meas")
        ry_stu_ret_num_df = self.data_extraction.retrieve_data(ry_stu_ret_number_output, "ry_stu_ret_num")
        ry_ret_stu_comparison_df = self.data_extraction.retrieve_data(ry_ret_stud_compared_with_output, "ry_ret_stud_comp")
        ry_prom_count_char_df = self.data_extraction.retrieve_data(ry_prom_count_characteristics_output, "ry_matching_char")
        ry_comp_df = self.data_extraction.retrieve_data(ry_comparison, "ry_comp")
        ry_comp_grp_school_df = self.data_extraction.retrieve_data(ry_comp_grp_school, "ry_comp_grp_school")
        
        ry_ss_df = pd.concat([
            ry_identify_ret_stu_df,
            ry_ret_stu_age_df,
            ry_ret_basis_df,
            ry_impact_meas_df,
            ry_stu_ret_num_df,
            ry_ret_stu_comparison_df,
            ry_prom_count_char_df,
            ry_comp_df,
            ry_comp_grp_school_df,
        ], axis=1, sort=False)
        
        self.data_extraction.clean_up(ry_ss_df)
        return ry_ss_df


    def soc_emo_learning_ss(self):
        """
        Retrieves data related to social and emotional learning.

        Returns:
            pandas.DataFrame: A data frame containing the following columns:
                - sel_involvement_df: Level of involvement of different groups in social and emotional learning
                - sel_invol_pupils_df: Involvement of all pupils in social and emotional learning
                - sel_invol_targ_groups_df: Involvement of targeted groups in social and emotional learning
                - sel_invol_classes_df: Involvement of different classes in social and emotional learning
                - sel_invol_whole_school_df: Involvement of the entire school in social and emotional learning
                - sel_invol_class_teachers_df: Involvement of class teachers in social and emotional learning
                - sel_invol_oth_staff_df: Involvement of other staff in social and emotional learning
                - sel_invol_out_experts_df: Involvement of outside experts in social and emotional learning
                - sel_invol_other_df: Other factors affecting involvement in social and emotional learning
                - sel_focus_df: Areas of focus in social and emotional learning
                - sel_location_df: Location of social and emotional learning activities

            If data is missing for any of these columns, it will be filled with "NA".
        """
        sel_involvement_df = self.data_extraction.retrieve_data(sel_involvement_output, "sel_involvement")
        sel_invol_pupils_df = self.data_extraction.retrieve_data(sel_invol_all_pupils, "sel_invol_pupils")
        sel_invol_targ_groups_df = self.data_extraction.retrieve_data(sel_invol_targ_grp, "sel_invol_targ_grps")
        sel_invol_classes_df = self.data_extraction.retrieve_data(sel_invol_classes, "sel_invol_classes")
        sel_invol_whole_school_df = self.data_extraction.retrieve_data(sel_invol_school, "sel_invol_whole_school")
        sel_invol_class_teachers_df = self.data_extraction.retrieve_data(sel_invol_teachers, "sel_invol_class_teachers")
        sel_invol_oth_staff_df = self.data_extraction.retrieve_data(sel_invol_other_staff, "sel_invol_oth_staff")
        sel_invol_out_experts_df = self.data_extraction.retrieve_data(sel_invol_outside_experts, "sel_invol_out_experts")
        sel_invol_other_df = self.data_extraction.retrieve_data(sel_invol_other, "sel_invol_other")
        sel_focus_df = self.data_extraction.retrieve_data(sel_focus_output, "sel_focus")
        sel_location_df = self.data_extraction.retrieve_data(sel_location_output, "sel_location")
        
        sel_ss_df = pd.concat([
            sel_involvement_df,
            sel_invol_pupils_df,
            sel_invol_targ_groups_df,
            sel_invol_classes_df,
            sel_invol_whole_school_df,
            sel_invol_class_teachers_df,
            sel_invol_oth_staff_df,
            sel_invol_out_experts_df,
            sel_invol_other_df,
            sel_focus_df,
            sel_location_df
        ], axis=1, sort=False)
        
        sel_ss_df.fillna("NA", inplace=True)
        return sel_ss_df


    def setting_streaming_ss(self):
        """
        Retrieves and returns the data related to setting and streaming.
            
        Returns:
            A pandas DataFrame containing the following columns:
                - sets_dir_grp_change: Data on grouping changes.
                - sets_dir_grp_type_regroup: Data on regrouping type.
                - sets_curr_taught_in_regroup: Data on curriculum taught in regrouping.
                - sets_dir_grp_type_streaming: Data on grouping type for streaming.
                - sets_dir_grp_type_gifted: Data on grouping type for gifted students.
                - sets_school_groupings: Data on school groupings.
                - sets_attain_grouping_levels: Data on attainment grouping levels.
                - sets_follow_same_curr: Data on whether students follow the same curriculum.
                - sets_approach_name: Data on the approach name.
                - sets_pupil_assignment: Data on pupil assignment.

            If data is missing for any of these columns, it will be filled with "NA".
        """
        sets_dir_grp_change_df = self.data_extraction.retrieve_data(sets_dir_grouping_change, "sets_dir_grp_change")
        """ # get grouping type within attainment data
        sets_grp_type_within_attain = self.data_extraction.get_data(sets_dir_grouping_type_within_attain)
        sets_grp_type_within_attain_df = pd.DataFrame(sets_grp_type_within_attain)
        sets_grp_type_within_attain_df = sets_grp_type_within_attain_df.T
        sets_grp_type_within_attain_df.columns = ["sets_grp_type_within_attain"] """
        """ # nested within grp type within attain ^
        # get curriculum taight within attainment data
        sets_curr_taught_attain = get_data(sets_curr_taught_in_attain_grp)
        sets_curr_taught_attain_df = pd.DataFrame(sets_curr_taught_attain)
        sets_curr_taught_attain_df = sets_curr_taught_attain_df.T
        sets_curr_taught_attain_df.columns = ["sets_curr_taught_in_attain"] """
        # get grouping type regroup data
        sets_dir_grp_type_regroup_df = self.data_extraction.retrieve_data(sets_dir_grouping_type_regroup, "sets_dir_grp_type_regroup")
        # nested within grp type regroup ^
        # get curr taught in regroup data
        sets_curr_taught_regroup_df = self.data_extraction.retrieve_data(sets_curr_taught_in_regroup, "sets_curr_taught_in_regroup")
        sets_dir_grp_stream_df = self.data_extraction.retrieve_data(sets_dir_grouping_stream, "sets_dir_grp_type_streaming")
        sets_dir_grp_gifted_df = self.data_extraction.retrieve_data(sets_dir_grouping_gifted, "sets_dir_grp_type_gifted")
        sets_schl_groupings_df = self.data_extraction.retrieve_data(sets_school_groupings, "sets_school_groupings")
        sets_attain_grp_levels_df = self.data_extraction.retrieve_data(sets_attain_grouping_level, "sets_attain_grouping_levels")
        sets_foll_same_curr_df = self.data_extraction.retrieve_data(sets_follow_same_curr, "sets_follow_same_curr")
        sets_appr_name_df = self.data_extraction.retrieve_data(sets_approach_name, "sets_approach_name")
        sets_pup_assignment_df = self.data_extraction.retrieve_data(sets_pupil_assignment, "sets_pup_assign")
        
        sets_ss_df = pd.concat([
            sets_dir_grp_change_df,
            sets_dir_grp_type_regroup_df,
            sets_curr_taught_regroup_df,
            sets_dir_grp_stream_df,
            sets_dir_grp_gifted_df,
            sets_schl_groupings_df,
            sets_attain_grp_levels_df,
            sets_foll_same_curr_df,
            sets_appr_name_df,
            sets_pup_assignment_df
        ], axis=1, sort=False)
        
        sets_ss_df.fillna("NA", inplace=True)
        return sets_ss_df


    def small_group_tuit_ss(self):
        """
        Retrieves data related to small group tuition, including group size, 
        composition, and teaching lead.

        Returns:
            A pandas dataframe containing the following information:
                - sgt_group_size: The size of the small group.
                - sgt_group_composition: The composition of the small group.
                - sgt_group_lead: The teaching lead of the small group.

            If data is missing for any of these columns, it will be filled with "NA".
        """
        group_size_df = self.data_extraction.retrieve_data(group_size_output, "sgt_group_size")
        group_size_HT_df = self.data_extraction.retrieve_ht(group_size_output, "sgt_group_size_ht")
        group_size_info_df = self.data_extraction.retrieve_info(group_size_output, "sgt_group_size_info")
        group_composition_df = self.data_extraction.retrieve_data(group_composition_output, "sgt_group_composition")
        group_composition_HT_df = self.data_extraction.retrieve_ht(group_composition_output, "sgt_group_composition_ht")
        group_composition_info_df = self.data_extraction.retrieve_info(group_composition_output, "sgt_group_composition_info")
        group_lead_df = self.data_extraction.retrieve_data(group_teaching_lead_output, "sgt_group_lead")
        group_lead_HT_df = self.data_extraction.retrieve_ht(group_teaching_lead_output, "sgt_group_lead_ht")
        group_lead_info_df = self.data_extraction.retrieve_info(group_teaching_lead_output, "sgt_group_lead_info")
       
        sgt_ss_df = pd.concat([group_size_df, group_composition_df, group_lead_df,
            ], axis=1, sort=False)
        
        sgt_ss_df.fillna("NA", inplace=True)
        return sgt_ss_df


    def summer_school_ss(self):
        """
        Retrieves data related to summer schools, including program aims, 
        pupil participation, and attendance.

        Returns:
            A pandas dataframe containing the following information:
            - ss_aim: The general aim of the summer school.
            - ss_aim_catch_up: Whether the summer school was aimed at helping students catch up.
            - ss_aim_enrich: Whether the summer school was aimed at enriching students' education.
            - ss_aim_trans: Whether the summer school was aimed at helping students transition to a new school.
            - ss_aim_gifted: Whether the summer school was aimed at serving gifted students.
            - ss_aim_unclear: Whether the aim of the summer school was unclear.
            - ss_pupil_part: The number and characteristics of pupils who participated in the summer school.
            - ss_resid_comp: Whether the summer school included residential components.
            - ss_grp_size: The size of the groups in the summer school.
            - ss_act_focus: The focus of the activities in the summer school.
            - ss_staff_kind: The kind of staff involved in the summer school.
            - ss_par_invol: The involvement of parents in the summer school.
            - ss_dig_tech: The use of digital technology in the summer school.
            - ss_attendance: The attendance rate of the summer school.
        """
        ss_aim_df = self.data_extraction.retrieve_data(ss_aim_output, "ss_aim")
        ss_aim_catch_up_df = self.data_extraction.retrieve_data(ss_aim_output_catch_up, "ss_aim_catch_up")
        ss_aim_enrich_df = self.data_extraction.retrieve_data(ss_aim_output_enrich, "ss_aim_enrich")
        ss_aim_trans_df = self.data_extraction.retrieve_data(ss_aim_output_school_trans, "ss_aim_trans")
        ss_aim_gifted_df = self.data_extraction.retrieve_data(ss_aim_output_gifted, "ss_aim_gifted")
        ss_aim_unclear_df = self.data_extraction.retrieve_data(ss_aim_output_unclear, "ss_aim_unclear")
        ss_pupil_part_df = self.data_extraction.retrieve_data(ss_pupil_part_output, "ss_pupil_part")
        ss_resid_comp_df = self.data_extraction.retrieve_data(ss_resid_comp_output, "ss_resid_comp")
        ss_grp_size_df = self.data_extraction.retrieve_data(ss_group_size_output, "ss_grp_size")
        ss_act_focus_df = self.data_extraction.retrieve_data(ss_activity_focus_output, "ss_act_focus")
        ss_staff_kind_df = self.data_extraction.retrieve_data(ss_staff_kind_output, "ss_staff_kind")
        ss_par_invol_df = self.data_extraction.retrieve_data(ss_parent_invol, "ss_par_invol")
        ss_dig_tech_df = self.data_extraction.retrieve_data(ss_digit_tech, "ss_dig_tech")
        ss_atten_df = self.data_extraction.retrieve_data(ss_attendance, "ss_attendance")
        
        SS_ss_df = pd.concat([
            ss_aim_df,
            ss_aim_catch_up_df,
            ss_aim_enrich_df,
            ss_aim_trans_df,
            ss_aim_gifted_df,
            ss_aim_unclear_df,
            ss_pupil_part_df,
            ss_resid_comp_df,
            ss_grp_size_df,
            ss_act_focus_df,
            ss_staff_kind_df,
            ss_par_invol_df,
            ss_dig_tech_df,
            ss_atten_df
        ], axis=1, sort=False)
        
        SS_ss_df.fillna("NA", inplace=True)
        return SS_ss_df


    def teach_assistants_ss(self):
        """
        Retrieves data related to teaching assistants, including their role, 
        group size, and description.

        Returns:
            A pandas dataframe containing the following information:
                - ta_desc: A description of the teaching assistant's role.
                - ta_role: The role of the teaching assistant.
                - ta_group_size: The size of the group the teaching assistant is assigned to.

            If data is missing for any of these columns, it will be filled with "NA".
        """
        ta_desc_df = self.data_extraction.retrieve_data(ta_description_output, "ta_desc")
        ta_desc_HT_df = self.data_extraction.retrieve_ht(ta_description_output, "ta_desc_ht")
        ta_desc_Comments_df = self.data_extraction.retrieve_info(ta_description_output, "ta_desc_info")
        ta_role_df = self.data_extraction.retrieve_data(ta_role_output, "ta_role")
        ta_role_HT_df = self.data_extraction.retrieve_ht(ta_role_output, "ta_role_ht")
        ta_role_Comments_df = self.data_extraction.retrieve_info(ta_role_output, "ta_role_info")
        ta_group_size_df = self.data_extraction.retrieve_data(ta_group_size_output, "ta_group_size")
        ta_group_size_HT_df = self.data_extraction.retrieve_ht(ta_group_size_output, "ta_group_size_ht")
        ta_group_size_Comments_df = self.data_extraction.retrieve_info(ta_group_size_output, "ta_group_size_info")
        
        ta_ss_df = pd.concat([ta_desc_df, ta_role_df, ta_group_size_df,
        ], axis=1, sort=False)
        
        self.data_extraction.clean_up(ta_ss_df)
        return ta_ss_df


    def parental_engagement(self):
        """
        Retrieves data related to parental engagement, including involvement, 
        activities, and focus.

        Returns:
            A pandas dataframe containing the following information:
                - pe_involved: The degree of parental involvement in the school.
                - pe_act_loc: The location of activities involving parents.
                - pe_prog_training: Programs offered to train parents in supporting their child's education.
                - pe_prog_support: Programs offered to support parents in other aspects of parenting.
                - pe_children: Opportunities for parents to work with their children in the school setting.
                - pe_focus: The main focus of the school's parental engagement efforts.

            If data is missing for any of these columns, it will be filled with "NA".
        """
        pe_involved_df = self.data_extraction.retrieve_data(pe_involved_output, "pe_involved")
        pe_act_loc_df = self.data_extraction.retrieve_data(pe_activity_location_output, "pe_act_loc")
        pe_prog_train_df = self.data_extraction.retrieve_data(pe_prog_training_output, "pe_prog_training")
        pe_prog_support_df = self.data_extraction.retrieve_data(pe_prog_support_output, "pe_prog_support")
        pe_children_work_with_df = self.data_extraction.retrieve_data(pe_children_output, "pe_children")
        pe_focus_df = self.data_extraction.retrieve_data(pe_focus_output, "pe_focus")
        
        pe_ss_df = pd.concat([
            pe_involved_df,
            pe_act_loc_df,
            pe_prog_train_df,
            pe_prog_support_df,
            pe_children_work_with_df,
            pe_focus_df,
        ], axis=1, sort=False) 
        
        pe_ss_df.fillna("NA", inplace=True)
        return pe_ss_df


    def phonics(self):
        """
        Retrieves data related to phonics instruction, including target population, 
        instructional approach, and parental involvement.

        Returns:
            A pandas dataframe containing the following information:
            - ph_targ_pop: The target population for phonics instruction.
            - ph_constit_part: The instructional approach used for phonics instruction.
            - ph_constit_part_synth_phon: Whether synthetic phonics is used as part of the instructional approach.
            - ph_constit_part_sys_phon: Whether systematic phonics is used as part of the instructional approach.
            - ph_constit_part_analyt_phon: Whether analytic phonics is used as part of the instructional approach.
            - ph_constit_part_analog_phon: Whether analogy phonics is used as part of the instructional approach.
            - ph_constit_part_emb_phon: Whether embedded phonics is used as part of the instructional approach.
            - ph_constit_part_phonem_aware: Whether phonemic awareness is included as part of the instructional approach.
            - ph_constit_part_phonol_aware: Whether phonological awareness is included as part of the instructional approach.
            - ph_constit_part_onset_rime: Whether onset and rime awareness is included as part of the instructional approach.
            - ph_constit_part_syll_instr: Whether syllable instruction is included as part of the instructional approach.
            - ph_constit_part_sight_vocab: Whether sight vocabulary is included as part of the instructional approach.
            - ph_constit_part_whole_word: Whether whole word instruction is included as part of the instructional approach.
            - ph_central_to_approach: The centrality of phonics instruction to the overall approach to teaching reading.
            - ph_par_invol: The level of parental involvement in phonics instruction.
            - ph_dig_tech: The use of digital technology in phonics instruction.
        """
        ph_tar_pop_df = self.data_extraction.retrieve_data(ph_targ_pop_output, "ph_targ_pop")
        ph_const_part_df = self.data_extraction.retrieve_data(ph_constit_part_approach_output, "ph_constit_part")
        ph_const_part_synth_df = self.data_extraction.retrieve_data(ph_constit_part_approach_synth_ph, "ph_constit_part_synth_phon")
        ph_const_part_sys_df = self.data_extraction.retrieve_data(ph_constit_part_approach_syst_ph, "ph_constit_part_sys_phon")
        ph_const_part_analyt_df = self.data_extraction.retrieve_data(ph_constit_part_approach_analyt_ph, "ph_constit_part_analyt_phon")
        ph_const_part_analog_df = self.data_extraction.retrieve_data(ph_constit_part_approach_analog_ph, "ph_constit_part_analog_phon")
        ph_const_part_emb_df = self.data_extraction.retrieve_data(ph_constit_part_approach_emb_ph, "ph_constit_part_emb_phon")
        ph_const_part_phon_aware_df = self.data_extraction.retrieve_data(ph_constit_part_approach_phon_aware, "ph_constit_part_phonem_aware")
        ph_const_part_phonol_aware_df = self.data_extraction.retrieve_data(ph_constit_part_approach_phonol_aware, "ph_constit_part_phonol_aware")
        ph_const_part_onset_rime_df = self.data_extraction.retrieve_data(ph_constit_part_approach_onset_rime, "ph_constit_part_onset_rime")
        ph_const_part_syll_instr_df = self.data_extraction.retrieve_data(ph_constit_part_approach_syll_instr, "ph_constit_part_syll_instr")
        ph_const_part_sight_vocab_df = self.data_extraction.retrieve_data(ph_constit_part_approach_sight_vocab, "ph_constit_part_sight_vocab")
        ph_const_part_whole_word_df = self.data_extraction.retrieve_data(ph_constit_part_approach_whole_word, "ph_constit_part_whole_word")
        ph_central_to_approach_df = self.data_extraction.retrieve_data(ph_central_teach_lit_output, "ph_central_to_approach")
        ph_par_invol_df = self.data_extraction.retrieve_data(ph_par_invol_output, "ph_par_invol")
        ph_dig_tech_df = self.data_extraction.retrieve_data(ph_digit_tech_output, "ph_dig_tech")
        
        ph_ss_df = pd.concat([
            ph_tar_pop_df,
            ph_const_part_df,
            ph_const_part_synth_df,
            ph_const_part_sys_df,
            ph_const_part_analyt_df,
            ph_const_part_analog_df,
            ph_const_part_emb_df,
            ph_const_part_phon_aware_df,
            ph_const_part_phonol_aware_df,
            ph_const_part_onset_rime_df,
            ph_const_part_syll_instr_df,
            ph_const_part_sight_vocab_df,
            ph_const_part_whole_word_df,
            ph_central_to_approach_df,
            ph_par_invol_df,
            ph_dig_tech_df
        ], axis=1, sort=False)
        
        ph_ss_df.fillna("NA", inplace=True)
        return ph_ss_df


    def performance_pay(self):
        """
        Retrieves data related to performance pay, including incentive criteria, 
        reward recipients, incentive timing, incentive type, incentive amount, and 
        teacher evaluation period.

        Returns:
            A pandas dataframe containing the following information:
                - pp_incent_criteria: The criteria used to determine incentive pay.
                - pp_reward_recip: The recipient(s) of the incentive pay.
                - pp_incent_timing: The timing of the incentive pay.
                - pp_incent_type: The type of incentive pay (e.g., monetary, non-monetary).
                - pp_incent_amount: The amount of incentive pay.
                - pp_teach_eval_per: The evaluation period for determining incentive pay.

            If data is missing for any of these columns, it will be filled with "NA".
        """
        pp_incent_crit_df = self.data_extraction.retrieve_data(pp_incentive_criteria_output, "pp_incent_criteria")
        pp_reward_recip_df = self.data_extraction.retrieve_data(pp_reward_recipient_output, "pp_reward_recip")
        pp_incent_timing_df = self.data_extraction.retrieve_data(pp_incentive_timing_output, "pp_incent_timing")
        pp_incent_type_df = self.data_extraction.retrieve_data(pp_incentive_type_output, "pp_incent_type")
        pp_incent_amount_df = self.data_extraction.retrieve_data(pp_incentive_amount_output, "pp_incent_amount")
        pp_teach_eval_per_df = self.data_extraction.retrieve_data(pp_teacher_eval_period_output, "pp_teach_eval_per")
        
        pp_ss_df = pd.concat([
            pp_incent_crit_df,
            pp_reward_recip_df,
            pp_incent_timing_df,
            pp_incent_type_df,
            pp_incent_amount_df,
            pp_teach_eval_per_df,
        ], axis=1, sort=False)
       
        pp_ss_df.fillna("NA", inplace=True)
        return pp_ss_df


    def within_class_grouping(self):
        """
        Retrieves data related to within-class grouping, including direction of 
        grouping change, pupils affected by within-class grouping, attainment 
        grouping levels, approach name, and pupil assignment.

        Returns:
            A pandas dataframe containing the following information:
                - wc_grp_dir: The direction of grouping change.
                - wc_curr_taught_att_grp: The current taught attainment group.
                - wc_pup_affected: The pupils affected by within-class grouping.
                - wc_attn_grouping_levels: The attainment grouping levels.
                - wc_follow_same_curr: Whether pupils follow the same curriculum.
                - wc_approach_name: The approach name for within-class grouping.
                - wc_pup_assign: How pupils are assigned to groups.

            If data is missing for any of these columns, it will be filled with "NA".
        """
        wc_grp_dir_df = self.data_extraction.retrieve_data(wcg_dir_grouping_change_output, "wc_grp_dir")
        wc_curr_taught_att_grp_df = self.data_extraction.retrieve_data(wcg_curr_taught_attain_grp_output, "wc_curr_taught_att_grp")
        wc_pup_affected_df = self.data_extraction.retrieve_data(wcg_pupils_affected_by_wcg_output, "wc_pup_affected")
        wc_att_grping_levels_df = self.data_extraction.retrieve_data(wcg_attain_grouping_level, "wc_attn_grouping_levels")
        wc_follow_same_curr_df = self.data_extraction.retrieve_data(wcg_follow_same_curr, "wc_follow_same_curr")
        wc_approach_name_df = self.data_extraction.retrieve_data(wcg_approach_name, "wc_approach_name")
        wc_pup_assign_df = self.data_extraction.retrieve_data(wcg_pupil_assignment, "wc_pup_assign")
        
        wc_ss_df = pd.concat([
            wc_grp_dir_df,
            wc_curr_taught_att_grp_df,
            wc_pup_affected_df,
            wc_att_grping_levels_df,
            wc_follow_same_curr_df,
            wc_approach_name_df,
            wc_pup_assign_df,
        ], axis=1, sort=False)
        
        self.data_extraction.clean_up(wc_ss_df)
        return wc_ss_df


    def strand_specific_df_selection(self, user_input):
        """
        Selects a strand-specific dataframe based on user input.

        Args:
            user_input (int): An integer representing the user's selection from 
            a list of strand-specific dataframes.

        Returns:
            A pandas dataframe containing data related to the selected strand.
        """
        match user_input:
            # MAIN TOOLKIT
            case 1: 
                print("- Strand specific datraframe selection: Arts Participation")
                ss_df = self.arts_participation_ss()
            case 2: 
                print("- Strand specific datraframe selection: Behaviour Interventions")
                ss_df = self.behaviour_int_ss()
            case 3:
                print("- Strand specific datraframe selection: Collaborative Learning")
                ss_df = self.collab_learning_ss()
            case 4: 
                print("- Strand specific datraframe selection: Extending School Time")
                ss_df = self.ext_school_time_ss()
            case 5: 
                print("- Strand specific datraframe selection: Feedback")
                ss_df = self.feedback_ss()
            case 6:
                print("- Strand specific datraframe selection: Homework")
                ss_df = self.homework_ss()
            case 7: 
                print("- Strand specific datraframe selection: Individualised Instruction")
                ss_df = self.indiv_instr_ss()
            case 8: 
                print("- Strand specific datraframe selection: Mentoring")
                ss_df = self.mentoring_ss()
            case 9:
                print("- Strand specific datraframe selection: Mastery Learning")
                ss_df = self.mastery_learning_ss()
            case 10: 
                print("- Strand specific datraframe selection: Metacognition & Self Regulation")
                ss_df = self.metacog_self_reg_ss()
            case 11:
                print("- Strand specific datraframe selection: One to One Tuition")
                ss_df = self.one_t_one_comp_ss()
            case 12: 
                print("- Strand specific datraframe selection: Oral Language")
                ss_df = self.oral_lang_ss()
            case 13:
                print("- Strand specific datraframe selection: Physical Activity")
                ss_df = self.phys_activity_ss()
            case 14: 
                print("- Strand specific datraframe selection: Parentel Engagement")
                ss_df = self.parental_engagement()
            case 15: 
                print("- Strand specific datraframe selection: Phonics")
                ss_df = self.phonics()
            case 16:
                print("- Strand specific datraframe selection: Performance Pay")
                ss_df = self.performance_pay()
            case 17: 
                print("- Strand specific datraframe selection: Peer Tutoring")
                ss_df = self.peer_tut()
            case 18: 
                print("- Strand specific datraframe selection: Reading Comprehension")
                ss_df = self.read_comprehension_ss()
            case 19:
                print("- Strand specific datraframe selection: Reducing Class Size")
                ss_df = self.red_class_size_ss()
            case 20: 
                print("- Strand specific datraframe selection: Repeating a Year")
                ss_df = self.repeat_year_ss()
            case 21: 
                print("- Strand specific datraframe selection: Social & Emotional Learning")
                ss_df = self.soc_emo_learning_ss()
            case 22: 
                print("- Strand specific datraframe selection: Setting/Streaming")
                ss_df = self.setting_streaming_ss()
            case 23: 
                print("- Strand specific datraframe selection: Small Group Tuition")
                ss_df = self.small_group_tuit_ss()
            case 24: 
                print("- Strand specific datraframe selection: Summer Schools")
                ss_df = self.summer_school_ss()
            case 25: 
                print("- Strand specific datraframe selection: Teaching Assistants")
                ss_df = self.teach_assistants_ss()
            case 26: 
                print("- Strand specific datraframe selection: Within-Class Grouping")
                ss_df = self.within_class_grouping()
            # EARLY YEARS TOOKLIT (overlap)
            case 27: 
                print("- Strand specific datraframe selection: Early Years - Early Literacy Approaches")
                ss_df = self.ey_early_lit_approaches_ss()
            case 28: 
                print("- Strand specific datraframe selection: Early Numeracy Approaches")
                ss_df = self.ey_early_num_approaches_ss()
            case 29: 
                print("- Strand specific datraframe selection: Earlier Starting Age")
                ss_df = self.ey_earlier_start_age_ss()
            case 30: 
                print("- Strand specific datraframe selection: Extra Hours")
                ss_df = self.ey_extra_hours_ss()
            case 31: 
                print("- Strand specific datraframe selection: Play Based Learning")
                ss_df = self.ey_play_based_learning_ss()
        return ss_df


class RiskofBias:
    def __init__(self, data_extractor):
        self.data_extraction = data_extractor

    def initialize_vars(self):
        self.year_df = self.data_extraction.retrieve_metadata("Year", "pub_year")
        self.eppiid_df = self.data_extraction.retrieve_metadata("ItemId", "id")
        self.author_df = self.data_extraction.retrieve_metadata("ShortTitle", "pub_author")
        self.admin_strand_df = self.data_extraction.retrieve_data(admin_strand_output, "strand_raw")
        self.publicationtype_df = self.data_extraction.retrieve_data(publication_type_output, "pub_type_raw")
        self.participant_assignment_df = self.data_extraction.retrieve_data(part_assign_output, "part_assig_raw")
        self.randomisation_df = self.data_extraction.retrieve_data(randomisation_details, "rand_raw")
        self.study_realism_df = self.data_extraction.retrieve_data(study_realism_output, "eco_valid_raw")
        self.number_of_schools_intervention_Comments_df = self.data_extraction.retrieve_info(number_of_schools_intervention_output, "school_treat_info")
        self.intervention_delivery_df = self.data_extraction.retrieve_data(intervention_delivery_output, "int_who_raw")
        self.number_of_classes_total_Comments_df = self.data_extraction.retrieve_info(num_of_class_tot_output, "class_total_info")
        self.InterventionEvaluation_df = self.data_extraction.retrieve_data(int_eval_output, "out_eval_raw")   
        self.comparability_df = self.data_extraction.retrieve_data(comparability_output, "comp_anal_raw")    
        self.comp_anal_ht = self.data_extraction.retrieve_ht(comparability_output, "comp_anal_ht")
        self.comp_anal_info = self.data_extraction.retrieve_info(comparability_output, "comp_anal_info")
        self.sample_size_Comments_df = self.data_extraction.retrieve_info(sample_size_output, "sample_analysed_info")
        self.overall_percent_attrition_Comments_df = self.data_extraction.retrieve_info(overall_perc_attr, "attri_perc_info")
        self.clustering_df = self.data_extraction.retrieve_data(clustering_output, "clust_anal_raw")  
        self.toolkit_test_type = self.data_extraction.get_outcome_data_lvl2(test_type_output, "out_test_type_raw_")
        self.toolkit_es_type = self.data_extraction.get_outcome_data_lvl2(es_type_output, "out_es_type_")
        all_variables, outfile5 = DataFrameCompilation.make_dataframe_5(self, save_file=False, clean_cols=False, verbose=False)
        self.toolkit_es_type = all_variables.out_es_type_tool
        all_variables, outfile5 = DataFrameCompilation.make_dataframe_5(self, save_file=False, clean_cols=False, verbose=False)
        self.toolkit_test_type = all_variables.out_test_type_raw_tool
        all_variables, outfile5 = DataFrameCompilation.make_dataframe_5(self, save_file=False, clean_cols=False, verbose=False)
        self.tool_prim_es = all_variables.smd_tool
        all_variables, outfile5 = DataFrameCompilation.make_dataframe_5(self, save_file=False, clean_cols=False, verbose=False)
        self.tool_prim_se = all_variables.se_tool
        self.participant_assignment_df['part_assig_raw'] = self.participant_assignment_df['part_assig_raw'].str[0]
        self.randomisation_df['rand_raw'] = self.randomisation_df['rand_raw'].str[0]
        self.study_realism_df['eco_valid_raw'] = self.study_realism_df['eco_valid_raw'].str[0]

    def rob_year(self):
        self.year_df["pub_year"] = self.year_df["pub_year"].apply(pd.to_numeric, errors='coerce').fillna(0)

        def pub_year_risk(row):
            if row["pub_year"] < 1980:
                return 'High Risk'
            if row["pub_year"] > 1979 and row["pub_year"] < 2000:
                return 'Medium Risk'
            if row["pub_year"] > 1999:
                return 'Low Risk'
            return 'NA'

        self.year_df["pub_year_raw_risk"] = self.year_df.apply(
            lambda row: pub_year_risk(row), axis=1)

        conditions = [
            (self.year_df["pub_year_raw_risk"] == 'High Risk'),
            (self.year_df["pub_year_raw_risk"] == 'Medium Risk'),
            (self.year_df["pub_year_raw_risk"] == 'Low Risk'),
        ]
        choices = [1, 2, 3]

        self.year_df['pub_year_risk_value'] = np.select(conditions, choices, default="NA")
        return self.year_df

    """ def rob_year(self):
        self.year_df["pub_year"] = pd.to_numeric(self.year_df["pub_year"], errors='coerce').fillna(0)

        conditions = [
            (self.year_df["pub_year"] < 1980),
            (self.year_df["pub_year"] >= 1980) & (self.year_df["pub_year"] < 2000),
            (self.year_df["pub_year"] >= 2000),
        ]
        choices_str = ['High Risk', 'Medium Risk', 'Low Risk']
        choices_val = [1, 2, 3]

        self.year_df["pub_year_raw_risk"] = np.select(conditions, choices_str, default="NA")
        self.year_df['pub_year_risk_value'] = np.select(conditions, choices_val, default="NA")

        return self.year_df """
    
    def rob_perc_attri(self):
        self.overall_percent_attrition_Comments_df.replace('%', '', regex=True, inplace=True)

        self.overall_percent_attrition_Comments_df["attri_perc_info"] = self.overall_percent_attrition_Comments_df["attri_perc_info"].apply(
            pd.to_numeric, errors='coerce').fillna(0)

        def perc_attrit_risk(row):
            if row["attri_perc_info"] < 10:
                return 'Low Risk'
            if row["attri_perc_info"] > 9 and row["attri_perc_info"] < 20:
                return 'Medium Risk'
            if row["attri_perc_info"] > 19:
                return 'High Risk'
            return 'NA'

        self.overall_percent_attrition_Comments_df["attri_perc_info_raw_risk"] = self.overall_percent_attrition_Comments_df.apply(
            lambda row: perc_attrit_risk(row), axis=1)

        conditions = [
            (self.overall_percent_attrition_Comments_df["attri_perc_info_raw_risk"] == 'High Risk'),
            (self.overall_percent_attrition_Comments_df["attri_perc_info_raw_risk"] == 'Medium Risk'),
            (self.overall_percent_attrition_Comments_df["attri_perc_info_raw_risk"] == 'Low Risk'),
        ]
        choices = [1, 2, 3]

        self.overall_percent_attrition_Comments_df['attri_perc_info_risk_value'] = np.select(conditions, choices, default="NA")
        return self.overall_percent_attrition_Comments_df

    """ def rob_perc_attri(self):
        self.overall_percent_attrition_Comments_df.replace('%', '', regex=True, inplace=True)

        self.overall_percent_attrition_Comments_df["attri_perc_info"] = pd.to_numeric(self.overall_percent_attrition_Comments_df["attri_perc_info"], errors='coerce').fillna(0)

        conditions = [
            (self.overall_percent_attrition_Comments_df["attri_perc_info"] < 10),
            (self.overall_percent_attrition_Comments_df["attri_perc_info"] >= 10) & (self.overall_percent_attrition_Comments_df["attri_perc_info"] < 20),
            (self.overall_percent_attrition_Comments_df["attri_perc_info"] >= 20),
        ]
        choices_str = ['Low Risk', 'Medium Risk', 'High Risk']
        choices_val = [3, 2, 1]

        self.overall_percent_attrition_Comments_df["attri_perc_info_raw_risk"] = np.select(conditions, choices_str, default="NA")
        self.overall_percent_attrition_Comments_df['attri_perc_info_risk_value'] = np.select(conditions, choices_val, default="NA")

        return self.overall_percent_attrition_Comments_df """

    def rob_clustering(self):

        # Medium/High risk for Yes/No – the difference is usually trivial 
        # (slightly wider confidence intervals), but reflects a less sophisticated analysis.

        self.clustering_df["clust_anal_raw"] = self.clustering_df["clust_anal_raw"].apply(
            lambda x: ",".join(x) if isinstance(x, list) else x)

        conditions = [
            (self.clustering_df['clust_anal_raw'] == "Yes"),
            (self.clustering_df['clust_anal_raw'] == "No"),
        ]

        # GET RISK LEVELS PER PUBLICATION TYPE
        choices = ['Medium Risk', 'High Risk', ]

        self.clustering_df["clust_anal_raw_risk"] = np.select(conditions, choices, default="NA")

        conditions = [
            (self.clustering_df["clust_anal_raw_risk"] == 'Medium Risk'),
            (self.clustering_df["clust_anal_raw_risk"] == 'High Risk'),
        ]

        choices = [2,1]

        self.clustering_df["clust_anal_risk_value"] = np.select(conditions, choices, default="NA")
        return self.clustering_df

    """ def rob_clustering(self):
        # Using .map() instead of .apply() for more efficient operations on pandas Series
        self.clustering_df["clust_anal_raw"] = self.clustering_df["clust_anal_raw"].map(
            lambda x: ",".join(x) if isinstance(x, list) else x
        )
        
        # Creating dictionary mapping for more straightforward replacement
        risk_mapping = {
            "Yes": "Medium Risk",
            "No": "High Risk"
        }
        self.clustering_df["clust_anal_raw_risk"] = self.clustering_df["clust_anal_raw"].map(
            risk_mapping, na_action='ignore'
        ).fillna("NA")
        
        risk_value_mapping = {
            "Medium Risk": 2,
            "High Risk": 1
        }
        self.clustering_df["clust_anal_risk_value"] = self.clustering_df["clust_anal_raw_risk"].map(
            risk_value_mapping, na_action='ignore'
        ).fillna("NA")
        
        return self.clustering_df """

    def rob_tkit_es_type(self):
        self.toolkit_es_type = pd.DataFrame(self.toolkit_es_type)

        #if len(self.toolkit_es_type.columns) > 1:
            #del self.toolkit_es_type[1]

        self.toolkit_es_type.columns = ["out_es_type"]
        self.toolkit_es_type["out_es_type"] = self.toolkit_es_type["out_es_type"].apply(lambda x: ",".join(x) if isinstance(x, list) else x)

        conditions = [
            (self.toolkit_es_type["out_es_type"] == "Post-test unadjusted (select one from this group)"),
            (self.toolkit_es_type["out_es_type"] == "Post-test adjusted for baseline attainment"),
            (self.toolkit_es_type["out_es_type"] == "Post-test adjusted for baseline attainment AND clustering"),
            (self.toolkit_es_type["out_es_type"] == "Pre-post gain"),
        ]

        choices = ['High Risk', 'Low Risk', 'Low Risk', 'Medium Risk']

        self.toolkit_es_type["out_es_type_raw_risk"] = np.select(conditions, choices, default="NA")

        conditions = [
            (self.toolkit_es_type["out_es_type_raw_risk"] == 'High Risk'),
            (self.toolkit_es_type["out_es_type_raw_risk"] == 'Medium Risk'),
            (self.toolkit_es_type["out_es_type_raw_risk"] == 'Low Risk'),
        ]

        choices = [1, 2, 3]

        self.toolkit_es_type["out_es_type_risk_value"] = np.select(conditions, choices, default="NA")
        return self.toolkit_es_type

    def rob_tkit_test_type(self):
        self.toolkit_test_type = pd.DataFrame(self.toolkit_test_type)

        if len(self.toolkit_test_type.columns) >1:
            del self.toolkit_test_type[1]

        self.toolkit_test_type.columns = ["out_test_type_raw"]
        self.toolkit_test_type["out_test_type_raw"] = self.toolkit_test_type["out_test_type_raw"].apply(
            lambda x: ",".join(x) if isinstance(x, list) else x)

        conditions = [
            (self.toolkit_test_type["out_test_type_raw"] == "Test type: Standardised test "),
            (self.toolkit_test_type["out_test_type_raw"] == "Test type: Researcher developed test"),
            (self.toolkit_test_type["out_test_type_raw"] == "Test type: National test"),
            (self.toolkit_test_type["out_test_type_raw"] == "Test type: School-developed test"),
            (self.toolkit_test_type["out_test_type_raw"] == "Test type: International tests"),
        ]

        # GET RISK LEVELS PER PUBLICATION TYPE
        choices = ['Low Risk', 'High Risk', 'Low Risk', 'Medium Risk', 'Low Risk']

        self.toolkit_test_type["out_test_type_raw_risk"] = np.select(conditions, choices, default="NA")

        conditions = [
            (self.toolkit_test_type["out_test_type_raw_risk"] == 'High Risk'),
            (self.toolkit_test_type["out_test_type_raw_risk"] == 'Medium Risk'),
            (self.toolkit_test_type["out_test_type_raw_risk"] == 'Low Risk'),
        ]

        choices = [1, 2, 3]

        self.toolkit_test_type["out_test_type_raw_risk_value"] = np.select(
            conditions, choices, default="NA")
        return self.toolkit_test_type

    def rob_sample_size_comments(self):
        self.sample_size_Comments_df["sample_analysed_info"] = self.sample_size_Comments_df["sample_analysed_info"].apply(
            pd.to_numeric, errors='coerce').fillna(0)

        def sample_size_risk(row):
            if row["sample_analysed_info"] <= 30: return 'High Risk'
            if row["sample_analysed_info"] > 30 and row["sample_analysed_info"] < 100: return 'Medium Risk'
            if row["sample_analysed_info"] > 99: return 'Low Risk'
            return 'NA'

        self.sample_size_Comments_df["sample_size_risk"] = self.sample_size_Comments_df.apply(lambda row: sample_size_risk(row), axis=1)

        conditions = [
            (self.sample_size_Comments_df["sample_size_risk"] == 'High Risk'),
            (self.sample_size_Comments_df["sample_size_risk"] == 'Medium Risk'),
            (self.sample_size_Comments_df["sample_size_risk"] == 'Low Risk'),
        ]
        choices = [1, 2, 3]

        self.sample_size_Comments_df['sample_size_risk_value'] = np.select(
            conditions, choices, default="NA")
        return self.sample_size_Comments_df

    def rob_pub_type(self):
        self.publicationtype_df["pub_type_raw"] = self.publicationtype_df["pub_type_raw"].apply(lambda x: ",".join(x) if isinstance(x, list) else x)

        conditions = [
            (self.publicationtype_df['pub_type_raw'] == "Journal article"),
            (self.publicationtype_df['pub_type_raw'] == "Dissertation or thesis"),
            (self.publicationtype_df['pub_type_raw'] == "Technical report"),
            (self.publicationtype_df['pub_type_raw'] == "Book or book chapter"),
            (self.publicationtype_df['pub_type_raw'] == "Conference paper"),
            (self.publicationtype_df['pub_type_raw'] == "Other (Please specify)"),
        ]

        # GET RISK LEVELS PER PUBLICATION TYPE
        choices = ['Low Risk', 'Low Risk', 'Low Risk', 'Medium Risk', 'Medium Risk', 'Medium Risk']

        self.publicationtype_df["pub_type_risk"] = np.select(conditions, choices, default="NA")

        conditions = [
            (self.publicationtype_df["pub_type_risk"] == 'High Risk'),
            (self.publicationtype_df["pub_type_risk"] == 'Medium Risk'),
            (self.publicationtype_df["pub_type_risk"] == 'Low Risk'),
        ]

        choices = [1, 2, 3]

        self.publicationtype_df["pub_type_risk_value"] = np.select(conditions, choices, default="NA")
        return self.publicationtype_df
    
    def rob_part_assign(self):

        conditions = [
            (self.participant_assignment_df['part_assig_raw'] == "Random (please specify)"),
            (self.participant_assignment_df['part_assig_raw'] == "Non-random, but matched"),
            (self.participant_assignment_df['part_assig_raw'] == "Non-random, not matched prior to treatment"),
            (self.participant_assignment_df['part_assig_raw'] == "Unclear"),
            (self.participant_assignment_df['part_assig_raw'] == "Not assigned - naturally occurring sample"),
            (self.participant_assignment_df['part_assig_raw'] == "Retrospective Quasi Experimental Design (QED)"),
            (self.participant_assignment_df['part_assig_raw'] == "Regression discontinuity"),
        ]
        choices = ['Low Risk', 'Medium Risk', 'Medium Risk', 'Medium Risk', 'Medium Risk', 'Medium Risk', 'Medium Risk']

        self.participant_assignment_df['part_assig_risk'] = np.select(conditions, choices, default="NA")

        conditions = [
            (self.participant_assignment_df['part_assig_risk'] == 'High Risk'),
            (self.participant_assignment_df['part_assig_risk'] == 'Medium Risk'),
            (self.participant_assignment_df['part_assig_risk'] == 'Low Risk'),
        ]
        choices = [1, 2, 3]

        self.participant_assignment_df['part_assig_risk_value'] = np.select(conditions, choices, default="NA")
        return self.participant_assignment_df

    def rob_randomisation(self):

        conditions = [
            (self.randomisation_df['rand_raw'] == 'Yes'),
            (self.randomisation_df['rand_raw'] == 'Not applicable'),
            (self.randomisation_df['rand_raw'] == 'No/Unclear'),
        ]
        choices = ['Low Risk', 'Medium Risk', 'Medium Risk']

        self.randomisation_df['rand_risk'] = np.select(conditions, choices, default="NA")

        conditions = [
            (self.randomisation_df['rand_risk'] == 'Low Risk'),
            (self.randomisation_df['rand_risk'] == 'Medium Risk'),
            (self.randomisation_df['rand_risk'] == 'Medium Risk'),
        ]
        choices = [3, 2, 2]

        self.randomisation_df['rand_risk_value'] = np.select(conditions, choices, default="NA")
        return self.randomisation_df

    def rob_eco_valid(self):

        conditions = [
            (self.study_realism_df['eco_valid_raw'] == 'High ecological validity'),
            (self.study_realism_df['eco_valid_raw'] == 'Low ecological validity'),
            (self.study_realism_df['eco_valid_raw'] == 'Unclear'),
        ]
        choices = ['Low Risk', 'High Risk', 'High Risk']

        self.study_realism_df['eco_valid_risk'] = np.select(conditions, choices, default="NA")

        conditions = [
            (self.study_realism_df['eco_valid_risk'] == 'Low Risk'),
            (self.study_realism_df['eco_valid_risk'] == 'High Risk'),
        ]
        choices = [3, 1]

        self.study_realism_df['eco_valid_risk_value'] = np.select(conditions, choices, default="NA")
        return self.study_realism_df
    
    def rob_num_schools_int(self):
        self.number_of_schools_intervention_Comments_df["school_treat_info_new"] = self.number_of_schools_intervention_Comments_df["school_treat_info"].apply(
            pd.to_numeric, errors='coerce').fillna(0)

        def school_treat_risk(row):
            if row['school_treat_info_new'] == 1: return 'High Risk'
            if row['school_treat_info_new'] > 1 and row['school_treat_info_new'] < 6: return 'Medium Risk'
            if row['school_treat_info_new'] > 5: return 'Low Risk'
            return 'NA'

        self.number_of_schools_intervention_Comments_df["school_treat_risk"] = self.number_of_schools_intervention_Comments_df.apply(
            lambda row: school_treat_risk(row), axis=1)

        conditions = [
            (self.number_of_schools_intervention_Comments_df["school_treat_risk"] == 'High Risk'),
            (self.number_of_schools_intervention_Comments_df["school_treat_risk"] == 'Medium Risk'),
            (self.number_of_schools_intervention_Comments_df["school_treat_risk"] == 'Low Risk'),
        ]
        choices = [1, 2, 3]

        self.number_of_schools_intervention_Comments_df['school_treat_risk_value'] = np.select(conditions, choices, default="NA")
        return self.number_of_schools_intervention_Comments_df

    def rob_num_classes_total(self):
        self.number_of_classes_total_Comments_df["class_total_info_new"] = self.number_of_classes_total_Comments_df["class_total_info"].apply(
            pd.to_numeric, errors='coerce').fillna(0)

        def class_total_risk1(row):
            if row['class_total_info_new'] == 1:
                return 'Higher Risk'
            if row['class_total_info_new'] > 1 and row['class_total_info_new'] < 6:
                return 'Medium Risk'
            if row['class_total_info_new'] > 5:
                return 'Low Risk'
            return 'NA'

        self.number_of_classes_total_Comments_df["class_total_info_risk"] = self.number_of_classes_total_Comments_df.apply(
            lambda row: class_total_risk1(row), axis=1)

        conditions = [
            (self.number_of_classes_total_Comments_df["class_total_info_risk"] == 'High Risk'),
            (self.number_of_classes_total_Comments_df["class_total_info_risk"] == 'Medium Risk'),
            (self.number_of_classes_total_Comments_df["class_total_info_risk"] == 'Low Risk'),
            (self.number_of_classes_total_Comments_df["class_total_info_risk"] == 'NA'),
        ]
        choices = [1, 2, 3, np.nan]

        self.number_of_classes_total_Comments_df['class_total_risk_value'] = np.select(conditions, choices, default="NA")
        return self.number_of_classes_total_Comments_df
    
    def rob_int_who(self):
        # originals
        #intervention_delivery_df["research staff"] = intervention_delivery_df["int_who_raw"].apply(lambda x: 'Research staff' in x)
        #intervention_delivery_df["class teachers"]  = intervention_delivery_df["int_who_raw"].apply(lambda x: 'Class teachers' in x)
        #intervention_delivery_df["other school staff"] = intervention_delivery_df["int_who_raw"].apply(lambda x: 'Other school staff' in x)

        self.intervention_delivery_df["peers"] = self.intervention_delivery_df["int_who_raw"].apply(lambda x: 'Peers' in x)
        self.intervention_delivery_df["lay persons/volunteers"] = self.intervention_delivery_df["int_who_raw"].apply(lambda x: 'Lay persons/volunteers' in x)
        self.intervention_delivery_df["digital technology"] = self.intervention_delivery_df["int_who_raw"].apply(lambda x: 'Digital technology' in x)
        self.intervention_delivery_df["parents/carers"] = self.intervention_delivery_df["int_who_raw"].apply(lambda x: 'Parents/carers' in x)
        self.intervention_delivery_df["external teachers"] = self.intervention_delivery_df["int_who_raw"].apply(lambda x: 'External teachers' in x)
        self.intervention_delivery_df["teaching assistants"] = self.intervention_delivery_df["int_who_raw"].apply(lambda x: 'Teaching assistants' in x)
        self.intervention_delivery_df["research staff"] = self.intervention_delivery_df["int_who_raw"].apply(lambda x: 'Research staff' in x)
        self.intervention_delivery_df["class teachers"] = self.intervention_delivery_df["int_who_raw"].apply(lambda x: 'Class teachers' in x)
        self.intervention_delivery_df["unclear/not specified"] = self.intervention_delivery_df["int_who_raw"].apply(lambda x: 'Unclear/not specified' in x)

        self.intervention_delivery_df.columns = [
            "int_who_raw", "peers", 
            "lay persons/volunteers", 
            "digital technology", 
            "parents/carers", 
            "external teachers", 
            "teaching assistants", 
            "research staff", 
            "class teachers", 
            "unclear/not specified"
        ]

        self.intervention_delivery_df.loc[self.intervention_delivery_df['int_who_raw'].map(str).str.contains('Unclear/not specified'), 'int_who_raw_risk_value'] = 1
        self.intervention_delivery_df.loc[self.intervention_delivery_df['int_who_raw'].map(str).str.contains('Peers'), 'int_who_raw_risk_value']   = 1
        self.intervention_delivery_df.loc[self.intervention_delivery_df['int_who_raw'].map(str).str.contains('Lay persons/volunteers'), 'int_who_raw_risk_value']  = 2
        self.intervention_delivery_df.loc[self.intervention_delivery_df['int_who_raw'].map(str).str.contains('Digital technology'), 'int_who_raw_risk_value']   = 1
        self.intervention_delivery_df.loc[self.intervention_delivery_df['int_who_raw'].map(str).str.contains('Teaching assistants'), 'int_who_raw_risk_value'] = 2
        self.intervention_delivery_df.loc[self.intervention_delivery_df['int_who_raw'].map(str).str.contains('Parents/carers'), 'int_who_raw_risk_value'] = 2
        self.intervention_delivery_df.loc[self.intervention_delivery_df['int_who_raw'].map(str).str.contains('Research staff'), 'int_who_raw_risk_value'] = 2
        self.intervention_delivery_df.loc[self.intervention_delivery_df['int_who_raw'].map(str).str.contains('Class teachers'), 'int_who_raw_risk_value'] = 3
        self.intervention_delivery_df.loc[self.intervention_delivery_df['int_who_raw'].map(str).str.contains('External teachers'), 'int_who_raw_risk_value'] = 2

        self.intervention_delivery_df['int_who_raw_risk_value'] = self.intervention_delivery_df['int_who_raw_risk_value']
        return self.intervention_delivery_df
    
    def rob_out_eval(self):
        #del self.InterventionEvaluation_df['eef_eval_raw']

        self.InterventionEvaluation_df['out_eval_raw'] = self.InterventionEvaluation_df['out_eval_raw'].str[0]

        conditions = [
            (self.InterventionEvaluation_df['out_eval_raw'] == "The developer"),
            (self.InterventionEvaluation_df['out_eval_raw'] == "A different organization paid by developer"),
            (self.InterventionEvaluation_df['out_eval_raw'] == "An organization commissioned independently to evaluate"),
            (self.InterventionEvaluation_df['out_eval_raw'] == "Unclear/not stated"),
        ]

        # GET RISK LEVELS PER OUTCOME EVALUATION
        choices = ['Medium Risk', 'Medium Risk', 'Low Risk', 'Medium Risk']

        self.InterventionEvaluation_df["out_eval_risk"] = np.select(conditions, choices, default="NA")

        conditions = [
            (self.InterventionEvaluation_df["out_eval_risk"] == 'High Risk'),
            (self.InterventionEvaluation_df["out_eval_risk"] == 'Medium Risk'),
            (self.InterventionEvaluation_df["out_eval_risk"] == 'Low Risk'),
        ]

        choices = [1, 2, 3]

        self.InterventionEvaluation_df["out_eval_risk_value"] = np.select(conditions, choices, default="NA")
        return self.InterventionEvaluation_df

    def rob_comparability(self):
        #del self.comparability_df["comp_anal_ht"]
        #del self.comparability_df["comp_anal_info"]

        self.comparability_df['comp_anal_raw'] = self.comparability_df['comp_anal_raw'].apply(lambda x: ",".join(x) if isinstance(x, list) else x)

        conditions = [
            (self.comparability_df['comp_anal_raw'] == "Yes"),
            (self.comparability_df['comp_anal_raw'] == "No"),
            (self.comparability_df['comp_anal_raw'] == "Unclear or details not provided"),
        ]

        choices = ['Low Risk', 'Medium Risk', 'Medium Risk']

        self.comparability_df["comp_anal_risk"] = np.select(conditions, choices, default="NA")

        conditions = [
            (self.comparability_df['comp_anal_risk'] == 'Low Risk'),
            (self.comparability_df['comp_anal_risk'] == 'Medium Risk'),
            (self.comparability_df['comp_anal_risk'] == 'High Risk'),
        ]
        choices = [3, 2, 1]

        self.comparability_df["comp_anal_risk_value"] = np.select(conditions, choices, default="NA")
        return self.comparability_df

    def rob_post_process(self):
        self.risk_of_bias_df = pd.concat([
            self.eppiid_df, 
            self.author_df, 
            self.tool_prim_es,
            self.tool_prim_se,
            self.year_df, 
            self.admin_strand_df,
            self.publicationtype_df,
            self.participant_assignment_df,
            self.study_realism_df,
            self.number_of_schools_intervention_Comments_df,
            self.intervention_delivery_df,
            self.number_of_classes_total_Comments_df,
            self.InterventionEvaluation_df,
            self.comparability_df,
            self.sample_size_Comments_df,
            self.toolkit_test_type,
            self.toolkit_es_type,
            self.overall_percent_attrition_Comments_df,
            self.clustering_df,
            self.randomisation_df
        ], axis=1, sort=False)
    
        # CONVERT OBJECT COLUMNS TO FLOAT (FOR ADDITION)
        """ self.risk_of_bias_df["rand_risk_value"] = self.risk_of_bias_df["rand_risk_value"].apply(pd.to_numeric, errors='coerce')
        self.risk_of_bias_df["part_assig_risk_value"] = self.risk_of_bias_df["part_assig_risk_value"].apply(pd.to_numeric, errors='coerce')
        self.risk_of_bias_df["eco_valid_risk_value"] = self.risk_of_bias_df["eco_valid_risk_value"].apply(pd.to_numeric, errors='coerce')
        self.risk_of_bias_df["school_treat_risk_value"] = self.risk_of_bias_df["school_treat_risk_value"].apply(pd.to_numeric, errors='coerce')
        self.risk_of_bias_df["pub_type_risk_value"] = self.risk_of_bias_df["pub_type_risk_value"].apply(pd.to_numeric, errors='coerce')
        self.risk_of_bias_df["class_total_risk_value"] = self.risk_of_bias_df["class_total_risk_value"].apply(pd.to_numeric, errors='coerce')
        self.risk_of_bias_df["out_eval_risk_value"] = self.risk_of_bias_df["out_eval_risk_value"].apply(pd.to_numeric, errors='coerce')
        self.risk_of_bias_df["comp_anal_risk_value"] = self.risk_of_bias_df["comp_anal_risk_value"].apply(pd.to_numeric, errors='coerce')
        self.risk_of_bias_df["sample_size_risk_value"] = self.risk_of_bias_df["sample_size_risk_value"].apply(pd.to_numeric, errors='coerce')
        self.risk_of_bias_df["out_test_type_raw_risk_value"] = self.risk_of_bias_df["out_test_type_raw_risk_value"].apply(pd.to_numeric, errors='coerce')
        self.risk_of_bias_df["out_es_type_risk_value"] = self.risk_of_bias_df["out_es_type_risk_value"].apply(pd.to_numeric, errors='coerce')
        self.risk_of_bias_df["int_who_raw_risk_value"] = self.risk_of_bias_df["int_who_raw_risk_value"].apply(pd.to_numeric, errors='coerce')
        self.risk_of_bias_df["attri_perc_info_risk_value"] = self.risk_of_bias_df["attri_perc_info_risk_value"].apply(pd.to_numeric, errors='coerce')
        self.risk_of_bias_df["clust_anal_risk_value"] = self.risk_of_bias_df["clust_anal_risk_value"].apply(pd.to_numeric, errors='coerce')
        self.risk_of_bias_df["pub_year_risk_value"] = self.risk_of_bias_df["pub_year_risk_value"].apply(pd.to_numeric, errors='coerce') """

        columns_to_convert = [
            "rand_risk_value",
            "part_assig_risk_value",
            "eco_valid_risk_value",
            "school_treat_risk_value",
            "pub_type_risk_value",
            "class_total_risk_value",
            "out_eval_risk_value",
            "comp_anal_risk_value",
            "sample_size_risk_value",
            "out_test_type_raw_risk_value",
            "out_es_type_risk_value",
            "int_who_raw_risk_value",
            "attri_perc_info_risk_value",
            "clust_anal_risk_value",
            "pub_year_risk_value"
        ]


        for column in columns_to_convert:
            self.risk_of_bias_df[column] = self.risk_of_bias_df[column].apply(pd.to_numeric, errors='coerce')

        """ self.risk_of_bias_df['strand_raw'] = self.risk_of_bias_df['strand_raw'].str.join(', ') """

        self.risk_of_bias_df['raw_total'] = self.risk_of_bias_df[[
            'pub_year_risk_value',
            'pub_type_risk_value',
            'part_assig_risk_value',
            'rand_risk_value',
            'out_test_type_raw_risk_value',
            'eco_valid_risk_value',
            'int_who_raw_risk_value',
            'school_treat_risk_value',
            'sample_size_risk_value',
            'class_total_risk_value',
            'out_eval_risk_value',
            'out_es_type_risk_value',
            'comp_anal_risk_value',
            'attri_perc_info_risk_value',
            'clust_anal_risk_value',
        ]].iloc[:].sum(axis=1)

        # concatanate risk values for mean calculation
        mean_calc = pd.concat([
            self.risk_of_bias_df["pub_year_risk_value"],
            self.risk_of_bias_df["pub_type_risk_value"],
            self.risk_of_bias_df["part_assig_risk_value"],
            self.risk_of_bias_df["rand_risk_value"],
            self.risk_of_bias_df["out_test_type_raw_risk_value"],
            self.risk_of_bias_df["eco_valid_risk_value"],
            self.risk_of_bias_df["school_treat_risk_value"],
            self.risk_of_bias_df["sample_size_risk_value"],
            self.risk_of_bias_df["class_total_risk_value"],
            self.risk_of_bias_df["out_eval_risk_value"],
            self.risk_of_bias_df["out_es_type_risk_value"],
            self.risk_of_bias_df["comp_anal_risk_value"],
            self.risk_of_bias_df["attri_perc_info_risk_value"],
            self.risk_of_bias_df["clust_anal_risk_value"],
            self.risk_of_bias_df['int_who_raw_risk_value']
        ], axis=1, sort=False)

        self.risk_of_bias_df["NA_values"] = mean_calc.isnull().sum(axis=1)

        # Replace zero with np.nan
        mean_calc = mean_calc.replace(0, np.nan)
        self.risk_of_bias_df["Mean"] = mean_calc.mean(axis=1)

        # Get median and assign to 'median' column on a row by row basis
        self.risk_of_bias_df["Median"] = mean_calc.median(axis=1)

        # Final data cleaning
        self.risk_of_bias_df.replace('~', '', regex=True, inplace=True)
        self.risk_of_bias_df.replace('<', '', regex=True, inplace=True)
        self.risk_of_bias_df.replace('≤', '', regex=True, inplace=True)
        self.risk_of_bias_df.replace(['NA'], 'NA', inplace=True)
        self.risk_of_bias_df.replace(['N'], 'NA', inplace=True)
        self.risk_of_bias_df.replace('\r', ' ', regex=True, inplace=True)
        self.risk_of_bias_df.replace('\n', ' ', regex=True, inplace=True)
        self.risk_of_bias_df.replace(':', ' ',  regex=True, inplace=True)
        self.risk_of_bias_df.replace(';', ' ',  regex=True, inplace=True)
        self.risk_of_bias_df.replace(r'^\s*$', "NA", regex=True)
        self.risk_of_bias_df.fillna('NA', inplace=True)

        # Append raw_total column to the end of the data frame
        final_score_col = self.risk_of_bias_df.pop('raw_total')
        self.risk_of_bias_df.insert(63, 'raw_total', final_score_col)


    def compile(self):
        self.initialize_vars()
        self.rob_year()
        self.rob_perc_attri()
        self.rob_clustering()
        self.rob_tkit_es_type()
        self.rob_tkit_test_type()
        self.rob_sample_size_comments()
        self.rob_pub_type()
        self.rob_part_assign()
        self.rob_randomisation()
        self.rob_eco_valid()
        self.rob_num_schools_int()
        self.rob_num_classes_total()
        self.rob_int_who()
        self.rob_out_eval()
        self.rob_comparability()
        self.rob_post_process()
    

    def save_dataframe(self):
        outfile7 = self.data_extraction.save_dataframe(self.risk_of_bias_df, "_Study_Security.csv", standard_info=True)
        return outfile7
    

    def padlocks(self):

        # % studies since year 2000 
        """ number_of_studies = len(self.risk_of_bias_df)
        self.risk_of_bias_df["pub_year"] = pd.to_numeric(self.risk_of_bias_df["pub_year"], errors='coerce')
        recent_studies = len(self.risk_of_bias_df[self.risk_of_bias_df["pub_year"] > 2000])
        perc_recent = recent_studies/number_of_studies*100
        perc_recent = np.round(perc_recent, 2) """

        self.risk_of_bias_df["pub_year"] = pd.to_numeric(self.risk_of_bias_df["pub_year"], errors='coerce')
        perc_recent = (self.risk_of_bias_df["pub_year"] > 2000).mean() * 100
        perc_recent = round(perc_recent, 2)

        #print(f"perc_recent: {perc_recent}")

        # total pupil number
        number_of_studies = len(self.risk_of_bias_df)
        total_pupil_number = self.risk_of_bias_df["sample_analysed_info"].sum().astype(int)

        # print(f"total_pupil_number: {total_pupil_number}")

        # percentage randomised
        perc_randomised = self.risk_of_bias_df[self.risk_of_bias_df["rand_raw"] == 'Yes'].shape[0]/len(self.risk_of_bias_df)*100
        perc_randomised = np.round(perc_randomised, 1)

        # print(f"perc_randomised: {perc_randomised}")

        # percentrage high ecological validity
        perc_high_eco_valid = self.risk_of_bias_df[self.risk_of_bias_df["eco_valid_raw"] == 'High ecological validity'].shape[0]/len(self.risk_of_bias_df)*100
        perc_high_eco_valid = np.round(perc_high_eco_valid, 1)

        # print(f"perc_high_eco_valid: {perc_high_eco_valid}")

        # mean ecological validity risk value
        self.risk_of_bias_df["eco_valid_risk_value"] = pd.to_numeric(self.risk_of_bias_df["eco_valid_risk_value"], errors='coerce')
        mean_eco_valid_risk = self.risk_of_bias_df["eco_valid_risk_value"].mean()
        mean_eco_valid_risk = np.round(mean_eco_valid_risk, 2)

        # print(f"mean_eco_valid_risk: {mean_eco_valid_risk}")

        # median school treatment number
        self.risk_of_bias_df["school_treat_info"] = pd.to_numeric(self.risk_of_bias_df["school_treat_info"], errors='coerce')
        median_school_number = self.risk_of_bias_df["school_treat_info"].median(skipna=True)
        median_school_number = np.round(median_school_number, 2)

        #print(f"median_school_number: {median_school_number}")

        # mean number of schools risk value
        self.risk_of_bias_df["school_treat_risk_value"] = pd.to_numeric(self.risk_of_bias_df["school_treat_risk_value"], errors='coerce')
        mean_number_schools_risk = self.risk_of_bias_df["school_treat_risk_value"].mean()
        mean_number_schools_risk = np.round(mean_number_schools_risk, 2)

        #print(f"mean_number_schools_risk: {mean_number_schools_risk}")

        # participant assignment risk value
        self.participant_assignment_df['part_assig_risk_value'] = pd.to_numeric(self.participant_assignment_df['part_assig_risk_value'], errors='coerce')
        participant_assignment_risk = self.participant_assignment_df['part_assig_risk_value'].mean()
        participant_assignment_risk.round(2)

        # print(f"participant_assignment_risk: {participant_assignment_risk}")

        # Percentage taught by research staff only (int_who_raw)
        self.risk_of_bias_df["class_total_info"] = pd.to_numeric(self.risk_of_bias_df["class_total_info"], errors='coerce')
        median_class_number = self.risk_of_bias_df["class_total_info"].median()
        median_class_number = np.round(median_class_number, 2)

        # print(f"median_class_number: {median_class_number}")

        # mean class number risk value
        self.risk_of_bias_df["class_total_risk_value"] = pd.to_numeric(self.risk_of_bias_df["class_total_risk_value"], errors='coerce')
        mean_class_risk = self.risk_of_bias_df["class_total_risk_value"].mean()
        mean_class_risk = np.round(mean_class_risk, 2)

        #print(f"mean_class_risk: {mean_class_risk}")

        # percentage independently evaluated
        perc_indep_eval = self.risk_of_bias_df[self.risk_of_bias_df["out_eval_raw"] == 'An organization commissioned independently to evaluate'].shape[0]/len(self.risk_of_bias_df)*100
        perc_indep_eval = np.round(perc_indep_eval, 1)

        #print(f"perc_indep_eval: {perc_indep_eval}")

        # median percent attrition reported
        self.overall_percent_attrition_Comments_df["attri_perc_info"] = pd.to_numeric(self.overall_percent_attrition_Comments_df["attri_perc_info"], errors='coerce')
        median_perc_attrit_reported = self.overall_percent_attrition_Comments_df["attri_perc_info"].median(skipna=True)
        median_perc_attrit_reported = np.round(median_perc_attrit_reported, 2)

        # print(f"median_perc_attrit_reported: {median_perc_attrit_reported}")

        # percentage taught by research staff only
        conditions = [
            (self.intervention_delivery_df['research staff'] == True) &
            (self.intervention_delivery_df["class teachers"] == False) &
            (self.intervention_delivery_df["external teachers"] == False),
        ]
        values = ['1']
        self.intervention_delivery_df['research_staff_only'] = np.select(conditions, values)
        research_staff_only = (self.intervention_delivery_df["research_staff_only"] == "1").sum()/len(self.intervention_delivery_df*100)

        # print(f"research_staff_only: {research_staff_only}")

        strand = self.admin_strand_df.iloc[0, 0]

        df = pd.DataFrame([[
            strand,
            number_of_studies, 
            perc_recent,
            total_pupil_number, 
            perc_randomised, 
            perc_high_eco_valid, 
            mean_eco_valid_risk,
            median_school_number,
            mean_number_schools_risk,
            median_class_number,
            mean_class_risk,
            perc_indep_eval,
            participant_assignment_risk,
            research_staff_only,
            median_perc_attrit_reported
        ]])

        df.columns = [
            "strand",
            "number_of_studies",
            "%_since_2000",
            "total_pupil_number",
            "%_randomised",
            "%_high_eco_valid",
            "mean_eco_valid_risk",
            "median_school_number",
            "mean_number_Schools_risk",
            "median_class_number",
            "mean_class_risk",
            "%_indep_eval",
            "part_assig_risk",
            "%_taught_res_staff_only",
            "%_median_attrit_reported"
        ]

        ########################################
        # % studies since 2000 padlock scale
        ########################################

        """ # convert %_since_2000 data to numeric
        df["%_since_2000"] = pd.to_numeric(df["%_since_2000"], errors='coerce').fillna(0)

        def perc_recent_risk(row):
            if row["%_since_2000"] > 49:
                return 'L'
            if row["%_since_2000"] > 25 and row["%_since_2000"] < 50:
                return 'M'
            if row["%_since_2000"] < 25:
                return 'H'
            return 'NA'

        # apply padlock function to number of studies column
        df["%_since_2000_padlock_scale"] = df.apply(lambda row: perc_recent_risk(row), axis=1) """

        df["%_since_2000"] = pd.to_numeric(df["%_since_2000"], errors='coerce').fillna(0)

        df["%_since_2000_padlock_scale"] = pd.cut(
            df["%_since_2000"],
            bins=[-np.inf, 25, 50, np.inf],
            labels=['H', 'M', 'L'],
            right=False,
            include_lowest=True
)

        ########################################
        # _median_attrit_reported padlock scale
        ########################################

        # convert median attrition data to numeric
        """ df["%_median_attrit_reported"] = pd.to_numeric(df["%_median_attrit_reported"], errors='coerce').fillna(0)

        def median_attrit_report_risk(row):
            if row["%_median_attrit_reported"] < 15:
                return 'L'
            if row["%_median_attrit_reported"] > 14 and row["%_median_attrit_reported"] < 30:
                return 'M'
            if row["%_median_attrit_reported"] > 29:
                return 'H'
            return 'NA'
        
        # apply padlock function to number of studies column
        df["%_median_attrit_reported_padlock_scale"] = df.apply(lambda row: median_attrit_report_risk(row), axis=1) """

        df["%_median_attrit_reported"] = pd.to_numeric(df["%_median_attrit_reported"], errors='coerce').fillna(0)

        df["%_median_attrit_reported_padlock_scale"] = pd.cut(
            df["%_median_attrit_reported"],
            bins=[-np.inf, 15, 30, np.inf],
            labels=['L', 'M', 'H'],
            right=False,
            include_lowest=True
        )


        ########################################
        # make number of studies padlock scale
        ########################################

        # convert number of studies data to numeric
        """ df["number_of_studies"] = pd.to_numeric(df["number_of_studies"], errors='coerce').fillna(0)

        def num_studies_risk(row):
            if row["number_of_studies"] < 10:
                return '0'
            if row["number_of_studies"] > 9 and row["number_of_studies"] < 25:
                return '1'
            if row["number_of_studies"] > 24 and row["number_of_studies"] < 35:
                return '2'
            if row["number_of_studies"] > 34 and row["number_of_studies"] < 60:
                return '3'
            if row["number_of_studies"] > 59 and row["number_of_studies"] < 90:
                return '4'
            if row["number_of_studies"] > 89:
                return '5'
            return 'NA'

        # apply padlock function to number of studies column
        df["number_of_studies_padlock_scale"] = df.apply(lambda row: num_studies_risk(row), axis=1) """

        df["number_of_studies"] = pd.to_numeric(df["number_of_studies"], errors='coerce').fillna(0)

        bins = [0, 10, 25, 35, 60, 90, np.inf]
        labels = ['0', '1', '2', '3', '4', '5']
        df["number_of_studies_padlock_scale"] = pd.cut(df["number_of_studies"], bins=bins, labels=labels, right=False, include_lowest=True)


        ########################################
        # make % randomised padlock scale
        ########################################

        # convert number of studies data to numeric
        """ df["%_randomised"] = pd.to_numeric(df["%_randomised"], errors='coerce').fillna(0)

        def perc_randomised_risk(row):
            if row["%_randomised"] < 30:
                return 'H'
            if row["%_randomised"] > 29 and row["%_randomised"] < 60:
                return 'M'
            if row["%_randomised"] > 59:
                return 'L'
            return 'NA'

        df["%_randomised_padlock_scale"] = df.apply(lambda row: perc_randomised_risk(row), axis=1) """

        df["%_randomised"] = pd.to_numeric(df["%_randomised"], errors='coerce').fillna(0)

        df["%_randomised_padlock_scale"] = pd.cut(
            df["%_randomised"],
            bins=[-np.inf, 30, 60, np.inf],
            labels=['H', 'M', 'L'],
            right=False,
            include_lowest=True
        )


        ########################################
        # make ecological validity padlock scale
        ########################################

        # convert number of studies data to numeric
        """ df["%_high_eco_valid"] = pd.to_numeric(df["%_high_eco_valid"], errors='coerce').fillna(0)

        def eco_valid_risk(row):
            if row["%_high_eco_valid"] < 50:
                return 'H'
            if row["%_high_eco_valid"] > 49 and row["%_high_eco_valid"] < 75:
                return 'M'
            if row["%_high_eco_valid"] > 74:
                return 'L'
            return 'NA'

        df["%_high_eco_valid_padlock_scale"] = df.apply(lambda row: eco_valid_risk(row), axis=1) """

        df["%_high_eco_valid"] = pd.to_numeric(df["%_high_eco_valid"], errors='coerce').fillna(0)

        df["%_high_eco_valid_padlock_scale"] = pd.cut(
            df["%_high_eco_valid"],
            bins=[-np.inf, 50, 75, np.inf],
            labels=['H', 'M', 'L'],
            right=False,
            include_lowest=True
        )


        ########################################
        # make % indep eval padlock scale
        ########################################

        # convert number of studies data to numeric
        """ df["%_indep_eval"] = pd.to_numeric(df["%_indep_eval"], errors='coerce').fillna(0)

        def perc_indep_eval_risk(row):
            if row["%_indep_eval"] < 10:
                return 'H'
            if row["%_indep_eval"] > 9 and row["%_indep_eval"] < 30:
                return 'M'
            if row["%_indep_eval"] > 29:
                return 'L'
            return 'NA'

        df["%_indep_eval_padlock_scale"] = df.apply(lambda row: perc_indep_eval_risk(row), axis=1) """

        df["%_indep_eval"] = pd.to_numeric(df["%_indep_eval"], errors='coerce').fillna(0)

        df["%_indep_eval_padlock_scale"] = pd.cut(
            df["%_indep_eval"],
            bins=[-np.inf, 10, 30, np.inf],
            labels=['H', 'M', 'L'],
            right=False,
            include_lowest=True
        )


        ####################################################
        # reduce padlock if any key ratings are High risk
        ####################################################

        """ df["number_of_studies_padlock_scale"] = pd.to_numeric(df["number_of_studies_padlock_scale"], errors='coerce').fillna(0)
        df["New_padlock"] = df["number_of_studies_padlock_scale"]

        def risk_impact(row):
            if row["%_randomised_padlock_scale"] == "H": 
                df["New_padlock"] = df["New_padlock"] - 1
            if row["%_high_eco_valid_padlock_scale"] == "H":
                df["New_padlock"] = df["New_padlock"] - 1
            if row["%_indep_eval_padlock_scale"] == "H":
                df["New_padlock"] = df["New_padlock"] - 1
            if row["%_since_2000_padlock_scale"] == "H":
                df["New_padlock"] = df["New_padlock"] - 1
            if row["%_median_attrit_reported_padlock_scale"] == "H":
                df["New_padlock"] = df["New_padlock"] - 1
            return df["New_padlock"]

        df["New_padlock"] = df.apply(lambda row: risk_impact(row), axis=1) """

        df["number_of_studies_padlock_scale"] = pd.to_numeric(df["number_of_studies_padlock_scale"], errors='coerce').fillna(0)
        df["New_padlock"] = df["number_of_studies_padlock_scale"]

        conditions = [
            (df["%_randomised_padlock_scale"] == "H"),
            (df["%_high_eco_valid_padlock_scale"] == "H"),
            (df["%_indep_eval_padlock_scale"] == "H"),
            (df["%_since_2000_padlock_scale"] == "H"),
            (df["%_median_attrit_reported_padlock_scale"] == "H")
        ]
        choices = [-1, -1, -1, -1, -1]

        df["New_padlock"] = df["New_padlock"] + np.select(conditions, choices, default=0)


        df = df[[
            "strand",
            "number_of_studies",
            "number_of_studies_padlock_scale",
            "%_since_2000",
            "%_since_2000_padlock_scale",
            "%_randomised",
            "%_randomised_padlock_scale",
            "%_high_eco_valid",
            "%_high_eco_valid_padlock_scale",
            "%_indep_eval",
            "%_indep_eval_padlock_scale",
            "%_median_attrit_reported",
            "%_median_attrit_reported_padlock_scale",
            "New_padlock"
        ]]

        #################################################################
        # make more than 10 studies checker (has received meta-analysis)
        #################################################################

        number_of_studies_check = len(self.risk_of_bias_df)

        if number_of_studies_check > 9 and df["New_padlock"][0] < 1:
            df["New_padlock"][0] = 1
            df["MA_floor"] = True
        else:
            df["MA_floor"] = False

        # write to disk
        outfile8 = self.data_extraction.save_dataframe(df, "_Padlocks.csv", standard_info=True)
        return outfile8

class CustomFrames:
    def __init__(self, data_extractor):
        self.data_extraction = data_extractor

        #eppiid_df = self.data_extraction.retrieve_metadata("ItemId", "id")

#/**********************************************/
#/   RETRIEVE INDIVIDUAL VARIABLE DATAFRAMES    /
#/**********************************************/

def group_desc_stats(attribute_text, column_prefix):
    group_data = json_extractor.get_outcome_lvl1(attribute_text)
    group_data_df = pd.DataFrame(group_data)
    # name each column (number depends on outcome number)
    group_data_df.columns = [
        column_prefix+'{}'.format(column+1) for column in group_data_df.columns
    ]
    group_data_df.fillna("NA", inplace=True)
    group_data_df = group_data_df.replace(r'^\s*$', "NA", regex=True)
    # get outcometypeId data (to check)
    outcometypeid = json_extractor.get_outcome_lvl1("OutcomeTypeId")
    outcometypeid_df = pd.DataFrame(outcometypeid)
    # name each column (number depends on outcome number)
    outcometypeid_df.columns = [
        "outcometype_df_"+'{}'.format(column+1) for column in outcometypeid_df.columns
    ]
    mask = pd.DataFrame(outcometypeid_df["outcometype_df_1"] == 0)
    mask.columns = ["mask"]
    mask = mask.iloc[:, 0]
    # replace all 0 instances (null data) with "NA"
    for col in group_data_df.columns:
        group_data_df.loc[mask, col] = "NA"
    return group_data_df


""" def gender_split():
    from src.attributeIDs import gender_split_output
    # Get gender split highlighted text
    gen_split_ht_df = json_extractor.process_ht(gender_split_output, "Gender_Split_HT")
    # Get gender split comments data
    gen_split_comments_df = json_extractor.process_info(gender_split_output, "Gender_Split_comments")
    # Concatenate all dataframes
    dataframes = [gen_split_ht_df, gen_split_comments_df]
    gen_split_df = pd.concat(dataframes, axis=1, sort=False)
    # Clean up data frame
    gen_split_df.replace('\r',' ', regex=True, inplace=True)
    gen_split_df.replace('\n',' ', regex=True, inplace=True)
    gen_split_df.fillna("NA", inplace=True)
    return gen_split_df """


def int_eval():

    # get intervention costs reported main data
    int_eval_df = json_extractor.process_data(int_eval_output, "out_eval_raw")

    int_eval_df["eef_eval_raw"] = int_eval_df["out_eval_raw"].map(
                set(["Is this an EEF evaluation?"]).issubset).astype(int)
    
    int_eval_df["eef_eval_raw"] = int_eval_df["eef_eval_raw"].replace(
                to_replace=[0, 1], value=["No", "Yes"])
    
    # get intervention costs reported highlighted text
    int_eval_ht_df = json_extractor.process_ht(int_eval_output, "out_eval_ht")

    # get intervention costs reported user comments
    int_eval_comments_df = json_extractor.process_info(int_eval_output, "out_eval_info")

    # Concatenate data frames
    dataframes = [int_eval_df, int_eval_ht_df, int_eval_comments_df]

    int_eval_df = pd.concat(dataframes, axis=1, sort=False)

    int_eval_df=int_eval_df[[
        "out_eval_raw", 
        "out_eval_ht", 
        "out_eval_info", 
        "eef_eval_raw"
    ]]

    json_extractor.clean_up(int_eval_df)

    int_eval_df.fillna("NA", inplace=True)
    return int_eval_df



""" def out_id():
    # Get outcome ID data
    outcome_ID = json_extractor.get_outcome_lvl1("OutcomeId")
    outcome_ID_df = pd.DataFrame(outcome_ID)
    # Name each column (number depends on outcome number)
    outcome_ID_df.columns = [
        "Outcome_ID_"+'{}'.format(column+1) for column in outcome_ID_df.columns]
    # Clean up data frame
    outcome_ID_df.fillna("NA", inplace=True)
    outcome_ID_df = outcome_ID_df.replace(r'^\s*$', "NA", regex=True)
    return outcome_ID_df """


""" def source():
    from src.attributeIDs import source_output
    from src.attributeIDs import source_EEF_Report_options
    # get source raw data
    source = json_extractor.get_data(source_output)
    source_df = pd.DataFrame(source)
    source_df = source_df.T
    source_df.columns = ["source_raw"]
    # get source EED options (nested) data
    eef_options = json_extractor.get_data(source_EEF_Report_options)
    eef_options_df = pd.DataFrame(eef_options)
    eef_options_df = eef_options_df.T
    eef_options_df.columns = ["source_eef_reports"]
    # concatenate data frames
    source_all_df = pd.concat([
        source_df,
        eef_options_df,
    ], axis=1, sort=False)
    # fill blanks with NA
    source_all_df.fillna("NA", inplace=True)
    return source_all_df """


""" def study_place():
    from src.attributeIDs import location_info
    # get study place info data
    study_place = json_extractor.get_data(location_info)
    study_place_df = pd.DataFrame(study_place)
    study_place_df = study_place_df.T
    study_place_df.columns = ["study_place_info"]
    # get study place ht data
    study_place_ht = json_extractor.highlighted_text(location_info)
    study_place_ht_df = pd.DataFrame(study_place_ht)
    study_place_ht_df = study_place_ht_df.T
    study_place_ht_df.columns = ["study_place_ht"]
    # concatenate data frames
    study_place_df = pd.concat([
        study_place_df,
        study_place_ht_df,
    ], axis=1, sort=False)
    # fill blanks with NA
    study_place_df.fillna("NA", inplace=True)
    return study_place_df """


def sample_main_check():
    sample_main_check = json_extractor.get_data(sample_output)
    sample_main_check_df = pd.DataFrame(sample_main_check)
    sample_main_check_df = sample_main_check_df.T
    sample_main_check_df.columns = ["main_check"]
    sample_main_check_df.fillna("NA", inplace=True)
    return sample_main_check_df


""" def toolkit_strand():
    from src.attributeIDs import toolkit_strand_codes
    # get toolkit strand data
    toolkitstrand = json_extractor.get_outcome_lvl2(toolkit_strand_codes)
    toolkitstrand_df = pd.DataFrame(toolkitstrand)
    # get toolkit strand comments
    toolkitstrand_Comments = json_extractor.comments(toolkit_strand_codes)
    toolkitstrand_Comments_df = pd.DataFrame(toolkitstrand_Comments)
    toolkitstrand_Comments_df = toolkitstrand_Comments_df.T
    toolkitstrand_Comments_df.columns = ["_info"]
    # fill blanks with NA
    toolkitstrand_df.fillna("NA", inplace=True)
    # name each column (number depends on outcome number)
    toolkitstrand_df.columns = [
        "out_strand_"+'{}'.format(column+1) for column in toolkitstrand_df.columns]
    return toolkitstrand_df """


""" def web_loc():
    from src.attributeIDs import study_loc
    from src.attributeIDs import study_loc_type
    # get location info highlighted text
    loc_HT = json_extractor.highlighted_text(study_loc)
    loc_HT_df = pd.DataFrame(loc_HT)
    loc_HT_df = loc_HT_df.T
    loc_HT_df.columns = ["loc_ht"]
    # get location type further info highlighted text
    loc_type_HT = json_extractor.highlighted_text(study_loc_type)
    loc_type_HT_df = pd.DataFrame(loc_type_HT)
    loc_type_HT_df = loc_type_HT_df.T
    loc_type_HT_df.columns = ["loc_type_ht"]
    # concatenate datafeames
    loc_info = pd.concat([
        loc_HT_df,
        loc_type_HT_df,
    ], axis=1, sort=False)
    return loc_info """

#/*************************/
#/   COMMAND LINE TABLES   /
#/*************************/

def data_analysis_cl_table():
    """
    """
    console = Console()
    custom_style_df1 = Style(bgcolor=GREY)

    main_table = Table(show_header=True, 
                      style=custom_style_df1,
                      title=None,
                      safe_box=False,
                      box=box.SIMPLE)

    main_table.add_column("", style="bold white")
    main_table.add_column("[bold #fc5424]Main Toolkit[/bold #fc5424]", header_style="bold", style=WHITE)

    main_table.add_row("1",  "Arts Participation")
    main_table.add_row("2",  "Behaviour Interventions")
    main_table.add_row("3",  "Collaborative Learning")
    main_table.add_row("4",  "Extending School Time")
    main_table.add_row("5",  "Feedback")
    main_table.add_row("6",  "Homework")
    main_table.add_row("7",  "Individualised Instruction")
    main_table.add_row("8",  "Mentoring")
    main_table.add_row("9",  "Mastery Learning")
    main_table.add_row("10",  "Metacognition & Self Regulation")
    main_table.add_row("11",  "One to One Tution")
    main_table.add_row("12",  "Oral Language")
    main_table.add_row("13",  "Physical Activity")
    main_table.add_row("14",  "Parentel Engagement")
    main_table.add_row("15",  "Phonics")
    main_table.add_row("16",  "Performance Pay")
    main_table.add_row("17",  "Peer Tutoring")
    main_table.add_row("18",  "Reading Comprehension")
    main_table.add_row("19",  "Reducing Class Size")
    main_table.add_row("20",  "Repeating a Year")
    main_table.add_row("21",  "Social & Emotional Learning")
    main_table.add_row("22",  "Setting/Streaming")
    main_table.add_row("23",  "Small Group Tuition")
    main_table.add_row("24",  "Summer Schools")
    main_table.add_row("25",  "Teaching Assistants")
    main_table.add_row("26",  "Within-Class Grouping")

    main_table.add_row("",    "")
    main_table.add_row("",    "[bold #fc5424]Early Years Toolkit[/bold #fc5424]")
    main_table.add_row("",    "")
    main_table.add_row("27",  "Early Literacy Approaches")
    main_table.add_row("28",  "Early Numeracy Approaches")
    main_table.add_row("29",  "Earlier Starting Age")
    main_table.add_row("30",  "Extra Hours")
    main_table.add_row("31",  "Play-Based Learning")


    # Create a new Panel object
    panel = Panel(main_table, 
                  title="Strand Specific Selection", 
                  style=custom_style_df1,
                  border_style="bold white",
                  title_align="left",
                  padding=(1, 2),
                  width=80)

    console = Console()
    print("\n")
    console.print(panel)
    print("\n")

     # Get user selection for strand specific dataframe (if needed)
    ss_user_input = int(input("Select strand specific option: "))
    return ss_user_input


def display_table_struct(funcs): 
    """
    """
    for num, func in track(enumerate(funcs), description="[green]Processing dataframes..\n[/green]"):
        func(save_file=True, clean_cols=True, verbose=False)



def data_cleaning_col_breakdown():

    table_title_style = Style(italic=False, bgcolor=GREY, color=WHITE, bold=True)
    header_style = Style(italic=False, bgcolor=GREY, color=WHITE, bold=True)
    column_style = Style(bgcolor=GREY, color=WHITE) 

    main_table2 = Table(show_header=True, 
                        box=box.MINIMAL,
                        highlight=False,
                        title_style=table_title_style,
                        title=None,                   
    )
    main_table2.add_column("Dataframe 1", header_style=header_style, style=column_style)
    main_table2.add_column("Dataframe 2", header_style=header_style, style=column_style)
    main_table2.add_column("Dataframe 3", header_style=header_style, style=column_style)
    main_table2.add_column("Dataframe 4", header_style=header_style, style=column_style)
    main_table2.add_column("Dataframe 5", header_style=header_style, style=column_style)
    main_table2.add_row("Study ID",  "Study ID",  "Study ID",  "Study ID",  "Study ID")
    main_table2.add_row("Author",  "Author",  "Author",  "Author",  "Author")
    main_table2.add_row("Year",  "Year",  "Year",  "Year",  "Year")
    main_table2.add_row("Abstract",  "Strand",  "Strand",  "Strand",  "Strand")
    main_table2.add_row("Admin Strand",  "Int Name",  "Gender",  "Desc Stats Prim Out",  "Outcome Type")
    main_table2.add_row("Publication Type EPPI",  "Int Description",  "Sample Size",  "Int Treat Grp Number",  "Standard Mean Difference")
    main_table2.add_row("Publication Type",  "Int Objective",  "SES/FSM",  "Int Treat Grp Pre-test Mean/SD",  "Standard Error")
    main_table2.add_row("Educational Setting", "Int Organisation Type",  "Int Treat Sample Size",  "Int Treat Grp Post-test Mean/SD",  "Confidence Interval (lb)")
    main_table2.add_row("Ecological Validity", "Int Training",  "Int Cont Sample Size",  "Int Treat Grp Gain Score Mean/SD",  "Confidence Interval (ub)")
    main_table2.add_row("Student Age",  "Int Focus",  "Int Treat Grp2 Sample Size",  "Int Treat Grp Any Other Info",  "Outcome")
    main_table2.add_row("Number of Schools",  "Int Teaching Approach",  "Int Treat Grp3 Sample Size",  "Int Cont Grp Number",  "Sample")
    main_table2.add_row("Number of Classes",  "Int Inclusion",  "Int Treat Sample Size Analyzed",  "Int Cont Grp Pre-test Mean/SD",  "Outcome Comparison")
    main_table2.add_row("Treatment Group",  "Int Time",  "Int Cont Sample Size Analyzed",  "Int Cont Grp Post-test Mean/SD",  "Effect Size Type")
    main_table2.add_row("Participant Assignment",  "Int Delivery",  "Int Treat Grp2 Sample Size Analyzed",  "Int Cont Grp Gain Score Mean/SD",  "Outcome Measure")
    main_table2.add_row("Level of Assignment", "Int Duration",  "Int Cont Grp2 Sample Size Analyzed",  "Int Cont Grp Any Other Info",  "Outcome Title")
    main_table2.add_row("Study Design", "Int Frequency",  "Attrition Reported",  "Int Treat Grp2 Number",  "Group1 N")
    main_table2.add_row( "Randomisation",  "Int Session Length",  "Attrition Treat Grp",  "Int Treat Grp2 Pre-test Mean/SD",  "Group2 N")
    main_table2.add_row("Other Outcomes",  "Int Detail",  "Attrition Total (%)",  "Int Treat Grp2 Post-test Mean/SD",  "Group1 Mean")
    main_table2.add_row("Additional Outcomes",  "Int Costs", "", "Int Treat Grp2 Gain Score Mean/SD", "Group2 Mean")
    main_table2.add_row("Other Participants Outcomes", "Int Evaluation",  "",   "Int Treat Grp2 Any Other Info", "Group1 SD")
    main_table2.add_row("",  "Baseline Differences", "",  "Int Cont Grp2 Number",  "Group2 SD")
    main_table2.add_row("", "Computational Analysis",  "", "Int Cont Grp2 Pre-test Mean/SD",  "Outcome Description")
    main_table2.add_row("",  "Comparability Variables Reported",  "", "Int Cont Grp2 Post-test Mean/SD",  "Test Type Outcome")
    main_table2.add_row("",  "Clustering",  "", "Int Cont Grp2 Gain Score Mean/SD", "")
    main_table2.add_row("",  "", "",  "Int Cont Grp2 Any Other Info", "")
    main_table2.add_row("",  "", "",  "Follow-up Information", "")
    main_table2.footer = "This is the footer."
    return main_table2


def display_main_menu():
    table_title_style = Style(italic=False, bgcolor=None, color="#fc5424", bold=True)
    header_style = Style(italic=False, bgcolor="#fc5424", color=WHITE, bold=True)
    column_style = Style(bgcolor=GREY, color=WHITE, bold=False) 

    main_table = Table(show_header=True,
                       highlight=False,
                       title=None,
                       title_style=table_title_style,
                       box=box.SIMPLE)

    selection_style = Style(italic=False, bgcolor=GREY, color="#fc5424", bold=True)
    description_style = Style(italic=False, bgcolor=GREY, color="#fc5424", bold=True)

    main_table.add_column("Selection", header_style=selection_style, style=column_style)
    main_table.add_column("Description", header_style=description_style, style=column_style)

    main_table.add_row(" 1. Dataframe 1",      "Study, Research & Design Variables")
    main_table.add_row(" 2. Dataframe 2",      "Intervention Details")
    main_table.add_row(" 3. Sample Size",      "Sample size variables")
    main_table.add_row(" 4. Effect Size A",    "Descriptive Statistics")
    main_table.add_row(" 5. Effect Size B",    "Outcome Details")
    main_table.add_row(" 6. Data Analysis",    "Key variables for data analysis")
    main_table.add_row(" 7. Outcome Data",     "Raw outcome data")
    main_table.add_row(" 8. Study Security",     "Study Security calculations")
    main_table.add_row(" 9. Padlocks",       "Strand level padlock data")
    main_table.add_row("10. References",     "Data for constructing study references")
    main_table.add_row("11. Column Selection", "Custom column selection")
    main_table.add_row("12. Study Selection", "Custom ID selection")

    main_table.add_row("", "")

    main_table.add_row(" 0. EXIT", "")
    return main_table


def dataframe_1_output_display(functions, outfile):
    console = Console()
    custom_style_df1 = Style(bgcolor=GREY)

    df1_table = Table(show_header=True, 
                      style=custom_style_df1,
                      title=None,
                      safe_box=False,
                      box=box.SIMPLE)

    df1_table.add_column("Selection", justify="center", header_style="#fc5424")
    df1_table.add_column("Output directory", justify="left", header_style="#fc5424")
    df1_table.add_row("Dataframe 1", outfile, style=WHITE)

    return df1_table


def dataframe_2_output_display(functions, outfile):
    console = Console()
    custom_style_df1 = Style(bgcolor=GREY)

    df2_table = Table(show_header=True, 
                      style=custom_style_df1,
                      title=None,
                      safe_box=False,
                      box=box.SIMPLE)

    df2_table.add_column("Selection", justify="center", header_style="#fc5424")
    df2_table.add_column("Output directory", justify="left", header_style=WHITE)
    df2_table.add_row("Dataframe 2", outfile, style=WHITE)

    return df2_table


def dataframe_3_output_display(functions, outfile):
    console = Console()
    custom_style_df1 = Style(bgcolor=GREY)

    df3_table = Table(show_header=True, 
                      style=custom_style_df1,
                      title=None,
                      safe_box=False,
                      box=box.SIMPLE)

    df3_table.add_column("Selection", justify="center", header_style="#fc5424")
    df3_table.add_column("Output directory", justify="left", header_style=WHITE)
    df3_table.add_row("Sample Size", outfile, style=WHITE)

    return df3_table


def dataframe_4_output_display(functions, outfile):
    console = Console()
    custom_style_df1 = Style(bgcolor=GREY)

    df4_table = Table(show_header=True, 
                      style=custom_style_df1,
                      title=None,
                      safe_box=False,
                      box=box.SIMPLE)

    df4_table.add_column("Selection", justify="center", header_style="#fc5424")
    df4_table.add_column("Output directory", justify="left", header_style=WHITE)
    df4_table.add_row("Effect Size A", outfile, style=WHITE)

    return df4_table


def dataframe_5_output_display(functions, outfile):
    console = Console()
    custom_style_df1 = Style(bgcolor=GREY)

    df5_table = Table(show_header=True, 
                      style=custom_style_df1,
                      title=None,
                      safe_box=False,
                      box=box.SIMPLE)

    df5_table.add_column("Selection", justify="center", header_style="#fc5424")
    df5_table.add_column("Output directory", justify="left", header_style=WHITE)
    df5_table.add_row("Effect Size B", outfile, style=WHITE)

    return df5_table


def dataframe_6_output_display(functions, outfile):
    console = Console()
    custom_style_df1 = Style(bgcolor=GREY)

    df6_table = Table(show_header=True, 
                      style=custom_style_df1,
                      title=None,
                      safe_box=False,
                      box=box.SIMPLE)

    df6_table.add_column("Selection", justify="center", header_style="#fc5424")
    df6_table.add_column("Output directory", justify="left", header_style="#fc5424")
    df6_table.add_row("Main Analysis", outfile, style=WHITE)

    return df6_table


def dataframe_7_output_display(functions, outfile):
    console = Console()
    custom_style_df1 = Style(bgcolor=GREY)

    df7_table = Table(show_header=True, 
                      style=custom_style_df1,
                      title=None,
                      safe_box=False,
                      box=box.SIMPLE)

    df7_table.add_column("Selection", justify="center", header_style="#fc5424")
    df7_table.add_column("Output directory", justify="left", header_style="#fc5424")
    df7_table.add_row("Outcome Data", outfile, style=WHITE)

    return df7_table

def dataframe_8_output_display(functions, outfile):
    console = Console()
    custom_style_df1 = Style(bgcolor=GREY)

    df8_table = Table(show_header=True, 
                      style=custom_style_df1,
                      title=None,
                      safe_box=False,
                      box=box.SIMPLE)

    df8_table.add_column("Selection", justify="center", header_style="#fc5424")
    df8_table.add_column("Output directory", justify="left", header_style="#fc5424")
    df8_table.add_row("Study Security", outfile, style=WHITE)

    return df8_table

def dataframe_9_output_display(functions, outfile):
    console = Console()
    custom_style_df1 = Style(bgcolor=GREY)

    df9_table = Table(show_header=True, 
                      style=custom_style_df1,
                      title=None,
                      safe_box=False,
                      box=box.SIMPLE)

    df9_table.add_column("Selection", justify="center", header_style="#fc5424")
    df9_table.add_column("Output directory", justify="left", header_style="#fc5424")
    df9_table.add_row("Padlocks", outfile, style=WHITE)

    return df9_table

def dataframe_10_output_display(functions, outfile):
    console = Console()
    custom_style_df1 = Style(bgcolor=GREY)

    df10_table = Table(show_header=True, 
                      style=custom_style_df1,
                      title=None,
                      safe_box=False,
                      box=box.SIMPLE)

    df10_table.add_column("Selection", justify="center", header_style="#fc5424")
    df10_table.add_column("Output directory", justify="left", header_style="#fc5424")
    df10_table.add_row("References", outfile, style=WHITE)

    return df10_table

def dataframe_11_output_display(functions, outfile):
    console = Console()
    custom_style_df1 = Style(bgcolor=GREY)

    df11_table = Table(show_header=True, 
                      style=custom_style_df1,
                      title=None,
                      safe_box=False,
                      box=box.SIMPLE)

    df11_table.add_column("Selection", justify="center", header_style="#fc5424")
    df11_table.add_column("Output directory", justify="left", header_style="#fc5424")
    df11_table.add_row("Custom", outfile, style=WHITE)

    return df11_table

def create_output_display_table(dataframe_name, outfile):
    console = Console()
    custom_style_df1 = Style(bgcolor=GREY)

    df_table = Table(show_header=True,
                     style=custom_style_df1,
                     title=None,
                     safe_box=False,
                     box=box.SIMPLE)

    df_table.add_column("Selection", justify="center", header_style="#fc5424")
    df_table.add_column("Output directory", justify="left", header_style="#fc5424")
    df_table.add_row(dataframe_name, outfile, style=WHITE)

    return df_table


def input_file_info_display(data_file):

    table_title_style = Style(italic=False, bgcolor=GREY, color=WHITE, bold=True)
    header_style = Style(italic=False, bgcolor=GREY, color="#fc5424", bold=True)
    column_style = Style(bgcolor=GREY, color=WHITE) 

    file_info_table = Table(show_header=True,
                       highlight=False,
                       title=None,
                       title_style=table_title_style,
                       box=box.SIMPLE)
    
    file_info_table.add_column("Your input file", header_style=header_style, style=column_style)
    file_info_table.add_row(data_file)
    return file_info_table

def main_menu_display():
    console = Console()
    #data_cleaning_var_table = data_cleaning_col_breakdown()
    main_menu_table = display_main_menu()
    datafile_info_table = input_file_info_display(data_file)

    custom_style_main = Style(bgcolor=GREY)
    custom_style_file_details = Style(bgcolor=GREY)
    custom_style_cleaning_info = Style(bgcolor=GREY)

    container_title = console.render_str("[bold white]EEF Data Extractor[/bold white]")

    top_title = console.render_str("[bold white]Welcome[/bold white]")
    title1 = console.render_str("[bold white]Main Menu[/bold white]")
    title2 = console.render_str("[bold white]Data File Details[/bold white]")

    # Set text for top panel of main menu
    top_panel_text = (
        "[#FFFFFF]Welcome to the EEF Data Extractor. Use the[/#FFFFFF] "
        "[bold #fc5424]Main Menu[/bold #fc5424] [#FFFFFF]to generate various dataframes containing data extracted "
        "from an input [bold #fc5424]JSON[/bold #fc5424] [#FFFFFF]datafile produced by the EEF Education Evidence "
        "Database.\n\n[bold #fc5424]Options 1-5[/bold #fc5424] [#FFFFFF]include our own custom dataframes "
        "for data cleaning prior to analysis.[/#FFFFFF] [bold #fc5424]Option 6[/bold #fc5424] [#FFFFFF]generates the "
        "final dataframe(s) used in our meta-analyses. [bold #fc5424]Option 7[/bold #fc5424] produces raw (unordered) "
        "outcome data. [bold #fc5424]Option 8[/bold #fc5424] produces a bespoke study security dataframe. "
        "[/#FFFFFF][bold #fc5424]Option 9[/bold #fc5424] produces a strand-level 'padlocks' dataframe. [bold #fc5424]Option 10[/bold #fc5424] [#FFFFFF]compiles "
        "the necessary data for constructing study references. Finally, [/#FFFFFF][bold #fc5424]Option 11[/bold #fc5424] "
        "[#FFFFFF]allows you to create your own custom column dataframe,[/#FFFFFF] and [bold #fc5424]option 12[/bold #fc5424] allows you to create your own "
        "individual study dataframe."
    )
    top_menu_style = Style(bgcolor=GREY)

    # create the panel with the text
    top_panel = Panel(
        top_panel_text,
        title=top_title, 
        border_style="bold white",
        title_align="left",
        style=top_menu_style,
        padding=(1, 2),
        width=120,
    )

    panel1 = Panel.fit(
        main_menu_table,
        title=title1,
        border_style="bold white",
        style=custom_style_main,
        title_align="left",
        padding=(1, 2),
        width=120,
    )

    panel2 = Panel.fit(
        datafile_info_table,
        title=title2,
        border_style="bold white",
        style=custom_style_file_details,
        title_align="left",
        padding=(1, 2),
        width=120,
    )

    # combine the text panel and panels into a new column
    column_combined = Columns([top_panel, panel1, panel2], equal=False)

    # create the layout with the combined column
    layout = Layout(column_combined)

    panel = Panel(
        layout,
        title=container_title,
        border_style="bold white",
        padding=(1, 2),
        title_align="center",
        style=custom_style_main,
        height=47,
        width=120,
    )

    console.clear()
    console.print(panel)
    print("\n")


def main_menu_display1(functions, outfile1, df_display):

    console = Console()
    output_file_info = df_display(functions, outfile1)
    main_menu_table = display_main_menu()
    datafile_info_table = input_file_info_display(data_file)

    custom_style_main = Style(bgcolor=GREY)
    custom_style_file_details = Style(bgcolor=GREY)
    custom_style_cleaning_info = Style(bgcolor=GREY)

    title1 = console.render_str("[bold white]Main Menu[/bold white]")
    title2 = console.render_str("[bold white]Data File Details[/bold white]")
    title3 = console.render_str("[bold white]Output Files[/bold white]")

    panel1a = Panel.fit(
        main_menu_table,
        title=title1,
        border_style="bold white",
        style=custom_style_main,
        title_align="left",
        padding=(1, 2),
    )
    panel1b = Panel.fit(
        datafile_info_table,
        title=title2,
        border_style="bold white",
        style=custom_style_file_details,
        title_align="left",
        padding=(1, 2),
    )

    panel2 = Panel.fit(
        output_file_info,
        title=title3,
        border_style="bold white",
        style=custom_style_cleaning_info,
        title_align="left",
        padding=(1, 2),
    )
    # create the first row of columns
    row1 = Columns([panel1a], equal=False)

    row1b = Columns([panel1b], equal=False)

    # create the second row of columns
    row2 = Columns([panel2], equal=False)

    # create the layout with the panels
    layout = Columns([row1, row1b, row2], equal=False)

    panel = Panel(
        layout, 
        title="EEF Teaching and Learning Toolkit Data Extractor", 
        border_style="bold white", 
        padding=(1, 2), 
        title_align="left",
        style=custom_style_main,
        width=120,
        height=44)

    console.clear()
    console.print(panel)
    print("\n")

path_completer = PathCompleter()


while True:
    data_file = prompt('Select your data file: ', completer=path_completer)
    if os.path.isfile(data_file) and data_file.endswith('.json'):
        break
    else:
        print('Invalid file. Please enter a valid .json file.')



json_extractor = JSONDataExtractor(data_file)