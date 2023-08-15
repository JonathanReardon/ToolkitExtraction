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

from .src.attributeIDs import *
from .src.funcs import (
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
    dataframe_11_output_display,
    input_file_info_display,
    main_menu_display,
    main_menu_display1,
)

# table1 
row_styles1 = ["#FFFFFF"] * 34
row_data_list1 = [
    "Study ID", 
    "Author", 
    "Year", 
    "Abstract", 
    "Admin Strand",
    "Country", 
    "Publication Type EPPI", 
    "Publication Type",
    "Student Age",
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
    main_table2.add_column("General Data", header_style=header_style, style=column_style, width=30)

    for idx, row_data in enumerate(row_data_list1, start=1):
        main_table2.add_row(f"{idx}", row_data, style=row_styles1[idx - 1])
    
    return main_table2

# table1 
row_styles2 = ["#FFFFFF"] * 48
row_data_list2 = [
    "(primary) Title", 
    "(primary) Description", 
    "(primary) Type", 
    "(primary) SMD", 
    "(primary) SE",
    "(primary) CI (lower)",
    "(primary) CI (upper)",
    "(primary) Measure", 
    "(primary) Group1 N", 
    "(primary) Group1 Mean",
    "(primary) Group1 SD", 
    "(primary) Group2 N",
    "(primary) Group2 Mean",
    "(primary) Group2 SD",
    "(primary) Test Type",
    "(primary) Effect Size Type",
    "(reading) Title",
    "(reading) Description", 
    "(reading) Type", 
    "(reading) SMD", 
    "(reading) SE",
    "(reading) CI (lower)",
    "(reading) CI (upper)",
    "(reading) Measure", 
    "(reading) Group1 N", 
    "(reading) Group1 Mean",
    "(reading) Group1 SD", 
    "(reading) Group2 N",
    "(reading) Group2 Mean",
    "(reading) Group2 SD",
    "(reading) Test Type",
    "(reading) Effect Size Type",
    "(writing) Title", 
    "(writing) Description", 
    "(writing) Type", 
    "(writing) SMD", 
    "(writing) SE",
    "(writing) CI (lower)",
    "(writing) CI (upper)",
    "(writing) Measure", 
    "(writing) Group1 N", 
    "(writing) Group1 Mean",
    "(writing) Group1 SD", 
    "(writing) Group2 N",
    "(writing) Group2 Mean",
    "(writing) Group2 SD",
    "(writing) Test Type",
    "(writing) Effect Size Type",
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
    main_table3.add_column("Outcome Specific Data", header_style=header_style, style=column_style, width=30)

    for idx, row_data in enumerate(row_data_list2, start=1):
        main_table3.add_row(f"{idx+34}", row_data, style=row_styles2[idx - 1])
    
    return main_table3

# table1 
row_styles3 = ["#FFFFFF"] * 48
row_data_list3 = [

    "(math) Title",
    "(math) Description", 
    "(math) Type", 
    "(math) SMD", 
    "(math) SE",
    "(math) CI (lower)",
    "(math) CI (upper)",
    "(math) Measure", 
    "(math) Group1 N", 
    "(math) Group1 Mean",
    "(math) Group1 SD", 
    "(math) Group2 N",
    "(math) Group2 Mean",
    "(math) Group2 SD",
    "(math) Test Type",
    "(math) Effect Size Type",
    "(science) Title", 
    "(science) Description", 
    "(science) Type", 
    "(science) SMD", 
    "(science) SE",
    "(science) CI (lower)",
    "(science) CI (upper)",
    "(science) Measure", 
    "(science) Group1 N", 
    "(science) Group1 Mean",
    "(science) Group1 SD", 
    "(science) Group2 N",
    "(science) Group2 Mean",
    "(science) Group2 SD",
    "(science) Test Type",
    "(science) Effect Size Type",
    "(fsm) Title",
    "(fsm) Description", 
    "(fsm) Type", 
    "(fsm) SMD", 
    "(fsm) SE",
    "(fsm) CI (lower)",
    "(fsm) CI (upper)",
    "(fsm) Measure", 
    "(fsm) Group1 N", 
    "(fsm) Group1 Mean",
    "(fsm) Group1 SD", 
    "(fsm) Group2 N",
    "(fsm) Group2 Mean",
    "(fsm) Group2 SD",
    "(fsm) Test Type",
    "(fsm) Effect Size Type",
]

def custom_outcome_vars_2():
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

    main_table4 = Table(show_header=True, 
                        box=box.SIMPLE,
                        highlight=False,
                        title_style=table_title_style,                  
    )

    main_table4.add_column("", header_style=header_style, style=column_style, width=3)
    main_table4.add_column("Outcome Specific Data", header_style=header_style, style=column_style, width=30)

    for idx, row_data in enumerate(row_data_list3, start=1):
        main_table4.add_row(f"{idx+82}", row_data, style=row_styles3[idx - 1])
    
    return main_table4

# table1 
row_styles4 = ["#FFFFFF"] * 49
row_data_list4 = [
    "Intervention Name (ht)",
    "Intervention Name (info)",
    "Intervention Description (ht)",
    "Intervention Description (info)",
    "Intervention Objective (ht)",
    "Intervention Objective (info)",
    "Intervention Training (raw)", 
    "Intervention Training (ht)", 
    "Intervention Training (info)", 
    "Intervention Approach (raw)", 
    "Intervention Approach (ht)",
    "Intervention Approach (info)",
    "Digital Technology (raw)",
    "Digital Technology (ht)", 
    "Digital Technology (info)", 
    "Parental Participation (raw)",
    "Parental Participation (ht)", 
    "Parental Participation (info)",
    "Interention When (raw)",
    "Interention When (ht)",
    "Interention When (info)",
    "Intervention Delivery (raw)",
    "Intervention Delivery (ht)",
    "Intervention Delivery (info)", 
    "Intervention Duration (ht)", 
    "Intervention Duration (info)",
    "Intervention Length (ht)",
    "Intervention Length (info)",
    "Intervention Setting (raw)", 
    "Intervention Setting (ht)", 
    "Intervention Setting (info)",
    "Intervention Focus (raw)",
    "Intervention Focus (ht)",
    "Intervention Focus (info)",
    "Intervention Detail (raw)",
    "Intervention Detail (ht)",
    "Intervention Detail (info)",
    "Intervention Costs (raw)",
    "Intervention Costs (ht)",
    "Intervention Costs (info)",
    "Baseline Differences (raw)",
    "Baseline Differences (ht)",
    "Baseline Differences (info)",
    "Comparability (raw)",
    "Comparability (ht)",
    "Comparability (info)",
    "Comparability Reported (raw)",
    "Comparability Reported (ht)",
    "Comparability Reported (info)",
]

def intervention_vars_3():
    """
    Displays a Rich list of [toolkit]'outcome' variables for the custom data frame builder
    - Outcome Titlepanel5
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

    main_table5 = Table(show_header=True, 
                        box=box.SIMPLE,
                        highlight=False,
                        title_style=table_title_style,                  
    )

    main_table5.add_column("", header_style=header_style, style=column_style, width=3)
    main_table5.add_column("Intervention Details", header_style=header_style, style=column_style, width=31)

    for idx, row_data in enumerate(row_data_list4, start=1):
        main_table5.add_row(f"{idx+130}", row_data, style=row_styles4[idx - 1])
    
    return main_table5

# table1 
row_styles5 = ["#FFFFFF"] * 35
row_data_list5 = [
    "Which Comp Var Reported (raw)",
    "Which Comp Var Reported (ht)",
    "Which Comp Var Reported (info)",
    "Clustering (raw)",
    "Clustering (ht)",
    "Clustering (info)",
    "Student Gender (raw)",
    "Student Gender (ht)",
    "Student Gender (info)",
    "Sample Size (ht)",
    "Sample Size (info)",
    "Intervention Sample Size (ht)",
    "Intervention Sample Size (info)",
    "Control Sample Size (ht)",
    "Control Sample Size (info)",
    "Intervention 2 Sample Size (ht)",
    "Intervention 2 Sample Size (info)",
    "Intervention 3 Sample Size (ht)",
    "Intervention 3 Sample Size (info)",
    "Intervention Sample Size Analyzed (ht)",
    "Intervention Sample Size Analyzed (info)",
    "Control Sample Size Analyzed (ht)",
    "Control Sample Size Analyzed (info)",
    "Intervention 2 Sample Size Analyzed (ht)",
    "Intervention 2 Sample Size Analyzed (info)",
    "Control 2 Sample Size Analyzed (ht)",
    "Control 2 Sample Size Analyzed (info)",
    "Attrition Reported (raw)",
    "Attrition Reported (ht)",
    "Attrition Reported (info)",
    "Treatment Group Attrition (ht)",
    "Treatment Group Attrition (info)",
    "Total % Attrition (ht)",
    "Total % Attrition (info)",
    "ALL"
]

def intervention_vars_4():
    """
    Displays a Rich list of [toolkit]'outcome' variables for the custom data frame builder
    - Outcome Titlepanel5
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

    main_table6 = Table(show_header=True, 
                        box=box.SIMPLE,
                        highlight=False,
                        title_style=table_title_style,                  
    )

    main_table6.add_column("", header_style=header_style, style=column_style, width=3)
    main_table6.add_column("Intervention Details", header_style=header_style, style=column_style, width=42)

    for idx, row_data in enumerate(row_data_list5, start=1):
        main_table6.add_row(f"{idx+179}", row_data, style=row_styles5[idx - 1])
    
    return main_table6

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
            console.print("Error: invalid input. Please enter a number from 0 to 11.")
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
                # Display list of outcome vars e.g. title, description, type etc.
                main_table4 = custom_outcome_vars_2()
                # Display list of outcome vars e.g. title, description, type etc.
                main_table5 = intervention_vars_3()
                # Display list of outcome vars e.g. title, description, type etc.
                main_table6 = intervention_vars_4()

                custom_style_main = Style(bgcolor="#37474f")
                custom_style_outer = Style(bgcolor="#37474f")

                panel1 = Panel(main_table2, style=custom_style_main, border_style="#37474f")
                panel2 = Panel(main_table3, style=custom_style_main, border_style="#37474f")
                panel3 = Panel(main_table4, style=custom_style_main, border_style="#37474f")
                panel4 = Panel(main_table5, style=custom_style_main, border_style="#37474f")
                panel5 = Panel(main_table6, style=custom_style_main, border_style="#37474f")

                # Combine the panels horizontally
                columns = Columns([panel1, panel2, panel3, panel4, panel5])

                # Create a larger panel with white background and black text to house the columns
                panel = Panel(columns, 
                                title="Custom Data Selection", 
                                style=custom_style_outer, 
                                border_style="#FFFFFF",
                                width=250)

                # Print the panel
                console.print(panel)
                
                df = CustomFrames(json_extractor)

                used_options = []

                # Compile list of invidividual data frames
                dataframes=[]
                all_df = pd.DataFrame()

                df_outcomes = DataFrameCompilation(json_extractor)
                df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)

                custom=True
                while custom==True:
                    try:
                        console.print("\nAdd variables to your data frame or 0 to Save file and exit")
                        num = int(Prompt.ask("Selection"))
                        if num < 0 or num > 2020:
                            raise ValueError
                    except ValueError:
                        print("Error: invalid input. Please enter a number from 0 to 2020.\n")
                        continue

                    match num:
                        case 0:
                            run_program=False
                            break
                        case 1: 
                            if "id" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["id"] = df.data_extraction.retrieve_metadata("ItemId", "id")
                                used_options.append("id")
                            else:
                                print("You have already selected this option!")
                        case 2: 
                            if "pub_author" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["pub_author"] = df.data_extraction.retrieve_metadata("ShortTitle", "pub_author")
                                used_options.append("pub_author")
                            else:
                                print("You have already selected this option!")
                        case 3: 
                            if "pub_year" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["pub_year"] = df.data_extraction.retrieve_metadata("Year", "pub_year")
                                used_options.append("pub_year")
                            else:
                                print("You have already selected this option!")
                        case 4:
                            if "abstract" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["abstract"] = df.data_extraction.retrieve_metadata("Abstract", "abstract")
                                used_options.append("abstract")
                            else:
                                print("You have already selected this option!")
                        case 5: 
                            if "strand_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["strand_raw"] = df.data_extraction.retrieve_data(admin_strand_output, "strand_raw")
                                used_options.append("strand_raw")
                            else:
                                print("You have already selected this option!")
                        case 6:
                            if "loc_country_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["loc_country_raw"] = df.data_extraction.retrieve_data(countries, "loc_country_raw")
                                used_options.append("loc_country_raw")
                            else:
                                print("You have already selected this option!")
                        case 7: 
                            if "pub_eppi" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["pub_eppi"] = df.data_extraction.retrieve_metadata("TypeName", "pub_eppi")
                                used_options.append("pub_eppi")
                            else:
                                print("You have already selected this option!")
                        case 8: 
                            if "pub_type_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["pub_type_raw"] = df.data_extraction.retrieve_data(publication_type_output, "pub_type_raw")
                                used_options.append("pub_type_raw")
                            else:
                                print("You have already selected this option!")
                        case 9: 
                            if "part_age_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                student_age_data = df.data_extraction.retrieve_data(student_age_output, "part_age_raw")
                                used_options.append("part_age_raw")
                            else:
                                print("You have already selected this option!")
                        case 10: 
                            if "eco_valid_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["eco_valid_raw"] = df.data_extraction.retrieve_data(study_realism_output, "eco_valid_raw")
                                used_options.append("eco_valid_raw")
                            else:
                                print("You have already selected this option!")
                        #/*************************/#
                        #/     NUMBER OF SCHOOLS   /#
                        #/*************************/#
                        case 11: 
                            if "school_treat_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["school_treat_info"] = df.data_extraction.retrieve_info(number_of_schools_intervention_output, "school_treat_info")
                                used_options.append("school_treat_info")
                            else:
                                print("You have already selected this option!")
                        case 12: 
                            if "school_treat_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["school_treat_ht"] = df.data_extraction.retrieve_ht(number_of_schools_intervention_output, "school_treat_ht")
                                used_options.append("school_treat_ht")
                            else:
                                print("You have already selected this option!")
                        case 13: 
                            if "school_cont_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["school_cont_info"] = df.data_extraction.retrieve_info(number_of_schools_control_output, "school_cont_info")
                                used_options.append("school_cont_info")
                            else:
                                print("You have already selected this option!")
                        case 14: 
                            if "school_cont_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["school_cont_ht"] = df.data_extraction.retrieve_ht(number_of_schools_control_output, "school_cont_ht")
                                used_options.append("school_cont_ht")
                            else:
                                print("You have already selected this option!")
                        case 15: 
                            if "school_total_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["school_total_info"] = df.data_extraction.retrieve_info(number_of_schools_total_output, "school_total_info")
                                used_options.append("school_total_info")
                            else:
                                print("You have already selected this option!")
                        case 16: 
                            if "school_total_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["school_total_ht"] = df.data_extraction.retrieve_ht(number_of_schools_total_output, "school_total_ht")
                                used_options.append("school_total_ht")
                            else:
                                print("You have already selected this option!")
                        #/*************************/#
                        #/    NUMBER OF CLASSES    /#
                        #/*************************/#
                        case 17: 
                            if "class_treat_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["class_treat_info"] = df.data_extraction.retrieve_info(num_of_class_int_output, "class_treat_info")
                                used_options.append("class_treat_info")
                            else:
                                print("You have already selected this option!")
                        case 18: 
                            if "class_treat_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["class_treat_ht"] = df.data_extraction.retrieve_ht(num_of_class_int_output, "class_treat_ht")
                                used_options.append("class_treat_ht")
                            else:
                                print("You have already selected this option!")
                        case 19: 
                            if "class_cont_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["class_cont_info"] = df.data_extraction.retrieve_info(num_of_class_cont_output, "class_cont_info")
                                used_options.append("class_cont_info")
                            else:
                                print("You have already selected this option!")
                        case 20: 
                            if "class_cont_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["class_cont_ht"] = df.data_extraction.retrieve_ht(num_of_class_cont_output, "class_cont_ht")
                                used_options.append("class_cont_ht")
                            else:
                                print("You have already selected this option!")
                        case 21: 
                            if "class_total_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["class_total_info"] = df.data_extraction.retrieve_info(num_of_class_tot_output, "class_total_info")
                                used_options.append("class_total_info")
                            else:
                                print("You have already selected this option!")
                        case 22: 
                            if "class_total_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["class_total_ht"] = df.data_extraction.retrieve_ht(num_of_class_tot_output, "class_total_ht")
                                used_options.append("class_total_ht")
                            else:
                                print("You have already selected this option!")
                        #/****************************/#
                        #/   PARTICIPANT ASSIGNMENT   /#
                        #/****************************/#
                        case 23: 
                            if "part_assig_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["part_assig_raw"] = df.data_extraction.retrieve_data(part_assign_output, "part_assig_raw")
                                used_options.append("part_assig_raw")
                            else:
                                print("You have already selected this option!")
                        case 24: 
                            if "part_assig_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["part_assig_ht"] = df.data_extraction.retrieve_ht(part_assign_output, "part_assig_ht")
                                used_options.append("part_assig_ht")
                            else:
                                print("You have already selected this option!")
                        case 25: 
                            if "part_assig_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["part_assig_info"] = df.data_extraction.retrieve_info(part_assign_output, "part_assig_info")
                                used_options.append("part_assig_info")
                            else:
                                print("You have already selected this option!")
                        #/*************************/#
                        #/   LEVEL OF ASSIGNMENT   /#
                        #/*************************/#
                        case 26: 
                            if "level_assig_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["level_assig_raw"] = df.data_extraction.retrieve_data(level_of_assignment_output, "level_assig_raw")
                                used_options.append("level_assig_raw")
                            else:
                                print("You have already selected this option!")
                        case 27: 
                            if "level_assig_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["level_assig_ht"] = df.data_extraction.retrieve_ht(level_of_assignment_output, "level_assig_ht")
                                used_options.append("level_assig_ht")
                            else:
                                print("You have already selected this option!")
                        case 28: 
                            if "level_assig_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["level_assig_info"] = df.data_extraction.retrieve_info(level_of_assignment_output, "level_assig_info")
                                used_options.append("level_assig_info")
                            else:
                                print("You have already selected this option!")
                        #/**********************/#
                        #/     STUDY DESIGN     /#
                        #/**********************/#
                        case 29: 
                            if "int_desig_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["int_design_raw"] = df.data_extraction.retrieve_data(study_design_output, "int_desig_raw")
                                used_options.append("int_desig_raw")
                            else:
                                print("You have already selected this option!")
                        case 30: 
                            if "int_design_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["int_design_ht"] = df.data_extraction.retrieve_ht(study_design_output, "int_design_ht")
                                used_options.append("int_design_ht")
                            else:
                                print("You have already selected this option!")
                        case 31: 
                            if "int_design_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["int_design_info"] = df.data_extraction.retrieve_info(study_design_output, "int_design_info")
                                used_options.append("int_design_info")
                            else:
                                print("You have already selected this option!")
                        #/**********************/#
                        #/     RANDOMISATION    /#
                        #/**********************/#
                        case 32: 
                            if "rand_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["rand_raw"] = df.data_extraction.retrieve_data(randomisation_details, "rand_raw")
                                used_options.append("rand_raw")
                            else:
                                print("You have already selected this option!")
                        case 33: 
                            if "rand_ht" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["rand_ht"] = df.data_extraction.retrieve_ht(randomisation_details, "rand_ht")
                                used_options.append("rand_ht")
                            else:
                                print("You have already selected this option!")
                        case 34: 
                            if "rand_info" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                all_df["rand_info"] = df.data_extraction.retrieve_info(randomisation_details, "rand_info")
                                used_options.append("rand_info")
                            else:
                                print("You have already selected this option!")
                        #/*************************/#
                        #/ TOOLKIT PRIMARY OUTCOME /#
                        #/*************************/#
                        case 35:
                            if "out_tit_tool" not in used_options:
                                row_styles2[num - 35] = highlight_style
                                all_df["out_tit_tool"] = df_out.out_tit_tool
                                used_options.append("out_tit_tool")
                            else:
                                print("You have already selected this option!")
                        case 36:
                            if "out_desc_tool" not in used_options:
                                row_styles2[num - 35] = highlight_style
                                all_df["out_desc_tool"] =  df_out.out_desc_tool
                                used_options.append("out_desc_tool")
                            else:
                                print("You have already selected this option!")
                        case 37:
                            if "out_type_tool" not in used_options:
                                row_styles2[num - 35] = highlight_style

                                all_df["out_type_tool"] = df_out.out_type_tool
                                used_options.append("out_type_tool")
                            else:
                                print("You have already selected this option!")
                        case 38:
                            if "smd_tool" not in used_options:
                                row_styles2[num - 35] = highlight_style
                                all_df["smd_tool"] = df_out.smd_tool
                                used_options.append("smd_tool")
                            else:
                                print("You have already selected this option!")
                        case 39:
                            if "se_tool" not in used_options:
                                row_styles2[num - 35] = highlight_style
                                all_df["se_tool"] = df_out.se_tool
                                used_options.append("se_tool")
                            else:
                                print("You have already selected this option!")
                        case 40:
                            if "ci_lower_tool" not in used_options:
                                row_styles2[num - 35] = highlight_style
                                all_df["ci_lower_tool"] = df_out.ci_lower_tool
                                used_options.append("ci_lower_tool")
                            else:
                                print("You have already selected this option!")
                        case 41:
                            if "ci_upper_tool" not in used_options:
                                row_styles2[num - 35] = highlight_style
                                all_df["ci_upper_tool"] = df_out.ci_upper_tool
                                used_options.append("ci_upper_tool")
                            else:
                                print("You have already selected this option!")
                        case 42:
                            if "out_measure_tool" not in used_options:
                                row_styles2[num - 35] = highlight_style
                                all_df["out_measure_tool"] = df_out.out_measure_tool
                                used_options.append("out_measure_tool")
                            else:
                                print("You have already selected this option!")
                        case 43:
                            if "out_g1_n_tool" not in used_options:
                                row_styles2[num - 35] = highlight_style
                                all_df["out_g1_n_tool"] = df_out.out_g1_n_tool
                                used_options.append("out_g1_n_tool")
                            else:
                                print("You have already selected this option!")
                        case 44:
                            if "out_g1_mean_tool" not in used_options:
                                row_styles2[num - 35] = highlight_style
                                all_df["out_g1_mean_tool"] = df_out.out_g1_mean_tool
                                used_options.append("out_g1_mean_tool")
                            else:
                                print("You have already selected this option!")
                        case 45:
                            if "out_g1_sd_tool" not in used_options:
                                row_styles2[num - 35] = highlight_style
                                all_df["out_g1_sd_tool"] = df_out.out_g1_sd_tool
                                used_options.append("out_g1_sd_tool")
                            else:
                                print("You have already selected this option!")
                        case 46:
                            if "out_g2_n_tool" not in used_options:
                                row_styles2[num - 35] = highlight_style
                                all_df["out_g2_n_tool"] = df_out.out_g2_n_tool
                                used_options.append("out_g2_n_tool")
                            else:
                                print("You have already selected this option!")
                        case 47:
                            if "out_g2_mean_tool" not in used_options:
                                row_styles2[num - 35] = highlight_style
                                all_df["out_g2_mean_tool"] = df_out.out_g2_mean_tool
                                used_options.append("out_g2_mean_tool")
                            else:
                                print("You have already selected this option!")
                        case 48:
                            if "out_g2_sd_tool" not in used_options:
                                row_styles2[num - 35] = highlight_style
                                all_df["out_g2_sd_tool"] = df_out.out_g2_sd_tool
                                used_options.append("out_g2_sd_tool")
                            else:
                                print("You have already selected this option!")
                        case 49:
                            if "out_test_type_raw_" not in used_options:
                                row_styles2[num - 35] = highlight_style
                                all_df["out_test_type_raw_"] = df_out.out_test_type_raw_tool
                                used_options.append("out_test_type_raw_")
                            else:
                                print("You have already selected this option!")
                        case 50:
                            if "out_es_type_tool" not in used_options:
                                row_styles2[num - 35] = highlight_style
                                all_df["out_es_type_tool"] = df_out.out_es_type_tool
                                used_options.append("out_es_type_tool")
                            else:
                                print("You have already selected this option!")
                        #/*************************/#
                        #/     READING OUTCOME     /#
                        #/*************************/#
                        case 51:
                                if "out_tit_red" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_tit_red"] = df_out.out_tit_red
                                    used_options.append("out_tit_red")
                                else:
                                    print("You have already selected this option!")
                        case 52:
                                if "out_desc_red" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_desc_red"] = df_out.out_desc_red
                                    used_options.append("out_desc_red")
                                else:
                                    print("You have already selected this option!")
                        case 53:
                                if "out_type_red" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_type_red"] = df_out.out_type_red
                                    used_options.append("out_type_red")
                                else:
                                    print("You have already selected this option!")
                        case 54:
                                if "smd_red" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["smd_red"] = df_out.smd_red
                                    used_options.append("smd_red")
                                else:
                                    print("You have already selected this option!")
                        case 55:
                                if "se_red" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["se_red"] = df_out.se_red
                                    used_options.append("se_red")
                                else:
                                    print("You have already selected this option!")
                        case 56:
                                if "ci_lower_red" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["ci_lower_red"] = df_out.ci_lower_red
                                    used_options.append("ci_lower_red")
                                else:
                                    print("You have already selected this option!")
                        case 57:
                                if "ci_upper_red" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["ci_upper_red"] = df_out.ci_upper_red
                                    used_options.append("ci_upper_red")
                                else:
                                    print("You have already selected this option!")
                        case 58:
                                if "out_measure_red" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_measure_red"] = df_out.out_measure_red
                                    used_options.append("out_measure_red")
                                else:
                                    print("You have already selected this option!")
                        case 59:
                                if "out_g1_n_red" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_g1_n_red"] = df_out.out_g1_n_red
                                    used_options.append("out_g1_n_red")
                                else:
                                    print("You have already selected this option!")
                        case 60:
                                if "out_g1_mean_red" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_g1_mean_red"] = df_out.out_g1_mean_red
                                    used_options.append("out_g1_mean_red")
                                else:
                                    print("You have already selected this option!")
                        case 61:
                                if "out_g1_sd_red" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_g1_sd_red"] = df_out.out_g1_sd_red
                                    used_options.append("out_g1_sd_red")
                                else:
                                    print("You have already selected this option!")
                        case 62:
                                if "out_g2_n_red" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_g2_n_red"] = df_out.out_g2_n_red
                                    used_options.append("out_g2_n_red")
                                else:
                                    print("You have already selected this option!")
                        case 63:
                                if "out_g2_mean_red" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_g2_mean_red"] = df_out.out_g2_mean_red
                                    used_options.append("out_g2_mean_red")
                                else:
                                    print("You have already selected this option!")
                        case 64:
                                if "out_g2_sd_red" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_g2_sd_red"] = df_out.out_g2_sd_red
                                    used_options.append("out_g2_sd_red")
                                else:
                                    print("You have already selected this option!")
                        case 65:
                                if "out_test_type_raw_red" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_test_type_raw_red"] = df_out.out_test_type_raw_red
                                    used_options.append("out_test_type_raw_red")
                                else:
                                    print("You have already selected this option!")
                        case 66:
                                if "out_es_type_red" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_es_type_red"] = df_out.out_es_type_red
                                    used_options.append("out_es_type_red")
                                else:
                                    print("You have already selected this option!")
                        #/*************************/#
                        #/     WRITING OUTCOME     /#
                        #/*************************/#
                        case 67:
                                if "out_tit_wri" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_tit_wri"] = df_out.out_tit_wri
                                    used_options.append("out_tit_wri")
                                else:
                                    print("You have already selected this option!")
                        case 68:
                                if "out_desc_wri" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_desc_wri"] = df_out.out_desc_wri
                                    used_options.append("out_desc_wri")
                                else:
                                    print("You have already selected this option!")
                        case 69:
                                if "out_type_wri" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_type_wri"] = df_out.out_type_wri
                                    used_options.append("out_type_wri")
                                else:
                                    print("You have already selected this option!")
                        case 70:
                                if "smd_wri" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["smd_wri"] = df_out.smd_wri
                                    used_options.append("smd_wri")
                                else:
                                    print("You have already selected this option!")
                        case 71:
                                if "se_wri" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["se_wri"] = df_out.se_wri
                                    used_options.append("se_wri")
                                else:
                                    print("You have already selected this option!")
                        case 72:
                                if "ci_lower_wri" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["ci_lower_wri"] = df_out.ci_lower_wri
                                    used_options.append("ci_lower_wri")
                                else:
                                    print("You have already selected this option!")
                        case 73:
                                if "ci_upper_wri" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["ci_upper_wri"] = df_out.ci_upper_wri
                                    used_options.append("ci_upper_wri")
                                else:
                                    print("You have already selected this option!")
                        case 74:
                                if "out_measure_wri" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_measure_wri"] = df_out.out_measure_wri
                                    used_options.append("out_measure_wri")
                                else:
                                    print("You have already selected this option!")
                        case 75:
                                if "out_g1_n_wri" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_g1_n_wri"] = df_out.out_g1_n_wri
                                    used_options.append("out_g1_n_wri")
                                else:
                                    print("You have already selected this option!")
                        case 76:
                                if "out_g1_mean_wri" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_g1_mean_wri"] = df_out.out_g1_mean_wri
                                    used_options.append("out_g1_mean_wri")
                                else:
                                    print("You have already selected this option!")
                        case 77:
                                if "out_g1_sd_wri" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_g1_sd_wri"] = df_out.out_g1_sd_wri
                                    used_options.append("out_g1_sd_wri")
                                else:
                                    print("You have already selected this option!")
                        case 78:
                                if "out_g2_n_wri" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_g2_n_wri"] = df_out.out_g2_n_wri
                                    used_options.append("out_g2_n_wri")
                                else:
                                    print("You have already selected this option!")
                        case 79:
                                if "out_g2_mean_wri" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_g2_mean_wri"] = df_out.out_g2_mean_wri
                                    used_options.append("out_g2_mean_wri")
                                else:
                                    print("You have already selected this option!")
                        case 80:
                                if "out_g2_sd_wri" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_g2_sd_wri"] = df_out.out_g2_sd_wri
                                    used_options.append("out_g2_sd_wri")
                                else:
                                    print("You have already selected this option!")
                        case 81:
                                if "out_test_type_raw_wri" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_test_type_raw_wri"] = df_out.out_test_type_raw_wri
                                    used_options.append("out_test_type_raw_wri")
                                else:
                                    print("You have already selected this option!")
                        case 82:
                                if "out_es_type_wri" not in used_options:
                                    row_styles2[num - 35] = highlight_style
                                    all_df["out_es_type_wri"] = df_out.out_es_type_wri
                                    used_options.append("out_es_type_wri")
                                else:
                                    print("You have already selected this option!")
                        #/*************************/#
                        #/        MATH OUTCOME     /#
                        #/*************************/#
                        case 83:
                                if "out_tit_math" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_tit_math"] = df_out.out_tit_math
                                    used_options.append("out_tit_math")
                                else:
                                    print("You have already selected this option!")
                        case 84:
                                if "out_desc_math" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_desc_math"] = df_out.out_desc_math
                                    used_options.append("out_desc_math")
                                else:
                                    print("You have already selected this option!")
                        case 85:
                                if "out_type_math" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_type_math"] = df_out.out_type_math
                                    used_options.append("out_type_math")
                                else:
                                    print("You have already selected this option!")
                        case 86:
                                if "smd_math" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["smd_math"] = df_out.smd_math
                                    used_options.append("smd_math")
                                else:
                                    print("You have already selected this option!")
                        case 87:
                                if "se_math" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["se_math"] = df_out.se_math
                                    used_options.append("se_math")
                                else:
                                    print("You have already selected this option!")
                        case 88:
                                if "ci_lower_math" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["ci_lower_math"] = df_out.ci_lower_math
                                    used_options.append("ci_lower_math")
                                else:
                                    print("You have already selected this option!")
                        case 89:
                                if "ci_upper_math" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["ci_upper_math"] = df_out.ci_upper_math
                                    used_options.append("ci_upper_math")
                                else:
                                    print("You have already selected this option!")
                        case 90:
                                if "out_measure_math" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_measure_math"] = df_out.out_measure_math
                                    used_options.append("out_measure_math")
                                else:
                                    print("You have already selected this option!")
                        case 91:
                                if "out_g1_n_math" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_g1_n_math"] = df_out.out_g1_n_math
                                    used_options.append("out_g1_n_math")
                                else:
                                    print("You have already selected this option!")
                        case 92:
                                if "out_g1_mean_math" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_g1_mean_math"] = df_out.out_g1_mean_math
                                    used_options.append("out_g1_mean_math")
                                else:
                                    print("You have already selected this option!")
                        case 93:
                                if "out_g1_sd_math" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_g1_sd_math"] = df_out.out_g1_sd_math
                                    used_options.append("out_g1_sd_math")
                                else:
                                    print("You have already selected this option!")
                        case 94:
                                if "out_g2_n_math" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_g2_n_math"] = df_out.out_g2_n_math
                                    used_options.append("out_g2_n_math")
                                else:
                                    print("You have already selected this option!")
                        case 95:
                                if "out_g2_mean_math" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_g2_mean_math"] = df_out.out_g2_mean_math
                                    used_options.append("out_g2_mean_math")
                                else:
                                    print("You have already selected this option!")
                        case 96:
                                if "out_g2_sd_math" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_g2_sd_math"] = df_out.out_g2_sd_math
                                    used_options.append("out_g2_sd_math")
                                else:
                                    print("You have already selected this option!")
                        case 97:
                                if "out_test_type_raw_math" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_test_type_raw_math"] = df_out.out_test_type_raw_math
                                    used_options.append("out_test_type_raw_math")
                                else:
                                    print("You have already selected this option!")
                        case 98:
                                if "out_es_type_math" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_es_type_math"] = df_out.out_es_type_math
                                    used_options.append("out_es_type_math")
                                else:
                                    print("You have already selected this option!")
                        #/*************************/#
                        #/     SCIENCE OUTCOME     /#
                        #/*************************/#
                        case 99:
                                if "out_tit_sci" not in used_options:
                                    row_styles3[num - 83] = highlight_style

                                    all_df["out_tit_sci"] = df_out.out_tit_sci
                                    used_options.append("out_tit_sci")
                                else:
                                    print("You have already selected this option!")
                        case 100:
                                if "out_desc_sci" not in used_options:
                                    row_styles3[num - 83] = highlight_style

                                    all_df["out_desc_sci"] = df_out.out_desc_sci
                                    used_options.append("out_desc_sci")
                                else:
                                    print("You have already selected this option!")
                        case 101:
                                if "out_type_sci" not in used_options:
                                    row_styles3[num - 83] = highlight_style

                                    all_df["out_type_sci"] = df_out.out_type_sci
                                    used_options.append("out_type_sci")
                                else:
                                    print("You have already selected this option!")
                        case 102:
                                if "smd_sci" not in used_options:
                                    row_styles3[num - 83] = highlight_style

                                    all_df["smd_sci"] = df_out.smd_sci
                                    used_options.append("smd_sci")
                                else:
                                    print("You have already selected this option!")
                        case 103:
                                if "se_sci" not in used_options:
                                    row_styles3[num - 83] = highlight_style

                                    all_df["se_sci"] = df_out.se_sci
                                    used_options.append("se_sci")
                                else:
                                    print("You have already selected this option!")
                        case 104:
                                if "ci_lower_sci" not in used_options:
                                    row_styles3[num - 83] = highlight_style

                                    all_df["ci_lower_sci"] = df_out.ci_lower_sci
                                    used_options.append("ci_lower_sci")
                                else:
                                    print("You have already selected this option!")
                        case 105:
                                if "ci_upper_sci" not in used_options:
                                    row_styles3[num - 83] = highlight_style

                                    all_df["ci_upper_sci"] = df_out.ci_upper_sci
                                    used_options.append("ci_upper_sci")
                                else:
                                    print("You have already selected this option!")
                        case 106:
                                if "out_measure_sci" not in used_options:
                                    row_styles3[num - 83] = highlight_style

                                    all_df["out_measure_sci"] = df_out.out_measure_sci
                                    used_options.append("out_measure_sci")
                                else:
                                    print("You have already selected this option!")
                        case 107:
                                if "out_g1_n_sci" not in used_options:
                                    row_styles3[num - 83] = highlight_style

                                    all_df["out_g1_n_sci"] = df_out.out_g1_n_sci
                                    used_options.append("out_g1_n_sci")
                                else:
                                    print("You have already selected this option!")
                        case 108:
                                if "out_g1_mean_sci" not in used_options:
                                    row_styles3[num - 83] = highlight_style

                                    all_df["out_g1_mean_sci"] = df_out.out_g1_mean_sci
                                    used_options.append("out_g1_mean_sci")
                                else:
                                    print("You have already selected this option!")
                        case 109:
                                if "out_g1_sd_sci" not in used_options:
                                    row_styles3[num - 83] = highlight_style

                                    all_df["out_g1_sd_sci"] = df_out.out_g1_sd_sci
                                    used_options.append("out_g1_sd_sci")
                                else:
                                    print("You have already selected this option!")
                        case 110:
                                if "out_g2_n_sci" not in used_options:
                                    row_styles3[num - 83] = highlight_style

                                    all_df["out_g2_n_sci"] = df_out.out_g2_n_sci
                                    used_options.append("out_g2_n_sci")
                                else:
                                    print("You have already selected this option!")
                        case 111:
                                if "out_g2_mean_sci" not in used_options:
                                    row_styles3[num - 83] = highlight_style

                                    all_df["out_g2_mean_sci"] = df_out.out_g2_mean_sci
                                    used_options.append("out_g2_mean_sci")
                                else:
                                    print("You have already selected this option!")
                        case 112:
                                if "out_g2_sd_sci" not in used_options:
                                    row_styles3[num - 83] = highlight_style

                                    all_df["out_g2_sd_sci"] = df_out.out_g2_sd_sci
                                    used_options.append("out_g2_sd_sci")
                                else:
                                    print("You have already selected this option!")
                        case 113:
                                if "out_test_type_raw_sci" not in used_options:
                                    row_styles3[num - 83] = highlight_style

                                    all_df["out_test_type_raw_sci"] = df_out.out_test_type_raw_sci
                                    used_options.append("out_test_type_raw_sci")
                                else:
                                    print("You have already selected this option!")
                        case 114:
                                if "out_es_type_sci" not in used_options:
                                    row_styles3[num - 83] = highlight_style

                                    all_df["out_es_type_sci"] = df_out.out_es_type_sci
                                    used_options.append("out_es_type_sci")
                                else:
                                    print("You have already selected this option!")
                        #/*************************/#
                        #/        FSM OUTCOME      /#
                        #/*************************/#
                        case 115:
                                if "out_tit_fsm" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_tit_fsm"] = df_out.out_tit_fsm
                                    used_options.append("out_tit_fsm")
                                else:
                                    print("You have already selected this option!")
                        case 116:
                                if "out_desc_fsm" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_desc_fsm"] = df_out.out_desc_fsm
                                    used_options.append("out_desc_fsm")
                                else:
                                    print("You have already selected this option!")
                        case 117:
                                if "out_type_fsm" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_type_fsm"] = df_out.out_type_fsm
                                    used_options.append("out_type_fsm")
                                else:
                                    print("You have already selected this option!")
                        case 118:
                                if "smd_fsm" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["smd_fsm"] = df_out.smd_fsm
                                    used_options.append("smd_fsm")
                                else:
                                    print("You have already selected this option!")
                        case 119:
                                if "se_fsm" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["se_fsm"] = df_out.se_fsm
                                    used_options.append("se_fsm")
                                else:
                                    print("You have already selected this option!")
                        case 120:
                                if "ci_lower_fsm" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["ci_lower_fsm"] = df_out.ci_lower_fsm
                                    used_options.append("ci_lower_fsm")
                                else:
                                    print("You have already selected this option!")
                        case 121:
                                if "ci_upper_fsm" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["ci_upper_fsm"] = df_out.ci_upper_fsm
                                    used_options.append("ci_upper_fsm")
                                else:
                                    print("You have already selected this option!")
                        case 122:
                                if "out_measure_fsm" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_measure_fsm"] = df_out.out_measure_fsm
                                    used_options.append("out_measure_fsm")
                                else:
                                    print("You have already selected this option!")
                        case 123:
                                if "out_g1_n_fsm" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_g1_n_fsm"] = df_out.out_g1_n_fsm
                                    used_options.append("out_g1_n_fsm")
                                else:
                                    print("You have already selected this option!")
                        case 124:
                                if "out_g1_mean_fsm" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_g1_mean_fsm"] = df_out.out_g1_mean_fsm
                                    used_options.append("out_g1_mean_fsm")
                                else:
                                    print("You have already selected this option!")
                        case 125:
                                if "out_g1_sd_fsm" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_g1_sd_fsm"] = df_out.out_g1_sd_fsm
                                    used_options.append("out_g1_sd_fsm")
                                else:
                                    print("You have already selected this option!")
                        case 126:
                                if "out_g2_n_fsm" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_g2_n_fsm"] = df_out.out_g2_n_fsm
                                    used_options.append("out_g2_n_fsm")
                                else:
                                    print("You have already selected this option!")
                        case 127:
                                if "out_g2_mean_fsm" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_g2_mean_fsm"] = df_out.out_g2_mean_fsm
                                    used_options.append("out_g2_mean_fsm")
                                else:
                                    print("You have already selected this option!")
                        case 128:
                                if "out_g2_sd_fsm" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_g2_sd_fsm"] = df_out.out_g2_sd_fsm
                                    used_options.append("out_g2_sd_fsm")
                                else:
                                    print("You have already selected this option!")
                        case 129:
                                if "out_test_type_raw_fsm" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_test_type_raw_fsm"] = df_out.out_test_type_raw_fsm
                                    used_options.append("out_test_type_raw_fsm")
                                else:
                                    print("You have already selected this option!")
                        case 130:
                                if "out_es_type_fsm" not in used_options:
                                    row_styles3[num - 83] = highlight_style
                                    all_df["out_es_type_fsm"] = df_out.out_es_type_fsm
                                    used_options.append("out_es_type_fsm")
                                else:
                                    print("You have already selected this option!")
                        #/*****************************/#
                        #/     INTERVENTION DETAILS    /#
                        #/*****************************/#
                        case 131: 
                            if "intervention_name_ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_name_ht"] = df.data_extraction.retrieve_ht(int_name_output, "intervention_name_ht")
                                used_options.append("intervention_name_ht")
                            else:
                                print("You have already selected this option!")
                        case 132: 
                            if "int_name_info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_name_info"] = df.data_extraction.retrieve_info(int_name_output, "int_name_info")
                                used_options.append("int_name_info")
                            else:
                                print("You have already selected this option!")
                        case 133: 
                            if "intervention_desc_ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_desc_ht"] = df.data_extraction.retrieve_ht(intervention_description_output, "intervention_desc_ht")
                                used_options.append("intervention_desc_ht")
                            else:
                                print("You have already selected this option!")
                        case 134: 
                            if "intervention_desc_info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_desc_info"] = df.data_extraction.retrieve_info(intervention_description_output, "intervention_desc_info")
                                used_options.append("intervention_desc_info")
                            else:
                                print("You have already selected this option!")
                        case 135: 
                            if "intervention_objec_ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_objec_ht"] = df.data_extraction.retrieve_ht(intervention_objectives_output, "intervention_objec_ht")
                                used_options.append("intervention_objec_ht")
                            else:
                                print("You have already selected this option!")
                        case 136: 
                            if "intervention_objec_info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_objec_info"] = df.data_extraction.retrieve_info(intervention_objectives_output, "intervention_objec_info")
                                used_options.append("intervention_objec_info")
                            else:
                                print("You have already selected this option!")
                        case 137: 
                            if "int_training_raw" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_training_raw"] = df.data_extraction.retrieve_data(int_training_provided_output, "int_training_raw")
                                used_options.append("int_training_raw")
                            else:
                                print("You have already selected this option!")
                        case 138: 
                            if "int_training_ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_training_ht"] = df.data_extraction.retrieve_ht(int_training_provided_output, "int_training_ht")
                                used_options.append("int_training_ht")
                            else:
                                print("You have already selected this option!")
                        case 139: 
                            if "int_training_info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_training_info"] = df.data_extraction.retrieve_info(int_training_provided_output, "int_training_info")
                                used_options.append("int_training_info")
                            else:
                                print("You have already selected this option!")
                        case 140: 
                            if "int_approach_raw" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_approach_raw"] = df.data_extraction.retrieve_data(intervention_teaching_approach, "int_approach_raw")
                                used_options.append("int_approach_raw")
                            else:
                                print("You have already selected this option!")
                        case 141: 
                            if "int_approach_ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_approach_ht"] = df.data_extraction.retrieve_ht(intervention_teaching_approach, "int_approach_ht")
                                used_options.append("int_approach_ht")
                            else:
                                print("You have already selected this option!")
                        case 142: 
                            if "int_approach_info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_approach_info"] = df.data_extraction.retrieve_info(intervention_teaching_approach, "int_approach_info")
                                used_options.append("int_approach_info")
                            else:
                                print("You have already selected this option!")
                        case 143: 
                            if "digit_tech_raw" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["digit_tech_raw"] = df.data_extraction.retrieve_data(int_appr_dig_tech, "digit_tech_raw")
                                used_options.append("digit_tech_raw")
                            else:
                                print("You have already selected this option!")
                        case 144: 
                            if "digit_tech_ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["digit_tech_ht"] = df.data_extraction.retrieve_ht(int_appr_dig_tech, "digit_tech_ht")
                                used_options.append("digit_tech_ht")
                            else:
                                print("You have already selected this option!")
                        case 145: 
                            if "digit_tech_info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["digit_tech_info"] = df.data_extraction.retrieve_info(int_appr_dig_tech, "digit_tech_info")
                                used_options.append("digit_tech_info")
                            else:
                                print("You have already selected this option!")
                        case 146: 
                            if "parent_partic_raw" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["parent_partic_raw"] = df.data_extraction.retrieve_data(int_appr_par_or_comm_vol, "parent_partic_raw")
                                used_options.append("parent_partic_raw")
                            else:
                                print("You have already selected this option!")
                        case 147: 
                            if "parent_partic_ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["parent_partic_ht"] = df.data_extraction.retrieve_ht(int_appr_par_or_comm_vol, "parent_partic_ht")
                                used_options.append("parent_partic_ht")
                            else:
                                print("You have already selected this option!")
                        case 148: 
                            if "parent_partic_info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["parent_partic_info"] = df.data_extraction.retrieve_info(int_appr_par_or_comm_vol, "parent_partic_info")
                                used_options.append("parent_partic_info")
                            else:
                                print("You have already selected this option!")
                        case 149: 
                            if "int_when_raw" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_when_raw"] = df.data_extraction.retrieve_data(intervention_time_output, "int_when_raw")
                                used_options.append("int_when_raw")
                            else:
                                print("You have already selected this option!")
                        case 150: 
                            if "int_when_ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_when_ht"] = df.data_extraction.retrieve_ht(intervention_time_output, "int_when_ht")
                                used_options.append("int_when_ht")
                            else:
                                print("You have already selected this option!")
                        case 151: 
                            if "int_when_info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_when_info"] = df.data_extraction.retrieve_info(intervention_time_output, "int_when_info")
                                used_options.append("int_when_info")
                            else:
                                print("You have already selected this option!")
                        case 152: 
                            if "int_who_raw" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_who_raw"] = df.data_extraction.retrieve_data(intervention_delivery_output, "int_who_raw")
                                used_options.append("int_who_raw")
                            else:
                                print("You have already selected this option!")
                        case 153: 
                            if "int_who_ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_who_ht"] = df.data_extraction.retrieve_ht(intervention_delivery_output, "int_who_ht")
                                used_options.append("int_who_ht")
                            else:
                                print("You have already selected this option!")
                        case 154: 
                            if "int_who_info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_who_info"] = df.data_extraction.retrieve_info(intervention_delivery_output, "int_who_info")
                                used_options.append("int_who_info")
                            else:
                                print("You have already selected this option!")
                        case 155: 
                            if "int_dur_ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_dur_ht"] = df.data_extraction.retrieve_ht(int_dur_output, "int_dur_ht")
                                used_options.append("int_dur_ht")
                            else:
                                print("You have already selected this option!")
                        case 156: 
                            if "int_dur_info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_dur_info"] = df.data_extraction.retrieve_info(int_dur_output, "int_dur_info")
                                used_options.append("int_dur_info")
                            else:
                                print("You have already selected this option!")
                        case 157: 
                            if "int_leng_ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_leng_ht"] = df.data_extraction.retrieve_ht(intervention_session_length_output, "int_leng_ht")
                                used_options.append("int_leng_ht")
                            else:
                                print("You have already selected this option!")
                        case 158: 
                            if "int_leng_info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_leng_info"] = df.data_extraction.retrieve_info(intervention_session_length_output, "int_leng_info")
                                used_options.append("int_leng_info")
                            else:
                                print("You have already selected this option!")
                        case 159: 
                            if "int_setting_raw" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_setting_raw"] = df.data_extraction.retrieve_info(edu_setting_output, "int_setting_raw")
                                used_options.append("int_setting_raw")
                            else:
                                print("You have already selected this option!")
                        case 160: 
                            if "int_setting_ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_setting_ht"] = df.data_extraction.retrieve_ht(edu_setting_output, "int_setting_ht")
                                used_options.append("int_setting_ht")
                            else:
                                print("You have already selected this option!")
                        case 161: 
                            if "int_setting_info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_setting_info"] = df.data_extraction.retrieve_info(edu_setting_output, "int_setting_info")
                                used_options.append("int_setting_info")
                            else:
                                print("You have already selected this option!")
                        case 162: 
                            if "int_part_raw" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_part_raw"] = df.data_extraction.retrieve_info(int_focus_output, "int_part_raw")
                                used_options.append("int_part_raw")
                            else:
                                print("You have already selected this option!")
                        case 163: 
                            if "int_part_ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_part_ht"] = df.data_extraction.retrieve_info(int_focus_output, "int_part_ht")
                                used_options.append("int_part_ht")
                            else:
                                print("You have already selected this option!")
                        case 164: 
                            if "int_part_info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_part_info"] = df.data_extraction.retrieve_info(int_focus_output, "int_part_info")
                                used_options.append("int_part_info")
                            else:
                                print("You have already selected this option!")
                        case 165: 
                            if "int_fidel_raw" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_fidel_raw"] = df.data_extraction.retrieve_data(int_impl_details, "int_fidel_raw")
                                used_options.append("int_fidel_raw")
                            else:
                                print("You have already selected this option!")
                        case 166: 
                            if "int_fidel_ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_fidel_ht"] = df.data_extraction.retrieve_ht(int_impl_details, "int_fidel_ht")
                                used_options.append("int_fidel_ht")
                            else:
                                print("You have already selected this option!")
                        case 167: 
                            if "int_fidel_info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_fidel_info"] = df.data_extraction.retrieve_info(int_impl_details, "int_fidel_info")
                                used_options.append("int_fidel_info")
                            else:
                                print("You have already selected this option!")
                        case 168: 
                            if "int_cost_raw" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_cost_raw"] = df.data_extraction.retrieve_data(int_costs_reported, "int_cost_raw")
                                used_options.append("int_cost_raw")
                            else:
                                print("You have already selected this option!")
                        case 169: 
                            if "int_cost_ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_cost_ht"] = df.data_extraction.retrieve_ht(int_costs_reported, "int_cost_ht")
                                used_options.append("int_cost_ht")
                            else:
                                print("You have already selected this option!")
                        case 170: 
                            if "int_cost_info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["int_cost_info"] = df.data_extraction.retrieve_info(int_costs_reported, "int_cost_info")
                                used_options.append("int_cost_info")
                            else:
                                print("You have already selected this option!")
                        case 171: 
                            if "base_diff_raw" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["base_diff_raw"] = df.data_extraction.retrieve_data(baseline_diff_output, "base_diff_raw")
                                used_options.append("base_diff_raw")
                            else:
                                print("You have already selected this option!")
                        case 172: 
                            if "base_diff_ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["base_diff_ht"] = df.data_extraction.retrieve_ht(baseline_diff_output, "base_diff_ht")
                                used_options.append("base_diff_ht")
                            else:
                                print("You have already selected this option!")
                        case 173: 
                            if "base_diff_info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["base_diff_info"] = df.data_extraction.retrieve_info(baseline_diff_output, "base_diff_info")
                                used_options.append("base_diff_info")
                            else:
                                print("You have already selected this option!")
                        case 174: 
                            if "comp_anal_raw" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["comp_anal_raw"] = df.data_extraction.retrieve_data(comparability_output, "comp_anal_raw")
                                used_options.append("comp_anal_raw")
                            else:
                                print("You have already selected this option!")
                        case 175: 
                            if "comp_anal_ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["comp_anal_ht"] = df.data_extraction.retrieve_ht(comparability_output, "comp_anal_ht")
                                used_options.append("comp_anal_ht")
                            else:
                                print("You have already selected this option!")
                        case 176: 
                            if "comp_anal_info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["comp_anal_info"] = df.data_extraction.retrieve_info(comparability_output, "comp_anal_info")
                                used_options.append("comp_anal_info")
                            else:
                                print("You have already selected this option!")
                        case 177: 
                            if "comp_var__raw" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["comp_var__raw"] = df.data_extraction.retrieve_data(comp_vars_rep, "comp_var__raw")
                                used_options.append("comp_var__raw")
                            else:
                                print("You have already selected this option!")
                        case 178: 
                            if "comp_var__ht" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["comp_var__ht"] = df.data_extraction.retrieve_ht(comp_vars_rep, "comp_var__ht")
                                used_options.append("comp_var__ht")
                            else:
                                print("You have already selected this option!")
                        case 179: 
                            if "comp_var__info" not in used_options:
                                row_styles4[num - 131] = highlight_style
                                all_df["comp_var__info"] = df.data_extraction.retrieve_info(comp_vars_rep, "comp_var__info")
                                used_options.append("comp_var__info")
                            else:
                                print("You have already selected this option!")
                        case 180: 
                            if "comp_var_rep_raw" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["comp_var_rep_raw"] = df.data_extraction.retrieve_data(which_comp_vars_rep_output, "comp_var_rep_raw")
                                used_options.append("comp_var_rep_raw")
                            else:
                                print("You have already selected this option!")
                        case 181: 
                            if "comp_var_rep_ht" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["comp_var_rep_ht"] = df.data_extraction.retrieve_ht(which_comp_vars_rep_output, "comp_var_rep_ht")
                                used_options.append("comp_var_rep_ht")
                            else:
                                print("You have already selected this option!")
                        case 182: 
                            if "comp_var_rep_info" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["comp_var_rep_info"] = df.data_extraction.retrieve_info(which_comp_vars_rep_output, "comp_var_rep_info")
                                used_options.append("comp_var_rep_info")
                            else:
                                print("You have already selected this option!")
                        # CLUSTERING
                        case 183: 
                            if "clust_anal_raw" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["clust_anal_raw"] = df.data_extraction.retrieve_data(clustering_output, "clust_anal_raw")
                                used_options.append("clust_anal_raw")
                            else:
                                print("You have already selected this option!")
                        case 184: 
                            if "clust_anal_ht" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["clust_anal_ht"] = df.data_extraction.retrieve_ht(clustering_output, "clust_anal_ht")
                                used_options.append("clust_anal_ht")
                            else:
                                print("You have already selected this option!")
                        case 185: 
                            if "clust_anal_info" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["clust_anal_info"] = df.data_extraction.retrieve_info(clustering_output, "clust_anal_info")
                                used_options.append("clust_anal_info")
                            else:
                                print("You have already selected this option!")
                        # STUDENT GENDER
                        case 186: 
                            if "part_gen_raw" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["part_gen_raw"] = df.data_extraction.retrieve_data(student_gender, "part_gen_raw")
                                used_options.append("part_gen_raw")
                            else:
                                print("You have already selected this option!")
                        case 187: 
                            if "part_gen_ht" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["part_gen_ht"] = df.data_extraction.retrieve_ht(student_gender, "part_gen_ht")
                                used_options.append("part_gen_ht")
                            else:
                                print("You have already selected this option!")
                        case 188: 
                            if "part_gen_info" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["part_gen_info"] = df.data_extraction.retrieve_info(student_gender, "part_gen_info")
                                used_options.append("part_gen_info")
                            else:
                                print("You have already selected this option!")
                        # SAMPLE SIZE
                        case 189: 
                            if "sample_analysed_ht" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["sample_analysed_ht"] = df.data_extraction.retrieve_ht(sample_size_output, "sample_analysed_ht")
                                used_options.append("sample_analysed_ht")
                            else:
                                print("You have already selected this option!")
                        case 190: 
                            if "sample_analysed_info" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["sample_analysed_info"] = df.data_extraction.retrieve_info(sample_size_output, "sample_analysed_info")
                                used_options.append("sample_analysed_info")
                            else:
                                print("You have already selected this option!")
                        # INTERVENTION SAMPLE SIZE
                        case 191: 
                            if "base_n_treat_ht" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["base_n_treat_ht"] = df.data_extraction.retrieve_ht(sample_size_intervention_output, "base_n_treat_ht")
                                used_options.append("base_n_treat_ht")
                            else:
                                print("You have already selected this option!")
                        case 192: 
                            if "base_n_treat_info" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["base_n_treat_info"] = df.data_extraction.retrieve_info(sample_size_intervention_output, "base_n_treat_info")
                                used_options.append("base_n_treat_info")
                            else:
                                print("You have already selected this option!")
                        # CONTROL SAMPLE SIZE
                        case 193: 
                            if "base_n_cont_ht" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["base_n_cont_ht"] = df.data_extraction.retrieve_ht(sample_size_control_output, "base_n_cont_ht")
                                used_options.append("base_n_cont_ht")
                            else:
                                print("You have already selected this option!")
                        case 194: 
                            if "base_n_cont_info" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["base_n_cont_info"] = df.data_extraction.retrieve_info(sample_size_control_output, "base_n_cont_info")
                                used_options.append("base_n_cont_info")
                            else:
                                print("You have already selected this option!")
                        # INTERVENTION 2 SAMPLE SIZE
                        case 195: 
                            if "base_n_treat2_ht" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["base_n_treat2_ht"] = df.data_extraction.retrieve_ht(sample_size_second_intervention_output, "base_n_treat2_ht")
                                used_options.append("base_n_treat2_ht")
                            else:
                                print("You have already selected this option!")
                        case 196: 
                            if "base_n_treat2_info" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["base_n_treat2_info"] = df.data_extraction.retrieve_info(sample_size_second_intervention_output, "base_n_treat2_info")
                                used_options.append("base_n_treat2_info")
                            else:
                                print("You have already selected this option!")
                        # INTERVENTION 3 SAMPLE SIZE
                        case 197: 
                            if "base_n_treat3_ht" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["base_n_treat3_ht"] = df.data_extraction.retrieve_ht(sample_size_third_intervention_output, "base_n_treat3_ht")
                                used_options.append("base_n_treat3_ht")
                            else:
                                print("You have already selected this option!")
                        case 198: 
                            if "base_n_treat3_info" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["base_n_treat3_info"] = df.data_extraction.retrieve_info(sample_size_third_intervention_output, "base_n_treat3_info")
                                used_options.append("base_n_treat3_info")
                            else:
                                print("You have already selected this option!") 
                        # INTERVENTION SAMPLE SIZE ANALYSED
                        case 199: 
                            if "n_treat_ht" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["n_treat_ht"] = df.data_extraction.retrieve_ht(samp_size_anal_int_output, "n_treat_ht")
                                used_options.append("n_treat_ht")
                            else:
                                print("You have already selected this option!")
                        case 200: 
                            if "n_treat_info" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["n_treat_info"] = df.data_extraction.retrieve_info(samp_size_anal_int_output, "n_treat_info")
                                used_options.append("n_treat_info")
                            else:
                                print("You have already selected this option!") 
                        # CONTROL SAMPLE SIZE ANALYSED
                        case 201: 
                            if "n_cont_ht" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["n_cont_ht"] = df.data_extraction.retrieve_ht(samp_size_anal_cont_output, "n_cont_ht")
                                used_options.append("n_cont_ht")
                            else:
                                print("You have already selected this option!")
                        case 202: 
                            if "n_cont_info" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["n_cont_info"] = df.data_extraction.retrieve_info(samp_size_anal_cont_output, "n_cont_info")
                                used_options.append("n_cont_info")
                            else:
                                print("You have already selected this option!") 
                        # INTERVENTION 2 SAMPLE SIZE ANALYSED
                        case 203: 
                            if "n_treat2_ht" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["n_treat2_ht"] = df.data_extraction.retrieve_ht(samp_size_anal_sec_int_output, "n_treat2_ht")
                                used_options.append("n_treat2_ht")
                            else:
                                print("You have already selected this option!")
                        case 204: 
                            if "n_treat2_info" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["n_treat2_info"] = df.data_extraction.retrieve_info(samp_size_anal_sec_int_output, "n_treat2_info")
                                used_options.append("n_treat2_info")
                            else:
                                print("You have already selected this option!") 
                        # CONTROL 2 SAMPLE SIZE ANALYSED
                        case 205: 
                            if "n_cont2_ht" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["n_cont2_ht"] = df.data_extraction.retrieve_ht(samp_size_anal_sec_cont_output, "n_cont2_ht")
                                used_options.append("n_cont2_ht")
                            else:
                                print("You have already selected this option!")
                        case 206: 
                            if "n_cont2_info" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["n_cont2_info"] = df.data_extraction.retrieve_info(samp_size_anal_sec_cont_output, "n_cont2_info")
                                used_options.append("n_cont2_info")
                            else:
                                print("You have already selected this option!") 
                        # ATTRITION REPORTED
                        case 207: 
                            if "attri_raw" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["attri_raw"] = df.data_extraction.retrieve_data(attr_dropout_rep_output, "attri_raw")
                                used_options.append("attri_raw")
                            else:
                                print("You have already selected this option!")
                        case 208: 
                            if "attri_ht" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["attri_ht"] = df.data_extraction.retrieve_ht(attr_dropout_rep_output, "attri_ht")
                                used_options.append("attri_ht")
                            else:
                                print("You have already selected this option!")
                        case 209: 
                            if "attri_info" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["attri_info"] = df.data_extraction.retrieve_info(attr_dropout_rep_output, "attri_info")
                                used_options.append("attri_info")
                            else:
                                print("You have already selected this option!")
                        # ATTRITION TREATMENT GROUP
                        case 210: 
                            if "attri_treat_ht" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["attri_treat_ht"] = df.data_extraction.retrieve_ht(treat_grp_attr, "attri_treat_ht")
                                used_options.append("attri_treat_ht")
                            else:
                                print("You have already selected this option!")
                        case 211: 
                            if "attri_treat_info" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["attri_treat_info"] = df.data_extraction.retrieve_info(treat_grp_attr, "attri_treat_info")
                                used_options.append("attri_treat_info")
                            else:
                                print("You have already selected this option!") 
                        # TOTAL % ATTRITION
                        case 212: 
                            if "attri_perc_ht" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["attri_perc_ht"] = df.data_extraction.retrieve_ht(overall_perc_attr, "attri_perc_ht")
                                used_options.append("attri_perc_ht")
                            else:
                                print("You have already selected this option!")
                        case 213: 
                            if "attri_perc_info" not in used_options:
                                row_styles5[num - 180] = highlight_style
                                all_df["attri_perc_info"] = df.data_extraction.retrieve_info(overall_perc_attr, "attri_perc_info")
                                used_options.append("attri_perc_info")
                            else:
                                print("You have already selected this option!") 
                        case 214:
                            console.print("Compiling..")

                            row_styles5[num - 180] = highlight_style
                                
                            all_df["id"] = df.data_extraction.retrieve_metadata("ItemId", "id")
                            all_df["pub_author"] = df.data_extraction.retrieve_metadata("ShortTitle", "pub_author")
                            all_df["pub_year"] = df.data_extraction.retrieve_metadata("Year", "pub_year")
                            all_df["abstract"] = df.data_extraction.retrieve_metadata("Abstract", "abstract")
                            all_df["strand_raw"] = df.data_extraction.retrieve_data(admin_strand_output, "strand_raw")
                            all_df["loc_country_raw"] = df.data_extraction.retrieve_data(countries, "loc_country_raw")
                            all_df["pub_eppi"] = df.data_extraction.retrieve_metadata("TypeName", "pub_eppi")
                            all_df["pub_type_raw"] = df.data_extraction.retrieve_data(publication_type_output, "pub_type_raw")
                            all_df["part_age_raw"] = df.data_extraction.retrieve_data(student_age_output, "part_age_raw")
                            all_df["eco_valid_raw"] = df.data_extraction.retrieve_data(study_realism_output, "eco_valid_raw")
                            
                            #/*************************/#
                            #/     NUMBER OF SCHOOLS   /#
                            #/*************************/#
        
                            all_df["school_treat_info"] = df.data_extraction.retrieve_info(number_of_schools_intervention_output, "school_treat_info")
                            all_df["school_treat_ht"] = df.data_extraction.retrieve_ht(number_of_schools_intervention_output, "school_treat_ht")
                            all_df["school_cont_info"] = df.data_extraction.retrieve_info(number_of_schools_control_output, "school_cont_info")
                            all_df["school_cont_ht"] = df.data_extraction.retrieve_ht(number_of_schools_control_output, "school_cont_ht")
                            all_df["school_total_info"] = df.data_extraction.retrieve_info(number_of_schools_total_output, "school_total_info")
                            all_df["school_total_ht"] = df.data_extraction.retrieve_ht(number_of_schools_total_output, "school_total_ht")
                            
                            
                            #/*************************/#
                            #/    NUMBER OF CLASSES    /#
                            #/*************************/#
                            
                            all_df["class_treat_info"] = df.data_extraction.retrieve_info(num_of_class_int_output, "class_treat_info")
                            all_df["class_treat_ht"] = df.data_extraction.retrieve_ht(num_of_class_int_output, "class_treat_ht")
                            all_df["class_cont_info"] = df.data_extraction.retrieve_info(num_of_class_cont_output, "class_cont_info")
                            all_df["class_cont_ht"] = df.data_extraction.retrieve_ht(num_of_class_cont_output, "class_cont_ht")
                            all_df["class_total_info"] = df.data_extraction.retrieve_info(num_of_class_tot_output, "class_total_info")
                            all_df["class_total_ht"] = df.data_extraction.retrieve_ht(num_of_class_tot_output, "class_total_ht")
                            
                            #/****************************/#
                            #/   PARTICIPANT ASSIGNMENT   /#
                            #/****************************/#
                            
                            all_df["part_assig_raw"] = df.data_extraction.retrieve_data(part_assign_output, "part_assig_raw")
                            all_df["part_assig_ht"] = df.data_extraction.retrieve_ht(part_assign_output, "part_assig_ht")
                            all_df["part_assig_info"] = df.data_extraction.retrieve_info(part_assign_output, "part_assig_info")
                        
                            #/*************************/#
                            #/   LEVEL OF ASSIGNMENT   /#
                            #/*************************/#
                            
                            all_df["level_assig_raw"] = df.data_extraction.retrieve_data(level_of_assignment_output, "level_assig_raw")
                            all_df["level_assig_ht"] = df.data_extraction.retrieve_ht(level_of_assignment_output, "level_assig_ht")
                            all_df["level_assig_info"] = df.data_extraction.retrieve_info(level_of_assignment_output, "level_assig_info")
                            
                            #/**********************/#
                            #/     STUDY DESIGN     /#
                            #/**********************/#
                            
                            all_df["int_design_raw"] = df.data_extraction.retrieve_data(study_design_output, "int_desig_raw")
                            all_df["int_design_ht"] = df.data_extraction.retrieve_ht(study_design_output, "int_design_ht")
                            all_df["int_design_info"] = df.data_extraction.retrieve_info(study_design_output, "int_design_info")

                            #/**********************/#
                            #/     RANDOMISATION    /#
                            #/**********************/#
                    
                            all_df["rand_raw"] = df.data_extraction.retrieve_data(randomisation_details, "rand_raw")
                            all_df["rand_ht"] = df.data_extraction.retrieve_ht(randomisation_details, "rand_ht")
                            all_df["rand_info"] = df.data_extraction.retrieve_info(randomisation_details, "rand_info")

                            #/*************************/#
                            #/ TOOLKIT PRIMARY OUTCOME /#
                            #/*************************/#

                            df_outcomes = DataFrameCompilation(json_extractor)
                            df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)

                            all_df["out_tit_tool"] = df_out.out_tit_tool
                            all_df["out_desc_tool"] = df_out.out_desc_tool
                            all_df["out_type_tool"] = df_out.out_type_tool
                            all_df["out_smd_tool"] = df_out.smd_tool
                            all_df["out_se_tool"] = df_out.se_tool
                            all_df["out_ci_lower_tool"] = df_out.ci_lower_tool
                            all_df["out_ci_upper_tool"] = df_out.ci_upper_tool
                            all_df["out_measure_tool"] = df_out.out_measure_tool
                            all_df["out_g1_n_tool"] = df_out.out_g1_n_tool
                            all_df["out_g1_mean_tool"] = df_out.out_g1_mean_tool
                            all_df["out_g1_sd_tool"] = df_out.out_g1_sd_tool
                            all_df["out_g2_n_tool"] = df_out.out_g2_n_tool
                            all_df["out_g2_mean_tool"] = df_out.out_g2_mean_tool
                            all_df["out_g2_sd_tool"] = df_out.out_g2_sd_tool
                            all_df["out_test_type_raw_tool"] = df_out.out_test_type_raw_tool
                            all_df["out_es_type_tool"] = df_out.out_es_type_tool

                            #/*************************/#
                            #/     READING OUTCOME     /#
                            #/*************************/#

                            all_df["out_tit_red"] = df_out.out_tit_red
                            all_df["out_desc_red"] = df_out.out_desc_red
                            all_df["out_type_red"] = df_out.out_type_red
                            all_df["out_smd_red"] = df_out.smd_red
                            all_df["out_se_red"] = df_out.se_red
                            all_df["out_ci_lower_red"] = df_out.ci_lower_red
                            all_df["out_ci_upper_red"] = df_out.ci_upper_red
                            all_df["out_measure_red"] = df_out.out_measure_red
                            all_df["out_g1_n_red"] = df_out.out_g1_n_red
                            all_df["out_g1_mean_red"] = df_out.out_g1_mean_red
                            all_df["out_g1_sd_red"] = df_out.out_g1_sd_red
                            all_df["out_g2_n_red"] = df_out.out_g2_n_red
                            all_df["out_g2_mean_red"] = df_out.out_g2_mean_red
                            all_df["out_g2_sd_red"] = df_out.out_g2_sd_red
                            all_df["out_test_type_raw_red"] = df_out.out_test_type_raw_red
                            all_df["out_es_type_red"] = df_out.out_es_type_red

                            #/*************************/#
                            #/     WRITING OUTCOME     /#
                            #/*************************/#

                            all_df["out_tit_wri"] = df_out.out_tit_wri
                            all_df["out_desc_wri"] = df_out.out_desc_wri
                            all_df["out_type_wri"] = df_out.out_type_wri
                            all_df["out_smd_wri"] = df_out.smd_wri
                            all_df["out_se_wri"] = df_out.se_wri
                            all_df["out_ci_lower_wri"] = df_out.ci_lower_wri
                            all_df["out_ci_upper_wri"] = df_out.ci_upper_wri
                            all_df["out_measure_wri"] = df_out.out_measure_wri
                            all_df["out_g1_n_wri"] = df_out.out_g1_n_wri
                            all_df["out_g1_mean_wri"] = df_out.out_g1_mean_wri
                            all_df["out_g1_sd_wri"] = df_out.out_g1_sd_wri
                            all_df["out_g2_n_wri"] = df_out.out_g2_n_wri
                            all_df["out_g2_mean_wri"] = df_out.out_g2_mean_wri
                            all_df["out_g2_sd_wri"] = df_out.out_g2_sd_wri
                            all_df["out_test_type_raw_wri"] = df_out.out_test_type_raw_wri
                            all_df["out_es_type_wri"] = df_out.out_es_type_wri

                            #/*************************/#
                            #/        MATH OUTCOME     /#
                            #/*************************/#

                            all_df["out_tit_math"] = df_out.out_tit_math
                            all_df["out_desc_math"] = df_out.out_desc_math
                            all_df["out_type_math"] = df_out.out_type_math
                            all_df["out_smd_math"] = df_out.smd_math
                            all_df["out_se_math"] = df_out.se_math
                            all_df["out_ci_lower_math"] = df_out.ci_lower_math
                            all_df["out_ci_upper_math"] = df_out.ci_upper_math
                            all_df["out_measure_math"] = df_out.out_measure_math
                            all_df["out_g1_n_math"] = df_out.out_g1_n_math
                            all_df["out_g1_mean_math"] = df_out.out_g1_mean_math
                            all_df["out_g1_sd_math"] = df_out.out_g1_sd_math
                            all_df["out_g2_n_math"] = df_out.out_g2_n_math
                            all_df["out_g2_mean_math"] = df_out.out_g2_mean_math
                            all_df["out_g2_sd_math"] = df_out.out_g2_sd_math
                            all_df["out_test_type_raw_math"] = df_out.out_test_type_raw_math
                            all_df["out_es_type_math"] = df_out.out_es_type_math

                            #/*************************/#
                            #/     SCIENCE OUTCOME     /#
                            #/*************************/#

                            all_df["out_tit_sci"] = df_out.out_tit_sci
                            all_df["out_desc_sci"] = df_out.out_desc_sci
                            all_df["out_type_sci"] = df_out.out_type_sci
                            all_df["out_smd_sci"] = df_out.smd_sci
                            all_df["out_se_sci"] = df_out.se_sci
                            all_df["out_ci_lower_sci"] = df_out.ci_lower_sci
                            all_df["out_ci_upper_sci"] = df_out.ci_upper_sci
                            all_df["out_measure_sci"] = df_out.out_measure_sci
                            all_df["out_g1_n_sci"] = df_out.out_g1_n_sci
                            all_df["out_g1_mean_sci"] = df_out.out_g1_mean_sci
                            all_df["out_g1_sd_sci"] = df_out.out_g1_sd_sci
                            all_df["out_g2_n_sci"] = df_out.out_g2_n_sci
                            all_df["out_g2_mean_sci"] = df_out.out_g2_mean_sci
                            all_df["out_g2_sd_sci"] = df_out.out_g2_sd_sci
                            all_df["out_test_type_raw_sci"] = df_out.out_test_type_raw_sci
                            all_df["out_es_type_sci"] = df_out.out_es_type_sci

                            #/*************************/#
                            #/        FSM OUTCOME      /#
                            #/*************************/#

                            all_df["out_tit_fsm"] = df_out.out_tit_fsm
                            all_df["out_desc_fsm"] = df_out.out_desc_fsm
                            all_df["out_type_fsm"] = df_out.out_type_fsm
                            all_df["out_smd_fsm"] = df_out.smd_fsm
                            all_df["out_se_fsm"] = df_out.se_fsm
                            all_df["out_ci_lower_fsm"] = df_out.ci_lower_fsm
                            all_df["out_ci_upper_fsm"] = df_out.ci_upper_fsm
                            all_df["out_measure_fsm"] = df_out.out_measure_fsm
                            all_df["out_g1_n_fsm"] = df_out.out_g1_n_fsm
                            all_df["out_g1_mean_fsm"] = df_out.out_g1_mean_fsm
                            all_df["out_g1_sd_fsm"] = df_out.out_g1_sd_fsm
                            all_df["out_g2_n_fsm"] = df_out.out_g2_n_fsm
                            all_df["out_g2_mean_fsm"] = df_out.out_g2_mean_fsm
                            all_df["out_g2_sd_fsm"] = df_out.out_g2_sd_fsm
                            all_df["out_test_type_raw_fsm"] = df_out.out_test_type_raw_fsm
                            all_df["out_es_type_fsm"] = df_out.out_es_type_fsm

                            #/*****************************/#
                            #/     INTERVENTION DETAILS    /#
                            #/*****************************/#
                            
                            all_df["intervention_name_ht"] = df.data_extraction.retrieve_ht(int_name_output, "intervention_name_ht")
                            all_df["int_name_info"] = df.data_extraction.retrieve_info(int_name_output, "int_name_info")

                            all_df["intervention_desc_ht"] = df.data_extraction.retrieve_ht(intervention_description_output, "intervention_desc_ht")
                            all_df["intervention_desc_info"] = df.data_extraction.retrieve_info(intervention_description_output, "intervention_desc_info")

                            all_df["intervention_objec_ht"] = df.data_extraction.retrieve_ht(intervention_objectives_output, "intervention_objec_ht")
                            all_df["intervention_objec_info"] = df.data_extraction.retrieve_info(intervention_objectives_output, "intervention_objec_info")

                            all_df["int_training_raw"] = df.data_extraction.retrieve_data(int_training_provided_output, "int_training_raw")
                            all_df["int_training_ht"] = df.data_extraction.retrieve_ht(int_training_provided_output, "int_training_ht")
                            all_df["int_training_info"] = df.data_extraction.retrieve_info(int_training_provided_output, "int_training_info")

                            all_df["int_approach_raw"] = df.data_extraction.retrieve_data(intervention_teaching_approach, "int_approach_raw")
                            all_df["int_approach_ht"] = df.data_extraction.retrieve_ht(intervention_teaching_approach, "int_approach_ht")
                            all_df["int_approach_info"] = df.data_extraction.retrieve_info(intervention_teaching_approach, "int_approach_info")

                            all_df["digit_tech_raw"] = df.data_extraction.retrieve_data(int_appr_dig_tech, "digit_tech_raw")
                            all_df["digit_tech_ht"] = df.data_extraction.retrieve_ht(int_appr_dig_tech, "digit_tech_ht")
                            all_df["digit_tech_info"] = df.data_extraction.retrieve_info(int_appr_dig_tech, "digit_tech_info")

                            all_df["parent_partic_raw"] = df.data_extraction.retrieve_data(int_appr_par_or_comm_vol, "parent_partic_raw")
                            all_df["parent_partic_ht"] = df.data_extraction.retrieve_ht(int_appr_par_or_comm_vol, "parent_partic_ht")
                            all_df["parent_partic_info"] = df.data_extraction.retrieve_info(int_appr_par_or_comm_vol, "parent_partic_info")

                            all_df["int_when_raw"] = df.data_extraction.retrieve_data(intervention_time_output, "int_when_raw")
                            all_df["int_when_ht"] = df.data_extraction.retrieve_ht(intervention_time_output, "int_when_ht")
                            all_df["int_when_info"] = df.data_extraction.retrieve_info(intervention_time_output, "int_when_info")

                            all_df["int_who_raw"] = df.data_extraction.retrieve_data(intervention_delivery_output, "int_who_raw")
                            all_df["int_who_ht"] = df.data_extraction.retrieve_ht(intervention_delivery_output, "int_who_ht")
                            all_df["int_who_info"] = df.data_extraction.retrieve_info(intervention_delivery_output, "int_who_info")

                            all_df["int_dur_ht"] = df.data_extraction.retrieve_ht(int_dur_output, "int_dur_ht")
                            all_df["int_dur_info"] = df.data_extraction.retrieve_info(int_dur_output, "int_dur_info")

                            all_df["int_leng_ht"] = df.data_extraction.retrieve_ht(intervention_session_length_output, "int_leng_ht")
                            all_df["int_leng_info"] = df.data_extraction.retrieve_info(intervention_session_length_output, "int_leng_info")

                            all_df["int_setting_raw"] = df.data_extraction.retrieve_info(edu_setting_output, "int_setting_raw")
                            all_df["int_setting_ht"] = df.data_extraction.retrieve_ht(edu_setting_output, "int_setting_ht")
                            all_df["int_setting_info"] = df.data_extraction.retrieve_info(edu_setting_output, "int_setting_info")

                            all_df["int_part_raw"] = df.data_extraction.retrieve_info(int_focus_output, "int_part_raw")
                            all_df["int_part_ht"] = df.data_extraction.retrieve_info(int_focus_output, "int_part_ht")
                            all_df["int_part_info"] = df.data_extraction.retrieve_info(int_focus_output, "int_part_info")

                            all_df["int_fidel_raw"] = df.data_extraction.retrieve_data(int_impl_details, "int_fidel_raw")
                            all_df["int_fidel_ht"] = df.data_extraction.retrieve_ht(int_impl_details, "int_fidel_ht")
                            all_df["int_fidel_info"] = df.data_extraction.retrieve_info(int_impl_details, "int_fidel_info")

                            all_df["int_cost_raw"] = df.data_extraction.retrieve_data(int_costs_reported, "int_cost_raw")
                            all_df["int_cost_ht"] = df.data_extraction.retrieve_ht(int_costs_reported, "int_cost_ht")
                            all_df["int_cost_info"] = df.data_extraction.retrieve_info(int_costs_reported, "int_cost_info")

                            all_df["base_diff_raw"] = df.data_extraction.retrieve_data(baseline_diff_output, "base_diff_raw")
                            all_df["base_diff_ht"] = df.data_extraction.retrieve_ht(baseline_diff_output, "base_diff_ht")
                            all_df["base_diff_info"] = df.data_extraction.retrieve_info(baseline_diff_output, "base_diff_info")

                            all_df["comp_anal_raw"] = df.data_extraction.retrieve_data(comparability_output, "comp_anal_raw")
                            all_df["comp_anal_ht"] = df.data_extraction.retrieve_ht(comparability_output, "comp_anal_ht")
                            all_df["comp_anal_info"] = df.data_extraction.retrieve_info(comparability_output, "comp_anal_info")

                            all_df["comp_var__raw"] = df.data_extraction.retrieve_data(comp_vars_rep, "comp_var__raw")
                            all_df["comp_var__ht"] = df.data_extraction.retrieve_ht(comp_vars_rep, "comp_var__ht")
                            all_df["comp_var__info"] = df.data_extraction.retrieve_info(comp_vars_rep, "comp_var__info")

                            all_df["comp_var_rep_raw"] = df.data_extraction.retrieve_data(which_comp_vars_rep_output, "comp_var_rep_raw")
                            all_df["comp_var_rep_ht"] = df.data_extraction.retrieve_ht(which_comp_vars_rep_output, "comp_var_rep_ht")
                            all_df["comp_var_rep_info"] = df.data_extraction.retrieve_info(which_comp_vars_rep_output, "comp_var_rep_info")

                            # CLUSTERING
                            
                            all_df["clust_anal_raw"] = df.data_extraction.retrieve_data(clustering_output, "clust_anal_raw")
                            all_df["clust_anal_ht"] = df.data_extraction.retrieve_ht(clustering_output, "clust_anal_ht")
                            all_df["clust_anal_info"] = df.data_extraction.retrieve_info(clustering_output, "clust_anal_info")
                                                        
                            # STUDENT GENDER
                            
                            all_df["part_gen_raw"] = df.data_extraction.retrieve_data(student_gender, "part_gen_raw")
                            all_df["part_gen_ht"] = df.data_extraction.retrieve_ht(student_gender, "part_gen_ht")
                            all_df["part_gen_info"] = df.data_extraction.retrieve_info(student_gender, "part_gen_info")
                            
                            # SAMPLE SIZE
                            
                            all_df["sample_analysed_ht"] = df.data_extraction.retrieve_ht(sample_size_output, "sample_analysed_ht")
                            all_df["sample_analysed_info"] = df.data_extraction.retrieve_info(sample_size_output, "sample_analysed_info")
                                                    
                            # INTERVENTION SAMPLE SIZE
                            
                            all_df["base_n_treat_ht"] = df.data_extraction.retrieve_ht(sample_size_intervention_output, "base_n_treat_ht")
                            all_df["base_n_treat_info"] = df.data_extraction.retrieve_info(sample_size_intervention_output, "base_n_treat_info")
                        
                            # CONTROL SAMPLE SIZE
                            
                            all_df["base_n_cont_ht"] = df.data_extraction.retrieve_ht(sample_size_control_output, "base_n_cont_ht")
                            all_df["base_n_cont_info"] = df.data_extraction.retrieve_info(sample_size_control_output, "base_n_cont_info")
                        
                            # INTERVENTION 2 SAMPLE SIZE
                            
                            all_df["base_n_treat2_ht"] = df.data_extraction.retrieve_ht(sample_size_second_intervention_output, "base_n_treat2_ht")
                            all_df["base_n_treat2_info"] = df.data_extraction.retrieve_info(sample_size_second_intervention_output, "base_n_treat2_info")
                        
                            # INTERVENTION 3 SAMPLE SIZE
                            
                            all_df["base_n_treat3_ht"] = df.data_extraction.retrieve_ht(sample_size_third_intervention_output, "base_n_treat3_ht")
                            all_df["base_n_treat3_info"] = df.data_extraction.retrieve_info(sample_size_third_intervention_output, "base_n_treat3_info")
                        
                            # INTERVENTION SAMPLE SIZE ANALYSED
                            
                            all_df["n_treat_ht"] = df.data_extraction.retrieve_ht(samp_size_anal_int_output, "n_treat_ht")
                            all_df["n_treat_info"] = df.data_extraction.retrieve_info(samp_size_anal_int_output, "n_treat_info")
                            
                            # CONTROL SAMPLE SIZE ANALYSED
                            
                            all_df["n_cont_ht"] = df.data_extraction.retrieve_ht(samp_size_anal_cont_output, "n_cont_ht")
                            all_df["n_cont_info"] = df.data_extraction.retrieve_info(samp_size_anal_cont_output, "n_cont_info")

                            # INTERVENTION 2 SAMPLE SIZE ANALYSED
                            
                            all_df["n_treat2_ht"] = df.data_extraction.retrieve_ht(samp_size_anal_sec_int_output, "n_treat2_ht")
                            all_df["n_treat2_info"] = df.data_extraction.retrieve_info(samp_size_anal_sec_int_output, "n_treat2_info")
                            
                            # CONTROL 2 SAMPLE SIZE ANALYSED
                            
                            all_df["n_cont2_ht"] = df.data_extraction.retrieve_ht(samp_size_anal_sec_cont_output, "n_cont2_ht")
                            all_df["n_cont2_info"] = df.data_extraction.retrieve_info(samp_size_anal_sec_cont_output, "n_cont2_info")
                            
                            # ATTRITION REPORTED
                            
                            all_df["attri_raw"] = df.data_extraction.retrieve_data(attr_dropout_rep_output, "attri_raw")
                            all_df["attri_ht"] = df.data_extraction.retrieve_ht(attr_dropout_rep_output, "attri_ht")
                            all_df["attri_info"] = df.data_extraction.retrieve_info(attr_dropout_rep_output, "attri_info")
                        
                            # ATTRITION TREATMENT GROUP
                            
                            all_df["attri_treat_ht"] = df.data_extraction.retrieve_ht(treat_grp_attr, "attri_treat_ht")
                            all_df["attri_treat_info"] = df.data_extraction.retrieve_info(treat_grp_attr, "attri_treat_info")
                        
                            # TOTAL % ATTRITION

                            all_df["attri_perc_ht"] = df.data_extraction.retrieve_ht(overall_perc_attr, "attri_perc_ht")
                            all_df["attri_perc_info"] = df.data_extraction.retrieve_info(overall_perc_attr, "attri_perc_info")

                    if not all_df.empty:
                        console = Console()
                        main_table2 = custom_general_vars1()
                        main_table3 = custom_outcome_vars_1()
                        main_table4 = custom_outcome_vars_2()
                        main_table5 = intervention_vars_3()
                        main_table6 = intervention_vars_4()
                        console.clear()

                        panel1 = Panel(main_table2, style=custom_style_main, border_style="#37474f")
                        panel2 = Panel(main_table3, style=custom_style_main, border_style="#37474f")
                        panel3 = Panel(main_table4, style=custom_style_main, border_style="#37474f")
                        panel4 = Panel(main_table5, style=custom_style_main, border_style="#37474f")
                        panel5 = Panel(main_table6, style=custom_style_main, border_style="#37474f")

                        # Combine the panels horizontally
                        columns = Columns([panel1, panel2, panel3, panel4, panel5])

                        # Create a larger panel with white background and black text to house the columns
                        panel = Panel(columns, 
                                      title="Custom Data Selection", 
                                      style=custom_style_outer, 
                                      border_style="#FFFFFF",
                                      width=250)
                        console.clear()
                        # Print the panel
                        console.print(panel)

                if not all_df.empty:
                    import datetime 
                    current_datetime = datetime.datetime.now()
                    console.print("\n[bold]Custom dataframe saved here..[/bold]\n")

                    outfile1 = df.data_extraction.save_dataframe(all_df, f"_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}_Custom.csv", custom_info=True)

                    outfile1=str(outfile1)
                    outfile1=outfile1
                    console.print(outfile1 + "\n")
                else: 
                    console.print("No data selected, thanks for using the EEF Teaching and Learning Toolkit Extractor.")
                
            case 12:

                print("Compiling..")

                all_df = pd.DataFrame()

                df = CustomFrames(json_extractor)

                all_df["id"] = df.data_extraction.retrieve_metadata("ItemId", "id")
                all_df["pub_author"] = df.data_extraction.retrieve_metadata("ShortTitle", "pub_author")
                all_df["pub_year"] = df.data_extraction.retrieve_metadata("Year", "pub_year")
                all_df["abstract"] = df.data_extraction.retrieve_metadata("Abstract", "abstract")
                all_df["strand_raw"] = df.data_extraction.retrieve_data(admin_strand_output, "strand_raw")
                all_df["loc_country_raw"] = df.data_extraction.retrieve_data(countries, "loc_country_raw")
                all_df["pub_eppi"] = df.data_extraction.retrieve_metadata("TypeName", "pub_eppi")
                all_df["pub_type_raw"] = df.data_extraction.retrieve_data(publication_type_output, "pub_type_raw")
                all_df["part_age_raw"] = df.data_extraction.retrieve_data(student_age_output, "part_age_raw")
                all_df["eco_valid_raw"] = df.data_extraction.retrieve_data(study_realism_output, "eco_valid_raw")

                #/*************************/#
                #/     NUMBER OF SCHOOLS   /#
                #/*************************/#
        
                all_df["school_treat_info"] = df.data_extraction.retrieve_info(number_of_schools_intervention_output, "school_treat_info")
                all_df["school_treat_ht"] = df.data_extraction.retrieve_ht(number_of_schools_intervention_output, "school_treat_ht")
                all_df["school_cont_info"] = df.data_extraction.retrieve_info(number_of_schools_control_output, "school_cont_info")
                all_df["school_cont_ht"] = df.data_extraction.retrieve_ht(number_of_schools_control_output, "school_cont_ht")
                all_df["school_total_info"] = df.data_extraction.retrieve_info(number_of_schools_total_output, "school_total_info")
                all_df["school_total_ht"] = df.data_extraction.retrieve_ht(number_of_schools_total_output, "school_total_ht")
                
                
                #/*************************/#
                #/    NUMBER OF CLASSES    /#
                #/*************************/#
                
                all_df["class_treat_info"] = df.data_extraction.retrieve_info(num_of_class_int_output, "class_treat_info")
                all_df["class_treat_ht"] = df.data_extraction.retrieve_ht(num_of_class_int_output, "class_treat_ht")
                all_df["class_cont_info"] = df.data_extraction.retrieve_info(num_of_class_cont_output, "class_cont_info")
                all_df["class_cont_ht"] = df.data_extraction.retrieve_ht(num_of_class_cont_output, "class_cont_ht")
                all_df["class_total_info"] = df.data_extraction.retrieve_info(num_of_class_tot_output, "class_total_info")
                all_df["class_total_ht"] = df.data_extraction.retrieve_ht(num_of_class_tot_output, "class_total_ht")
                
                #/****************************/#
                #/   PARTICIPANT ASSIGNMENT   /#
                #/****************************/#
                
                all_df["part_assig_raw"] = df.data_extraction.retrieve_data(part_assign_output, "part_assig_raw")
                all_df["part_assig_ht"] = df.data_extraction.retrieve_ht(part_assign_output, "part_assig_ht")
                all_df["part_assig_info"] = df.data_extraction.retrieve_info(part_assign_output, "part_assig_info")
            
                #/*************************/#
                #/   LEVEL OF ASSIGNMENT   /#
                #/*************************/#
                
                all_df["level_assig_raw"] = df.data_extraction.retrieve_data(level_of_assignment_output, "level_assig_raw")
                all_df["level_assig_ht"] = df.data_extraction.retrieve_ht(level_of_assignment_output, "level_assig_ht")
                all_df["level_assig_info"] = df.data_extraction.retrieve_info(level_of_assignment_output, "level_assig_info")
                
                #/**********************/#
                #/     STUDY DESIGN     /#
                #/**********************/#
                
                all_df["int_design_raw"] = df.data_extraction.retrieve_data(study_design_output, "int_desig_raw")
                all_df["int_design_ht"] = df.data_extraction.retrieve_ht(study_design_output, "int_design_ht")
                all_df["int_design_info"] = df.data_extraction.retrieve_info(study_design_output, "int_design_info")

                #/**********************/#
                #/     RANDOMISATION    /#
                #/**********************/#
        
                all_df["rand_raw"] = df.data_extraction.retrieve_data(randomisation_details, "rand_raw")
                all_df["rand_ht"] = df.data_extraction.retrieve_ht(randomisation_details, "rand_ht")
                all_df["rand_info"] = df.data_extraction.retrieve_info(randomisation_details, "rand_info")

                #/*************************/#
                #/ TOOLKIT PRIMARY OUTCOME /#
                #/*************************/#

                df_outcomes = DataFrameCompilation(json_extractor)
                df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)

                all_df["out_tit_tool"] = df_out.out_tit_tool
                all_df["out_desc_tool"] = df_out.out_desc_tool
                all_df["out_type_tool"] = df_out.out_type_tool
                all_df["out_smd_tool"] = df_out.smd_tool
                all_df["out_se_tool"] = df_out.se_tool
                all_df["out_ci_lower_tool"] = df_out.ci_lower_tool
                all_df["out_ci_upper_tool"] = df_out.ci_upper_tool
                all_df["out_measure_tool"] = df_out.out_measure_tool
                all_df["out_g1_n_tool"] = df_out.out_g1_n_tool
                all_df["out_g1_mean_tool"] = df_out.out_g1_mean_tool
                all_df["out_g1_sd_tool"] = df_out.out_g1_sd_tool
                all_df["out_g2_n_tool"] = df_out.out_g2_n_tool
                all_df["out_g2_mean_tool"] = df_out.out_g2_mean_tool
                all_df["out_g2_sd_tool"] = df_out.out_g2_sd_tool
                all_df["out_test_type_raw_tool"] = df_out.out_test_type_raw_tool
                all_df["out_es_type_tool"] = df_out.out_es_type_tool

                #/*************************/#
                #/     READING OUTCOME     /#
                #/*************************/#

                all_df["out_tit_red"] = df_out.out_tit_red
                all_df["out_desc_red"] = df_out.out_desc_red
                all_df["out_type_red"] = df_out.out_type_red
                all_df["out_smd_red"] = df_out.smd_red
                all_df["out_se_red"] = df_out.se_red
                all_df["out_ci_lower_red"] = df_out.ci_lower_red
                all_df["out_ci_upper_red"] = df_out.ci_upper_red
                all_df["out_measure_red"] = df_out.out_measure_red
                all_df["out_g1_n_red"] = df_out.out_g1_n_red
                all_df["out_g1_mean_red"] = df_out.out_g1_mean_red
                all_df["out_g1_sd_red"] = df_out.out_g1_sd_red
                all_df["out_g2_n_red"] = df_out.out_g2_n_red
                all_df["out_g2_mean_red"] = df_out.out_g2_mean_red
                all_df["out_g2_sd_red"] = df_out.out_g2_sd_red
                all_df["out_test_type_raw_red"] = df_out.out_test_type_raw_red
                all_df["out_es_type_red"] = df_out.out_es_type_red

                #/*************************/#
                #/     WRITING OUTCOME     /#
                #/*************************/#

                all_df["out_tit_wri"] = df_out.out_tit_wri
                all_df["out_desc_wri"] = df_out.out_desc_wri
                all_df["out_type_wri"] = df_out.out_type_wri
                all_df["out_smd_wri"] = df_out.smd_wri
                all_df["out_se_wri"] = df_out.se_wri
                all_df["out_ci_lower_wri"] = df_out.ci_lower_wri
                all_df["out_ci_upper_wri"] = df_out.ci_upper_wri
                all_df["out_measure_wri"] = df_out.out_measure_wri
                all_df["out_g1_n_wri"] = df_out.out_g1_n_wri
                all_df["out_g1_mean_wri"] = df_out.out_g1_mean_wri
                all_df["out_g1_sd_wri"] = df_out.out_g1_sd_wri
                all_df["out_g2_n_wri"] = df_out.out_g2_n_wri
                all_df["out_g2_mean_wri"] = df_out.out_g2_mean_wri
                all_df["out_g2_sd_wri"] = df_out.out_g2_sd_wri
                all_df["out_test_type_raw_wri"] = df_out.out_test_type_raw_wri
                all_df["out_es_type_wri"] = df_out.out_es_type_wri

                #/*************************/#
                #/        MATH OUTCOME     /#
                #/*************************/#

                all_df["out_tit_math"] = df_out.out_tit_math
                all_df["out_desc_math"] = df_out.out_desc_math
                all_df["out_type_math"] = df_out.out_type_math
                all_df["out_smd_math"] = df_out.smd_math
                all_df["out_se_math"] = df_out.se_math
                all_df["out_ci_lower_math"] = df_out.ci_lower_math
                all_df["out_ci_upper_math"] = df_out.ci_upper_math
                all_df["out_measure_math"] = df_out.out_measure_math
                all_df["out_g1_n_math"] = df_out.out_g1_n_math
                all_df["out_g1_mean_math"] = df_out.out_g1_mean_math
                all_df["out_g1_sd_math"] = df_out.out_g1_sd_math
                all_df["out_g2_n_math"] = df_out.out_g2_n_math
                all_df["out_g2_mean_math"] = df_out.out_g2_mean_math
                all_df["out_g2_sd_math"] = df_out.out_g2_sd_math
                all_df["out_test_type_raw_math"] = df_out.out_test_type_raw_math
                all_df["out_es_type_math"] = df_out.out_es_type_math

                #/*************************/#
                #/     SCIENCE OUTCOME     /#
                #/*************************/#

                all_df["out_tit_sci"] = df_out.out_tit_sci
                all_df["out_desc_sci"] = df_out.out_desc_sci
                all_df["out_type_sci"] = df_out.out_type_sci
                all_df["out_smd_sci"] = df_out.smd_sci
                all_df["out_se_sci"] = df_out.se_sci
                all_df["out_ci_lower_sci"] = df_out.ci_lower_sci
                all_df["out_ci_upper_sci"] = df_out.ci_upper_sci
                all_df["out_measure_sci"] = df_out.out_measure_sci
                all_df["out_g1_n_sci"] = df_out.out_g1_n_sci
                all_df["out_g1_mean_sci"] = df_out.out_g1_mean_sci
                all_df["out_g1_sd_sci"] = df_out.out_g1_sd_sci
                all_df["out_g2_n_sci"] = df_out.out_g2_n_sci
                all_df["out_g2_mean_sci"] = df_out.out_g2_mean_sci
                all_df["out_g2_sd_sci"] = df_out.out_g2_sd_sci
                all_df["out_test_type_raw_sci"] = df_out.out_test_type_raw_sci
                all_df["out_es_type_sci"] = df_out.out_es_type_sci

                #/*************************/#
                #/        FSM OUTCOME      /#
                #/*************************/#

                all_df["out_tit_fsm"] = df_out.out_tit_fsm
                all_df["out_desc_fsm"] = df_out.out_desc_fsm
                all_df["out_type_fsm"] = df_out.out_type_fsm
                all_df["out_smd_fsm"] = df_out.smd_fsm
                all_df["out_se_fsm"] = df_out.se_fsm
                all_df["out_ci_lower_fsm"] = df_out.ci_lower_fsm
                all_df["out_ci_upper_fsm"] = df_out.ci_upper_fsm
                all_df["out_measure_fsm"] = df_out.out_measure_fsm
                all_df["out_g1_n_fsm"] = df_out.out_g1_n_fsm
                all_df["out_g1_mean_fsm"] = df_out.out_g1_mean_fsm
                all_df["out_g1_sd_fsm"] = df_out.out_g1_sd_fsm
                all_df["out_g2_n_fsm"] = df_out.out_g2_n_fsm
                all_df["out_g2_mean_fsm"] = df_out.out_g2_mean_fsm
                all_df["out_g2_sd_fsm"] = df_out.out_g2_sd_fsm
                all_df["out_test_type_raw_fsm"] = df_out.out_test_type_raw_fsm
                all_df["out_es_type_fsm"] = df_out.out_es_type_fsm

                #/*****************************/#
                #/     INTERVENTION DETAILS    /#
                #/*****************************/#
                
                all_df["intervention_name_ht"] = df.data_extraction.retrieve_ht(int_name_output, "intervention_name_ht")
                all_df["int_name_info"] = df.data_extraction.retrieve_info(int_name_output, "int_name_info")

                all_df["intervention_desc_ht"] = df.data_extraction.retrieve_ht(intervention_description_output, "intervention_desc_ht")
                all_df["intervention_desc_info"] = df.data_extraction.retrieve_info(intervention_description_output, "intervention_desc_info")

                all_df["intervention_objec_ht"] = df.data_extraction.retrieve_ht(intervention_objectives_output, "intervention_objec_ht")
                all_df["intervention_objec_info"] = df.data_extraction.retrieve_info(intervention_objectives_output, "intervention_objec_info")

                all_df["int_training_raw"] = df.data_extraction.retrieve_data(int_training_provided_output, "int_training_raw")
                all_df["int_training_ht"] = df.data_extraction.retrieve_ht(int_training_provided_output, "int_training_ht")
                all_df["int_training_info"] = df.data_extraction.retrieve_info(int_training_provided_output, "int_training_info")

                all_df["int_approach_raw"] = df.data_extraction.retrieve_data(intervention_teaching_approach, "int_approach_raw")
                all_df["int_approach_ht"] = df.data_extraction.retrieve_ht(intervention_teaching_approach, "int_approach_ht")
                all_df["int_approach_info"] = df.data_extraction.retrieve_info(intervention_teaching_approach, "int_approach_info")

                all_df["digit_tech_raw"] = df.data_extraction.retrieve_data(int_appr_dig_tech, "digit_tech_raw")
                all_df["digit_tech_ht"] = df.data_extraction.retrieve_ht(int_appr_dig_tech, "digit_tech_ht")
                all_df["digit_tech_info"] = df.data_extraction.retrieve_info(int_appr_dig_tech, "digit_tech_info")

                all_df["parent_partic_raw"] = df.data_extraction.retrieve_data(int_appr_par_or_comm_vol, "parent_partic_raw")
                all_df["parent_partic_ht"] = df.data_extraction.retrieve_ht(int_appr_par_or_comm_vol, "parent_partic_ht")
                all_df["parent_partic_info"] = df.data_extraction.retrieve_info(int_appr_par_or_comm_vol, "parent_partic_info")

                all_df["int_when_raw"] = df.data_extraction.retrieve_data(intervention_time_output, "int_when_raw")
                all_df["int_when_ht"] = df.data_extraction.retrieve_ht(intervention_time_output, "int_when_ht")
                all_df["int_when_info"] = df.data_extraction.retrieve_info(intervention_time_output, "int_when_info")

                all_df["int_who_raw"] = df.data_extraction.retrieve_data(intervention_delivery_output, "int_who_raw")
                all_df["int_who_ht"] = df.data_extraction.retrieve_ht(intervention_delivery_output, "int_who_ht")
                all_df["int_who_info"] = df.data_extraction.retrieve_info(intervention_delivery_output, "int_who_info")

                all_df["int_dur_ht"] = df.data_extraction.retrieve_ht(int_dur_output, "int_dur_ht")
                all_df["int_dur_info"] = df.data_extraction.retrieve_info(int_dur_output, "int_dur_info")

                all_df["int_leng_ht"] = df.data_extraction.retrieve_ht(intervention_session_length_output, "int_leng_ht")
                all_df["int_leng_info"] = df.data_extraction.retrieve_info(intervention_session_length_output, "int_leng_info")

                all_df["int_setting_raw"] = df.data_extraction.retrieve_info(edu_setting_output, "int_setting_raw")
                all_df["int_setting_ht"] = df.data_extraction.retrieve_ht(edu_setting_output, "int_setting_ht")
                all_df["int_setting_info"] = df.data_extraction.retrieve_info(edu_setting_output, "int_setting_info")

                all_df["int_part_raw"] = df.data_extraction.retrieve_info(int_focus_output, "int_part_raw")
                all_df["int_part_ht"] = df.data_extraction.retrieve_info(int_focus_output, "int_part_ht")
                all_df["int_part_info"] = df.data_extraction.retrieve_info(int_focus_output, "int_part_info")

                all_df["int_fidel_raw"] = df.data_extraction.retrieve_data(int_impl_details, "int_fidel_raw")
                all_df["int_fidel_ht"] = df.data_extraction.retrieve_ht(int_impl_details, "int_fidel_ht")
                all_df["int_fidel_info"] = df.data_extraction.retrieve_info(int_impl_details, "int_fidel_info")

                all_df["int_cost_raw"] = df.data_extraction.retrieve_data(int_costs_reported, "int_cost_raw")
                all_df["int_cost_ht"] = df.data_extraction.retrieve_ht(int_costs_reported, "int_cost_ht")
                all_df["int_cost_info"] = df.data_extraction.retrieve_info(int_costs_reported, "int_cost_info")

                all_df["base_diff_raw"] = df.data_extraction.retrieve_data(baseline_diff_output, "base_diff_raw")
                all_df["base_diff_ht"] = df.data_extraction.retrieve_ht(baseline_diff_output, "base_diff_ht")
                all_df["base_diff_info"] = df.data_extraction.retrieve_info(baseline_diff_output, "base_diff_info")

                all_df["comp_anal_raw"] = df.data_extraction.retrieve_data(comparability_output, "comp_anal_raw")
                all_df["comp_anal_ht"] = df.data_extraction.retrieve_ht(comparability_output, "comp_anal_ht")
                all_df["comp_anal_info"] = df.data_extraction.retrieve_info(comparability_output, "comp_anal_info")

                all_df["comp_var__raw"] = df.data_extraction.retrieve_data(comp_vars_rep, "comp_var__raw")
                all_df["comp_var__ht"] = df.data_extraction.retrieve_ht(comp_vars_rep, "comp_var__ht")
                all_df["comp_var__info"] = df.data_extraction.retrieve_info(comp_vars_rep, "comp_var__info")

                all_df["comp_var_rep_raw"] = df.data_extraction.retrieve_data(which_comp_vars_rep_output, "comp_var_rep_raw")
                all_df["comp_var_rep_ht"] = df.data_extraction.retrieve_ht(which_comp_vars_rep_output, "comp_var_rep_ht")
                all_df["comp_var_rep_info"] = df.data_extraction.retrieve_info(which_comp_vars_rep_output, "comp_var_rep_info")

                # CLUSTERING
                
                all_df["clust_anal_raw"] = df.data_extraction.retrieve_data(clustering_output, "clust_anal_raw")
                all_df["clust_anal_ht"] = df.data_extraction.retrieve_ht(clustering_output, "clust_anal_ht")
                all_df["clust_anal_info"] = df.data_extraction.retrieve_info(clustering_output, "clust_anal_info")
                                            
                # STUDENT GENDER
                
                all_df["part_gen_raw"] = df.data_extraction.retrieve_data(student_gender, "part_gen_raw")
                all_df["part_gen_ht"] = df.data_extraction.retrieve_ht(student_gender, "part_gen_ht")
                all_df["part_gen_info"] = df.data_extraction.retrieve_info(student_gender, "part_gen_info")
                
                # SAMPLE SIZE
                
                all_df["sample_analysed_ht"] = df.data_extraction.retrieve_ht(sample_size_output, "sample_analysed_ht")
                all_df["sample_analysed_info"] = df.data_extraction.retrieve_info(sample_size_output, "sample_analysed_info")
                                        
                # INTERVENTION SAMPLE SIZE
                
                all_df["base_n_treat_ht"] = df.data_extraction.retrieve_ht(sample_size_intervention_output, "base_n_treat_ht")
                all_df["base_n_treat_info"] = df.data_extraction.retrieve_info(sample_size_intervention_output, "base_n_treat_info")
            
                # CONTROL SAMPLE SIZE
                
                all_df["base_n_cont_ht"] = df.data_extraction.retrieve_ht(sample_size_control_output, "base_n_cont_ht")
                all_df["base_n_cont_info"] = df.data_extraction.retrieve_info(sample_size_control_output, "base_n_cont_info")
            
                # INTERVENTION 2 SAMPLE SIZE
                
                all_df["base_n_treat2_ht"] = df.data_extraction.retrieve_ht(sample_size_second_intervention_output, "base_n_treat2_ht")
                all_df["base_n_treat2_info"] = df.data_extraction.retrieve_info(sample_size_second_intervention_output, "base_n_treat2_info")
            
                # INTERVENTION 3 SAMPLE SIZE
                
                all_df["base_n_treat3_ht"] = df.data_extraction.retrieve_ht(sample_size_third_intervention_output, "base_n_treat3_ht")
                all_df["base_n_treat3_info"] = df.data_extraction.retrieve_info(sample_size_third_intervention_output, "base_n_treat3_info")
            
                # INTERVENTION SAMPLE SIZE ANALYSED
                
                all_df["n_treat_ht"] = df.data_extraction.retrieve_ht(samp_size_anal_int_output, "n_treat_ht")
                all_df["n_treat_info"] = df.data_extraction.retrieve_info(samp_size_anal_int_output, "n_treat_info")
                
                # CONTROL SAMPLE SIZE ANALYSED
                
                all_df["n_cont_ht"] = df.data_extraction.retrieve_ht(samp_size_anal_cont_output, "n_cont_ht")
                all_df["n_cont_info"] = df.data_extraction.retrieve_info(samp_size_anal_cont_output, "n_cont_info")

                # INTERVENTION 2 SAMPLE SIZE ANALYSED
                
                all_df["n_treat2_ht"] = df.data_extraction.retrieve_ht(samp_size_anal_sec_int_output, "n_treat2_ht")
                all_df["n_treat2_info"] = df.data_extraction.retrieve_info(samp_size_anal_sec_int_output, "n_treat2_info")
                
                # CONTROL 2 SAMPLE SIZE ANALYSED
                
                all_df["n_cont2_ht"] = df.data_extraction.retrieve_ht(samp_size_anal_sec_cont_output, "n_cont2_ht")
                all_df["n_cont2_info"] = df.data_extraction.retrieve_info(samp_size_anal_sec_cont_output, "n_cont2_info")
                
                # ATTRITION REPORTED
                
                all_df["attri_raw"] = df.data_extraction.retrieve_data(attr_dropout_rep_output, "attri_raw")
                all_df["attri_ht"] = df.data_extraction.retrieve_ht(attr_dropout_rep_output, "attri_ht")
                all_df["attri_info"] = df.data_extraction.retrieve_info(attr_dropout_rep_output, "attri_info")
            
                # ATTRITION TREATMENT GROUP
                
                all_df["attri_treat_ht"] = df.data_extraction.retrieve_ht(treat_grp_attr, "attri_treat_ht")
                all_df["attri_treat_info"] = df.data_extraction.retrieve_info(treat_grp_attr, "attri_treat_info")
            
                # TOTAL % ATTRITION

                all_df["attri_perc_ht"] = df.data_extraction.retrieve_ht(overall_perc_attr, "attri_perc_ht")
                all_df["attri_perc_info"] = df.data_extraction.retrieve_info(overall_perc_attr, "attri_perc_info")
                #dataframes.append(df_out_tit_tool)

                #all_df = pd.concat(dataframes, axis=1)

                new_df = pd.DataFrame()

                added_ids = []

                while True:
                    user_id = input("Enter EPPI ID (or 'q' to finish): ")
                    
                    if user_id.lower() == 'q':
                        break

                    try:
                        user_id = int(user_id)
                    except ValueError:
                        print("The ID you entered is not an integer. Please enter a valid ID.")
                        continue

                    # Filter the row from DataFrame
                    filtered_df = all_df.loc[all_df['id'] == user_id]

                    # If there is no such ID in the DataFrame, print an error message
                    if filtered_df.empty:
                        print(f"No data found for ID {user_id}")
                    else:
                        # Append the filtered row to the new DataFrame
                        new_df = new_df.append(filtered_df)
                        # Append the added ID to the list
                        added_ids.append(user_id)
                        # Print the list of added IDs
                        print(f"Added ID: {user_id}: {filtered_df['pub_author'].values[0]}")

                if not new_df.empty:
                    console = Console()
                    import datetime 
                    current_datetime = datetime.datetime.now()
                    console.print("\n[bold]Custom dataframe saved here..[/bold]\n")

                    outfile1 = df.data_extraction.save_dataframe(new_df, f"_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}_Custom.csv", custom_info=True)

                    outfile1=str(outfile1)
                    outfile1=outfile1
                    console.print(outfile1 + "\n")
                else: 
                    console = Console()
                    console.print("No data selected, thanks for using the EEF Teaching and Learning Toolkit Extractor.")
                break



                
if __name__ == "__main__":
    main()