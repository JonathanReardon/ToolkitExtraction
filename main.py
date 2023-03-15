#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__Author__ = "Jonathan Reardon"

import os

# Third Party imports
from rich import print
from rich.prompt import Prompt
from rich.console import Console
from rich.columns import Columns
from rich.style import Style
from rich.panel import Panel

from rich.table import Table
from rich import box
from rich.pretty import Pretty

import pandas as pd
from src.attributeIDs import *

# Local imports
from src.funcs import (
    data_analysis_cl_table,
    data_cleaning_col_breakdown,
    display_main_menu,
    dataframe_1_output_display,
    dataframe_2_output_display,
    dataframe_3_output_display,
    dataframe_4_output_display,
    dataframe_5_output_display,
    dataframe_6_output_display,
    dataframe_7_output_display,
    JSONDataExtractor,
    DataFrameCompilation,
    StrandSpecificFrames,
    RiskofBias,
    CustomFrames,
    input_file_info_display,
    data_file,
    main_menu_display,
    main_menu_display1,
)

# table1 
row_styles1 = ["#ffffff"] * 10
row_data_list1 = [
    "Study ID", "Author", "Year", "Abstract", "Admin Strand",
    "Country", "Publication Type EPPI", "Publication Type",
    "Educational Setting", "Student Age"
]

def general_vars1():

    console = Console()

    custom_style_main = Style(bgcolor="#21241d")
    title1 = console.render_str("[bold]Custom Data Selection[/bold]")

    table_title_style = Style(italic=False, bgcolor=None, color="blue", bold=True)
    header_style = Style(italic=False, bgcolor=None, color="blue", bold=True)
    column_style = Style() 

    main_table2 = Table(show_header=True, 
                        box=box.SIMPLE,
                        highlight=True,
                        title_style=table_title_style,               
    )

    main_table2.add_column("", header_style=header_style, style=column_style, width=2)
    main_table2.add_column("General Variables", header_style=header_style, style=column_style)

    for idx, row_data in enumerate(row_data_list1, start=1):
        main_table2.add_row(f"{idx+0}", row_data, style=row_styles1[idx - 1])
    
    return main_table2

# table1 
row_styles2 = ["#ffffff"] * 10
row_data_list2 = [
    "Outcome Title", "Outcome Description", "Outcome Type", "SMD", "SE",
    "Outcome Measure", "Outcome Group1 N", "Outcome Group1 Mean",
    "Outcome Group1 SD", "Outcome Group2 N"
]


def outcome_vars_1():
    
    console = Console()

    custom_style_main = Style(bgcolor="#21241d")
    title1 = console.render_str("[bold]Custom Data Selection[/bold]")

    table_title_style = Style(italic=False, bgcolor=None, color="blue", bold=True)
    header_style = Style(italic=False, bgcolor=None, color="blue", bold=True)
    column_style = Style(bgcolor=None, color="white") 

    # Outcome variables table
    main_table3 = Table(show_header=True, 
                        box=box.SIMPLE,
                        highlight=False,
                        title_style=table_title_style,                 
    )

    main_table3.add_column("", header_style=header_style, style=column_style, width=3)
    main_table3.add_column("Toolkit Primary Outcome", header_style=header_style, style=column_style)

    for idx, row_data in enumerate(row_data_list2, start=1):
        main_table3.add_row(f"{idx+10}", row_data, style=row_styles2[idx - 1])
    
    return main_table3

console = Console()
main_table2 = general_vars1()
main_table3 = outcome_vars_1()
tables = Columns([main_table2, main_table3])
console.print(tables)

highlight_style = "#FFD700"

