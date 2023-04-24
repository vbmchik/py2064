import flet
from flet import Row, icons, IconButton, TextField, Page, TextStyle, TextButton


def main(page:Page):
    page.title = "Counter App"
    page.vertical_alignment = "center"
       
    def minus(e):
        if str(textfield.value) !='0' :
            textfield.value = int(textfield.value)-1
        page.update()
    
    def plus(e): 
        textfield.value = int(textfield.value)+1
        page.update()
        
    def focus_my(e):
        textfield.color = "RED"
        page.update()
    
    def blur_my(e):
        textfield.color = "BLUE"
        page.update()
        
    textfield = TextField(text_align='center', value='0', width=100, on_focus=focus_my, on_blur=blur_my)    
    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus),
                textfield,
                IconButton(icons.ADD, on_click=plus )
            ],
            alignment='center'
        )
    )

flet.app(target=main, view=flet.WEB_BROWSER)