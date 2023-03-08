#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__Author__ = "Jonathan Reardon"

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

def data_cleaning_col_breakdown():
    from rich.console import Console
    from rich.progress import track
    from rich.style import Style
    from rich.table import Table
    from rich.columns import Columns
    from rich.panel import Panel
    from rich import box
    from rich import print

    table_title_style = Style(italic=False, bgcolor=None, color="blue", bold=True)
    header_style = Style(italic=False, bgcolor=None, color="blue", bold=True)
    column_style = Style(bgcolor=None, color="white") 

    main_table2 = Table(show_header=True, 
                        box=box.SIMPLE,
                        highlight=False,
                        title_style=table_title_style,
                        title=None,                   
    )
    main_table2.add_column("", header_style=header_style, style=column_style, width=2)
    main_table2.add_column("Variables", header_style=header_style, style=column_style)
    main_table2.add_column("", header_style=header_style, style=column_style, width=2)
    main_table2.add_column("Variables", header_style=header_style, style=column_style)
    main_table2.add_column("", header_style=header_style, style=column_style, width=2)
    main_table2.add_column("Variables", header_style=header_style, style=column_style)
    main_table2.add_column("", header_style=header_style, style=column_style, width=2)
    main_table2.add_column("Variables", header_style=header_style, style=column_style)

    main_table2.add_row("1", "Study ID", "26", "Treatment Grp Attrition", "51", "Int Session Length", "76", "Ctrl Grp Other Information")
    main_table2.add_row("2", "Author", "27", "Attrition Overall %", "52", "Int Detail", "77", "Int Grp 2 N")
    main_table2.add_row("3", "Year", "28", "Low SES %", "53", "Int Costs", "78", "Int Grp 2 Pre-test Mean")
    main_table2.add_row("4", "Abstract", "29", "Furthe SES Info", "54", "Int Evaluation", "79", "Int Grp 2 Pre-test SD")
    main_table2.add_row("5", "Admin Strand", "30", "No Low SES Info", "55", "Baseline Differences", "80", "Int Grp 2 Post-test Mean")
    main_table2.add_row("6", "Country", "31", "Treatment Grp", "56", "Computational Analysis", "81", "Int Grp 2 Post-test SD")
    main_table2.add_row("7", "Publication Type EPPI", "32", "Participant Assignment", "57", "Comp Vars Reported", "82", "Int Grp 2 Gain Score Mean")
    main_table2.add_row("8", "Publication Type", "33","Level of Assignment", "58", "Which Comp Vars Reported", "83", "Int Grp 2 Gain Score SD")
    main_table2.add_row("9", "Educational Setting", "34","Randomisation", "59", "Clustering", "84", "Int Grp 2 Other Information")
    main_table2.add_row("10", "Student Age", "35", "Other Outcomes", "60", "Desc Stats Primary Out Reported", "85", "Ctrl Grp 2 N")
    main_table2.add_row("11", "Student Gender", "36", "Additional Outcome Data", "61", "Int Grp N", "86", "Ctrl Grp 2 Pre-test Mean")
    main_table2.add_row("12", "Number of Schools", "37", "Toolkit Version", "62", "Int Grp Pre-test Mean", "87", "Ctrl Grp 2 Pre-test SD")
    main_table2.add_row("13", "Number of Classes", "38", "Int Name", "63", "Int Grp Pre-test SD", "88", "Ctrl Grp 2 Post-test Mean")
    main_table2.add_row("14", "Ecological Validity", "39", "Int Description", "64", "Int Grp Post-test Mean", "89", "Ctrl Grp 2 Post-test SD") 
    main_table2.add_row("15", "Study Design", "40","Int Objective", "65", "Int Grp Post-test SD", "90", "Ctrl Grp 2 Gain Score Mean")
    main_table2.add_row("16", "Sample Size", "41","Int Organisation Type", "66", "Int Grp Gain Score Mean", "91", "Ctrl Grp 2 Gain Score SD")
    main_table2.add_row("17", "Sample Size Int", "42", "Int Training Provided", "67", "Int Grp Gain Score SD", "92", "Ctrl Grp Other Information")
    main_table2.add_row("18", "Sample Size Ctrl", "43", "Int Focus", "68", "Int Grp Other Information", "93", "Follow-up Data")
    main_table2.add_row("19", "Sample Size 2nd Int", "44", "Int Teching Approach", "69", "Ctrl Grp N", "94", "")
    main_table2.add_row("20", "Sample Size 3rd Int", "45", "Digital Technology", "70", "Ctrl Grp Pre-test Mean", "95", "")
    main_table2.add_row("21", "Sample Size Analysed (Int)", "46", "Parental Engagement", "71", "Ctrl Grp Pre-test SD", "96", "")
    main_table2.add_row("22", "Sample Size Analysed (Ctrl)",  "47", "Int Time", "72", "Ctrl Grp Post-test Mean", "97", "")
    main_table2.add_row("23", "Sample Size Analysed (2nd Int Grp)", "48", "Int Delivery", "73", "Ctrl Grp Post-test SD", "98", "")
    main_table2.add_row("24", "Sample Size Analysed (2nd Ctrl Grp)", "49", "Int Duration", "74", "Ctrl Grp Gain Score Mean", "99", "")
    main_table2.add_row("25", "Attrition", "50", "Int Frequency", "75", "Ctrl Grp Gain Score SD", "100", "")

    console = Console()
    custom_style_main = Style(bgcolor="#282c24")
    title1 = console.render_str("[bold]Custom Data Variables[/bold]")

    panel = Panel.fit(
            main_table2,
            title=title1,
            border_style="magenta",
            style=custom_style_main,
            title_align="left",
            padding=(1, 2),
        )

    return panel

