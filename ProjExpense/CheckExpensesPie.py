import flet as ft
from flet import *
import ExpensesLogic as elg




def main(page: ft.Page):
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf",
        "RobotoMono": "https://github.com/google/fonts/raw/main/apache/robotomono/RobotoMono%5Bwght%5D.ttf"
    }

    unit = "3E"
    month = "May"

    page.window.width = 750
    page.window.height = 1000



    getit = elg.get_values(unit, month)
    u_val, m_val, r_val, e_val, w_val, o_val = getit
    # print(u_val, m_val, r_val, e_val, w_val, o_val)
    # get_uval.value= f"{u_val}"
    page.update()

    #Pie Chart
    normal_radius = 100
    hover_radius = 110
    badge_size = 35

    #Icon Template
    def badge(icon, iconsize):
        return ft.Container(
            ft.Icon(icon, size= iconsize), width=iconsize, height=iconsize, bgcolor=colors.TRANSPARENT
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
                r_val,
                color=ft.colors.BROWN_300,
                radius=normal_radius,
                badge=badge(icons.OTHER_HOUSES_OUTLINED, badge_size),
                badge_position=0.50,

            ),
            ft.PieChartSection(
                e_val,
                color=ft.colors.YELLOW,
                radius=normal_radius,
                badge=badge(icons.ELECTRIC_BOLT_OUTLINED, normal_badge_size),
                badge_position=0.50,

            ),
            ft.PieChartSection(
                w_val,
                color=ft.colors.BLUE_300,
                radius=normal_radius,
                badge=badge(ft.icons.WATER_DROP_OUTLINED, normal_badge_size),
                badge_position=0.50,
            ),
            ft.PieChartSection(
                o_val,
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

    # b = ft.IconButton(icon=icons.SEARCH_ROUNDED, icon_color='#D67229', on_click=search_clicked, icon_size= 50 )
    page.add(Row([chart])

            )
    page.update()
    


ft.app(target=main)