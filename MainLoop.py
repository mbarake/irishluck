import dash_core_components as dcc
import dash
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import Helper
import plotly.graph_objs as go

center = {
    'display': 'block',
    'margin-left': 'auto',
    'margin-right': 'auto',
    'width': '60%',
}

colors = {
    'background': '#111111',
    'text': '#3C5C7B',
    'title': '#00FF00',
    'section': '#585858',
    'black': '#000000'
}

tabs_styles = {
    'height': '50px'
}

tab_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'font-size': '18px'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '2px solid #d6d6d6',
    'backgroundColor': '#a9a9a9',
    'font-size': '18px',
    'padding': '6px'
}

h3_style = {
    'padding': '10px',
    'textAlign': 'center',
    'color': colors['text']

}

df_hosting = pd.read_csv('data/hosting_agreement.csv')
df_critical = pd.read_csv('data/critical.csv')
df_learning = pd.read_csv('data/learn.csv')
df_learning2 = pd.read_csv('data/learn2.csv')
df_empl = pd.read_csv('data/aa.csv')

path = 'policy/privacy_policy.md'
with open(path) as this_file:
    text_markdown = this_file.read()

path = 'blog/blessington.md'
with open(path) as this_file:
    blog_bless = this_file.read()

path = 'blog/cyclingtobray.md'
with open(path) as this_file:
    blog_cyclingbray = this_file.read()

path = 'blog/dublin.md'
with open(path) as this_file:
    blog_dublin = this_file.read()

path = 'blog/hillwalk.md'
with open(path) as this_file:
    blog_hill = this_file.read()

path = 'blog/skills.md'
with open(path) as this_file:
    blog_skills = this_file.read()

path = 'blog/stamps.md'
with open(path) as this_file:
    blog_stamps = this_file.read()

path = 'blog/skerries.md'
with open(path) as this_file:
    blog_skerries = this_file.read()

app = dash.Dash(__name__)

server = app.server
app.title = 'WorkEIR'
app.config['suppress_callback_exceptions'] = True

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
    <title> 
        Work and Study in Ireland
    </title>
     <meta name="google-site-verification" content="5NTDB8vBVOHlvRwHZT5VpiVInyO-vJN50DBgt2Q-TT8" />
     
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        
        
        <script data-ad-client="ca-pub-7852532704466921" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>  
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

app.layout = html.Div(style={'background': '##E5E7E9'}, children=[

    html.Div(style={'backgroundColor': colors['background'], 'margin': 'auto',
                    'width': '100%'}, children=[

        html.H1(
            children='Ireland',
            style={
                'textAlign': 'center',
                'color': colors['title']
            }
        ),

        html.H3(children='Study and Work in Ireland.', style={
            'textAlign': 'center',
            'color': colors['title']
        })]),

    html.Div(style={'margin': 'auto', 'width': '75%'}, children=[

        dcc.Tabs(id="tabs", value='blog', children=[
            dcc.Tab(label='Blog', value='blog', style=tab_style,
                    selected_style=tab_selected_style),
            dcc.Tab(label='Stamps', value='stamps', style=tab_style,
                    selected_style=tab_selected_style),
            dcc.Tab(label='Hosting Agreement', value='hosting', style=tab_style,
                    selected_style=tab_selected_style),
            dcc.Tab(label='Critical Skills', value='critical', style=tab_style,
                    selected_style=tab_selected_style),
            dcc.Tab(label='Keep Learning', value='learn', style=tab_style,
                    selected_style=tab_selected_style),
            dcc.Tab(label='Photos', value='photos', style=tab_style,
                    selected_style=tab_selected_style),
            dcc.Tab(label='Stats', value='stats', style=tab_style,
                    selected_style=tab_selected_style),
            dcc.Tab(label='Privacy Policy', value='privacy', style=tab_style,
                    selected_style=tab_selected_style),
        ]),
        html.Div(id='tabs-content')
    ])
])


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'blog':
        return tab_blog()
    elif tab == 'stamps':
        return tab_general()
    elif tab == "hosting":
        return tab_hosting()
    elif tab == "critical":
        return tab_critical()
    elif tab == "photos":
        return tab_photos()
    elif tab == "learn":
        return tab_learn()
    elif tab == "stats":
        return tab_stats()
    elif tab == "privacy":
        return tab_privacy()
    else:
        return tab_general()
    

