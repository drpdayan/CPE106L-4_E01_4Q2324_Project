import flet as ft
from flet import *


from pymongo import MongoClient as mc
import pprint
import re
from initiallogic import get_lessee_list as gll

# print(glist)

def main(page: Page) -> None:
    page.title = 'Application Collection System'

    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        #Home Page
        page.window_width = 800
        page.window_height = 300
        page.views.append(
            View(
                route = '/',
                controls = [
                    AppBar(title=Text('Home Page'), bgcolor='#f0a150'),
                    # ElevatedButton(text= 'New Window', on_click=lambda _:page.go('/store')),
                    Row(
                        [
                        Container(
                            IconButton(
                                icon=ft.icons.PERSON_OUTLINE,
                                icon_color="#FF7900",
                                icon_size=150,
                                tooltip="User Profile",
                                on_click=lambda _:page.go('/poutline'),
                            ),
                            padding = 20
                        ),
                        Container(
                            IconButton(
                                icon=ft.icons.SENSOR_DOOR_OUTLINED,
                                icon_color="#FF7900",
                                icon_size=150,
                                tooltip="Unit Status",
                                on_click=lambda _:page.go('/ustatus'),
                            ),
                            padding = 20
                        ),
                        Container(
                            IconButton(
                                icon=ft.icons.ATTACH_MONEY_ROUNDED,
                                icon_color="#FF7900",
                                icon_size=150,
                                tooltip="Payments",
                                on_click=lambda _:page.go('/payment'),
                            ),
                            padding = 20
                        ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                ],
                # # vertical_alignment=MainAxisAlignment.CENTER,
                # horizontal_alignment=CrossAxisAlignment.STRETCH,
                # spacing = 26
            ),

        )
    
        #Lessee_Information Page
        if page.route == '/poutline':
            glist = gll()
            page.window_width = 1500
            page.window_height = 1000
            page.views.append(
                #Top Layer
                View(
                    route = '/poutline',
                    controls = [
                        AppBar(title=Text('User Profile'), bgcolor='#f0a150'),
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
            

        #Unit_Status Page
        page.window_width = 1500
        page.window_height = 1000
        if page.route == '/ustatus':
            page.views.append(
                #Top Layer
                View(
                    route = '/ustatus',
                    controls = [
                        AppBar(title=Text('Unit Status'), bgcolor='#f0a150'),
                        IconButton(
                            icon=ft.icons.HOME_ROUNDED,
                            icon_color="black",
                            icon_size=75,
                            tooltip="Home Page",
                            on_click=lambda _:page.go('/')
                        ),
                        Row(controls=[
                            ft.TextField(label="Enter Unit"),
                            ft.ElevatedButton(text="Check"),
                        ],alignment= MainAxisAlignment.CENTER)     
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



