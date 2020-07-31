import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Output, Input

from functions import vacantes, preprocessing
from main import semestre, ramos

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
colors = {
    'background': '#250000',
    'text': 'white'
}
siglas = [r['sigla'] for r in ramos]  # Para usar en el Output de los callbacks

n_rows = len(ramos) // 2 if len(ramos) % 2 == 0 else len(ramos) // 2 + 1
rows = [[] for _ in range(n_rows)]
for ramo in ramos:
    for row in rows:
        if len(row) < 2:
            pass
        else:
            continue
        nrc, sigla, sec = ramo.values()
        data, name_ = vacantes(semestre, nrc, sigla, sec)
        df = preprocessing(data)

        fig = px.sunburst(
            data_frame=df, path=['T_Vacante', 'Escuela'],
            values='Vacantes',
            color='T_Vacante',
            color_discrete_map={'Disponible': 'Lavender',
                                'Ocupada': 'Firebrick'},
        )
        fig.update_layout(margin=dict(t=30, b=30),
                          plot_bgcolor=colors['background'],
                          paper_bgcolor=colors['background'],
                          font_color=colors['text'],
                          )
        row.append(
            html.Div([
                html.H6(children=[
                    html.B(children=f'{sigla}-{sec}',
                           style={'textAlign': 'center',
                                  'color': colors['text']}), f': {name_}'
                ],
                    style={'textAlign': 'center',
                           'color': colors['text']}),
                dcc.Graph(id=f'{sigla}', figure=fig, animate=True)
            ], className="six columns")
        )
        break

rows = [html.Div(row, className='row') for row in rows]
children = [
               html.H1(children=[
                   html.B(children=f'Toma de ramos {semestre}')
               ],
                   style={'textAlign': 'center',
                          'color': colors['text'],
                          'marginTop': 25})
           ] + rows + [dcc.Interval(id='graph-update', interval=5 * 1000)]

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=children)


@app.callback([Output(s, 'figure') for s in siglas],
              [Input('graph-update', 'n_intervals')])
def update_graphs(_):
    """

    Returns
    -------
    list
      Lista de figuras que se actualizarán en la página
    """
    # print('Updating!')
    figures = []
    for ramo in ramos:
        nrc, sigla, sec = ramo.values()
        data, name_ = vacantes(semestre, nrc, sigla, sec)
        df = preprocessing(data)

        fig = px.sunburst(
            data_frame=df, path=['T_Vacante', 'Escuela'],
            values='Vacantes',
            color='T_Vacante',
            color_discrete_map={'Disponible': 'Lavender',
                                'Ocupada': 'Firebrick'}
        )
        fig.update_layout(margin=dict(t=30, b=30),
                          plot_bgcolor=colors['background'],
                          paper_bgcolor=colors['background'],
                          font_color=colors['text'])
        figures.append(fig)
    return figures


if __name__ == '__main__':
    app.run_server(debug=True)
