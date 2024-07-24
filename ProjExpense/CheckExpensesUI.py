import flet as ft
from flet import *
import ExpensesLogic as elg


def main(page: ft.Page):
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf",
        "RobotoMono": "https://github.com/google/fonts/raw/main/apache/robotomono/RobotoMono%5Bwght%5D.ttf"
    }

    page.window.width = 750
    page.window.height = 250

    #Text Fields
    EnterUnit = TextField(label="Enter Unit", width=150)

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

    def allormonth():
        if MonthCheck.value == True:


            getit = elg.get_values(EnterUnit.value, MonthDropDown.value)
            u_val, m_val, r_val, e_val, w_val, o_val = getit

            page.update()

            expense_total = (r_val + e_val + w_val + o_val)
            rent_percent = (r_val/expense_total) *100
            elec_percent = (e_val/expense_total) *100
            wat_percent = (w_val/expense_total) *100
            out_percent = (o_val/expense_total) *100
            
            page.window.width = 750
            page.window.height = 1150

            #Pie Chart
            normal_radius = 150
            hover_radius = 165
            badge_size = 50
            normal_title_style = TextStyle( size= 1, color=colors.WHITE, weight=FontWeight.BOLD )
            hover_title_style = TextStyle( font_family= 'RobotoSlab' ,size=22, color='#f0a150', weight=FontWeight.BOLD, shadow=BoxShadow(blur_radius=2, color=colors.GREY_400),)

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

            page.clean()
            page.add(Row([EnterUnit,MonthDropDown,b],alignment=MainAxisAlignment.CENTER),
                    Row([Container(MonthCheck)], alignment=MainAxisAlignment.CENTER),
                    Container(chart, margin=125, alignment=alignment.center),
                    Row([RentContainer,], MainAxisAlignment.CENTER, spacing= -100),
                    Row([ElecContainer,], MainAxisAlignment.CENTER), 
                    Row([WaterContainer,], MainAxisAlignment.CENTER), 
                    Row([OutContainer,], MainAxisAlignment.CENTER),
                    Row([Container(b_delete, padding= 50)], alignment=MainAxisAlignment.CENTER),
            )
            page.update()



        elif MonthCheck.value == False:

            getall = elg.get_unit_expense_all(EnterUnit.value)

            page.window.width = 750
            page.window.height = 600

            # Extract column names from the dictionary keys
            columns = list(getall[0].keys())

            # Create DataColumn objects for each key with Text controls (numeric for Age)
            flet_columns = [
                ft.DataColumn(ft.Text(col_name, font_family="RobotoSlab", weight=FontWeight.BOLD, size=16))
                for col_name in columns
            ]

            # Create DataRow objects from each dictionary in the list
            flet_rows = []
            for x in getall:
                cells = [ft.DataCell(ft.Text(str(value), font_family="RobotoMono", weight=FontWeight.NORMAL, size=14)) for value in x.values()]
                flet_rows.append(ft.DataRow(cells=cells,))

            # Create the DataTable object
            table= DataTable(
                columns=flet_columns,
                rows=flet_rows,
                column_spacing=15,
                width=700,
                border_radius= 20
            )
            page.clean()
            page.add(
                        Row([EnterUnit,MonthDropDown,b],alignment=MainAxisAlignment.CENTER),
                        Row([Container(MonthCheck)], alignment=MainAxisAlignment.CENTER),
                        Row([Container(table)], alignment= MainAxisAlignment.CENTER),
                        
            )
            page.update()

    def search_clicked(e):
        allormonth()
        page.update()

    def delete_clicked(e):
        elg.delete_expense(EnterUnit.value, MonthDropDown.value)
        page.update()


    b = IconButton(icon=icons.SEARCH_ROUNDED, icon_color='#D67229', on_click=search_clicked, icon_size= 50 )
    b_delete = FilledButton("Delete Expense",icon=icons.DELETE_OUTLINE_ROUNDED, icon_color='white', on_click=delete_clicked, style= ButtonStyle(color= 'white', bgcolor= 'red'),)
    page.add(Row([EnterUnit,MonthDropDown,b],alignment=MainAxisAlignment.CENTER),
             Row([Container(MonthCheck)], alignment=MainAxisAlignment.CENTER),
            )
    # print(u_val, m_val, r_val, e_val, w_val, o_val)

    page.update()
    


ft.app(target=main)