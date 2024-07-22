import flet as ft
from flet import *
import ExpensesLogic as elg




def main(page: ft.Page):
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf",
        "RobotoMono": "https://github.com/google/fonts/raw/main/apache/robotomono/RobotoMono%5Bwght%5D.ttf"
    }

    unit = "3E"
    month = "February"

    page.window.width = 750
    page.window.height = 1000



    getit = elg.get_values(unit, month)
    u_val, m_val, r_val, e_val, w_val, o_val = getit
    # print(u_val, m_val, r_val, e_val, w_val, o_val)
    # get_uval.value= f"{u_val}"
    page.update()

    expense_total = (r_val + e_val + w_val + o_val)
    rent_percent = (r_val/expense_total) *100
    elec_percent = (e_val/expense_total) *100
    wat_percent = (w_val/expense_total) *100
    out_percent = (o_val/expense_total) *100
    


    #Pie Chart
    normal_radius = 150
    hover_radius = 165
    badge_size = 50
    normal_title_style = TextStyle( size= 1, color=colors.WHITE, weight=FontWeight.BOLD )
    hover_title_style = TextStyle( font_family= 'RobotoSlab' ,size=22, color=colors.WHITE, weight=FontWeight.BOLD, shadow=BoxShadow(blur_radius=2, color=colors.BLACK54), )

    #Icon Template
    def badge(icon, iconsize, expensepercent):
        return ft.Container(
            ft.Icon(icon, size= iconsize, tooltip= f"{expensepercent:.2f}%"), width=iconsize, height=iconsize, bgcolor=colors.TRANSPARENT, 
            )

    #PieChart Hover
    def on_chart_event_pie(e: ft.PieChartEvent):
        for idx, section in enumerate(chart.sections):
            if idx == e.section_index:
                section.radius = hover_radius
                section.title_style = hover_title_style
                
            else:
                section.radius = normal_radius
                section.title_style = normal_title_style
        chart.update()

    #Pie Chart
    chart = ft.PieChart(
        
        sections=[
            ft.PieChartSection(
                r_val,
                title=f"Rent: \n ₱ {r_val:.2f} ",
                title_position=1.25 ,
                title_style=normal_title_style,
                color=ft.colors.BROWN_400,
                radius=normal_radius,
                badge=badge(icons.OTHER_HOUSES, badge_size, rent_percent),
                badge_position=0.50,

            ),
            ft.PieChartSection(
                e_val,
                title=f"Electricity: \n ₱ {e_val:.2f} ",
                title_position=1.25,
                title_style=normal_title_style,
                color=ft.colors.YELLOW_400,
                radius=normal_radius,
                badge=badge(icons.ELECTRIC_BOLT, badge_size, elec_percent),
                badge_position=0.50,

            ),
            ft.PieChartSection(
                w_val,
                title=f"Water: \n ₱ {w_val:.2f} ",
                title_position=1.25,
                title_style=normal_title_style,
                color=ft.colors.BLUE_400,
                radius=normal_radius,
                badge=badge(ft.icons.WATER_DROP, badge_size, wat_percent),
                badge_position=0.50,
            ),
            ft.PieChartSection(
                o_val,
                title=f"Oustanding Balance: \n ₱ {o_val:.2f} ",
                title_position=1.25,
                title_style=normal_title_style,
                color=ft.colors.GREEN_400,
                radius=normal_radius,
                badge=badge(ft.icons.ATTACH_MONEY, badge_size, out_percent),
                badge_position=0.50,
            ),
        ],
        sections_space=0,
        center_space_radius=35,
        on_chart_event=on_chart_event_pie,
        expand=True,     
    )

    RentContainer = Container(
                        theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
                        # theme_mode=ft.ThemeMode.DARK,
                        content=Text(f"RENT: ₱{r_val:.2f} ", font_family='RobotoSlab', weight=FontWeight.BOLD, color="Gray", size='20'), 
                        bgcolor=ft.colors.BROWN_400,
                        padding=20,
                        width=450,
                        border_radius=30,ink=True,
                        )
    # RentIcon = Container(Icon(icons.ELECTRIC_BOLT), border=ft.border.all(ft.colors.BROWN_300), width=70, height = 70, border_radius= 200)
    ElecContainer = Container(
                        theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
                        # theme_mode=ft.ThemeMode.DARK,
                        content=Text(f"ELECTRICITY: ₱{e_val:.2f} ", font_family='RobotoSlab', weight=FontWeight.BOLD, color="Gray", size='20'), 
                        bgcolor=ft.colors.YELLOW_400,
                        padding=20,
                        width=450,
                        border_radius=30,  
                        )

    WaterContainer = Container(
                        theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
                        # theme_mode=ft.ThemeMode.DARK,
                        content=Text(f"WATER: ₱{w_val:.2f} ", font_family='RobotoSlab', weight=FontWeight.BOLD, color="Gray", size='20'),
                        bgcolor=ft.colors.BLUE_400,
                        padding=20,
                        width=450,
                        border_radius=30,  
                        )

    OutContainer = Container(
                        theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
                        # theme_mode=ft.ThemeMode.DARK,
                        content=Text(f"OUTSTANDING: ₱{o_val:.2f} ", font_family='RobotoSlab', weight=FontWeight.BOLD, color="Gray", size='20'),
                        bgcolor=ft.colors.GREEN_400,
                        padding=20,
                        width=450,
                        border_radius=30,  
                        )

    # b = ft.IconButton(icon=icons.SEARCH_ROUNDED, icon_color='#D67229', on_click=search_clicked, icon_size= 50 )
    page.add(Container(chart, margin=125, alignment=alignment.center),
              Row([RentContainer,], MainAxisAlignment.CENTER, spacing= -100),
              Row([ElecContainer,], MainAxisAlignment.CENTER), 
              Row([WaterContainer,], MainAxisAlignment.CENTER), 
              Row([OutContainer,], MainAxisAlignment.CENTER),  
            )

            
    page.update()
    


ft.app(target=main)