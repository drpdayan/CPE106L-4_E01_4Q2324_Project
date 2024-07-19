import flet as ft
from flet import *
import ExpensesLogic as elg


def main(page: ft.Page):
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf",
        "RobotoMono": "https://github.com/google/fonts/raw/main/apache/robotomono/RobotoMono%5Bwght%5D.ttf"
    }

    page.window.width = 750
    page.window.height = 1000

    #Text Fields
    EnterUnit = TextField(label="Enter Unit", width=150)
    uval = Text()
    mval = Text()
    rval = Text()
    eval = Text()
    wval = Text()
    oval = Text()
    allval = Text()
    get_uval =  Text()


    
    #Dropdown Menu
    MonthDropDown = ft.Dropdown(
        disabled= True,
        hint_text="Enter Month",
        options=[
            ft.dropdown.Option("January"), ft.dropdown.Option("February"), ft.dropdown.Option("March"), ft.dropdown.Option("April"), ft.dropdown.Option("May"), ft.dropdown.Option("June"), 
            ft.dropdown.Option("July"), ft.dropdown.Option("August"), ft.dropdown.Option("September"), ft.dropdown.Option("October"), ft.dropdown.Option("November"), ft.dropdown.Option("December"),
        ],
        width=200,
    )



    #CheckBox
    def checkbox_changed(e):
        MonthDropDown.disabled =  not e.control.value
        page.update()
    MonthCheck = ft.Checkbox(label="Search for Specific Month",label_position= LabelPosition.LEFT, on_change=checkbox_changed)


    def search_clicked(e):
        if MonthCheck.value == True:
            UnitMonthlyExpense = elg.get_unit_expense_month(EnterUnit.value, MonthDropDown.value)
            get_dict = UnitMonthlyExpense[0]
            uval.value = f"{get_dict['Unit']}"
            mval.value = f"{get_dict['Month']}"
            rval.value = f"{get_dict['Rent']}"
            eval.value = f"{get_dict['Electricity']}"
            wval.value = f"{get_dict['Water']}"
            oval.value = f"{get_dict['Outstanding Balance']}"     
            page.update()


        elif MonthCheck.value == False:
            getall = elg.get_unit_expense_all(EnterUnit.value)
            allval.value = f"{getall}"
            page.update()


    b = ft.IconButton(icon=icons.SEARCH_ROUNDED, icon_color='#D67229', on_click=search_clicked, icon_size= 50 )
    page.add(Row([EnterUnit,MonthDropDown,b],alignment=MainAxisAlignment.CENTER),
             Row([Container(MonthCheck)], alignment=MainAxisAlignment.CENTER),
             Row([uval, mval, rval, eval, wval, oval]),
             Row([get_uval]),
             Row([allval]),

            )
    page.update()
    


ft.app(target=main)