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

# Local imports
from src.funcs import (
    data_analysis_cl_table,
    strand_specific_df_selection,
    data_cleaning_col_breakdown,
    display_main_menu,
    dataframe_1_output_display,
    dataframe_2_output_display,
    dataframe_3_output_display,
    dataframe_4_output_display,
    dataframe_5_output_display,
    dataframe_6_output_display,
    JSONDataExtractor,
    DataFrameCompilation,
    input_file_info_display,
    data_file,
    main_menu_display,
    main_menu_display1,
)

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

    # Display user option prompt
    data_frame_option = Prompt.ask("Enter an option from the [bold magenta]Main Menu[/bold magenta]")
    data_frame_option=int(data_frame_option)

    while True:

        match data_frame_option:
            case 1:
                all_variables, outfile1 = data_frame_compilation.make_dataframe_1(save_file=True, clean_cols=True, verbose=False)

                functions = [data_frame_compilation.make_dataframe_1]

                # Display main menu
                main_menu_display1(functions, outfile1, dataframe_1_output_display)

                # Crate input file display table
                input_file_info_display(data_file)

                # Display user option prompt
                data_frame_option = Prompt.ask("Enter an option from the [bold magenta]Main Menu[/bold magenta]")
                data_frame_option=int(data_frame_option)

            case 2: 
                all_variables, outfile2 = data_frame_compilation.make_dataframe_2(save_file=True, clean_cols=True, verbose=False)

                functions = [data_frame_compilation.make_dataframe_2]

                # Display main menu
                main_menu_display1(functions, outfile2, dataframe_2_output_display)

                # Crate input file display table
                input_file_info_display(data_file)

                # Display user option prompt
                data_frame_option = Prompt.ask("Enter an option from the [bold magenta]Main Menu[/bold magenta]")
                data_frame_option=int(data_frame_option)
            case 3:
                all_variables, outfile3 = data_frame_compilation.make_dataframe_3(save_file=True, clean_cols=True, verbose=False)

                functions = [data_frame_compilation.make_dataframe_3]

                # Display main menu
                main_menu_display1(functions, outfile3, dataframe_3_output_display)

                # Crate input file display table
                input_file_info_display(data_file)

                # Display user option prompt
                data_frame_option = Prompt.ask("Enter an option from the [bold magenta]Main Menu[/bold magenta]")
                data_frame_option=int(data_frame_option)
            case 4:
                all_variables, outfile4 = data_frame_compilation.make_dataframe_4(save_file=True, clean_cols=True, verbose=False)

                functions = [data_frame_compilation.make_dataframe_4]

                # Display main menu
                main_menu_display1(functions, outfile4, dataframe_4_output_display)

                # Crate input file display table
                input_file_info_display(data_file)

                # Display user option prompt
                data_frame_option = Prompt.ask("Enter an option from the [bold magenta]Main Menu[/bold magenta]")
                data_frame_option=int(data_frame_option)
            case 5:
                all_variables, outfile5 = data_frame_compilation.make_dataframe_5(save_file=True, clean_cols=True, verbose=False)

                functions = [data_frame_compilation.make_dataframe_5]

                # Display main menu
                main_menu_display1(functions, outfile5, dataframe_5_output_display)

                # Crate input file display table
                input_file_info_display(data_file)

                # Display user option prompt
                data_frame_option = Prompt.ask("Enter an option from the [bold magenta]Main Menu[/bold magenta]")
                data_frame_option=int(data_frame_option)
            case 6:
                strand_specific_option = data_analysis_cl_table()
                strand_specific_df = strand_specific_df_selection(strand_specific_option)

                all_variables, outfile6 = data_frame_compilation.make_dataframe_6(strand_specific_df, save_file=True)
                functions = data_frame_compilation.make_dataframe_6(strand_specific_df)

                # Display main menu
                main_menu_display1(functions, outfile6, dataframe_6_output_display)

                # Crate input file display table
                input_file_info_display(data_file)

                # Display user option prompt
                data_frame_option = Prompt.ask("Enter an option from the [bold magenta]Main Menu[/bold magenta]")
                data_frame_option=int(data_frame_option)
            case 7:
                print("Thank you and goodbye.")
                break

if __name__ == "__main__":
    main()