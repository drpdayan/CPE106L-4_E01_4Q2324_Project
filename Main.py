import flet as ft
from flet import *
import initiallogic as ilg 
from pymongo import MongoClient as mc
import pprint
import re
from initiallogic import get_lessee_list as gll
# print(glist)
def main(page: Page) -> None:
    page.title = 'Application Collection System'
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf",
        "RobotoMono": "https://github.com/google/fonts/raw/main/apache/robotomono/RobotoMono%5Bwght%5D.ttf"
    }
    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()
        #Home Page

        def User_Hover(e):
            User.Container(
                content= Row([IconButton(
                                        icon=ft.icons.PERSON_OUTLINE,
                                        icon_color="White",
                                        icon_size=100,
                                        tooltip="Lessee Profile",
                                    ),
                                Text("Lessee Profile", font_family='RobotoMono',weight=FontWeight.BOLD , size='40' , color=colors.WHITE),
                            ]
                        ),

                padding = 20,
                bgcolor= "#FF7900",
                shape= BoxShape.RECTANGLE,
                border_radius= 70
            )
            page.update()

        User = Container(
            IconButton(
                icon=ft.icons.PERSON_OUTLINE,
                icon_color="White",
                icon_size=100,
                tooltip="User Profile",

            ), 
            padding = 20,
            bgcolor= "#FF7900",
            shape= BoxShape.CIRCLE,
            on_hover=lambda e: User_Hover
        )

        UserHover = Container(
            content= Row([IconButton(
                                    icon=ft.icons.PERSON_OUTLINE,
                                    icon_color="White",
                                    icon_size=100,
                                    tooltip="Lessee Profile",
                                ),
                            Text("Lessee Profile", font_family='RobotoMono',weight=FontWeight.BOLD , size='40' , color=colors.WHITE),
                        ]
                    ),

            padding = 20,
            bgcolor= "#FF7900",
            shape= BoxShape.RECTANGLE,
            border_radius= 70
        )



        page.window_width = 800
        page.window_height = 900
        page.views.append(
            View(
                route = '/',
                controls = [
                    AppBar(title=Text('Home Page'), bgcolor='#f0a150'),
                    # ElevatedButton(text= 'New Window', on_click=lambda _:page.go('/store')),
                    Row(
                        [User], alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        [ UserHover ], alignment=MainAxisAlignment.CENTER,
                    ),
                    Row([Container(
                            IconButton(
                                icon=ft.icons.ATTACH_MONEY_ROUNDED,
                                icon_color="#FF7900",
                                icon_size=150,
                                tooltip="Payments",
                                on_click=lambda _:page.go('/payment'),
                            ),
                            padding = 20
                        ),], alignment=MainAxisAlignment.CENTER)
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
                        output_text = " "
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


            tb1 = ft.TextField(label="Enter Unit")
            b = ft.IconButton(icon=icons.SEARCH_SHARP, on_click=lesseeinfo_button_clicked)
            b = ft.IconButton(icon=icons.SEARCH_SHARP,icon_size=50, on_click=lesseeinfo_button_clicked)
            page.window_width = 750
            page.window_height = 400
            page.views.append(
                #Top Layer
                View(
                    route = '/poutline',
                    controls = [
                        AppBar(title=Text('User Profile'), bgcolor='#f0a150'),
                        AppBar(title=Text('Lessee Profile'), bgcolor='#f0a150'),

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
                    lessee_info = ilg.update_lessee(vunit.value, vpurpose.value, vname.value, vtin.value)
                    if lessee_info:  # Check if lessee information is found
                        ilg.update_lessee(vunit.value, vpurpose.value, vname.value, vtin.value)
                        if ilg.update_lessee:
                            t.value = "LESSEE INFORMATION UPDATED"
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
            
            vunit = TextField(label="Enter Unit")
            unittext = Text(":Unit", font_family='RobotoMono', color="#D67229", size='20')
            vpurpose = TextField(label="Enter Purpose")
            purposetext = Text(":Rental Purpose""\n""(Commercial/Residential/Vacant)", font_family='RobotoMono', color="#D67229", size='20')
            vname = TextField(label="Enter Name",)
            nametext = Text(":Name", font_family='RobotoMono', color="#D67229", size='20')
            vtin = TextField(label="Enter TIN")
            tintext = Text(":Tax Identification Number", font_family='RobotoMono', color="#D67229", size='20')
            b = ft.ElevatedButton(text="Update", color='#D67229', on_click=lessee_button_clicked)
            page.window_width = 750
            page.window_height = 475
            page.views.append(
                #Top Layer
                View(
                    route = '/poutline',
                    controls = [
                        AppBar(title=Text('Edit Lessee'), bgcolor='#f0a150'),
                        Row([vunit,unittext]),
                        Row([vpurpose,purposetext]),
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
                        output_text = " "
                        output_text = ""
                        for field, value in unit_info.items():
                            output_text += f"{field}: {value}\n"
                        t.value = output_text
                    else:
                        t.value = "Unit not found."

                elif not unit_info:
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
 
            tb1 = ft.TextField(label="Enter Unit")
            b = ft.IconButton(icon=icons.SEARCH_SHARP, on_click=unitinfo_button_clicked)
            page.window_width = 600
            page.window_height = 400
            page.views.append(
                #Top Layer
                View(
                    route = '/ustatus',
                    controls = [
                        AppBar(title=Text('User Profile'), bgcolor='#f0a150'),
                        AppBar(title=Text('Unit Status'), bgcolor='#f0a150'),
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
                    check_unit = ilg.update_unit(vunit1.value, vstatus.value, vdate.value)
                    if check_unit:  # Check if lessee information is found
                        ilg.update_unit(vunit1.value, vstatus.value, vdate.value)
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
            vunit1 = TextField(label="Enter Unit")
            unittext1 = Text(":Unit", font_family='RobotoMono', color="#D67229", size='20')
            vstatus = TextField(label="Enter Status")
            statustext = Text(":Occupancy Status (Occupied/Vacant)", font_family='RobotoMono', color="#D67229", size='20')
            vdate = TextField(label="Enter Date")
            datetext = Text(":Lease Date (dd/mm/yyyy)", font_family='RobotoMono', color="#D67229", size='20')
            b = ft.ElevatedButton(text="Update", color='#D67229', on_click=unit_button_clicked)
            
            page.window_width = 800
            page.window_height = 400
            page.views.append(
                #Top Layer
                View(
                    route = '/payment',
                    controls = [
                        AppBar(title=Text('Edit Unit'), bgcolor='#f0a150'),
                        Row([vunit1,unittext1]),
                        Row([vstatus,statustext]),
                        Row([vdate,datetext]), 
                        Row([b]),
                        Row([t], alignment=MainAxisAlignment.CENTER)     
                    ]  
                ),
            )
        #Payment Page
        if page.route == '/payment':
            page.views.append(
                #Top Layer
                View(
                    route = '/payment',
                    controls = [
                        AppBar(title=Text('Payments'), bgcolor='#f0a150'),
                        IconButton(
                            icon=ft.icons.HOME_ROUNDED,
                            icon_color="black",
                            icon_size=75,
                            tooltip="Home Page",
                            on_click=lambda _:page.go('/')
                        ),     
                    ]  
                ),
            )
        page.update()
    def view_pop(e: ViewPopEvent):
        page.views.pop()
        top_view: View=page.views[-1]
        page.go(top_view.route)
    page.on_route_change = route_change
    page.on_view_pop =  view_pop
    page.go(page.route)
if __name__ == '__main__':
    ft.app(target = main)

# import flet as ft
# from flet import *

# def main(page:Page):
 
# 	def runanimate(e):
# 		mycon.border_radius = 30 if mycon.border_radius == 0 else 0
# 		mycon.offset = transform.Offset(0,1) if mycon.offset == transform.Offset(0,0) else transform.Offset(0,0)
# 		mycon.scale = 1 if mycon.scale == 0.5 else 0.5
# 		mycon.opacity = 0 if mycon.opacity == 1  else 1
 
# 		# FOR TEXT
# 		mytext.offset = transform.Offset(0,0) if mytext.offset == transform.Offset(1,0) else transform.Offset(1,0)
# 		page.update()
 
# 	mytext = Text("hello",
# 		color="white",
# 		size=25,
# 		offset=transform.Offset(1,0),
# 		animate_offset = animation.Animation(duration=400,curve="easeOut")
# 		)
# 	mycon = Container(
# 		bgcolor="red",
# 		width=200,
# 		height=180,
# 		content=Column([
# 			mytext
 
# 			]),
# 		opacity = 1,
# 		animate_opacity = animation.Animation(duration=300,curve="easeInCubic"),
# 		margin = margin.only(top=50,left=20),
# 		offset = transform.Offset(0,0),
# 		border_radius = 30,
# 		animate_offset = animation.Animation(duration=600,curve="easeIn"),
# 		scale=transform.Scale(scale=0.5,
# 			alignment=alignment.center
# 			),
# 		animate_scale = animation.Animation(duration=300,curve="bounceIn")
# 		)
# 	mybutton = ElevatedButton(
# 		"show animate",
# 		# offset = transform.Offset(0,4),
# 		on_click=runanimate
 
# 		)
 
# 	page.add(
# 		mycon,
# 		mybutton
 
# 		)
 
# if __name__ == '__main__':
#      ft.app(target = main)