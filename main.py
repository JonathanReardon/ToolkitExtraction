#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Jonathan Reardon"

import pandas as pd

from rich import print
from rich.prompt import Prompt
from rich.console import Console
from rich.columns import Columns
from rich.style import Style
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.pretty import Pretty

from src.attributeIDs import *
from src.funcs import (
    CustomFrames,
    DataFrameCompilation,
    JSONDataExtractor,
    RiskofBias,
    StrandSpecificFrames,
    data_analysis_cl_table,
    data_file,
    dataframe_1_output_display,
    dataframe_2_output_display,
    dataframe_3_output_display,
    dataframe_4_output_display,
    dataframe_5_output_display,
    dataframe_6_output_display,
    dataframe_7_output_display,
    dataframe_8_output_display,
    dataframe_9_output_display,
    dataframe_10_output_display,
    input_file_info_display,
    main_menu_display,
    main_menu_display1,
)

# table1 
row_styles1 = ["#FFFFFF"] * 36
row_data_list1 = [
    "Study ID", 
    "Author", 
    "Year", 
    "Abstract", 
    "Admin Strand",
    "Country", 
    "Publication Type EPPI", 
    "Publication Type",
    "Educational Setting", 
    "Student Age",
    "Strand",
    "Ecological Validity",
    "Number of Schools Int (info)",
    "Number of Schools Int (ht)",
    "Number of Schools Ctrl (info)",
    "Number of Schools Ctrl (ht)",
    "Number of Schools Total (info)",
    "Number of Schools Total (ht)",
    "Number of Classes Int (info)",
    "Number of Classes Int (ht)",
    "Number of Classes Ctrl (info)",
    "Number of Classes Ctrl (ht)",
    "Number of Classes Total (info)",
    "Number of Classes Total (ht)",
    "Participant Assignment (raw)",
    "Participant Assignment (ht)",
    "Participant Assignment (info)",
    "Level of Assignment (raw)",
    "Level of Assignment (ht)",
    "Level of Assignment (info)",
    "Study Design (raw)",
    "Study Design (ht)",
    "Study Design (info)",
    "Randomisation (raw)",
    "Randomisation (ht)",
    "Randomisation (info)",
]

highlight_style = "#fc5424"

def custom_general_vars1():
    """
    Displays a Rich list of 'general' variables for the custom data frame builder
    - Study ID
    - Author
    - Year 
    - Astract
    - Admin Strand
    - Country
    - Publication Type EPPI
    - Publication Type
    - Educational Setting
    - Student Age
    """

    console = Console()
    custom_style_main = Style(bgcolor="#37474f")

    table_title_style = Style(italic=False, bgcolor="#37474f", color="#fc5424", bold=True)
    header_style = Style(italic=False, bgcolor="#37474f", color="#fc5424", bold=True)
    column_style = Style(bgcolor="#37474f", color="#fc5424", bold=True) 

    main_table2 = Table(show_header=True, 
                        box=box.SIMPLE,
                        highlight=False,
                        title_style=table_title_style,               
    )

    main_table2.add_column("", header_style=header_style, style=column_style, width=2)
    main_table2.add_column("General Variables", header_style=header_style, style=column_style, width=30)

    for idx, row_data in enumerate(row_data_list1, start=1):
        main_table2.add_row(f"{idx+0}", row_data, style=row_styles1[idx - 1])
    
    return main_table2

# table1 
row_styles2 = ["#FFFFFF"] * 16
row_data_list2 = [
    "Outcome Title", 
    "Outcome Description", 
    "Outcome Type", 
    "SMD", 
    "SE",
    "CI (lower)",
    "CI (upper)",
    "Outcome Measure", 
    "Outcome Group1 N", 
    "Outcome Group1 Mean",
    "Outcome Group1 SD", 
    "Outcome Group2 N",
    "Outcome Group2 Mean",
    "Outcome Group2 SD",
    "Outcome Test Type",
    "Outcome Effect Size Type",
]

