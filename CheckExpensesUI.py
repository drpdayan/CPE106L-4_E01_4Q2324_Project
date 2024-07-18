import flet as ft
from flet import *


def main(page: ft.Page):
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf",
        "RobotoMono": "https://github.com/google/fonts/raw/main/apache/robotomono/RobotoMono%5Bwght%5D.ttf"
    }

    t = ft.Text()
    
    #Dropdown Menu
    def dropdown_changed(e):
        t.value = f"Dropdown changed to {dd.value}"
        page.update()

    dd = ft.Dropdown(
        hint_text='Enter Month',
        on_change=dropdown_changed,
        options=[
            ft.dropdown.Option("January"),
            ft.dropdown.Option("February"),
            ft.dropdown.Option("March"),
            ft.dropdown.Option("April"),
            ft.dropdown.Option("May"),
            ft.dropdown.Option("June"),
        ],
        width=200,
    )
    #PieChart
    electricity_val = 7500
    water_val = 1250
    rent_val = 8500
    outstanding_val = 0

    normal_radius = 100
    hover_radius = 110


    normal_badge_size = 35

    #Icon Template
    def badge(icon, iconsize):
        return ft.Container(
            ft.Icon(icon, size= iconsize),
            width=iconsize,
            height=iconsize,
            bgcolor=colors.TRANSPARENT,
        )

    #PieChart Hover
    def on_chart_event_pie(e: ft.PieChartEvent):
        for idx, section in enumerate(chart.sections):
            if idx == e.section_index:
                section.radius = hover_radius
                
            else:
                section.radius = normal_radius
        chart.update()

    #Pie Chart
    chart = ft.PieChart(
        
        sections=[
            ft.PieChartSection(
                rent_val,
                color=ft.colors.BROWN_300,
                radius=normal_radius,
                badge=badge(icons.OTHER_HOUSES_OUTLINED, normal_badge_size),
                badge_position=0.50,

            ),
            ft.PieChartSection(
                electricity_val,
                color=ft.colors.YELLOW,
                radius=normal_radius,
                badge=badge(icons.ELECTRIC_BOLT_OUTLINED, normal_badge_size),
                badge_position=0.50,

            ),
            ft.PieChartSection(
                water_val,
                color=ft.colors.BLUE_300,
                radius=normal_radius,
                badge=badge(ft.icons.WATER_DROP_OUTLINED, normal_badge_size),
                badge_position=0.50,
            ),
            ft.PieChartSection(
                outstanding_val,
                color=ft.colors.GREEN,
                radius=normal_radius,
                badge=badge(ft.icons.ATTACH_MONEY_ROUNDED, normal_badge_size),
                badge_position=0.50,
            ),
        ],
        sections_space=0,
        center_space_radius=55,
        on_chart_event=on_chart_event_pie,
        expand=True,     
    )





    t = Text()
    tb1 = TextField(label="Enter Unit", width=150)
    unittext = Text("Unit", font_family='RobotoMono', color="#D67229", size='20')
    tb2 = TextField(label="Enter Purpose")
    purposetext = Text("Month", font_family='RobotoMono', color="#D67229", size='20')
    


    b = ft.IconButton(icon=icons.SEARCH_ROUNDED, icon_color='#D67229',icon_size=50, on_click=dropdown_changed)
    page.add(Row([tb1,dd,b],alignment=MainAxisAlignment.CENTER
                 ),
             Row([t]),
             Row([chart])
            )
             


ft.app(target=main)