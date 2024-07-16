import flet as ft
from flet import *

def main(page: ft.Page):
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf",
        "RobotoMono": "https://github.com/google/fonts/raw/main/apache/robotomono/RobotoMono%5Bwght%5D.ttf"
    }
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}'"
        page.update()

    t = Text()
    tb1 = TextField(label="Enter Unit")
    unittext = Text(":Unit", font_family='RobotoMono', color="#D67229", size='20')
    tb2 = TextField(label="Enter Purpose")
    purposetext = Text(":Rental Purpose""\n""(Commerical/Residential/Vacant)", font_family='RobotoMono', color="#D67229", size='20')
    tb3 = TextField(label="Enter Name",)
    nametext = Text(":Name", font_family='RobotoMono', color="#D67229", size='20')
    tb4 = TextField(label="Enter TIN")
    tintext = Text(":Tax Identification Number", font_family='RobotoMono', color="#D67229", size='20')

    b = ft.ElevatedButton(text="Update", color='#D67229', on_click=button_clicked)
    page.add(Row([tb1,unittext]),
             Row([tb2,purposetext]),
             Row([tb3,nametext]), 
             Row([tb4,tintext]), 
             t, b
             )

ft.app(target=main)