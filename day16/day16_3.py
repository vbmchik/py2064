import flet as ft
from flet import Page, Text, TextField, Column, Row, IconButton
import numpy
import pandas
from flet.plotly_chart import PlotlyChart
import plotly_express as px

from solver import solve

def main(page: Page):
    
    def draw(e):
        a = int(startx.value)
        b = int(endx.value)
        
        data = list(numpy.arange(a,b,0.1))
        funcs = func.value
        
        try:
            values = list(map(lambda t: solve(funcs.replace('@x', f"{(t)})")), data))
            df = pandas.DataFrame(dict(x=data,y=values))
            fig = px.line(df, x="x", y="y", title=f"User function = {funcs}")
            column = Column([
                rowf,
                rowrange,
                PlotlyChart(fig, expand=False)
            ], scroll=ft.ScrollMode.ADAPTIVE)
            page.clean()
            page.add(column)
            page.update()
        except Exception as ex:
            column = Column([
                rowf,
                rowrange,
                Text(str(ex), size=40, color=ft.colors.RED)
            ], scroll=ft.ScrollMode.ADAPTIVE)
            page.clean()
            page.add(column)
            page.update()
        
    
    text = Text('Enter you function with variable as @x', size=30)
    func = TextField(value="", text_size=30)
    buttonstart = IconButton(icon=ft.icons.CALCULATE_ROUNDED, icon_size=60, on_click=draw)
    
    textStartLabel = Text('Enter start value', size=30)
    startx = TextField(value="", text_size=30)
    
    textEndtLabel = Text('Enter start value', size=30)
    endx = TextField(value="", text_size=30)
    
    rowf = Row([text, func, buttonstart])
    rowrange = Row([textStartLabel, startx,textEndtLabel, endx])
    
    column = Column([rowf, rowrange])
    page.add(column)
    
ft.app(target=main)