import flet as ft
from flet import *
import ExpensesLogic as elg


unit = "2C"

# def dataprep()
#     data = elg.get_unit_expense_all(unit)


def main(page: ft.Page):


    # Prepare data for chart
    months = [item["month_num"] for item in data]
    rent = [item["rent"] for item in data]
    electricity = [item["electricity"] for item in data]
    water = [item["water"] for item in data]
    outstanding_balance = [item["outstanding_balance"] for item in data]

    line_chart = ft.LineChart(
        [
            Line(Series(months, rent), color="blue", name="Rent"),
            Line(Series(months, electricity), color="orange", name="Electricity"),
            Line(Series(months, water), color="green", name="Water"),
            Line(Series(months, outstanding_balance), color="red", name="Outstanding Balance"),
        ],
        title=ft.Text("Monthly Expenses"),
        # Customize chart appearance as needed
    )

    page.add(line_chart)
    page.update()

ft.app(target=main)