def get_user_input():
    while True:

        try:
            # Display user option prompt
            data_cleaning_option = Prompt.ask("Enter an option from the [bold magenta]Main Menu[/bold magenta]")
            data_cleaning_option=int(data_cleaning_option)
            if data_cleaning_option < 0 or data_cleaning_option > 9:
                raise ValueError
            break
        except ValueError:
            print("Error: invalid input. Please enter a number from 0 to 8.\n")
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

                data_cleaning_option = get_user_input()
            case 6:
                strand_specific_option = data_analysis_cl_table()
                print(strand_specific_option)

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
                main_panel = data_cleaning_col_breakdown()
                console.print(main_panel)

                console = Console()
                
                custom_style_df1 = Style(bgcolor="#282c24")
                custom_style_main = Style(bgcolor="#282c24")

                table = Table(show_header=True, 
                                style=custom_style_df1,
                                title=None,
                                safe_box=False,
                                header_style="bold magenta",
                                box=box.MINIMAL,
                                width=None)
                
                table.add_column("", style="bold white")
                table.add_column("Data", style="bold white")

                df = CustomFrames(json_extractor)

                used_options = []

                def add_row_to_table(table, row, cell_style=None):
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
                    return table

                dataframes=[]
                while True:
                    try:
                        console.print("[bold green]Add variables to your data frame (0=Save file and exit)[/bold green]")
                        num = int(Prompt.ask("Selection"))

                        if num < 0 or num > 100:
                            raise ValueError
                    except ValueError:
                        print("Error: invalid input. Please enter a number from 0 to 5.\n")
                        continue

                    match num:
                        case 0:
                            run_program=False
                            break
                        case 1: 
                            if "id" not in used_options:
                                eppiid_df = df.data_extraction.retrieve_metadata("ItemId", "id")
                                print(eppiid_df)
                                dataframes.append(eppiid_df)
                                table = add_row_to_table(table, "Study ID")
                                used_options.append("id")
                            else:
                                print("You have already selected this option!")
                        case 2: 
                            if "pub_author" not in used_options:
                                author_df = df.data_extraction.retrieve_metadata("ShortTitle", "pub_author")
                                dataframes.append(author_df)
                                table = add_row_to_table(table, "Publication Author")
                                used_options.append("pub_author")
                            else:
                                print("You have already selected this option!")
                        case 3: 
                            if "pub_year" not in used_options:
                                year_df = df.data_extraction.retrieve_metadata("Year", "pub_year")
                                dataframes.append(year_df)
                                table = add_row_to_table(table, "Publication Year")
                                used_options.append("pub_year")
                            else:
                                print("You have already selected this option!")
                        case 4:
                            if "abstract" not in used_options:
                                abstract_df = df.data_extraction.retrieve_metadata("Abstract", "abstract")
                                dataframes.append(abstract_df)
                                table = add_row_to_table(table, "Abstract")
                                used_options.append("abstract")
                            else:
                                print("You have already selected this option!")
                        case 5: 
                            if "strand_raw" not in used_options:
                                admin_strand_df = df.data_extraction.retrieve_data(admin_strand_output, "strand_raw")
                                dataframes.append(admin_strand_df)
                                table = add_row_to_table(table, "Strand")
                                used_options.append("strand_raw")
                            else:
                                print("You have already selected this option!")
                        case 6:
                            if "loc_country_raw" not in used_options:
                                country_df = df.data_extraction.retrieve_data(countries, "loc_country_raw")
                                dataframes.append(country_df)
                                table = add_row_to_table(table, "Country")
                                used_options.append("loc_country_raw")
                            else:
                                print("You have already selected this option!")
                        case 7: 
                            if "pub_eppi" not in used_options:
                                pubtype_eppi_df = df.data_extraction.retrieve_metadata("TypeName", "pub_eppi")
                                dataframes.append(pubtype_eppi_df)
                                table = add_row_to_table(table, "Publication Type EPPI")
                                used_options.append("pub_eppi")
                            else:
                                print("You have already selected this option!")
                        case 8: 
                            if "pub_type_raw" not in used_options:
                                pub_type_data = df.data_extraction.retrieve_data(publication_type_output, "pub_type_raw")
                                dataframes.append(pub_type_data)
                                table = add_row_to_table(table, "Publication Type")
                                used_options.append("pub_type_raw")
                            else:
                                print("You have already selected this option!")
                        case 9: 
                            if "int_setting_raw" not in used_options:
                                edu_setting_data = df.data_extraction.retrieve_data(edu_setting_output, "int_setting_raw")
                                dataframes.append(edu_setting_data)
                                table = add_row_to_table(table, "Educational Setting")
                                used_options.append("int_setting_raw")
                            else:
                                print("You have already selected this option!")
                        case 10: 
                            if "part_age_raw" not in used_options:
                                student_age_data = df.data_extraction.retrieve_data(student_age_output, "part_age_raw")
                                dataframes.append(student_age_data)
                                table = add_row_to_table(table, "Student Age")
                                used_options.append("part_age_raw")
                            else:
                                print("You have already selected this option!")
                        case 11: 
                            if "part_gen_raw" not in used_options:
                                gender_df = df.data_extraction.retrieve_data(student_gender, "part_gen_raw")
                                dataframes.append(gender_df)
                                table = add_row_to_table(table, "Student Gender")
                                used_options.append("part_gen_raw")
                            else:
                                print("You have already selected this option!")
                        case 12: 
                            if "school_treat_info" not in used_options:
                                number_of_school_int_info = df.data_extraction.retrieve_info(number_of_schools_intervention_output, "school_treat_info")
                                dataframes.append(number_of_school_int_info)
                                table = add_row_to_table(table, "Number of Schools")
                                used_options.append("school_treat_info")
                            else:
                                print("You have already selected this option!")
                        case 13: 
                            if "class_treat_info" not in used_options:
                                number_of_classes_int_info = df.data_extraction.retrieve_info(num_of_class_int_output, "class_treat_info")
                                dataframes.append(number_of_classes_int_info)
                                table = add_row_to_table(table, "Number of Classes")
                                used_options.append("class_treat_info")
                            else:
                                print("You have already selected this option!")
                        case 14: 
                            if "eco_valid_raw" not in used_options:
                                study_realism_data = df.data_extraction.retrieve_data(study_realism_output, "eco_valid_raw")
                                dataframes.append(study_realism_data)
                                table = add_row_to_table(table, "Ecological Validity")
                                used_options.append("eco_valid_raw")
                            else:
                                print("You have already selected this option!")
                        case 15: 
                            if "int_desig_raw" not in used_options:
                                study_design_data = df.data_extraction.retrieve_data(study_design_output, "int_desig_raw")
                                dataframes.append(study_design_data)
                                table = add_row_to_table(table, "Study Design")
                                used_options.append("int_desig_raw")
                            else:
                                print("You have already selected this option!")






                        case 16: 
                            if "sample_analysed_info" not in used_options:
                                sample_size_comments_df = df.data_extraction.retrieve_info(sample_size_output, "sample_analysed_info")
                                dataframes.append(sample_size_comments_df)
                                table = add_row_to_table(table, "Sample Size")
                                used_options.append("sample_analysed_info")
                            else:
                                print("You have already selected this option!")



                        case 17: 
                            if "base_n_treat_info" not in used_options:
                                sample_size_intervention_Comments_df = df.data_extraction.retrieve_info(sample_size_intervention_output, "base_n_treat_info")
                                dataframes.append(sample_size_intervention_Comments_df)
                                table = add_row_to_table(table, "Sample Size Int")
                                used_options.append("base_n_treat_info")
                            else:
                                print("You have already selected this option!")


                        case 17: 
                            if "base_n_treat_info" not in used_options:
                                sample_size_intervention_Comments_df = df.data_extraction.retrieve_info(sample_size_intervention_output, "base_n_treat_info")
                                dataframes.append(sample_size_intervention_Comments_df)
                                table = add_row_to_table(table, "Sample Size Int")
                                used_options.append("base_n_treat_info")
                            else:
                                print("You have already selected this option!")


                        case 94:
                                if "out_tit_tool" not in used_options:
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_out_tit_tool = df_out.out_tit_tool
                                    dataframes.append(df_out_tit_tool)
                                    table = add_row_to_table(table, "Toolkit Outcome Title")
                                    used_options.append("out_tit_tool")
                                else:
                                    print("You have already selected this option!")
                        case 95:
                                if "out_desc_tool" not in used_options:
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_out_desc_tool = df_out.out_desc_tool
                                    dataframes.append(df_out_desc_tool)
                                    table = add_row_to_table(table, "Toolkit Outcome Description")
                                    used_options.append("out_desc_tool")
                                else:
                                    print("You have already selected this option!")
                        case 96:
                                if "out_type_tool" not in used_options:
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_out_type_tool = df_out.out_type_tool
                                    dataframes.append(df_out_type_tool)
                                    table = add_row_to_table(table, "Toolkit Outcome Type")
                                    used_options.append("out_type_tool")
                                else:
                                    print("You have already selected this option!")
                        case 97:
                                if "smd_tool" not in used_options:
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_smd_tool = df_out.smd_tool
                                    dataframes.append(df_smd_tool)
                                    table = add_row_to_table(table, "Toolkit SMD")
                                    used_options.append("smd_tool")
                                else:
                                    print("You have already selected this option!")
                        case 98:
                                if "se_tool" not in used_options:
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_se_tool = df_out.se_tool
                                    dataframes.append(df_se_tool)
                                    table = add_row_to_table(table, "Toolkit SE")
                                    used_options.append("se_tool")
                                else:
                                    print("You have already selected this option!")
                        case 99:
                                if "out_measure_tool" not in used_options:
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_out_measure_tool = df_out.out_measure_tool
                                    dataframes.append(df_out_measure_tool)
                                    table = add_row_to_table(table, "Toolkit Outcome Measure")
                                    used_options.append("out_measure_tool")
                                else:
                                    print("You have already selected this option!")
                        case 100:
                                if "out_g1_n_tool" not in used_options:
                                    df_outcomes = DataFrameCompilation(json_extractor)
                                    df_out, _ = df_outcomes.make_dataframe_5(save_file=False, clean_cols=False, verbose=False)
                                    df_g1_n_tool = df_out.out_g1_n_tool
                                    dataframes.append(df_g1_n_tool)
                                    table = add_row_to_table(table, "Toolkit Outcome Group1 N")
                                    used_options.append("out_g1_n_tool")
                                else:
                                    print("You have already selected this option!")
                        case _:
                                print("Error: invalid option selected")
                                console.clear()
                                console.print(panel)

                    if dataframes:
                        all_df = pd.concat(dataframes, axis=1)
                        console.print("\nDataframe Builder..\n", style="white")

                        pretty = Pretty(all_df)
                        panel = Panel(pretty, 
                                    title="Data Selection", 
                                    style=custom_style_df1,
                                    border_style="white",
                                    title_align="left",
                                    padding=(1, 2))
                        #print(panel)

                
                if dataframes:

                    all_df = pd.concat(dataframes, axis=1)
                    console.print("\nHere is your final dataframe selection..\n", style="white")
                    pretty = Pretty(all_df)

                    panel = Panel(pretty, 
                                  title="Data Selection", 
                                  style=custom_style_df1,
                                  border_style="white",
                                  title_align="left",
                                  padding=(1, 2))
                    outfile1 = df.data_extraction.save_dataframe(all_df, "_Custom.csv")
                    print(outfile1)
                else: 
                    print("no objects selected, goodbye.")
                break
            case 9:
                print("Exiting..")
                run_program = False
            #case _:
                #print("Error: test")
                #console.clear()

                    


if __name__ == "__main__":
    main()