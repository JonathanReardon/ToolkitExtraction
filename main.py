#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__Author__ = "Jonathan Reardon"

# Third Party imports
from rich import print
from rich import box
from rich.console import Console
from rich.table import Table
from rich.progress import track

# Local imports
from src.funcs import (
    make_dataframe_1,
    make_dataframe_2,
    make_dataframe_3,
    make_dataframe_4,
    make_dataframe_5,
    make_dataframe_6,
    display_table_struct,
    data_analysis_cl_table,
    strand_specific_df_selection,
    data_cleaning_col_breakdown,
    load_json,
)


def main():
    """
    
    """
    console = Console()

    while True:

        main_table = Table(show_header=True, 
                        header_style="bold magenta",
                        title="\nData Cleaning Dataframe Selection",
                        box=box.MINIMAL,                    
        )
        main_table.add_column("")
        main_table.add_column("Selection", header_style="bold green")
        main_table.add_column("Content", header_style="bold magenta")

        main_table.add_row("1", "Dataframe 1", "Study, Research & Design Variables")
        main_table.add_row("2", "Dataframe 2", "Inteverntion Details")
        main_table.add_row("3", "Sample Size", "Sample size variables")
        main_table.add_row("4", "Effect Size A", "Descriptive Statistics")
        main_table.add_row("5", "Effect Size B", "Outcome Details")
        main_table.add_row("6", "Data Analysis", "Key variables for data analysis")
        main_table.add_row("7", "[bold red]EXIT[/bold red]", "")

        console.print(main_table)

        prompt_text = "Enter the number corresponding to the dataframe(s) you want: "
        data_cleaning_option = int(console.input(prompt_text))
        print("")

        match data_cleaning_option:
            case 1:
                all_variables, outfile1 = make_dataframe_1(save_file=True, clean_cols=True, verbose=False)
                functions = [make_dataframe_1]
                table = display_table_struct(functions)

                table.add_row("[bold white]1[/bold white]", "[white]Dataframe 1[/white]", "[white]✔[/white]", outfile1)
                table.add_row("[bold white]2[/bold white]", "[green]Dataframe 2[/green]", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("[bold white]3[/bold white]", "[green]Sample Size[/green]", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("[bold white]4[/bold white]", "[green]Effect Size A[/green]", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("[bold white]5[/bold white]", "[green]Effect Size B[/green]", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("[bold white]6[/bold white]", "[green]All", "[red]✗[/red]", "[red]✗[/red]")
                console.print(table)
            case 2: 
                all_variables, outfile2 = make_dataframe_2(save_file=True, clean_cols=True, verbose=False)
                functions = [make_dataframe_2]
                table = display_table_struct(functions)

                table.add_row("1", "[white]Dataframe 1[/white]", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("2", "Dataframe 2", "[white]✔[/white]", outfile2)
                table.add_row("3", "Sample Size", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("4", "Effect Size A", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("5", "Effect Size B", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("6", "All", "[red]✗[/red]", "[red]✗[/red]")
                console.print(table)
            case 3:
                all_variables, outfile3 = make_dataframe_3(save_file=True, clean_cols=True, verbose=False)
                functions = [make_dataframe_3]
                table = display_table_struct(functions)

                table.add_row("1", "Dataframe 1", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("2", "Dataframe 2", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("3", "Sample Size", "[green]✔[/green]", outfile3)
                table.add_row("4", "Effect Size A", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("5", "Effect Size B", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("6", "All", "[red]✗[/red]", "[red]✗[/red]")
                console.print(table)
            case 4:
                all_variables, outfile4 = make_dataframe_4(save_file=True, clean_cols=True, verbose=False)
                functions = [make_dataframe_4]
                table = display_table_struct(functions)

                table.add_row("1", "Dataframe 1", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("2", "Dataframe 2", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("3", "Sample Size", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("4", "Effect Size A", "[green]✔[/green]", outfile4)
                table.add_row("5", "Effect Size B", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("6", "All", "[red]✗[/red]", "[red]✗[/red]")
                console.print(table)
            case 5:
                all_variables, outfile5 = make_dataframe_5(save_file=True, clean_cols=True, verbose=False)
                functions = [make_dataframe_5]
                table = display_table_struct(functions)

                table.add_row("1", "Dataframe 1", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("2", "Dataframe 2", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("3", "Sample Size", "[red]✗[/red]", "[red]✗[/red]")
                table.add_row("4", "Effect Size A", "[red]✗[/red]",  "[red]✗[/red]")
                table.add_row("5", "Effect Size B", "[green]✔[/green]", outfile5)
                table.add_row("6", "All", "[red]✗[/red]", "[red]✗[/red]")
                console.print(table)
            case 6:
                strand_specific_option = data_analysis_cl_table()
                strand_specific_df = strand_specific_df_selection(strand_specific_option)
                make_dataframe_6(ss_df=strand_specific_df, save_file=True, verbose=False)

            case 7:
                print("End.")
                break

if __name__ == "__main__":
    load_json()
    main()