def custom_outcome_vars_1():
    """
    Displays a Rich list of [toolkit]'outcome' variables for the custom data frame builder
    - Outcome Title
    - Outcome Description
    - Outcome Type
    - SMD
    - SE
    - Outcome Measure
    - Outcome Group1 N
    - Outcome Group1 Mean
    - Outcome Group1 SD
    - Outcome Group2 N
    """
    console = Console()
    custom_style_main = Style(bgcolor="#37474f")

    table_title_style = Style(italic=False, bgcolor="#37474f", color="#fc5424", bold=True)
    header_style = Style(italic=False, bgcolor="#37474f", color="#fc5424", bold=True)
    column_style = Style(bgcolor="#37474f", color="#fc5424", bold=True) 

    main_table3 = Table(show_header=True, 
                        box=box.SIMPLE,
                        highlight=False,
                        title_style=table_title_style,                  
    )

    main_table3.add_column("", header_style=header_style, style=column_style, width=3)
    main_table3.add_column("Toolkit Primary Outcome", header_style=header_style, style=column_style, width=30)

    for idx, row_data in enumerate(row_data_list2, start=1):
        main_table3.add_row(f"{idx+36}", row_data, style=row_styles2[idx - 1])
    
    return main_table3


def get_user_input():
    while True:
        try:
            data_cleaning_option = Prompt.ask("Enter an option from the Main Menu")
            data_cleaning_option=int(data_cleaning_option)
            if data_cleaning_option < 0 or data_cleaning_option > 90:
                raise ValueError
            break
        except ValueError:
            console=Console()
            console.print("Error: invalid input. Please enter a number from 0 to 8.")
    return data_cleaning_option


