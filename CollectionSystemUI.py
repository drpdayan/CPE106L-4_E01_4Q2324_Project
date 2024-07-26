import flet as ft
from flet import *
import initiallogic as ilg 
from initiallogic import get_lessee_list as gll
import ExpensesLogic as elg


def main(page: Page) -> None:
    page.title = 'Application Collection System'
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf",
        "RobotoMono": "https://github.com/google/fonts/raw/main/apache/robotomono/RobotoMono%5Bwght%5D.ttf"
    }
    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        #Home Page
        page.window.width = 800
        page.window.height = 550
        page.views.append(
            View(
                route = '/',
                controls = [
                    AppBar(title=Text('Home Page', font_family='RobotoSlab',weight=FontWeight.BOLD , size='28' , color=colors.GREY_800), bgcolor='#f0a150'),
                    # ElevatedButton(text= 'New Window', on_click=lambda _:page.go('/store')),
                    Row(
                        [
                        Container(
                                content= Row([IconButton(
                                                        icon=ft.icons.PERSON_OUTLINE,
                                                        icon_color="White",
                                                        icon_size=75,
                                                        
                                                    ),
                                                Text("Lessee Profile", font_family='RobotoMono',weight=FontWeight.BOLD , size='40' , color=colors.WHITE),
                                            ]
                                        ),
                                
                                padding = 7.5,
                                bgcolor= "#D67229",
                                shape= BoxShape.RECTANGLE,
                                border_radius= 70,
                                ink = True,
                                on_click=lambda _:page.go('/poutline'),
                                width= 525, margin= 5, tooltip="Lessee Profile"
                        )
                        ], alignment=MainAxisAlignment.CENTER
                    ),

                    Row(
                        [
                        Container(
                                content= Row([IconButton(
                                                        icon=ft.icons.SENSOR_DOOR_OUTLINED,
                                                        icon_color="White",
                                                        icon_size=100,
                                                        
                                                    ),
                                                Text("Unit Status", font_family='RobotoMono',weight=FontWeight.BOLD , size='40' , color=colors.WHITE),
                                            ]
                                        ),

                                padding = 7.5,
                                bgcolor= "#D67229",
                                shape= BoxShape.RECTANGLE,
                                border_radius= 70,
                                ink = True,
                                on_click=lambda _:page.go('/ustatus'),
                                width= 525, margin= 5, tooltip="Unit Status"
                        )
                        ], alignment=MainAxisAlignment.CENTER
                    ),

                    Row(
                        [
                        Container(
                                content= Row([IconButton(
                                                        icon=ft.icons.ATTACH_MONEY_ROUNDED,
                                                        icon_color="White",
                                                        icon_size=100,
                                                        
                                                    ),
                                                Text("Unit Expenses", font_family='RobotoMono',weight=FontWeight.BOLD , size='40' , color=colors.WHITE),
                                            ]
                                        ),

                                padding = 7.5,
                                bgcolor= "#D67229",
                                shape= BoxShape.RECTANGLE,
                                border_radius= 70,
                                ink = True,
                                on_click=lambda _:page.go('/payment'),
                                width= 525, margin= 5, tooltip="Expenses"
                        )
                        ], alignment=MainAxisAlignment.CENTER
                    ),


                ],

            ),

        )
    
        #Lessee_Information Page
        if page.route == '/poutline':
            glist = gll()
            def lesseeinfo_button_clicked(e):
                if ilg.open_connection():
                    t.value = "Connection ok..."
                    lessee_info = ilg.find_lessee(tb1.value)
                    if lessee_info:  # Check if lessee information is found
                        output_text = ""
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
                font_family="RobotoMono",
                )
            HeadingText = Text("Lessee Info:", color='black',
                weight=FontWeight.BOLD,
                size=40,
                tooltip="Home Page",
                font_family="RobotoSlab")
            Edit_Lessee = ElevatedButton("Update Lessee",
                                         icon=icons.UPDATE_ROUNDED,
                                         icon_color="gray",
                                         color="#D67229",
                                         on_click=lambda _:page.go('/ulessee')
                                         )
 

            tb1 = TextField(label="Enter Unit")
            b = IconButton(icon=icons.SEARCH_ROUNDED, icon_color='#D67229', icon_size= 50,  on_click=lesseeinfo_button_clicked)
            page.window.width = 750
            page.window.height = 400
            page.views.append(
                #Top Layer
                View(
                    route = '/poutline',
                    controls = [
                        AppBar(title=Text('Lessee Profile', font_family='RobotoSlab',weight=FontWeight.NORMAL , size='28' , color=colors.GREY_900), bgcolor='#f0a150'),

                        Row([tb1, b, Edit_Lessee]),
                        Row([HeadingText], alignment=CrossAxisAlignment.START),
                        Row([t],alignment=MainAxisAlignment.START),

                    ]  
                ),  
            )


        #Update_Lessee Page
        if page.route == '/ulessee':
            def lessee_button_clicked(e):
                if ilg.open_connection():
                    t.value = "Connection ok..."
                    lessee_info = ilg.update_lessee(vunit.value, PurposeDropDown.value, vname.value, vtin.value)
                    if lessee_info:  # Check if lessee information is found
                        ilg.update_lessee(vunit.value, PurposeDropDown.value, vname.value, vtin.value)
                        if ilg.update_lessee:
                            t.value = "LESSEE INFORMATION UPDATED"
                        else:
                            t.value = "ERROR! TRY AGAIN"
                        
                    else:
                        t.value = "ERROR! TRY AGAIN"
                else:
                    t.value = "NO CONNECTION"
                page.update()
            t = Text(color='gray', weight=FontWeight.BOLD, size=25, font_family="RobotoSlab",)

            PurposeDropDown = Dropdown(
                hint_text= "Enter Purpose",
                options=[
                    dropdown.Option("Commercial"), dropdown.Option("Residential"), dropdown.Option("Vacant"), 
                ], 
            )
            
            vunit = TextField(label="Enter Unit")
            unittext = Text(":Unit", font_family='RobotoMono', color="#D67229", size='20')          
            purposetext = Text(":Rental Purpose""\n""(Commercial/Residential/Vacant)", font_family='RobotoMono', color="#D67229", size='20')
            vname = TextField(label="Enter Name",)
            nametext = Text(":Name", font_family='RobotoMono', color="#D67229", size='20')
            vtin = TextField(label="Enter TIN")
            tintext = Text(":Tax Identification Number", font_family='RobotoMono', color="#D67229", size='20')
            b = ElevatedButton(text="Update", color='#D67229', on_click=lessee_button_clicked)

            page.window.width = 750
            page.window.height = 475
            page.views.append(
                #Top Layer
                View(
                    route = '/poutline',
                    controls = [
                        AppBar(title=Text('Edit Lessee', font_family='RobotoSlab',weight=FontWeight.NORMAL , size='28' , color=colors.GREY_900), bgcolor='#f0a150'),
                        Row([vunit,unittext]),
                        Row([PurposeDropDown,purposetext]),
                        Row([vname,nametext]), 
                        Row([vtin,tintext]),
                        Row([b]),
                        Row([t], alignment=MainAxisAlignment.CENTER) 


                    ]  
                ),  
            )


        #Unit_Status Page
        if page.route == '/ustatus':
            def unitinfo_button_clicked(e):
                if ilg.open_connection():
                    t.value = "Connection ok..."
                    unit_info = ilg.check_unit(tb1.value)
                    if unit_info:  # Check if lessee information is found
                        output_text = ""
                        for field, value in unit_info.items():
                            output_text += f"{field}: {value}\n"
                        t.value = output_text
                    else:
                        t.value = "UNIT NOT FOUND"
                else:
                    t.value = "NO connection..."
                page.update()
            t = Text(color='#D67229',
                weight=FontWeight.NORMAL,
                size=25,
                font_family="RobotoMono",
                )
            HeadingText = Text("Unit Status:", color='black',
                weight=FontWeight.BOLD,
                size=40,
                tooltip="Home Page",
                font_family="RobotoSlab")
            Edit_Lessee = ElevatedButton("Update Unit",
                                         icon=icons.UPDATE_ROUNDED,
                                         icon_color="gray",
                                         color="#D67229",
                                         on_click=lambda _:page.go('/uunit') 
                                         )
 

            tb1 = TextField(label="Enter Unit")
            b = IconButton(icon=icons.SEARCH_ROUNDED, icon_color='#D67229', icon_size= 50,  on_click=unitinfo_button_clicked)
            page.window.width = 600
            page.window.height = 400
            page.views.append(
                #Top Layer
                View(
                    route = '/ustatus',
                    controls = [
                        AppBar(title=Text('Unit Status', font_family='RobotoSlab',weight=FontWeight.NORMAL , size='28' , color=colors.GREY_900), bgcolor='#f0a150'),
                        Row([tb1, b, Edit_Lessee]),
                        Row([HeadingText], alignment=CrossAxisAlignment.START),
                        Row([t],alignment=MainAxisAlignment.START),

                    ]  
                ),  
            )


        #Update_unit Page
        if page.route == '/uunit':
            def unit_button_clicked(e):
                if ilg.open_connection():
                    # t.value = "Connection ok..."
                    check_unit = ilg.update_unit(vunit1.value, OccupancyDropDown.value, vdate.value)
                    if check_unit:  # Check if lessee information is found
                        ilg.update_unit(vunit1.value, OccupancyDropDown.value, vdate.value)
                        if ilg.update_unit:
                            t.value = "UNIT STATUS UPDATED"
                        else:
                            t.value = "ERROR! TRY AGAIN"
                        
                    else:
                        t.value = "ERROR! TRY AGAIN"
                else:
                    t.value = "NO CONNECTION"
                page.update()

            t = Text(color='gray',
                weight=FontWeight.BOLD,
                size=25,
                font_family="RobotoSlab",
                )

            OccupancyDropDown = Dropdown(
                hint_text= "Enter Status",
                options=[
                    dropdown.Option("Occupied"), dropdown.Option("Vacant"), 
                ], 
            )

            vunit1 = TextField(label="Enter Unit")
            unittext1 = Text(":Unit", font_family='RobotoMono', color="#D67229", size='20')
            statustext = Text(":Occupancy Status (Occupied/Vacant)", font_family='RobotoMono', color="#D67229", size='20')
            vdate = TextField(label="Enter Date")
            datetext = Text(":Lease Date (dd/mm/yyyy)", font_family='RobotoMono', color="#D67229", size='20')
            b = ElevatedButton(text="Update", color='#D67229', on_click=unit_button_clicked)
            
            page.window.width = 800
            page.window.height = 400
            page.views.append(
                #Top Layer
                View(
                    route = '/uunit',
                    controls = [
                        AppBar(title=Text('Edit Unit', font_family='RobotoSlab',weight=FontWeight.NORMAL , size='28' , color=colors.GREY_900), bgcolor='#f0a150'),
                        Row([vunit1,unittext1]),
                        Row([OccupancyDropDown,statustext]),
                        Row([vdate,datetext]), 
                        Row([b]),
                        Row([t], alignment=MainAxisAlignment.CENTER)     
                    ]  
                ),
            )
            

        #Payments Page
        if page.route == '/payment':

            page.window.width = 750
            page.window.height = 200
            #Text Fields
            EnterUnit = TextField(label="Enter Unit", width=150)

            #Dropdown Menu
            MonthDropDown = Dropdown(
                disabled= True,
                hint_text="Enter Month",
                options=[
                    dropdown.Option("January"), dropdown.Option("February"), dropdown.Option("March"), dropdown.Option("April"), dropdown.Option("May"), dropdown.Option("June"), 
                    dropdown.Option("July"), dropdown.Option("August"), dropdown.Option("September"), dropdown.Option("October"), dropdown.Option("November"), dropdown.Option("December"),
                ],
                width=200,
            )
            #CheckBox
            def checkbox_changed(e):
                MonthDropDown.disabled =  not e.control.value
                page.update()
            MonthCheck = Checkbox(label="Search for Specific Month",label_position= LabelPosition.LEFT, on_change=checkbox_changed)

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
                    page.window.height = 1200

                    #Pie Chart
                    normal_radius = 150
                    hover_radius = 165
                    badge_size = 50
                    normal_title_style = TextStyle( size= 1, color=colors.WHITE, weight=FontWeight.BOLD )
                    hover_title_style = TextStyle( font_family= 'RobotoSlab' ,size=22, color='#f0a150', weight=FontWeight.BOLD, shadow=BoxShadow(blur_radius=2, color=colors.GREY_400), )

                    #Icon Template
                    def badge(icon, iconsize, expensepercent):
                        return Container(
                            Icon(icon, size= iconsize, tooltip= f"{expensepercent:.2f}%"), width=iconsize, height=iconsize, bgcolor=colors.TRANSPARENT, 
                            )

                    #PieChart Hover
                    def on_chart_event_pie(e: PieChartEvent):
                        for idx, section in enumerate(chart.sections):
                            if idx == e.section_index:
                                section.radius = hover_radius
                                section.title_style = hover_title_style
                                
                            else:
                                section.radius = normal_radius
                                section.title_style = normal_title_style
                        chart.update()

                    #Pie Chart
                    chart = PieChart(
                        
                        sections=[
                            PieChartSection(
                                r_val,
                                title=f"Rent: \n ₱ {r_val:.2f} ",
                                title_position=1.25 ,
                                title_style=normal_title_style,
                                color=colors.BROWN_400,
                                radius=normal_radius,
                                badge=badge(icons.OTHER_HOUSES, badge_size, rent_percent),
                                badge_position=0.50,

                            ),
                            PieChartSection(
                                e_val,
                                title=f"Electricity: \n ₱ {e_val:.2f} ",
                                title_position=1.25,
                                title_style=normal_title_style,
                                color=colors.YELLOW_400,
                                radius=normal_radius,
                                badge=badge(icons.ELECTRIC_BOLT, badge_size, elec_percent),
                                badge_position=0.50,

                            ),
                            PieChartSection(
                                w_val,
                                title=f"Water: \n ₱ {w_val:.2f} ",
                                title_position=1.25,
                                title_style=normal_title_style,
                                color=colors.BLUE_400,
                                radius=normal_radius,
                                badge=badge(icons.WATER_DROP, badge_size, wat_percent),
                                badge_position=0.50,
                            ),
                            PieChartSection(
                                o_val,
                                title=f"Oustanding Balance: \n ₱ {o_val:.2f} ",
                                title_position=1.25,
                                title_style=normal_title_style,
                                color=colors.GREEN_400,
                                radius=normal_radius,
                                badge=badge(icons.ATTACH_MONEY, badge_size, out_percent),
                                badge_position=0.50,
                            ),
                        ],
                        sections_space=0,
                        center_space_radius=35,
                        on_chart_event=on_chart_event_pie,
                        expand=True,     
                    )

                    RentContainer = Container(
                                        theme=Theme(color_scheme_seed=colors.INDIGO),
                                        # theme_mode=ThemeMode.DARK,
                                        content=Text(f"RENT: ₱{r_val:.2f} ", font_family='RobotoSlab', weight=FontWeight.BOLD, color="Gray", size='20'), 
                                        bgcolor=colors.BROWN_400,
                                        padding=20,
                                        width=450,
                                        border_radius=30,ink=True,
                                        )
                    # RentIcon = Container(Icon(icons.ELECTRIC_BOLT), border=border.all(colors.BROWN_300), width=70, height = 70, border_radius= 200)
                    ElecContainer = Container(
                                        theme=Theme(color_scheme_seed=colors.INDIGO),
                                        # theme_mode=ThemeMode.DARK,
                                        content=Text(f"ELECTRICITY: ₱{e_val:.2f} ", font_family='RobotoSlab', weight=FontWeight.BOLD, color="Gray", size='20'), 
                                        bgcolor=colors.YELLOW_400,
                                        padding=20,
                                        width=450,
                                        border_radius=30,  
                                        )

                    WaterContainer = Container(
                                        theme=Theme(color_scheme_seed=colors.INDIGO),
                                        # theme_mode=ThemeMode.DARK,
                                        content=Text(f"WATER: ₱{w_val:.2f} ", font_family='RobotoSlab', weight=FontWeight.BOLD, color="Gray", size='20'),
                                        bgcolor=colors.BLUE_400,
                                        padding=20,
                                        width=450,
                                        border_radius=30,  
                                        )

                    OutContainer = Container(
                                        theme=Theme(color_scheme_seed=colors.INDIGO),
                                        # theme_mode=ThemeMode.DARK,
                                        content=Text(f"OUTSTANDING: ₱{o_val:.2f} ", font_family='RobotoSlab', weight=FontWeight.BOLD, color="Gray", size='20'),
                                        bgcolor=colors.GREEN_400,
                                        padding=20,
                                        width=450,
                                        border_radius=30,  
                                        )

                    page.clean()
                    page.views.append(
                        View(
                            route = '/payment',
                            controls = [
                                AppBar(title=Text('Payments', font_family='RobotoSlab',weight=FontWeight.NORMAL , size='28' , color=colors.GREY_900), bgcolor='#f0a150'),
                                # IconButton(
                                #     icon=icons.HOME_ROUNDED, icon_color="black", icon_size=75, tooltip="Home Page", on_click=lambda _:page.go('/')
                                # ),
                                Row([EnterUnit,MonthDropDown,b, Go_AddExpenses],alignment=MainAxisAlignment.CENTER),
                                Row([Container(MonthCheck)], alignment=MainAxisAlignment.CENTER),
                                Container(chart, margin=125, alignment=alignment.center),
                                Row([RentContainer,], MainAxisAlignment.CENTER, spacing= -100),
                                Row([ElecContainer,], MainAxisAlignment.CENTER), 
                                Row([WaterContainer,], MainAxisAlignment.CENTER), 
                                Row([OutContainer,], MainAxisAlignment.CENTER),
                                Row([Container(b_delete, padding= 50)], alignment=MainAxisAlignment.CENTER),       
                            ]  
                        ),
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
                        DataColumn(Text(col_name, font_family="RobotoSlab", weight=FontWeight.BOLD, size=16))
                        for col_name in columns
                    ]

                    # Create DataRow objects from each dictionary in the list
                    flet_rows = []
                    for x in getall:
                        cells = [DataCell(Text(str(value), font_family="RobotoMono", weight=FontWeight.NORMAL, size=14)) for value in x.values()]
                        flet_rows.append(DataRow(cells=cells,))

                    # Create the DataTable object
                    table= DataTable(
                        columns=flet_columns,
                        rows=flet_rows,
                        column_spacing=15,
                        width=700,
                        border_radius= 20
                    )
                    page.clean()
                    page.views.append(
                        View(
                            route = '/payment',
                            controls = [
                                #Top Layer
                                AppBar(title=Text('Payments', font_family='RobotoSlab',weight=FontWeight.NORMAL , size='28' , color=colors.GREY_900), bgcolor='#f0a150'),
                                # IconButton(
                                #     icon=icons.HOME_ROUNDED, icon_color="black", icon_size=75, tooltip="Home Page", on_click=lambda _:page.go('/')
                                # ),
                                Row([EnterUnit,MonthDropDown,b, Go_AddExpenses],alignment=MainAxisAlignment.CENTER),
                                Row([Container(MonthCheck)], alignment=MainAxisAlignment.CENTER),
                                Row([Container(table)], alignment= MainAxisAlignment.CENTER)
            
                            ]  
                        ),
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
            Go_AddExpenses = ElevatedButton("Add Unit Expenses",
                                         icon=icons.UPDATE_ROUNDED,
                                         icon_color="gray",
                                         color="#D67229",
                                         on_click=lambda _:page.go('/apayment') 
                                         )
            page.window.width = 900
            page.window.height =750
            page.views.append(
                View(
                    route = '/payment',
                    controls = [
                        #Top Layer
                        AppBar(title=Text('Payments',  font_family='RobotoSlab',weight=FontWeight.NORMAL , size='28' , color=colors.GREY_900), bgcolor='#f0a150'),
                        # IconButton(
                        #     icon=icons.HOME_ROUNDED, icon_color="black", icon_size=75, tooltip="Home Page", on_click=lambda _:page.go('/')
                        # ),
                        Row([EnterUnit,MonthDropDown,b, Go_AddExpenses],alignment=MainAxisAlignment.CENTER),
                        Row([Container(MonthCheck)], alignment=MainAxisAlignment.CENTER),     
                    ]  
                ),
            )
            page.update()

        #Add_Payments Page
        if page.route == '/apayment':
            page.window.width = 900
            page.window.height =750

            def checkbox_changed(e):
                tb2.disabled =  not e.control.value
                page.update()

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

                try:
                    elg.add_expense(tb1.value, MonthDropDown.value, c.value, out_bal, ren, elec, wat)
                    t.value = "UNIT STATUS UPDATED"
                except:
                    t.value = "ERROR! TRY AGAIN"
                page.update()
                    
            t = Text()
            tb1 = TextField(label="Enter Unit", width= 200)
            unittext = Text(":Unit", font_family='RobotoMono', color="#D67229", size='20')
            c = Checkbox(label="Outstanding Balance?",label_position= LabelPosition.LEFT, on_change=checkbox_changed)
            MonthDropDown = Dropdown(
                hint_text= "Enter Month",
                width=200,
                options=[
                    dropdown.Option("January"), dropdown.Option("February"), dropdown.Option("March"), dropdown.Option("April"), dropdown.Option("May"), dropdown.Option("June"), 
                    dropdown.Option("July"), dropdown.Option("August"), dropdown.Option("September"), dropdown.Option("October"), dropdown.Option("November"), dropdown.Option("December")
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

            b_update = ElevatedButton(text="Add Expense", color='#D67229', on_click=button_clicked)

            page.views.append(
                View(
                    route = '/apayment',
                    controls = [
                        #Top Layer
                        AppBar(title=Text('Add Payments',  font_family='RobotoSlab',weight=FontWeight.NORMAL , size='28' , color=colors.GREY_900), bgcolor='#f0a150'),
                        # IconButton(
                        #     icon=icons.HOME_ROUNDED, icon_color="black", icon_size=75, tooltip="Home Page", on_click=lambda _:page.go('/')
                        # ),
                        # Row([EnterUnit,MonthDropDown,b],alignment=MainAxisAlignment.CENTER),
                        # Row([Container(MonthCheck)], alignment=MainAxisAlignment.CENTER),
                        Row([tb1,unittext]),
                        Row([MonthDropDown, monthtext]), 
                        Row([c]),
                        Row([tb2,outtext]),
                        Row([tb3,renttext]), 
                        Row([tb4,electext]), 
                        Row([tb5,watertext]), b_update ,
                        Row([t], alignment=MainAxisAlignment.CENTER)     
                    ]  
                ),
            )
            page.update()

        page.update()

    def view_pop(e: ViewPopEvent):
        page.views.pop()
        top_view: View=page.views[0]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop =  view_pop
    page.go(page.route)

if __name__ == '__main__':
    app(target = main)



