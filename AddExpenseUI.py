import flet as ft
from flet import *
import ExpensesLogic as elg

def main(page: ft.Page):
    page.window_width = 900
    page.window_height =750
    def checkbox_changed(e):
        tb2.disabled =  not e.control.value
        page.update()
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf",
        "RobotoMono": "https://github.com/google/fonts/raw/main/apache/robotomono/RobotoMono%5Bwght%5D.ttf"
    }
    def button_clicked(e):
        if c.value == False:
                out_bal = 0.00
                ren = tb3.value
                elec = tb4.value
                wat = tb5.value

        elif c.value == True:
                out_bal = tb2.value
                ren = tb3.value
                elec = tb4.value
                wat = tb5.value
        # if elg.check_unit(tb1.value):
        #     # t.value = "Connection ok..."
        #     check_unit = elg.check_unit(tb1.value)
        #     if check_unit:  # Check if lessee information is found
        try:
            elg.add_expense(tb1.value, dd.value, c.value, out_bal, ren, elec, wat)
            t.value = "UNIT STATUS UPDATED"
        except:
            t.value = "ERROR! TRY AGAIN"
        
        #     else:
        #         t.value = "UNIT NOT FOUND! TRY AGAIN"
        # else:
        #     t.value = "NO CONNECTION"

        # print(tb1.value)
        # print(dd.value)
        # print(c.value)
        # print(out_bal)
        # print(ren)
        # print(elec)
        # print(wat)

        page.update()

    t = Text()
    tb1 = TextField(label="Enter Unit", width= 200)
    unittext = Text(":Unit", font_family='RobotoMono', color="#D67229", size='20')
    c = ft.Checkbox(label="Outstanding Balance?",label_position= LabelPosition.LEFT, on_change=checkbox_changed)
    dd = ft.Dropdown(
        hint_text= "Enter Month",
        width=200,
        options=[
            ft.dropdown.Option("January"),
            ft.dropdown.Option("February"),
            ft.dropdown.Option("March"),
            ft.dropdown.Option("April"),
            ft.dropdown.Option("May"),
            ft.dropdown.Option("June"),
            ft.dropdown.Option("July"),
        ],
    )
    tb2 = TextField(label="Enter Outstanding Balance", disabled=True)
    outtext = Text(":Outstanding Balance", font_family='RobotoMono', color="#D67229", size='20')
    tb3 = TextField(label="Enter Rent")
    renttext = Text("Rent", font_family='RobotoMono', color="#D67229", size='20')
    tb4 = TextField(label="Enter Electricity")
    electext = Text("Electricity", font_family='RobotoMono', color="#D67229", size='20')
    tb5 = TextField(label="Enter Water")
    watertext = Text("Water", font_family='RobotoMono', color="#D67229", size='20')
    monthtext = Text("Month", font_family='RobotoMono', color="#D67229", size='20')
    t = Text(color='gray', weight=FontWeight.BOLD, size=25, font_family="RobotoSlab")

    b = ft.ElevatedButton(text="Add Expense", color='#D67229', on_click=button_clicked)
    page.add(Row([tb1,unittext]),
             Row([dd, monthtext]), 
             Row([c]),
             Row([tb2,outtext]),
             Row([tb3,renttext]), 
             Row([tb4,electext]), 
             Row([tb5,watertext]),  
             Row([t], alignment=MainAxisAlignment.CENTER)
             , b
             )

ft.app(target=main)