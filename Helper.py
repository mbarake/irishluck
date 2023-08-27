import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import numpy as np

colors = {
    'background': '#111111',
    'text': '#3C5C7B',
    'title': '#00FF00',
    'section': '#585858',
    'black': '#000000'
}


def table_link(dataframe, link_column):
    csstable = {

        'border-collapse': 'collapse',
        'width': '100%'
    }

    thtd = {
        'padding': '5px',
        'left-margin': '30px',
        'text-align': 'left',
        'border-bottom': '1px solid #ddd'
    }

    rows = []
    for i in range(len(dataframe)):
        row = []
        for col in dataframe.columns:
            value = dataframe.iloc[i][col]
            if col == link_column:

                cell = html.Td(html.A(value, href=value), style=thtd)
            else:
                cell = html.Td(children=value, style=thtd)

            row.append(cell)
        rows.append(html.Tr(row))

        result = html.Table(style=csstable,
                            children=[html.Tr(
                                [html.Th(col.title(), style=thtd) for col in
                                 dataframe.columns])] +
                                     rows, className='table',
                            )
    return result


def generate_blog(app, names):
    comp = []

    clover = html.Div(html.Img(src=app.get_asset_url('clover.png'),
                               width='20%'),
                      style={'textAlign': 'center', 'margin-top': '3em'})
    comp.append(clover)
    for n in names:
        traces = [go.Bar(
            x=['Food', 'Education', 'Entertainment', 'Nature', 'Safety'],
            y=n[2],
           marker={'color':["orange","lightgreen","cyan","yellow","violet"]})]

        comp.append(dcc.Markdown(n[0]))
        img = html.Img(src=app.get_asset_url(n[1]), style={'margin': 'auto',
                                                           'width': '50%',
                                                           'display': 'block'})
        comp.append(img)

        if n[2]:
            comp.append(dcc.Graph(id=str(n[1]),

                                  config={'staticPlot': True},

                                  figure={'data': traces}

                                  )),
        comp.append(html.Div(
            style={'background-color': colors['section'], 'margin-top': '3em',
                   'width': '40%', 'display': 'block',
                   'margin-left': 'auto', 'margin-right': 'auto'},
            children=[html.Br()]), )

    comp.append(clover)

    result = html.Div(
        style={'margin-top': '3em', 'vertical-align': 'middle',
               'width': '100%'}, children=comp)

    return result


def table_img(app, images, n):
    csstable = {

        'border-collapse': 'collapse',
        'width': '100%',
    }

    thtd = {
        'padding': '20px',
    }

    rows = []
    row = []
    for i, im in enumerate(images):
        cell = html.Img(src=app.get_asset_url(im), width='100%', height='80%')
        if i == len(images) - 1:
            row.append(html.Td(cell, rowSpan='2', colSpan='2', style=thtd))
            rows.append(html.Tr(row))
            break
        row.append(html.Td(cell, style=thtd))
        if (i + 1) % n == 0:
            rows.append(html.Tr(row))
            row = []

    result = html.Table(style=csstable,
                        children=rows, className='table')
    return result
