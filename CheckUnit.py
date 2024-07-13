import flet as ft
import initiallogic as ilg  


def main(page: ft.Page):
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

  t = ft.Text(color='#7B3F00')
  tb1 = ft.TextField(label="Enter Unit Number")
  b = ft.ElevatedButton(text="Check", on_click=button_clicked)
  page.add(
    ft.Row(controls=[tb1, b]), t) 

ft.app(target=main)
