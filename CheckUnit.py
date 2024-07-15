import flet as ft
import initiallogic as ilg  
from flet import *


def main(page: ft.Page):
  page.fonts = {
      "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf",
      "RobotoMono": "https://github.com/google/fonts/raw/main/apache/robotomono/RobotoMono%5Bwght%5D.ttf"
  }
  def button_clicked(e):
    if ilg.open_connection():
      t.value = "Connection ok..."
      lessee_info = ilg.check_unit(tb1.value)
      if lessee_info:  # Check if lessee information is found
        output_text = " "
        for field, value in lessee_info.items():
          output_text += f"{field}: {value}\n"
        t.value = output_text
      else:
        t.value = "Lessee not found."
    else:
      t.value = "NO connection..."
    page.update()

  t = Text(color='#D67229',
              weight=FontWeight.NORMAL,
              size=25,
              font_family="RobotoMono"
              )
  HeadingText = Text("Unit Status:", color='black',
                     weight=FontWeight.BOLD,
                     size=40,
                     tooltip="Home Page",
                     font_family="RobotoSlab")

  tb1 = ft.TextField(label="Enter Unit Number")
  b = ft.IconButton(icon=icons.SEARCH_SHARP, on_click=button_clicked)
  page.add(
    Row([tb1, b,]),
    Row([HeadingText], alignment=MainAxisAlignment.CENTER),
    Row([t], alignment=MainAxisAlignment.CENTER)
    )
ft.app(target=main)