def tab_blog():
    return Helper.generate_blog(app,[(blog_bless,'bless.png',[30, 50, 20, 90, 90]),
                                     (blog_hill,
        'hillwalk.png', []), (blog_dublin,'dublin.png', [50, 80, 60, 70, 70]),
                                     (blog_cyclingbray,
                                                      'bray2.png', [70, 70, 80, 80,65]),
                                     (blog_skerries, 'skerries2.png', [70, 65, 50, 95 , 90])])

def tab_general():
    return html.Div(style={'margin-top': '3em'}, children=[

        html.Div(html.Img(src=app.get_asset_url('clover.png'), width='20%'),
                 style={'textAlign': 'center', 'margin-top': '3em'}),

        html.H2(
            children='Beautiful Ireland',
            style={
                'textAlign': 'center',
                'color': colors['text'],
            }
        ),

        dcc.Markdown(children=''' 
           Ireland is a relatively small country with a beautiful countryside. The west coast is simply
           amazing with stunning beaches and beautiful waves. Go surfing, hiking or simply go back in time and navigate 
           the narrow countryside roads. 
           
           Ireland is a hub for big pharmaceuticals and tech giants. You will find interesting work. As a Non-EU, 
           you will need a work permit to work in Ireland. Either study in Ireland and apply for a work permit,
           get a hosting agreement as a researcher or get a work permit based on critical skills scheme.
        '''),

        html.Div(
            style={'background-color': colors['section'], 'margin-top': '3em'},
            children=[html.Br()]),

        html.H2(
            children='Stamps',
            style={
                'textAlign': 'center',
                'color': colors['text'],
            }
        ),

        dcc.Markdown(children=blog_stamps),

        html.Div(
            style={'background-color': colors['section'], 'margin-top': '3em'},
            children=[html.Br()]),

        html.H2(
            children='State Diagram',
            style={
                'textAlign': 'center',
                'color': colors['text'],
            }
        ),

        html.Div(html.Img(src=app.get_asset_url('stamps.png'), width='80%'),
                 style={'textAlign': 'center'}),

        html.Div(html.Img(src=app.get_asset_url('clover.png'), width='20%'),
                 style={'textAlign': 'center', 'margin-top': '3em'})

    ])


def tab_privacy():
    return html.Div(style={'margin-top': '3em'}, children=[

        dcc.Markdown(text_markdown)

    ])


def tab_learn():
    return html.Div(style={'margin-top': '3em'}, children=[

        html.Div(html.Img(src=app.get_asset_url('clover.png'), width='20%'),
                 style={'textAlign': 'center', 'margin-top': '3em'}),

        html.H2(
            children='Essential skills that will give you a competitive advantage and let you enjoy more what you do',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),

        dcc.Markdown(blog_skills),

        html.Div(
            style={'background-color': colors['section'], 'margin-top': '3em'},
            children=[html.Br()]),

        html.H2(
            children='Consider learning the following skills',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),

        Helper.table_link(df_learning, "link"),

        html.Div(
            style={'background-color': colors['section'], 'margin-top': '3em'},
            children=[html.Br()]),

        html.H2(
            children='Other interesting courses',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),

        Helper.table_link(df_learning2, "link"),

        html.Div(html.Img(src=app.get_asset_url('clover.png'), width='20%'),
                 style={'textAlign': 'center', 'margin-top': '3em'}),

    ])


