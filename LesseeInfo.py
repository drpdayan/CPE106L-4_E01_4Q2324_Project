import flet as ft
from flet import *
from initiallogic import get_lessee_list as gl


glists = gl()
def main(page: ft.Page):

    # Extract column names from the dictionary keys
    columns = list(glists[0].keys())

    # Create DataColumn objects for each key with Text controls (numeric for Age)
    flet_columns = [
        ft.DataColumn(ft.Text(col_name))
        for col_name in columns
    ]

    # Create DataRow objects from each dictionary in the list
    flet_rows = []
    for person in glists:
        cells = [ft.DataCell(ft.Text(str(value))) for value in person.values()]
        flet_rows.append(ft.DataRow(cells=cells))

    # Create the DataTable object
    table= DataTable(
        columns=flet_columns,
        rows=flet_rows,
    )

    # Add the table to the page and update
    page.add(table)
    page.update()

ft.app(target=main)
