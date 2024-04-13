app.layout = html.Div(children=[ html.H1("Flight Delay Time Statistics",style={"textAlign":"center","color":"#503D36","font-size":30}
                                html.Div(["Input Year: ", dcc.Input(id="input-year",value=2010,type="number",style={"height":"35px","font-size":30})],
                                style={'font-size': 30}),
                                html.Br(),
                                html.Br(), 
                                html.Div([
                                        html.Div(dcc.Graph(id="carrier-plot")),
                                        html.Div(dcc.Graph(id="weather-plot"))
                                ], style={'display': 'flex'}),
    
                                html.Div([
                                        html.Div(dcc.Graph(id="nas-plot")),
                                        html.Div(dcc.Graph(id="security-plot"))
                                ], style={'display': 'flex'}),
                                
                                html.Div(dcc.Graph(id="late-plot"), style={'width':'65%'})])