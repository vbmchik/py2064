import flet as ft
from flet import Page, IconButton, Text, TextField, icons, TextButton
from dbHelp import DataHelp



def main(page:Page):

    page.horizontal_alignment='center'
    
    def checknsave(e):
        db = DataHelp()
        year = int(yearText.value)
        month = int(monthText.value)
        business = int(businessText.value)
        income = int(incomeText.value)
        try:
            if db.checkExist(year,month, business):
                page.dialog = dlg1
                dlg1.open=True
                page.update()
                return
            db.insert_into_query(year=year, month=month, business=business, income=income)
            yearText.clean()
            monthText.clean()
            businessText.clean()
            incomeText.clean()
            page.update()
        except:
            page.dialog = dlg1
            dlg1.open=True
            page.update()    
    
    def submityear(e):
        try:
            c = int(yearText.value)
            if c<1970 or c>2050:
               raise "Value error"
            monthText.focus()
        except:
            page.dialog = dlg
            dlg.open=True
            yearText.focus()
            page.update()
        
    def submitmonth(e):
        businessText.focus()
    
    
    def submitbusiness(e):
        incomeText.focus()
        
        
    def close_dlg(e):
        dlg.open = False
        page.update()
    
    def close_dlg1(e):
        dlg1.open = False
        page.update()
  
        
    dlg = ft.AlertDialog( modal=True,
                         title=ft.Text("Data Error!"), 
                         content=ft.Text("Please check format of your data"),
                         actions=[ft.TextButton("OK",on_click=close_dlg)])
    dlg1 = ft.AlertDialog( modal=True,
                         title=ft.Text("Data Error!"), 
                         content=ft.Text("Combination of year, month and business exists"),
                         actions=[ft.TextButton("OK",on_click=close_dlg1)])
        
    yearLabel = Text("Year: ", color=ft.colors.RED, size=40)
    yearText = TextField(value="", color=ft.colors.BLUE, text_size=40, on_submit=submityear )
    yearRow = ft.Row([yearLabel, yearText],vertical_alignment='center')
    
    monthLabel = Text("Month: ", color=ft.colors.RED, size=40)
    monthText = TextField(value="", color=ft.colors.BLUE, text_size=40, on_submit=submitmonth)
    monthRow = ft.Row([monthLabel, monthText],vertical_alignment='center')
    
    businessLabel = Text("Business: ", color=ft.colors.RED, size=40)
    businessText = TextField(value="", color=ft.colors.BLUE, text_size=40, on_submit=submitbusiness)
    businessRow = ft.Row([businessLabel, businessText],vertical_alignment='center')
    
    incomeLabel = Text("Income: ", color=ft.colors.RED, size=40)
    incomeText = TextField(value="", color=ft.colors.BLUE, text_size=40)
    incomeRow = ft.Row([incomeLabel, incomeText],vertical_alignment='center')
    
    start = TextButton(text="Save", on_click=checknsave)
    buttonRow = ft.Row([start],vertical_alignment='center')
    page.add(ft.Column([yearRow, monthRow, businessRow, incomeRow, buttonRow], horizontal_alignment='center'))
    page.horizontal_alignment='center'
    
    
ft.app(target=main)