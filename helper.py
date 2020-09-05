KV = '''
<ContentNavigationDrawer>:
    BoxLayout:
        orientation:'vertical'
        spacing:'8dp'
        padding:'8dp'

        Image:      
            source:'images\cat.png'
            user_font_size:'2sp'

        ScrollView:

            MDList:

                OneLineIconListItem:
                    text: "Open"
                    on_press:
                        app.opening()
                    IconLeftWidget:
                        icon:'android' 



                


Screen:
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
    NavigationLayout:
        x: toolbar.height
        ScreenManager:
            id: screen_manager
            Screen:
                name: "scr 1"

                MDIconButton:

                    pos_hint:{'center_x':0.5,'center_y':0.3}
                    icon:'images\start.png'
                    md_bg_color:1,1,1,0.9 
                    user_font_size:'80sp'
                    on_release:app.text_detection_start() 

                MDLabel:
                    text:'Start!'
                    halign:'center'
                    pos_hint:{'center_x':0.5,'center_y':0.15} 
                    theme_text_color:'Custom'
                    text_color: 1,1,1,0.9
                    font_style: 'H5'    

                
                MDRaisedButton:
                    text:  "Where to save"
                    pos_hint:{'center_x':0.5,'center_y':0.7}
                    on_release: app.browse_directory_for_saving() 
                     
                MDRaisedButton:
                    text:  "Select Image"
                    pos_hint:{'center_x':0.5,'center_y':0.55}
                    on_release: app.select_image_for_rec()         

                

            Screen:
                name: "scr 2"

                MDTextField:
                    id:studentname
                    hint_text:'Enter Student Name'
                    mode:'fill'
                    fill_color:0,0,0,0.5
                    pos_hint:{'center_x':0.5,'center_y':0.65} 
                    size_hint_x:None 
                    width:400
                    normal_color:app.theme_cls.primary_color
                    icon_right:'lock'
                    icon_right_color:app.theme_cls.primary_color   

                MDTextField:
                    id:studentrollnumber
                    hint_text:'Enter Student Roll Number'
                    mode:'fill'
                    fill_color:0,0,0,0.5
                    pos_hint:{'center_x':0.5,'center_y':0.45} 
                    size_hint_x:None 
                    width:400
                    normal_color:app.theme_cls.primary_color
                    icon_right:'lock'
                    icon_right_color:app.theme_cls.primary_color 

                MDIconButton:
                    pos_hint:{'center_x':0.4,'center_y':0.2}
                    icon:'add (1).png'
                    md_bg_color:1,1,1,0.9 
                    user_font_size:'6sp'    

                MDTextButton:
                    text:'Add New Student'  
                    pos_hint:{'center_x':0.5,'center_y':0.2}
                    custom_color:1,1,1,1   
                    on_release:app.add_img_to_train_folder()    
            Screen:
                name: 'scr 3'

                MDTextField:
                    id:deletingsrollnumber
                    hint_text:'Enter Student Roll Number'
                    mode:'fill'
                    fill_color:0,0,0,0.5
                    pos_hint:{'center_x':0.5,'center_y':0.65} 
                    size_hint_x:None 
                    width:400
                    normal_color:app.theme_cls.primary_color
                    icon_right:'lock'
                    icon_right_color:app.theme_cls.primary_color 




                MDRectangleFlatButton:
                    text:'Remove Student'  
                    pos_hint:{'center_x':0.5,'center_y':0.4}  
                    on_release:app.deleting_image_from_train_folder()






        MDNavigationDrawer:

            id: nav_drawer
            BoxLayout:
                orientation:'vertical'
                spacing:'15dp'
                padding:'20dp'
                ContentNavigationDrawer:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer
'''