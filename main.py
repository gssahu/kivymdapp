from kivymd.app import MDApp
from kivy.lang import Builder

kv = '''
MDScreen:
    MDNavigationLayout:
        MDTopAppBar:
            title: "Appointment"
            pos_hint:{"top":1}
            left_action_items:[['menu',lambda x: drawer.set_state("open")]]
        ScreenManager:
            id:screenmanager
            MDScreen:
                name:"home"
                MDBoxLayout:
                    orientation:"vertical"
                    spacing:"10dp"

                    MDIcon:
                        icon:"language-python"
                        padding: 0, "85dp", 0, 0
                        pos_hint:{"center_x":0.5,"center_y":0.1}
                    MDLabel:
                        text:"C A S A  ILA"
                        size_hint_y: None
                        font_size: 20
                        bold: True
                        halign: 'center'
                        text_size: None, None
                        adaptive_height: True
                    MDLabel:
                        text:"Spcial Castle Caffee"
                        size_hint_y: None
                        font_size: 15
                        bold: True
                        halign: 'center'
                        text_size: None, None
                        color: [.8, .8, .8, 1]
                        adaptive_height: True
                    MDRaisedButton:
                        text:"Book Here"
                        pos_hint:{"center_x":0.5,"center_y":0.4}
                        size_hint_x: 0.5
                        padding:"20dp"
                    MDRaisedButton:
                        text:"Contact Us"
                        pos_hint:{"center_x":0.5,"center_y":0.3}
                        size_hint_x: 0.5
                    MDBoxLayout:
                        orientation:"vertical"
                        Image:
                            source: 'images.jpg'
                            # Giving the size of image
                            size_hint_x: 0.7
                            # allow stretching of image 
                            #allow_stretch: True
                            pos_hint:{"center_x":0.5,"center_y":0.5}
                    Widget:
                        id: separator
                        size_hint_y: None
                        height: 6
                        canvas:
                            Color:
                                rgb: 1., 0., 0.
                            Rectangle:
                                pos: 0, separator.center_y
                                size: separator.width, 2
                    MDBoxLayout:
                        halign:"center"
                        adaptive_height:True
                        padding: "100dp", 0, 0, "20dp"
                        MDIcon:
                            icon:"facebook"
                        MDIcon:
                            icon:"twitter"
                        MDIcon:
                            icon:"youtube"
                        MDIcon:
                            icon:"instagram"



            MDScreen:
                name:"book"
                MDLabel:
                    text:"Book"
                    halign:"center"
            MDScreen:
                name:"contactus"
                MDLabel:
                    text:"Contact Us"
                    halign:"center"                                
        MDNavigationDrawer:
            id:drawer
            MDBoxLayout:
                orientation:"vertical"
                MDFillRoundFlatButton:
                    text:"X"
                    pos_hint:{"center_x":.85,"center_y":.9}
                    on_release:drawer.set_state("close")
                MDBoxLayout:
                    orientation:"vertical"
                    MDList:
                        OneLineIconListItem:
                            text:"Home"
                            on_release:screenmanager.current = "home";drawer.set_state("close")
                        OneLineIconListItem:
                            text:"Booking"
                            on_release:screenmanager.current = "book";drawer.set_state("close")
                        OneLineIconListItem:
                            text:"Contact Us"                        
                            on_release:screenmanager.current = "contactus";drawer.set_state("close")   
                MDBoxLayout:

'''

class mybook(MDApp):
    def build(self):
        return Builder.load_string(kv)
    
mybook().run()
