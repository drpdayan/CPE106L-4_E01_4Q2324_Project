import flet as ft
from flet import *
import ExpensesLogic as elg

unit = "2C"
getall = elg.get_unit_expense_all(unit)


def main(page: ft.Page):
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf",
        "RobotoMono": "https://github.com/google/fonts/raw/main/apache/robotomono/RobotoMono%5Bwght%5D.ttf"
    }



    page.window.width = 750
    page.window.height = 1000

        # Extract column names from the dictionary keys
    columns = list(getall[0].keys())

    # Create DataColumn objects for each key with Text controls (numeric for Age)
    flet_columns = [
        ft.DataColumn(ft.Text(col_name, font_family="RobotoSlab", weight=FontWeight.BOLD, size=16))
        for col_name in columns
    ]

    # Create DataRow objects from each dictionary in the list
    flet_rows = []
    for x in getall:
        cells = [ft.DataCell(ft.Text(str(value), font_family="RobotoMono", weight=FontWeight.NORMAL, size=14)) for value in x.values()]
        flet_rows.append(ft.DataRow(cells=cells,))

    # Create the DataTable object
    table= DataTable(
        columns=flet_columns,
        rows=flet_rows,
        column_spacing=15,
        width=700,
        border_radius= 20
        
    )

    # Add the table to the page and update
    page.add(Row([Container(table)]))
    page.update()




    page.update()

ft.app(target=main)