def get_user_input():
    while True:
        try:
            data_cleaning_option = Prompt.ask("Enter an option from the [bold magenta]Main Menu[/bold magenta]")
            data_cleaning_option=int(data_cleaning_option)
            if data_cleaning_option < 0 or data_cleaning_option > 8:
                raise ValueError
            break
        except ValueError:
            console=Console()
            console.print("Error: invalid input. Please enter a number from [bold magenta]0 to 8[/bold magenta].")
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
                console.print("Thanks for using the [bold magenta]EEF Toolkit Data Extractor![bold magenta]")
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
                data_cleaning_option = Prompt.ask("Enter an option from the [bold magenta]Main Menu[/bold magenta]")
                data_cleaning_option=int(data_cleaning_option)
            case 6:
                console = Console()
                console.clear()
                strand_specific_option = data_analysis_cl_table()

                ss = StrandSpecificFrames(json_extractor)

                strand_specific_df = ss.strand_specific_df_selection(strand_specific_option)

                all_variables, outfile6 = data_frame_compilation.make_dataframe_6(strand_specific_df, save_file=True)
                functions = data_frame_compilation.make_dataframe_6(strand_specific_df)

                # Display main menu
                main_menu_display1(functions, outfile6, dataframe_6_output_display)

                # Crate input file display table
                input_file_info_display(data_file)

                data_cleaning_option = get_user_input()
            case 7:
                _, outfile7 = data_frame_compilation.make_references(save_file=True)
                functions = [data_frame_compilation.make_references]

                # Display main menu
                main_menu_display1(functions, outfile7, dataframe_7_output_display)

                # Crate input file display table
                input_file_info_display(data_file)

                data_cleaning_option = get_user_input()
            case 8:
                console = Console()
                console.clear()
                main_table2 = general_vars1()
                main_table3 = outcome_vars_1()
                tables = Columns([main_table2, main_table3])
                console.print(tables)
                
                #custom_style_df1 = Style(bgcolor="#21241d")
                #custom_style_main = Style(bgcolor="#21241d")

                #table = Table(show_header=True, 
                #                style=custom_style_df1,
                #                title=None,
                #                safe_box=False,
                #                header_style="bold magenta",
                #                box=box.MINIMAL,
                #                width=None)
                
                #table.add_column("", style="bold white")
                #table.add_column("Data", style="bold white")

                df = CustomFrames(json_extractor)

                used_options = []

                """ def add_row_to_table(table, row, cell_style=None):
                    table.add_row("[bold green]✓[/bold green]", row)
                    if cell_style:
                        table.columns[1].cells[-1].style = cell_style
                    panel = Panel.fit(table, 
                                    title="Custom Data Selection", 
                                    style=custom_style_df1,
                                    border_style="white",
                                    title_align="left",
                                    padding=(1, 2))
                    panel1 = data_cleaning_col_breakdown()
                    row1 = Columns([panel1, panel], equal=False)
                    layout = Columns([row1], equal=False)
                    panel = Panel(layout, 
                                title="TST", 
                                border_style="white", 
                                padding=(1, 2), 
                                title_align="left",
                                style=custom_style_main,
                                width=200)
                    console.clear()
                    console.print(panel)
                    return table """

                # Compile list of invidividual data frames
                dataframes=[]
                while True:
                    try:
                        console.print("Add variables to your data frame ([bold magenta]0=Save file and exit)[/bold magenta]")
                        num = int(Prompt.ask("Selection"))
                        if num < 0 or num > 150:
                            raise ValueError
                    except ValueError:
                        print("Error: invalid input. Please enter a number from 0 to 150.\n")
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
                                #table = add_row_to_table(table, "Study ID")
                                used_options.append("id")
                            else:
                                print("You have already selected this option!")
                        case 2: 
                            if "pub_author" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                author_df = df.data_extraction.retrieve_metadata("ShortTitle", "pub_author")
                                dataframes.append(author_df)
                                #table = add_row_to_table(table, "Publication Author")
                                used_options.append("pub_author")
                            else:
                                print("You have already selected this option!")
                        case 3: 
                            if "pub_year" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                year_df = df.data_extraction.retrieve_metadata("Year", "pub_year")
                                dataframes.append(year_df)
                                #table = add_row_to_table(table, "Publication Year")
                                used_options.append("pub_year")
                            else:
                                print("You have already selected this option!")
                        case 4:
                            if "abstract" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                abstract_df = df.data_extraction.retrieve_metadata("Abstract", "abstract")
                                dataframes.append(abstract_df)
                                #table = add_row_to_table(table, "Abstract")
                                used_options.append("abstract")
                            else:
                                print("You have already selected this option!")
                        case 5: 
                            if "strand_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                admin_strand_df = df.data_extraction.retrieve_data(admin_strand_output, "strand_raw")
                                dataframes.append(admin_strand_df)
                                #table = add_row_to_table(table, "Strand")
                                used_options.append("strand_raw")
                            else:
                                print("You have already selected this option!")
                        case 6:
                            if "loc_country_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                country_df = df.data_extraction.retrieve_data(countries, "loc_country_raw")
                                dataframes.append(country_df)
                                #table = add_row_to_table(table, "Country")
                                used_options.append("loc_country_raw")
                            else:
                                print("You have already selected this option!")
                        case 7: 
                            if "pub_eppi" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                pubtype_eppi_df = df.data_extraction.retrieve_metadata("TypeName", "pub_eppi")
                                dataframes.append(pubtype_eppi_df)
                                #table = add_row_to_table(table, "Publication Type EPPI")
                                used_options.append("pub_eppi")
                            else:
                                print("You have already selected this option!")
                        case 8: 
                            if "pub_type_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                pub_type_data = df.data_extraction.retrieve_data(publication_type_output, "pub_type_raw")
                                dataframes.append(pub_type_data)
                                #table = add_row_to_table(table, "Publication Type")
                                used_options.append("pub_type_raw")
                            else:
                                print("You have already selected this option!")
                        case 9: 
                            if "int_setting_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                edu_setting_data = df.data_extraction.retrieve_data(edu_setting_output, "int_setting_raw")
                                dataframes.append(edu_setting_data)
                                #table = add_row_to_table(table, "Educational Setting")
                                used_options.append("int_setting_raw")
                            else:
                                print("You have already selected this option!")
                        case 10: 
                            if "part_age_raw" not in used_options:
                                row_styles1[num - 1] = highlight_style
                                student_age_data = df.data_extraction.retrieve_data(student_age_output, "part_age_raw")
                                dataframes.append(student_age_data)
                                #table = add_row_to_table(table, "Student Age")
                                used_options.append("part_age_raw")
                            else:
                                print("You have already selected this option!")
                        #/*************************/#
                        #/ TOOLKIT PRIMARY OUTCOME /#
                        #/*************************/#
                        case 11:
                                if "out_tit_tool" not in used_options:
                                    row_styles2[num - 11] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_out_tit_tool = df_out.out_tit_tool
                                    dataframes.append(df_out_tit_tool)
                                    #table = add_row_to_table(table, "Toolkit Outcome Title")
                                    used_options.append("out_tit_tool")
                                else:
                                    print("You have already selected this option!")
                        case 12:
                                if "out_desc_tool" not in used_options:
                                    row_styles2[num - 11] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_out_desc_tool = df_out.out_desc_tool
                                    dataframes.append(df_out_desc_tool)
                                    used_options.append("out_desc_tool")
                                else:
                                    print("You have already selected this option!")
                        case 13:
                                if "out_type_tool" not in used_options:
                                    row_styles2[num - 11] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_out_type_tool = df_out.out_type_tool
                                    dataframes.append(df_out_type_tool)
                                    used_options.append("out_type_tool")
                                else:
                                    print("You have already selected this option!")
                        case 14:
                                if "smd_tool" not in used_options:
                                    row_styles2[num - 11] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_smd_tool = df_out.smd_tool
                                    dataframes.append(df_smd_tool)
                                    used_options.append("smd_tool")
                                else:
                                    print("You have already selected this option!")
                        case 15:
                                if "se_tool" not in used_options:
                                    row_styles2[num - 11] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_se_tool = df_out.se_tool
                                    dataframes.append(df_se_tool)
                                    used_options.append("se_tool")
                                else:
                                    print("You have already selected this option!")
                        case 16:
                                if "out_measure_tool" not in used_options:
                                    row_styles2[num - 11] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_out_measure_tool = df_out.out_measure_tool
                                    dataframes.append(df_out_measure_tool)
                                    used_options.append("out_measure_tool")
                                else:
                                    print("You have already selected this option!")
                        case 17:
                                if "out_g1_n_tool" not in used_options:
                                    row_styles2[num - 11] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_g1_n_tool = df_out.out_g1_n_tool
                                    dataframes.append(df_g1_n_tool)
                                    used_options.append("out_g1_n_tool")
                                else:
                                    print("You have already selected this option!")
                        case 18:
                                if "out_g1_mean_tool" not in used_options:
                                    row_styles2[num - 11] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_g1_mean_tool = df_out.out_g1_mean_tool
                                    dataframes.append(df_g1_mean_tool)
                                    used_options.append("out_g1_mean_tool")
                                else:
                                    print("You have already selected this option!")
                        case 19:
                                if "out_g1_sd_tool" not in used_options:
                                    row_styles2[num - 11] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_g1_sd_tool = df_out.out_g1_sd_tool
                                    dataframes.append(df_g1_sd_tool)
                                    used_options.append("out_g1_sd_tool")
                                else:
                                    print("You have already selected this option!")
                        case 20:
                                if "out_g2_n_tool" not in used_options:
                                    row_styles2[num - 11] = highlight_style
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_g2_n_tool = df_out.out_g2_n_tool
                                    dataframes.append(df_g2_n_tool)
                                    used_options.append("out_g2_n_tool")
                                else:
                                    print("You have already selected this option!")
                        case _:
                            print("Error: invalid option selected")
                            #os.system('cls' if os.name == 'nt' else 'clear')
                            #console.print(panel)
                    
                    if dataframes:
                        all_df = pd.concat(dataframes, axis=1)
                        console = Console()
                        main_table2 = general_vars1()
                        main_table3 = outcome_vars_1()
                        console.clear()
                        tables = Columns([main_table2, main_table3])
                        console.print(tables)

                if dataframes:
                    all_df = pd.concat(dataframes, axis=1)
                    console.print("\n[bold]Custom data frame saved here..[/bold]\n", style="white")
                    outfile1 = df.data_extraction.save_dataframe(all_df, "_Custom.csv")
                    outfile1=str(outfile1)
                    console.print(outfile1 + "\n")
                    console.print("Thanks for using the [bold magenta]EEF Toolkit Data Extractor![bold magenta]")
                else: 
                    console.print("No data selected, thanks for using the [bold magenta]EEF Teaching and Learning Toolkit Extractor.[/bold magenta]")
                break

if __name__ == "__main__":
    main()