import flet as ft
from flet import *
import ExpensesLogic as elg

def main(page: ft.Page):
    page.window_width = 900
    page.window_height =750

    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf",
        "RobotoMono": "https://github.com/google/fonts/raw/main/apache/robotomono/RobotoMono%5Bwght%5D.ttf"
    }

    def checkbox_changed(e):
        tb2.disabled =  not e.control.value
        page.update()

    def button_clicked(e):
        if c.value == False:
                out_bal = 0.00
                out_bal = float(out_bal)
                ren = tb3.value
                ren = float(ren)
                elec = tb4.value
                elec = float(elec)
                wat = tb5.value
                wat = float(wat)
                paid = tb6.value
                paid = float(paid)

        elif c.value == True:
                out_bal = tb2.value
                ren = tb3.value
                elec = tb4.value
                wat = tb5.value
                paid = tb6.value
                out_bal = float(out_bal)
                ren = float(ren)
                elec = float(elec)
                wat = float(wat)
                paid = float(paid)
        
        totalval = out_bal+ren+elec+wat
        pendingval = totalval-paid
        
        try:
            elg.add_expense(tb1.value, MonthDropDown.value, c.value, out_bal, ren, elec, wat, paid, pendingval, totalval)
            t.value = f"Outstanding Balance for Next Month: ₱{pendingval:.2f}"
            print(pendingval)
        except:
            t.value = "ERROR! TRY AGAIN"
        page.update()
        
    t = Text()
    tb1 = TextField(label="Enter Unit", width= 200)
    unittext = Text(":Unit", font_family='RobotoMono', color="#D67229", size='20')
    c = ft.Checkbox(label="Outstanding Balance?",label_position= LabelPosition.LEFT, on_change=checkbox_changed)
    MonthDropDown = ft.Dropdown(
        hint_text= "Enter Month",
        width=200,
        options=[
            ft.dropdown.Option("January"), ft.dropdown.Option("February"), ft.dropdown.Option("March"), ft.dropdown.Option("April"), ft.dropdown.Option("May"), ft.dropdown.Option("June"), 
            ft.dropdown.Option("July"), ft.dropdown.Option("August"), ft.dropdown.Option("September"), ft.dropdown.Option("October"), ft.dropdown.Option("November"), ft.dropdown.Option("December")
        ],
    )
    tb2 = TextField(label="Enter Outstanding Balance", disabled=True)
    outtext = Text(":Outstanding Balance", font_family='RobotoMono', color="#D67229", size='20')
    tb3 = TextField(label="Enter Rent")
    renttext = Text(":Rent", font_family='RobotoMono', color="#D67229", size='20')
    tb4 = TextField(label="Enter Electricity")
    electext = Text(":Electricity", font_family='RobotoMono', color="#D67229", size='20')
    tb5 = TextField(label="Enter Water")
    watertext = Text(":Water", font_family='RobotoMono', color="#D67229", size='20')
    monthtext = Text(":Month", font_family='RobotoMono', color="#D67229", size='20')
    t = Text(color='gray', weight=FontWeight.BOLD, size=25, font_family="RobotoSlab")
    tb6 = TextField(label="Enter Amount Paid")
    paidtext = Text(":Amount Paid", font_family='RobotoMono', color="#D67229", size='20')
    

    b = ft.ElevatedButton(text="Add Expense", color='#D67229', on_click=button_clicked)
    page.add(Row([tb1,unittext]),
             Row([MonthDropDown, monthtext]), 
             Row([c]),
             Row([tb2,outtext]),
             Row([tb3,renttext]), 
             Row([tb4,electext]), 
             Row([tb5,watertext]),
             Row([tb6,paidtext]), b ,
             Row([t], alignment=MainAxisAlignment.CENTER)
             )
    page.update()
ft.app(target=main)