def main():
    """
    
    """
    # Create instance of json extractor class
    json_extractor = JSONDataExtractor(data_file)

    # Create instance of dataframe compilation class
    data_frame_compilation = DataFrameCompilation(json_extractor)

    # Display main menu
    main_menu_display()

    # Crate input file display table
    input_file_info_display(data_file)

    data_cleaning_option = get_user_input()
    run_program = True
    while run_program:
        
        match data_cleaning_option:
            case 0: 
                console = Console()
                console.print("Thanks for using the EEF Toolkit Data Extractor.")
                run_program = False
            case 1:
                _, outfile1 = data_frame_compilation.make_dataframe_1(save_file=True, clean_cols=True, verbose=False)
                functions = [data_frame_compilation.make_dataframe_1]
        
                # Display main menu
                main_menu_display1(functions, outfile1, dataframe_1_output_display)

                # Crate input file display table
                input_file_info_display(data_file)

                data_cleaning_option = get_user_input()
            case 2: 
                _, outfile2 = data_frame_compilation.make_dataframe_2(save_file=True, clean_cols=True, verbose=False)
                functions = [data_frame_compilation.make_dataframe_2]

                # Display main menu
                main_menu_display1(functions, outfile2, dataframe_2_output_display)

                # Crate input file display table
                input_file_info_display(data_file)

                data_cleaning_option = get_user_input()
            case 3:
                _, outfile3 = data_frame_compilation.make_dataframe_3(save_file=True, clean_cols=True, verbose=False)
                functions = [data_frame_compilation.make_dataframe_3]

                # Display main menu
                main_menu_display1(functions, outfile3, dataframe_3_output_display)

                # Crate input file display table
                input_file_info_display(data_file)

                data_cleaning_option = get_user_input()
            case 4:
                _, outfile4 = data_frame_compilation.make_dataframe_4(save_file=True, clean_cols=True, verbose=False)
                functions = [data_frame_compilation.make_dataframe_4]
                
                # Display main menu
                main_menu_display1(functions, outfile4, dataframe_4_output_display)

                # Crate input file display table
                input_file_info_display(data_file)

                data_cleaning_option = get_user_input()
            case 5:
                _, outfile5 = data_frame_compilation.make_dataframe_5(save_file=True, clean_cols=True, verbose=False)
                functions = [data_frame_compilation.make_dataframe_5]
                # Display main menu
                main_menu_display1(functions, outfile5, dataframe_5_output_display)

                # Crate input file display table
                input_file_info_display(data_file)

                # Display user option prompt
                data_cleaning_option = Prompt.ask("Enter an option from the Main Menu")
                data_cleaning_option=int(data_cleaning_option)
            case 6:
                console = Console()
                console.clear()
                strand_specific_option = data_analysis_cl_table()

                ss = StrandSpecificFrames(json_extractor)

                strand_specific_df = ss.strand_specific_df_selection(strand_specific_option)
                _, outfile6 = data_frame_compilation.make_dataframe_6(strand_specific_df, save_file=True)
                functions = data_frame_compilation.make_dataframe_6(strand_specific_df)
                # Display main menu
                main_menu_display1(functions, outfile6, dataframe_6_output_display)

                # Crate input file display table
                input_file_info_display(data_file)

                data_cleaning_option = get_user_input()
            case 7:
                outfile7 = data_frame_compilation.getOutcomeData(save_file=True)
                functions = [data_frame_compilation.getOutcomeData]

                # Display main menu
                main_menu_display1(functions, outfile7, dataframe_7_output_display)

                # Crate input file display table
                input_file_info_display(data_file)
                data_cleaning_option = get_user_input()

            case 8:
                # Create instance of risk of bias class
                rob = RiskofBias(json_extractor)
                # Combine and save data frame
                functions = rob.compile()
                outfile7=rob.save_dataframe()

                # Display main menu
                main_menu_display1(functions, outfile7, dataframe_8_output_display)

                # Crate input file display table
                input_file_info_display(data_file)

                data_cleaning_option = get_user_input()
            case 9:
                # Create instance of risk of bias class
                rob = RiskofBias(json_extractor)
                # Combine and save data frame
                functions = rob.compile()
                outfile8 = rob.padlocks()
                # Display main menu
                main_menu_display1(functions, outfile8, dataframe_9_output_display)

                # Crate input file display table
                input_file_info_display(data_file)

                data_cleaning_option = get_user_input()
            case 10:
                _, outfile9 = data_frame_compilation.make_references(save_file=True)
                functions = [data_frame_compilation.make_references]

                # Display main menu
                main_menu_display1(functions, outfile9, dataframe_10_output_display)

                # Crate input file display table
                input_file_info_display(data_file)

                data_cleaning_option = get_user_input()
            case 11:
                console = Console()
                console.clear()

                # Display list of 'general vars e.g. id, author, year etc.
                main_table2 = custom_general_vars1()
                # Display list of outcome vars e.g. title, description, type etc.
                main_table3 = custom_outcome_vars_1()

                custom_style_main = Style(bgcolor="#37474f")
                custom_style_outer = Style(bgcolor="#37474f")

                panel1 = Panel(main_table2, style=custom_style_main, border_style="#37474f")
                panel2 = Panel(main_table3, style=custom_style_main, border_style="#37474f")

                # Combine the panels horizontally
                columns = Columns([panel1, panel2])

                # Create a larger panel with white background and black text to house the columns
                panel = Panel(columns, 
                                title="Custom Data Selection", 
                                style=custom_style_outer, 
                                border_style="#FFFFFF",
                                width=94)

                # Print the panel
                console.print(panel)
                
                df = CustomFrames(json_extractor)

                used_options = []

                # Compile list of invidividual data frames
                dataframes=[]
                while True:
                    try:
                        console.print("\nAdd variables to your data frame or 0 to Save file and exit")
                        num = int(Prompt.ask("Selection"))
                        if num < 0 or num > 60:
                            raise ValueError
                    except ValueError:
                        print("Error: invalid input. Please enter a number from 0 to 51.\n")
                        continue

                    match num:
                        case 0:
                            run_program=False
                            break
                        case 1: 
                            if "id" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                eppiid_df = df.data_extraction.retrieve_metadata("ItemId", "id")
                                dataframes.append(eppiid_df)
                                used_options.append("id")
                            else:
                                print("You have already selected this option!")
                        case 2: 
                            if "pub_author" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                author_df = df.data_extraction.retrieve_metadata("ShortTitle", "pub_author")
                                dataframes.append(author_df)
                                used_options.append("pub_author")
                            else:
                                print("You have already selected this option!")
                        case 3: 
                            if "pub_year" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                year_df = df.data_extraction.retrieve_metadata("Year", "pub_year")
                                dataframes.append(year_df)
                                used_options.append("pub_year")
                            else:
                                print("You have already selected this option!")
                        case 4:
                            if "abstract" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                abstract_df = df.data_extraction.retrieve_metadata("Abstract", "abstract")
                                dataframes.append(abstract_df)
                                used_options.append("abstract")
                            else:
                                print("You have already selected this option!")
                        case 5: 
                            if "strand_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                admin_strand_df = df.data_extraction.retrieve_data(admin_strand_output, "strand_raw")
                                dataframes.append(admin_strand_df)
                                used_options.append("strand_raw")
                            else:
                                print("You have already selected this option!")
                        case 6:
                            if "loc_country_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                country_df = df.data_extraction.retrieve_data(countries, "loc_country_raw")
                                dataframes.append(country_df)
                                used_options.append("loc_country_raw")
                            else:
                                print("You have already selected this option!")
                        case 7: 
                            if "pub_eppi" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                pubtype_eppi_df = df.data_extraction.retrieve_metadata("TypeName", "pub_eppi")
                                dataframes.append(pubtype_eppi_df)
                                used_options.append("pub_eppi")
                            else:
                                print("You have already selected this option!")
                        case 8: 
                            if "pub_type_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                pub_type_data = df.data_extraction.retrieve_data(publication_type_output, "pub_type_raw")
                                dataframes.append(pub_type_data)
                                used_options.append("pub_type_raw")
                            else:
                                print("You have already selected this option!")
                        case 9: 
                            if "int_setting_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                edu_setting_data = df.data_extraction.retrieve_data(edu_setting_output, "int_setting_raw")
                                dataframes.append(edu_setting_data)
                                used_options.append("int_setting_raw")
                            else:
                                print("You have already selected this option!")
                        case 10: 
                            if "part_age_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                student_age_data = df.data_extraction.retrieve_data(student_age_output, "part_age_raw")
                                dataframes.append(student_age_data)
                                used_options.append("part_age_raw")
                            else:
                                print("You have already selected this option!")
                        case 11: 
                            if "strand_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                admin_strand_data = df.data_extraction.retrieve_data(admin_strand_output, "strand_raw")
                                dataframes.append(admin_strand_data)
                                used_options.append("strand_raw")
                            else:
                                print("You have already selected this option!")
                        case 12: 
                            if "eco_valid_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                eco_valid_raw = df.data_extraction.retrieve_data(study_realism_output, "eco_valid_raw")
                                dataframes.append(eco_valid_raw)
                                used_options.append("eco_valid_raw")
                            else:
                                print("You have already selected this option!")
                        #/*************************/#
                        #/     NUMBER OF SCHOOLS   /#
                        #/*************************/#
                        case 13: 
                            if "school_treat_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                number_of_school_int_info = df.data_extraction.retrieve_info(number_of_schools_intervention_output, "school_treat_info")
                                dataframes.append(number_of_school_int_info)
                                used_options.append("school_treat_info")
                            else:
                                print("You have already selected this option!")
                        case 14: 
                            if "school_treat_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                number_of_school_int_ht = df.data_extraction.retrieve_ht(number_of_schools_intervention_output, "school_treat_ht")
                                dataframes.append(number_of_school_int_ht)
                                used_options.append("school_treat_ht")
                            else:
                                print("You have already selected this option!")
                        case 15: 
                            if "school_cont_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                number_of_school_control_info = df.data_extraction.retrieve_info(number_of_schools_control_output, "school_cont_info")
                                dataframes.append(number_of_school_control_info)
                                used_options.append("school_cont_info")
                            else:
                                print("You have already selected this option!")
                        case 16: 
                            if "school_cont_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                number_of_school_control_ht = df.data_extraction.retrieve_ht(number_of_schools_control_output, "school_cont_ht")
                                dataframes.append(number_of_school_int_ht)
                                used_options.append("school_cont_ht")
                            else:
                                print("You have already selected this option!")
                        case 17: 
                            if "school_total_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                number_of_school_total_info = df.data_extraction.retrieve_info(number_of_schools_total_output, "school_total_info")
                                dataframes.append(number_of_school_total_info)
                                used_options.append("school_total_info")
                            else:
                                print("You have already selected this option!")
                        case 18: 
                            if "school_total_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                number_of_school_total_ht = df.data_extraction.retrieve_ht(number_of_schools_total_output, "school_total_ht")
                                dataframes.append(number_of_school_total_ht)
                                used_options.append("school_total_ht")
                            else:
                                print("You have already selected this option!")
                        #/*************************/#
                        #/    NUMBER OF CLASSES    /#
                        #/*************************/#
                        case 19: 
                            if "class_treat_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                number_of_classes_int_info = df.data_extraction.retrieve_info(num_of_class_int_output, "class_treat_info")
                                dataframes.append(number_of_classes_int_info)
                                used_options.append("class_treat_info")
                            else:
                                print("You have already selected this option!")
                        case 20: 
                            if "class_treat_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                number_of_classes_int_ht = df.data_extraction.retrieve_ht(num_of_class_int_output, "class_treat_ht")
                                dataframes.append(number_of_classes_int_ht)
                                used_options.append("class_treat_ht")
                            else:
                                print("You have already selected this option!")
                        case 21: 
                            if "class_cont_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                number_of_classes_control_info = df.data_extraction.retrieve_info(num_of_class_cont_output, "class_cont_info")
                                dataframes.append(number_of_classes_control_info)
                                used_options.append("class_cont_info")
                            else:
                                print("You have already selected this option!")
                        case 22: 
                            if "class_cont_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                number_of_classes_control_ht = df.data_extraction.retrieve_ht(num_of_class_cont_output, "class_cont_ht")
                                dataframes.append(number_of_classes_control_ht)
                                used_options.append("class_cont_ht")
                            else:
                                print("You have already selected this option!")
                        case 23: 
                            if "class_total_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                number_of_classes_total_info = df.data_extraction.retrieve_info(num_of_class_tot_output, "class_total_info")
                                dataframes.append(number_of_classes_total_info)
                                used_options.append("class_total_info")
                            else:
                                print("You have already selected this option!")
                        case 24: 
                            if "class_total_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                number_of_classes_total_ht = df.data_extraction.retrieve_ht(num_of_class_tot_output, "class_total_ht")
                                dataframes.append(number_of_classes_total_ht)
                                used_options.append("class_total_ht")
                            else:
                                print("You have already selected this option!")
                        #/****************************/#
                        #/   PARTICIPANT ASSIGNMENT   /#
                        #/****************************/#
                        case 25: 
                            if "part_assig_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                part_assig_data = df.data_extraction.retrieve_data(part_assign_output, "part_assig_raw")
                                dataframes.append(part_assig_data)
                                used_options.append("part_assig_raw")
                            else:
                                print("You have already selected this option!")
                        case 26: 
                            if "part_assig_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                part_assig_ht = df.data_extraction.retrieve_ht(part_assign_output, "part_assig_ht")
                                dataframes.append(part_assig_ht)
                                used_options.append("part_assig_ht")
                            else:
                                print("You have already selected this option!")
                        case 27: 
                            if "part_assig_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                part_assig_info = df.data_extraction.retrieve_info(part_assign_output, "part_assig_info")
                                dataframes.append(part_assig_ht)
                                used_options.append("part_assig_info")
                            else:
                                print("You have already selected this option!")
                        #/*************************/#
                        #/   LEVEL OF ASSIGNMENT   /#
                        #/*************************/#
                        case 28: 
                            if "level_assig_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                level_of_assign_data = df.data_extraction.retrieve_data(level_of_assignment_output, "level_assig_raw")
                                dataframes.append(level_of_assign_data)
                                used_options.append("level_assig_raw")
                            else:
                                print("You have already selected this option!")
                        case 29: 
                            if "level_assig_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                level_of_assign_ht = df.data_extraction.retrieve_ht(level_of_assignment_output, "level_assig_ht")
                                dataframes.append(level_of_assign_ht)
                                used_options.append("level_assig_ht")
                            else:
                                print("You have already selected this option!")
                        case 30: 
                            if "level_assig_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                level_of_assign_info = df.data_extraction.retrieve_info(level_of_assignment_output, "level_assig_info")
                                dataframes.append(level_of_assign_info)
                                used_options.append("level_assig_info")
                            else:
                                print("You have already selected this option!")
                        #/**********************/#
                        #/     STUDY DESIGN     /#
                        #/**********************/#
                        case 31: 
                            if "int_desig_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                study_design_data = df.data_extraction.retrieve_data(study_design_output, "int_desig_raw")
                                dataframes.append(study_design_data)
                                used_options.append("int_desig_raw")
                            else:
                                print("You have already selected this option!")
                        case 32: 
                            if "int_design_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                study_design_ht = df.data_extraction.retrieve_ht(study_design_output, "int_design_ht")
                                dataframes.append(study_design_ht)
                                used_options.append("int_design_ht")
                            else:
                                print("You have already selected this option!")
                        case 33: 
                            if "int_design_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                study_design_info = df.data_extraction.retrieve_info(study_design_output, "int_design_info")
                                dataframes.append(study_design_info)
                                used_options.append("int_design_info")
                            else:
                                print("You have already selected this option!")
                        #/**********************/#
                        #/     RANDOMISATION    /#
                        #/**********************/#
                        case 34: 
                            if "rand_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                rand_data = df.data_extraction.retrieve_data(randomisation_details, "rand_raw")
                                dataframes.append(rand_data)
                                used_options.append("rand_raw")
                            else:
                                print("You have already selected this option!")
                        case 35: 
                            if "rand_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                rand_ht = df.data_extraction.retrieve_ht(randomisation_details, "rand_ht")
                                dataframes.append(rand_ht)
                                used_options.append("rand_ht")
                            else:
                                print("You have already selected this option!")
                        case 36: 
                            if "rand_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                rand_info = df.data_extraction.retrieve_info(randomisation_details, "rand_info")
                                dataframes.append(rand_info)
                                used_options.append("rand_info")
                            else:
                                print("You have already selected this option!")



                        #/*************************/#
                        #/ TOOLKIT PRIMARY OUTCOME /#
                        #/*************************/#
                        case 37:
                                if "out_tit_tool" not in used_options:
                                    row_styles2[num - 37] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_out_tit_tool = df_out.out_tit_tool
                                    dataframes.append(df_out_tit_tool)
                                    used_options.append("out_tit_tool")
                                else:
                                    print("You have already selected this option!")
                        case 38:
                                if "out_desc_tool" not in used_options:
                                    row_styles2[num - 37] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_out_desc_tool = df_out.out_desc_tool
                                    dataframes.append(df_out_desc_tool)
                                    used_options.append("out_desc_tool")
                                else:
                                    print("You have already selected this option!")
                        case 39:
                                if "out_type_tool" not in used_options:
                                    row_styles2[num - 37] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_out_type_tool = df_out.out_type_tool
                                    dataframes.append(df_out_type_tool)
                                    used_options.append("out_type_tool")
                                else:
                                    print("You have already selected this option!")
                        case 40:
                                if "smd_tool" not in used_options:
                                    row_styles2[num - 37] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_smd_tool = df_out.smd_tool
                                    dataframes.append(df_smd_tool)
                                    used_options.append("smd_tool")
                                else:
                                    print("You have already selected this option!")
                        case 41:
                                if "se_tool" not in used_options:
                                    row_styles2[num - 37] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_se_tool = df_out.se_tool
                                    dataframes.append(df_se_tool)
                                    used_options.append("se_tool")
                                else:
                                    print("You have already selected this option!")
                        case 42:
                                if "ci_lower_tool" not in used_options:
                                    row_styles2[num - 37] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_ci_lower_tool = df_out.ci_lower_tool
                                    dataframes.append(df_ci_lower_tool)
                                    used_options.append("ci_lower_tool")
                                else:
                                    print("You have already selected this option!")
                        case 43:
                                if "ci_upper_tool" not in used_options:
                                    row_styles2[num - 37] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_ci_upper_tool = df_out.ci_upper_tool
                                    dataframes.append(df_ci_upper_tool)
                                    used_options.append("ci_upper_tool")
                                else:
                                    print("You have already selected this option!")
                        case 44:
                                if "out_measure_tool" not in used_options:
                                    row_styles2[num - 37] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_out_measure_tool = df_out.out_measure_tool
                                    dataframes.append(df_out_measure_tool)
                                    used_options.append("out_measure_tool")
                                else:
                                    print("You have already selected this option!")
                        case 45:
                                if "out_g1_n_tool" not in used_options:
                                    row_styles2[num - 37] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_g1_n_tool = df_out.out_g1_n_tool
                                    dataframes.append(df_g1_n_tool)
                                    used_options.append("out_g1_n_tool")
                                else:
                                    print("You have already selected this option!")
                        case 46:
                                if "out_g1_mean_tool" not in used_options:
                                    row_styles2[num - 37] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_g1_mean_tool = df_out.out_g1_mean_tool
                                    dataframes.append(df_g1_mean_tool)
                                    used_options.append("out_g1_mean_tool")
                                else:
                                    print("You have already selected this option!")
                        case 47:
                                if "out_g1_sd_tool" not in used_options:
                                    row_styles2[num - 37] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_g1_sd_tool = df_out.out_g1_sd_tool
                                    dataframes.append(df_g1_sd_tool)
                                    used_options.append("out_g1_sd_tool")
                                else:
                                    print("You have already selected this option!")
                        case 48:
                                if "out_g2_n_tool" not in used_options:
                                    row_styles2[num - 37] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_g2_n_tool = df_out.out_g2_n_tool
                                    dataframes.append(df_g2_n_tool)
                                    used_options.append("out_g2_n_tool")
                                else:
                                    print("You have already selected this option!")
                        case 49:
                                if "out_g2_mean_tool" not in used_options:
                                    row_styles2[num - 37] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_g2_mean_tool = df_out.out_g2_mean_tool
                                    dataframes.append(df_g2_mean_tool)
                                    used_options.append("out_g2_mean_tool")
                                else:
                                    print("You have already selected this option!")
                        case 50:
                                if "out_g2_sd_tool" not in used_options:
                                    row_styles2[num - 37] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_g2_sd_tool = df_out.out_g2_sd_tool
                                    dataframes.append(df_g2_sd_tool)
                                    used_options.append("out_g2_sd_tool")
                                else:
                                    print("You have already selected this option!")
                        case 51:
                                if "out_test_type_raw_" not in used_options:
                                    row_styles2[num - 37] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_out_test_type = df_out.out_test_type_raw_tool
                                    dataframes.append(df_out_test_type)
                                    used_options.append("out_test_type_raw_")
                                else:
                                    print("You have already selected this option!")
                        case 52:
                                if "out_es_type_tool" not in used_options:
                                    row_styles2[num - 37] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_out_es_type = df_out.out_es_type_tool
                                    dataframes.append(df_out_es_type)
                                    used_options.append("out_es_type_tool")
                                else:
                                    print("You have already selected this option!")









                        case _:
                            print("Error: invalid option selected")
                    
                    if dataframes:
                        all_df = pd.concat(dataframes, axis=1)
                        console = Console()
                        main_table2 = custom_general_vars1()
                        main_table3 = custom_outcome_vars_1()
                        console.clear()

                        panel1 = Panel(main_table2, style=custom_style_main, border_style="#37474f")
                        panel2 = Panel(main_table3, style=custom_style_main, border_style="#37474f")

                        # Combine the panels horizontally
                        columns = Columns([panel1, panel2])

                        # Create a larger panel with white background and black text to house the columns
                        panel = Panel(columns, 
                                      title="Custom Data Selection", 
                                      style=custom_style_outer, 
                                      border_style="#FFFFFF",
                                      width=92)

                        # Print the panel
                        console.print(panel)

                if dataframes:
                    all_df = pd.concat(dataframes, axis=1)
                    console.print("\n[bold]Custom data frame saved here..[/bold]\n")
                    outfile1 = df.data_extraction.save_dataframe(all_df, "_Custom.csv")
                    outfile1=str(outfile1)
                    outfile1=outfile1
                    console.print(outfile1 + "\n")
                    console.print("Thanks for using the EEF Toolkit Data Extractor!")
                else: 
                    console.print("No data selected, thanks for using the EEF Teaching and Learning Toolkit Extractor.")
                break

if __name__ == "__main__":
    main()