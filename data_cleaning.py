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
    get_outfile_dir,
    load_json,
)

def main():
    """
    
    """
    # improve for error checking
    load_json()
    console = Console()

    while True:

        main_table = Table(show_header=True, 
                        header_style="bold magenta",
                        title="\nData Cleaning Dataframe Selection",
                        box=box.MINIMAL,
                        highlight=True,                     
        )
        main_table.add_column("")
        main_table.add_column("Selection", header_style="bold green")
        main_table.add_column("Content", header_style="bold magenta")

        main_table.add_row("[bold white]1[/bold white]", "[green]Dataframe 1[/green]", "[magenta]Study, Research & Design Variables[/magenta]")
        main_table.add_row("[bold white]2[/bold white]", "[green]Dataframe 2[/green]", "[magenta]Inteverntion Details[/magenta]")
        main_table.add_row("[bold white]3[/bold white]", "[green]Sample Size[/green]", "[magenta]Sample size variables[/magenta]")
        main_table.add_row("[bold white]4[/bold white]", "[green]Effect Size A[/green]", "[magenta]Descriptive Statistics[/magenta]")
        main_table.add_row("[bold white]5[/bold white]", "[green]Effect Size B[/green]", "[magenta]Outcome Details[/magenta]")
        main_table.add_row("[bold white]6[/bold white]", "[green]All 5 dataframes[/green]", "[magenta]All[/magenta]")
        main_table.add_row("[bold white]7[/bold white]", "[bold white]Exit[/bold white]", "")

        console.print(main_table)

        prompt_text = "Enter the number corresponding to the dataframe(s) you want: "
        data_cleaning_option = int(console.input(prompt_text))
        print("")

        def display_table_struct(funcs): 
            """
            """
            for num, func in track(enumerate(funcs), description="[green]Processing dataframes..\n[/green]"):
                func(save_file=True, clean_cols=True, verbose=False)

            table = Table(show_header=True, 
                          header_style="bold magenta",
                          title="Data Cleaning Dataframe Info Table",
                          safe_box=True,
                          box=box.MINIMAL)
                    
            table.add_column("", style="green")
            table.add_column("Dataframes", header_style="bold green")
            table.add_column("Selection", justify="center", header_style="bold red")
            table.add_column("Save dir", justify="left", header_style="white")

            return table

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
                functions = [
                    make_dataframe_1,
                    make_dataframe_2,
                    make_dataframe_3,
                    make_dataframe_4,
                    make_dataframe_5
                ]
                all_variables1, outfile1 = make_dataframe_1(save_file=True, clean_cols=True, verbose=False)
                outfile1 = get_outfile_dir(all_variables1, "_DataFrame1.csv")
                all_variables2, outfile2 = make_dataframe_2(save_file=True, clean_cols=True, verbose=False)
                outfile2 = get_outfile_dir(all_variables2, "_DataFrame2.csv")
                all_variables3, outfile3 = make_dataframe_3(save_file=True, clean_cols=True, verbose=False)
                outfile3 = get_outfile_dir(all_variables3, "_DataFrame3.csv")
                all_variables4, outfile4 = make_dataframe_4(save_file=True, clean_cols=True, verbose=False)
                outfile4 = get_outfile_dir(all_variables4, "_DataFrame4.csv")
                all_variables5, outfile5 = make_dataframe_5(save_file=True, clean_cols=True, verbose=False)
                outfile5 = get_outfile_dir(all_variables5, "_DataFrame5.csv")

                table = display_table_struct(functions)

                table.add_row(
                    "1", "Dataframe 1", "[green]✔[/green]", outfile1,
                )
                table.add_row(
                    "2", "Dataframe 2", "[green]✔[/green]", outfile2,
                )
                table.add_row(
                    "3", "Sample Size", "[green]✔[/green]", outfile3,
                )
                table.add_row(
                    "4", "Effect Size A", "[green]✔[/green]", outfile4,
                )
                table.add_row(
                    "5", "Effect Size B", "[green]✔[/green]", outfile5,
                )
                console.print(table)
            case 7:
                print("End.")
                break

if __name__ == "__main__":
    main()