def tab_stats():
    return html.Div(style={'margin-top': '3em'}, children=[

        html.Div(html.Img(src=app.get_asset_url('clover.png'), width='20%'),
                 style={'textAlign': 'center', 'margin-top': '3em'}),

        html.H2(
            children='Employment in Ireland by Region and Year',
            style={
                'textAlign': 'center',
                'color': colors['text'],
            }
        ),

        html.Label('Year', style={'width': '50%'}),

        dcc.Dropdown(
            id='year',
            options=[{'label': i, 'value': i} for i in range(2008, 2018)],
            value='2017',
            placeholder='Select...',
            multi=False,
            style={'width': '50%'}
        ),

        dcc.Graph(id='empl_by_region', config={'staticPlot': True}),

        html.Div(
            style={'background-color': colors['section'], 'margin-top': '3em'},
            children=[html.Br()]),

        html.Div(html.Img(src=app.get_asset_url('clover.png'), width='20%'),
                 style={'textAlign': 'center', 'margin-top': '3em'}),

    ])


@app.callback(Output('empl_by_region', 'figure'),
              [Input('year', 'value')])
def update_graph(year):
    s = df_empl[str(year)]

    traces = [go.Bar(
        x=s.index,
        y=s.values
    )]

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'title': 'Region',
                   'titlefont': dict(size=18, color='darkgrey')},
            yaxis={'title': 'Employment',
                   'titlefont': dict(size=18, color='darkgrey')}, ),

    }


def tab_critical():
    return html.Div(style={'margin-top': '3em'}, children=[

        html.Div(html.Img(src=app.get_asset_url('clover.png'), width='20%'),
                 style={'textAlign': 'center', 'margin-top': '3em'}),

        html.H2(
            children='The Critical Skills Employment Permit',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),

        dcc.Markdown(''' 
            The Critical Skills Employment Permit have attracted highly skilled people into the 
            labour market. It is very attractive as you can apply for immediate family reunification.
            For more information consult the government website at dbei.gov.ie
        '''),

        html.Div(
            style={'background-color': colors['section'], 'margin-top': '3em'},
            children=[html.Br()]),

        html.H2(
            children='The following organisations are known in the past to have provided sponsorship',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),

        Helper.table_link(df_critical, "Link"),

        html.Div(html.Img(src=app.get_asset_url('clover.png'), width='20%'),
                 style={'textAlign': 'center', 'margin-top': '3em'}),

    ])


def tab_hosting():
    return html.Div(style={'margin-top': '3em'}, children=[

        html.Div(html.Img(src=app.get_asset_url('clover.png'), width='20%'),
                 style={'textAlign': 'center', 'margin-top': '3em'}),

        html.H2(
            children='Hosting Agreement',
            style={
                'textAlign': 'center',
                'color': colors['text'],
            }
        ),

        dcc.Markdown('''
            
            
            A hosting agreement  provides for a fast track procedure for admitting nationals from countries outside 
            of the European Economic Area. It has the following features:
            
            * Period between three months to five years.
            
            * Carry out a research project with an accredited research institution.

            * A separate work permit is not required.
            
            * Family reunification.  
            
            '''),

        html.Div(
            style={'background-color': colors['section'], 'margin-top': '3em'},
            children=[html.Br()]),

        html.H2(
            children='The following research organisations are accredited to issue Hosting Agreements to Non-EU researchers',
            style={
                'textAlign': 'left',
                'color': colors['text'],
            }
        ),

        Helper.table_link(df_hosting, "Link"),

        html.Div(html.Img(src=app.get_asset_url('clover.png'), width='20%'),
                 style={'textAlign': 'center', 'margin-top': '3em'}),
    ])


def tab_photos():
    return html.Div(style={'margin-top': '3em'}, children=[

        html.Div(html.Img(src=app.get_asset_url('clover.png'), width='20%'),
                 style={'textAlign': 'center', 'margin-top': '3em'}),

        Helper.table_img(app,
                         ['door.jpg', 'arch.jpg', 'moher.jpg', 'old.jpg',
                          'sheep.jpg', 'trinity.jpg', 'ruins.jpg', 'hike.jpg',
                          'oceon.jpg',
                          ],
                         2),

        html.Div(html.Img(src=app.get_asset_url('clover.png'), width='20%'),
                 style={'textAlign': 'center', 'margin-top': '3em'}),

    ])


if __name__ == '__main__':
    app.run_server(debug=True)
