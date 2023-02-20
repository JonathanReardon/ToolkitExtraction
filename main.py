#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

__Author__ = "Jonathan Reardon"

# Third Party imports
from rich import print
from rich import box
from rich.console import Console
from rich.table import Table

# Local imports
from src.funcs import (
    display_table_struct,
    data_analysis_cl_table,
    strand_specific_df_selection,
    data_cleaning_col_breakdown,
    dataframe_1_output_display,
    dataframe_2_output_display,
    dataframe_3_output_display,
    dataframe_4_output_display,
    dataframe_5_output_display,
    json_extractor,
)

def main():
    """
    
    """
    console = Console()
    while True:
        main_table = Table(show_header=True, 
                        header_style="bold magenta",
                        title="\nOptions",
                        box=box.MINIMAL,                    
        )
        main_table.add_column("")
        main_table.add_column("Selection", header_style="bold green")
        main_table.add_column("Description", header_style="bold magenta")

        main_table.add_row("1", "Dataframe Contents", "")
        main_table.add_row("2", "Dataframe 1", "Study, Research & Design Variables")
        main_table.add_row("3", "Dataframe 2", "Inteverntion Details")
        main_table.add_row("4", "Sample Size", "Sample size variables")
        main_table.add_row("5", "Effect Size A", "Descriptive Statistics")
        main_table.add_row("6", "Effect Size B", "Outcome Details")
        main_table.add_row("7", "Data Analysis", "Key variables for data analysis")
        main_table.add_row("8", "[bold red]EXIT[/bold red]", "")

        console.print(main_table)

        prompt_text = "Enter the number corresponding to the dataframe(s) you want: "
        data_cleaning_option = int(console.input(prompt_text))
        print("")

        match data_cleaning_option:
            case 1:
                data_cleaning_col_breakdown()
            case 2:
                all_variables, outfile1 = json_extractor.make_dataframe_1(save_file=True, clean_cols=True, verbose=False)
                functions = [json_extractor.make_dataframe_1]
                dataframe_1_output_display(functions, outfile1)
            case 3: 
                all_variables, outfile2 = json_extractor.make_dataframe_2(save_file=True, clean_cols=True, verbose=False)
                functions = [json_extractor.make_dataframe_2]
                dataframe_2_output_display(functions, outfile2)
            case 4:
                all_variables, outfile3 = json_extractor.make_dataframe_3(save_file=True, clean_cols=True, verbose=False)
                functions = [json_extractor.make_dataframe_3]
                dataframe_3_output_display(functions, outfile3)
            case 5:
                all_variables, outfile4 = json_extractor.make_dataframe_4(save_file=True, clean_cols=True, verbose=False)
                functions = [json_extractor.make_dataframe_4]
                dataframe_4_output_display(functions, outfile4)
            case 6:
                all_variables, outfile5 = json_extractor.make_dataframe_5(save_file=True, clean_cols=True, verbose=False)
                functions = [json_extractor.make_dataframe_5]
                dataframe_5_output_display(functions, outfile5)
            case 7:
                strand_specific_option = data_analysis_cl_table()
                strand_specific_df = strand_specific_df_selection(strand_specific_option)
                json_extractor.make_dataframe_6(ss_df=strand_specific_df, save_file=True, verbose=False)
            case 8:
                print("Thank you and goodbye.")
                break

if __name__ == "__main__":
    main()