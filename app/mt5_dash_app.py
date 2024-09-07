# # # # from dash import Dash, html, dcc
# # # # import dash_bootstrap_components as dbc
# # # # from dash.dependencies import Input, Output, State
# # # # import pandas as pd
# # # # import plotly.graph_objects as go
# # # # import MetaTrader5 as mt5
# # # # from mt5_funcs import get_symbol_names, TIMEFRAMES, TIMEFRAME_DICT

# # # # # creates the Dash App
# # # # app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# # # # symbol_dropdown = html.Div([
# # # #     html.P('Symbol:'),
# # # #     dcc.Dropdown(
# # # #         id='symbol-dropdown',
# # # #         options=[{'label': symbol, 'value': symbol} for symbol in get_symbol_names()],
# # # #         value='EURUSD'
# # # #     )
# # # # ])

# # # # timeframe_dropdown = html.Div([
# # # #     html.P('Timeframe:'),
# # # #     dcc.Dropdown(
# # # #         id='timeframe-dropdown',
# # # #         options=[{'label': timeframe, 'value': timeframe} for timeframe in TIMEFRAMES],
# # # #         value='D1'
# # # #     )
# # # # ])

# # # # num_bars_input = html.Div([
# # # #     html.P('Number of Candles'),
# # # #     dbc.Input(id='num-bar-input', type='number', value='20')
# # # # ])

# # # # # creates the layout of the App
# # # # app.layout = html.Div([
# # # #     html.H1('Real Time Charts'),

# # # #     dbc.Row([
# # # #         dbc.Col(symbol_dropdown),
# # # #         dbc.Col(timeframe_dropdown),
# # # #         dbc.Col(num_bars_input)
# # # #     ]),

# # # #     html.Hr(),

# # # #     dcc.Interval(id='update', interval=200),

# # # #     html.Div(id='page-content')

# # # # ], style={'margin-left': '5%', 'margin-right': '5%', 'margin-top': '20px'})


# # # # @app.callback(
# # # #     Output('page-content', 'children'),
# # # #     Input('update', 'n_intervals'),
# # # #     State('symbol-dropdown', 'value'), State('timeframe-dropdown', 'value'), State('num-bar-input', 'value')
# # # # )
# # # # def update_ohlc_chart(interval, symbol, timeframe, num_bars):
# # # #     timeframe_str = timeframe
# # # #     timeframe = TIMEFRAME_DICT[timeframe]
# # # #     num_bars = int(num_bars)

# # # #     print(symbol, timeframe, num_bars)

# # # #     bars = mt5.copy_rates_from_pos(symbol, timeframe, 0, num_bars)
# # # #     df = pd.DataFrame(bars)
# # # #     df['time'] = pd.to_datetime(df['time'], unit='s')

# # # #     fig = go.Figure(data=go.Candlestick(x=df['time'],
# # # #                     open=df['open'],
# # # #                     high=df['high'],
# # # #                     low=df['low'],
# # # #                     close=df['close']))

# # # #     fig.update(layout_xaxis_rangeslider_visible=False)
# # # #     fig.update_layout(yaxis={'side': 'right'})
# # # #     fig.layout.xaxis.fixedrange = True
# # # #     fig.layout.yaxis.fixedrange = True

# # # #     return [
# # # #         html.H2(id='chart-details', children=f'{symbol} - {timeframe_str}'),
# # # #         dcc.Graph(figure=fig, config={'displayModeBar': False})
# # # #         ]


# # # # if __name__ == '__main__':
# # # #     # starts the server
# # # #     app.run_server()
# # # from dash import Dash, html, dcc, callback
# # # import dash_bootstrap_components as dbc
# # # from dash.dependencies import Input, Output, State
# # # import pandas as pd
# # # import plotly.graph_objects as go
# # # import MetaTrader5 as mt5
# # # from mt5_funcs import get_symbol_names, TIMEFRAMES, TIMEFRAME_DICT
# # # import plotly.io as pio

# # # # Set up dark theme for Plotly
# # # pio.templates.default = "plotly_dark"

# # # # Create the Dash App with dark theme
# # # app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# # # # Improved layouts for dropdowns and inputs
# # # def create_dropdown(id, options, value, label):
# # #     return html.Div([
# # #         html.Label(label, className='text-light'),
# # #         dcc.Dropdown(
# # #             id=id,
# # #             options=[{'label': opt, 'value': opt} for opt in options],
# # #             value=value,
# # #             className='mb-3'
# # #         )
# # #     ])

# # # symbol_dropdown = create_dropdown('symbol-dropdown', get_symbol_names(), 'EURUSD', 'Symbol:')
# # # timeframe_dropdown = create_dropdown('timeframe-dropdown', TIMEFRAMES, 'D1', 'Timeframe:')

# # # num_bars_input = html.Div([
# # #     html.Label('Number of Candles:', className='text-light'),
# # #     dbc.Input(id='num-bar-input', type='number', value=100, min=10, max=1000, step=10, className='mb-3')
# # # ])

# # # # New features
# # # indicator_dropdown = create_dropdown('indicator-dropdown', ['None', 'SMA', 'EMA', 'Bollinger Bands'], 'None', 'Indicator:')
# # # period_input = html.Div([
# # #     html.Label('Indicator Period:', className='text-light'),
# # #     dbc.Input(id='period-input', type='number', value=20, min=1, max=200, step=1, className='mb-3')
# # # ])

# # # # Improved layout
# # # app.layout = dbc.Container([
# # #     html.H1('Real-Time Forex Charts', className='text-center text-light mt-4 mb-4'),

# # #     dbc.Row([
# # #         dbc.Col(symbol_dropdown, width=3),
# # #         dbc.Col(timeframe_dropdown, width=3),
# # #         dbc.Col(num_bars_input, width=2),
# # #         dbc.Col(indicator_dropdown, width=2),
# # #         dbc.Col(period_input, width=2),
# # #     ], className='mb-4'),

# # #     dcc.Graph(id='ohlc-chart', config={'displayModeBar': True, 'scrollZoom': True}),

# # #     dcc.Interval(id='update', interval=1000),  # Update every second

# # # ], fluid=True, style={'backgroundColor': '#222', 'minHeight': '100vh'})

# # # @app.callback(
# # #     Output('ohlc-chart', 'figure'),
# # #     [Input('update', 'n_intervals'),
# # #      Input('symbol-dropdown', 'value'),
# # #      Input('timeframe-dropdown', 'value'),
# # #      Input('num-bar-input', 'value'),
# # #      Input('indicator-dropdown', 'value'),
# # #      Input('period-input', 'value')]
# # # )
# # # def update_ohlc_chart(interval, symbol, timeframe, num_bars, indicator, period):
# # #     timeframe = TIMEFRAME_DICT[timeframe]
# # #     num_bars = int(num_bars)
# # #     period = int(period)

# # #     bars = mt5.copy_rates_from_pos(symbol, timeframe, 0, num_bars)
# # #     df = pd.DataFrame(bars)
# # #     df['time'] = pd.to_datetime(df['time'], unit='s')

# # #     fig = go.Figure()

# # #     # Candlestick chart
# # #     fig.add_trace(go.Candlestick(
# # #         x=df['time'],
# # #         open=df['open'],
# # #         high=df['high'],
# # #         low=df['low'],
# # #         close=df['close'],
# # #         name='OHLC'
# # #     ))

# # #     # Add indicators
# # #     if indicator == 'SMA':
# # #         df['SMA'] = df['close'].rolling(window=period).mean()
# # #         fig.add_trace(go.Scatter(x=df['time'], y=df['SMA'], name=f'SMA ({period})'))
# # #     elif indicator == 'EMA':
# # #         df['EMA'] = df['close'].ewm(span=period, adjust=False).mean()
# # #         fig.add_trace(go.Scatter(x=df['time'], y=df['EMA'], name=f'EMA ({period})'))
# # #     elif indicator == 'Bollinger Bands':
# # #         df['SMA'] = df['close'].rolling(window=period).mean()
# # #         df['BOLU'] = df['SMA'] + 2 * df['close'].rolling(window=period).std()
# # #         df['BOLD'] = df['SMA'] - 2 * df['close'].rolling(window=period).std()
# # #         fig.add_trace(go.Scatter(x=df['time'], y=df['BOLU'], name='Upper BB', line=dict(dash='dash')))
# # #         fig.add_trace(go.Scatter(x=df['time'], y=df['BOLD'], name='Lower BB', line=dict(dash='dash')))

# # #     # Improve chart layout
# # #     fig.update_layout(
# # #         title=f'{symbol} - {TIMEFRAMES[list(TIMEFRAME_DICT.values()).index(timeframe)]}',
# # #         yaxis_title='Price',
# # #         xaxis_rangeslider_visible=False,
# # #         legend_title_text='Legend',
# # #         height=700,
# # #         template='plotly_dark',
# # #         hovermode='x unified',
# # #         yaxis={'side': 'right'}
# # #     )

# # #     fig.update_xaxes(
# # #         rangeslider_visible=False,
# # #         rangeselector=dict(
# # #             buttons=list([
# # #                 dict(count=1, label="1d", step="day", stepmode="backward"),
# # #                 dict(count=7, label="1w", step="day", stepmode="backward"),
# # #                 dict(count=1, label="1m", step="month", stepmode="backward"),
# # #                 dict(count=6, label="6m", step="month", stepmode="backward"),
# # #                 dict(count=1, label="YTD", step="year", stepmode="todate"),
# # #                 dict(count=1, label="1y", step="year", stepmode="backward"),
# # #                 dict(step="all")
# # #             ])
# # #         )
# # #     )

# # #     return fig

# # # if __name__ == '__main__':
# # #     app.run_server(debug=True)

# # from dash import Dash, html, dcc, callback
# # import dash_bootstrap_components as dbc
# # from dash.dependencies import Input, Output, State
# # import pandas as pd
# # import plotly.graph_objects as go
# # import MetaTrader5 as mt5
# # from mt5_funcs import get_symbol_names, TIMEFRAMES, TIMEFRAME_DICT
# # import plotly.io as pio
# # import numpy as np
# # from ta.trend import MACD
# # from ta.momentum import RSIIndicator
# # from ta.volatility import BollingerBands

# # # Set up dark theme for Plotly
# # pio.templates.default = "plotly_dark"

# # # Create the Dash App with dark theme
# # app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# # # Improved layouts for dropdowns and inputs
# # def create_dropdown(id, options, value, label):
# #     return html.Div([
# #         html.Label(label, className='text-light'),
# #         dcc.Dropdown(
# #             id=id,
# #             options=[{'label': opt, 'value': opt} for opt in options],
# #             value=value,
# #             className='mb-3'
# #         )
# #     ])

# # symbol_dropdown = create_dropdown('symbol-dropdown', get_symbol_names(), 'EURUSD', 'Symbol:')
# # timeframe_dropdown = create_dropdown('timeframe-dropdown', TIMEFRAMES, 'H1', 'Timeframe:')

# # num_bars_input = html.Div([
# #     html.Label('Number of Candles:', className='text-light'),
# #     dbc.Input(id='num-bar-input', type='number', value=200, min=50, max=5000, step=50, className='mb-3')
# # ])

# # # Enhanced indicator selection
# # indicator_checklist = dbc.Checklist(
# #     id='indicator-checklist',
# #     options=[
# #         {'label': 'SMA', 'value': 'SMA'},
# #         {'label': 'EMA', 'value': 'EMA'},
# #         {'label': 'Bollinger Bands', 'value': 'BB'},
# #         {'label': 'MACD', 'value': 'MACD'},
# #         {'label': 'RSI', 'value': 'RSI'},
# #     ],
# #     value=['SMA', 'EMA'],
# #     inline=True,
# #     className='mb-3'
# # )

# # period_input = html.Div([
# #     html.Label('SMA/EMA Period:', className='text-light'),
# #     dbc.Input(id='period-input', type='number', value=20, min=1, max=200, step=1, className='mb-3')
# # ])

# # # Improved layout
# # app.layout = dbc.Container([
# #     html.H1('Advanced Forex Charts', className='text-center text-light mt-4 mb-4'),

# #     dbc.Row([
# #         dbc.Col(symbol_dropdown, width=3),
# #         dbc.Col(timeframe_dropdown, width=3),
# #         dbc.Col(num_bars_input, width=2),
# #         dbc.Col(period_input, width=2),
# #     ], className='mb-4'),

# #     dbc.Row([
# #         dbc.Col(html.Label("Select Indicators:", className='text-light'), width=2),
# #         dbc.Col(indicator_checklist, width=10),
# #     ], className='mb-4'),

# #     dcc.Loading(
# #         id="loading-1",
# #         type="default",
# #         children=[dcc.Graph(id='ohlc-chart', config={'displayModeBar': True, 'scrollZoom': True})],
# #     ),

# #     html.Div(id='price-info', className='text-light mt-3'),

# #     # dcc.Interval(id='update', interval=5000),  # Update every 5 seconds

# # ], fluid=True, style={'backgroundColor': '#222', 'minHeight': '100vh'})

# # @app.callback(
# #     [Output('ohlc-chart', 'figure'),
# #      Output('price-info', 'children')],
# #     [Input('update', 'n_intervals'),
# #      Input('symbol-dropdown', 'value'),
# #      Input('timeframe-dropdown', 'value'),
# #      Input('num-bar-input', 'value'),
# #      Input('indicator-checklist', 'value'),
# #      Input('period-input', 'value')]
# # )
# # def update_ohlc_chart(interval, symbol, timeframe, num_bars, indicators, period):
# #     timeframe = TIMEFRAME_DICT[timeframe]
# #     num_bars = int(num_bars)
# #     period = int(period)

# #     bars = mt5.copy_rates_from_pos(symbol, timeframe, 0, num_bars)
# #     df = pd.DataFrame(bars)
# #     df['time'] = pd.to_datetime(df['time'], unit='s')

# #     fig = go.Figure()

# #     # Candlestick chart
# #     fig.add_trace(go.Candlestick(
# #         x=df['time'],
# #         open=df['open'],
# #         high=df['high'],
# #         low=df['low'],
# #         close=df['close'],
# #         name='OHLC'
# #     ))

# #     # Add indicators
# #     if 'SMA' in indicators:
# #         df['SMA'] = df['close'].rolling(window=period).mean()
# #         fig.add_trace(go.Scatter(x=df['time'], y=df['SMA'], name=f'SMA ({period})', line=dict(color='yellow')))

# #     if 'EMA' in indicators:
# #         df['EMA'] = df['close'].ewm(span=period, adjust=False).mean()
# #         fig.add_trace(go.Scatter(x=df['time'], y=df['EMA'], name=f'EMA ({period})', line=dict(color='magenta')))

# #     if 'BB' in indicators:
# #         bb = BollingerBands(df['close'], window=20, window_dev=2)
# #         df['BB_upper'] = bb.bollinger_hband()
# #         df['BB_lower'] = bb.bollinger_lband()
# #         fig.add_trace(go.Scatter(x=df['time'], y=df['BB_upper'], name='Upper BB', line=dict(color='lightblue', dash='dash')))
# #         fig.add_trace(go.Scatter(x=df['time'], y=df['BB_lower'], name='Lower BB', line=dict(color='lightblue', dash='dash')))

# #     if 'MACD' in indicators:
# #         macd = MACD(df['close'])
# #         df['MACD'] = macd.macd()
# #         df['MACD_signal'] = macd.macd_signal()
# #         fig.add_trace(go.Scatter(x=df['time'], y=df['MACD'], name='MACD', line=dict(color='cyan')))
# #         fig.add_trace(go.Scatter(x=df['time'], y=df['MACD_signal'], name='MACD Signal', line=dict(color='orange')))

# #     if 'RSI' in indicators:
# #         rsi = RSIIndicator(df['close'], window=14)
# #         df['RSI'] = rsi.rsi()
# #         fig.add_trace(go.Scatter(x=df['time'], y=df['RSI'], name='RSI', line=dict(color='purple'), yaxis="y2"))

# #     # Improve chart layout
# #     fig.update_layout(
# #         title=f'{symbol} - {TIMEFRAMES[list(TIMEFRAME_DICT.values()).index(timeframe)]}',
# #         yaxis_title='Price',
# #         xaxis_rangeslider_visible=False,
# #         legend_title_text='Legend',
# #         height=800,
# #         template='plotly_dark',
# #         hovermode='x unified',
# #         yaxis=dict(
# #             title="Price",
# #             side="right",
# #             showgrid=False
# #         ),
# #         yaxis2=dict(
# #             title="RSI",
# #             overlaying="y",
# #             side="left",
# #             range=[0, 100],
# #             showgrid=False
# #         )
# #     )

# #     fig.update_xaxes(
# #         rangeslider_visible=False,
# #         rangeselector=dict(
# #             buttons=list([
# #                 dict(count=1, label="1h", step="hour", stepmode="backward"),
# #                 dict(count=1, label="1d", step="day", stepmode="backward"),
# #                 dict(count=7, label="1w", step="day", stepmode="backward"),
# #                 dict(count=1, label="1m", step="month", stepmode="backward"),
# #                 dict(count=6, label="6m", step="month", stepmode="backward"),
# #                 dict(count=1, label="YTD", step="year", stepmode="todate"),
# #                 dict(count=1, label="1y", step="year", stepmode="backward"),
# #                 dict(step="all")
# #             ])
# #         )
# #     )

# #     # Price information
# #     last_price = df['close'].iloc[-1]
# #     price_change = df['close'].iloc[-1] - df['close'].iloc[-2]
# #     price_change_pct = (price_change / df['close'].iloc[-2]) * 100

# #     price_info = html.Div([
# #         html.H3(f"Current Price: {last_price:.5f}"),
# #         html.P(f"Change: {price_change:.5f} ({price_change_pct:.2f}%)",
# #                style={'color': 'green' if price_change >= 0 else 'red'})
# #     ])

# #     return fig, price_info

# # if __name__ == '__main__':
# #     app.run_server(debug=True)
# import asyncio
# import json
# from dash import Dash, html, dcc, callback
# import dash_bootstrap_components as dbc
# from dash.dependencies import Input, Output, State
# import pandas as pd
# import plotly.graph_objects as go
# from mt5_funcs import get_symbol_names, TIMEFRAMES, TIMEFRAME_DICT
# import plotly.io as pio
# from ta.trend import MACD, IchimokuIndicator
# from ta.momentum import RSIIndicator
# from ta.volatility import BollingerBands, AverageTrueRange
# import websocket
# from threading import Thread

# # Set up dark theme for Plotly
# pio.templates.default = "plotly_dark"

# # Create the Dash App with dark theme
# app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# # Global variable to store the latest data
# latest_data = {}

# # WebSocket setup
# def on_message(ws, message):
#     global latest_data
#     data = json.loads(message)
#     latest_data = data

# def on_error(ws, error):
#     print(error)

# def on_close(ws):
#     print("WebSocket connection closed")

# def on_open(ws):
#     print("WebSocket connection opened")

# def run_websocket():
#     websocket.enableTrace(True)
#     ws = websocket.WebSocketApp("ws://localhost:8765",
#                                 on_message=on_message,
#                                 on_error=on_error,
#                                 on_close=on_close,
#                                 on_open=on_open)
#     ws.run_forever()

# # Start WebSocket connection in a separate thread
# websocket_thread = Thread(target=run_websocket)
# websocket_thread.start()

# # Improved layouts for dropdowns and inputs
# def create_dropdown(id, options, value, label):
#     return html.Div([
#         html.Label(label, className='text-light'),
#         dcc.Dropdown(
#             id=id,
#             options=[{'label': opt, 'value': opt} for opt in options],
#             value=value,
#             className='mb-3'
#         )
#     ])

# symbol_dropdown = create_dropdown('symbol-dropdown', get_symbol_names(), 'EURUSD', 'Symbol:')
# timeframe_dropdown = create_dropdown('timeframe-dropdown', TIMEFRAMES, 'H1', 'Timeframe:')

# num_bars_input = html.Div([
#     html.Label('Number of Candles:', className='text-light'),
#     dbc.Input(id='num-bar-input', type='number', value=500, min=50, max=10000, step=50, className='mb-3')
# ])

# # Enhanced indicator selection
# indicator_checklist = dbc.Checklist(
#     id='indicator-checklist',
#     options=[
#         {'label': 'SMA', 'value': 'SMA'},
#         {'label': 'EMA', 'value': 'EMA'},
#         {'label': 'Bollinger Bands', 'value': 'BB'},
#         {'label': 'MACD', 'value': 'MACD'},
#         {'label': 'RSI', 'value': 'RSI'},
#         {'label': 'Stochastic', 'value': 'Stoch'},
#         {'label': 'Ichimoku Cloud', 'value': 'Ichimoku'},
#         {'label': 'ATR', 'value': 'ATR'},
#     ],
#     value=['SMA', 'EMA'],
#     inline=True,
#     className='mb-3'
# )

# period_input = html.Div([
#     html.Label('SMA/EMA Period:', className='text-light'),
#     dbc.Input(id='period-input', type='number', value=20, min=1, max=200, step=1, className='mb-3')
# ])

# # Chart type selection
# chart_type_radio = dbc.RadioItems(
#     id='chart-type-radio',
#     options=[
#         {'label': 'Candlestick', 'value': 'candlestick'},
#         {'label': 'OHLC', 'value': 'ohlc'},
#         {'label': 'Line', 'value': 'line'},
#     ],
#     value='candlestick',
#     inline=True,
#     className='mb-3'
# )

# # Improved layout
# app.layout = dbc.Container([
#     html.H1('Advanced Forex Analytics Dashboard', className='text-center text-light mt-4 mb-4'),

#     dbc.Row([
#         dbc.Col(symbol_dropdown, width=3),
#         dbc.Col(timeframe_dropdown, width=3),
#         dbc.Col(num_bars_input, width=2),
#         dbc.Col(period_input, width=2),
#         dbc.Col(chart_type_radio, width=2),
#     ], className='mb-4'),

#     dbc.Row([
#         dbc.Col(html.Label("Select Indicators:", className='text-light'), width=2),
#         dbc.Col(indicator_checklist, width=10),
#     ], className='mb-4'),

#     dcc.Loading(
#         id="loading-1",
#         type="default",
#         children=[dcc.Graph(id='main-chart', config={'displayModeBar': True, 'scrollZoom': True})],
#     ),

#     html.Div(id='price-info', className='text-light mt-3'),

#     dbc.Row([
#         dbc.Col(dcc.Graph(id='volume-chart'), width=6),
#         dbc.Col(dcc.Graph(id='rsi-chart'), width=6),
#     ], className='mt-4'),

#     dcc.Interval(id='update-interval', interval=100),  # Update every 100ms

# ], fluid=True, style={'backgroundColor': '#222', 'minHeight': '100vh'})

# @app.callback(
#     Output('symbol-dropdown', 'value'),
#     Input('symbol-dropdown', 'value')
# )
# def update_symbol(value):
#     if value:
#         ws = websocket.WebSocket()
#         ws.connect("ws://localhost:8765")
#         ws.send(json.dumps({"symbol": value}))
#         ws.close()
#     return value

# @app.callback(
#     [Output('main-chart', 'figure'),
#      Output('price-info', 'children'),
#      Output('volume-chart', 'figure'),
#      Output('rsi-chart', 'figure')],
#     [Input('update-interval', 'n_intervals'),
#      Input('symbol-dropdown', 'value'),
#      Input('timeframe-dropdown', 'value'),
#      Input('num-bar-input', 'value'),
#      Input('indicator-checklist', 'value'),
#      Input('period-input', 'value'),
#      Input('chart-type-radio', 'value')]
# )
# def update_charts(n_intervals, symbol, timeframe, num_bars, indicators, period, chart_type):
#     global latest_data

#     if not latest_data:
#         return {}, "", {}, {}

#     df = pd.DataFrame(latest_data['bars'])
#     df['time'] = pd.to_datetime(df['time'], unit='s')

#     # ... (rest of the update_charts function remains the same)

#     return fig, price_info, volume_fig, rsi_fig

# if __name__ == '__main__':
#     app.run_server(debug=True)

import json
from dash import Dash, html, dcc, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objects as go
from mt5_funcs import get_symbol_names, TIMEFRAMES, TIMEFRAME_DICT
import plotly.io as pio
from ta.trend import MACD, IchimokuIndicator
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands, AverageTrueRange
import websocket
from threading import Thread

# Set up dark theme for Plotly
pio.templates.default = "plotly_dark"

# Create the Dash App with dark theme
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Global variable to store the latest data
latest_data = {}

# WebSocket setup
def on_message(ws, message):
    global latest_data
    data = json.loads(message)
    latest_data = data

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("WebSocket connection closed")

def on_open(ws):
    print("WebSocket connection opened")

def run_websocket():
    ws = websocket.WebSocketApp("ws://localhost:8765",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                on_open=on_open)
    ws.run_forever()

# Start WebSocket connection in a separate thread
websocket_thread = Thread(target=run_websocket)
websocket_thread.start()

# Improved layouts for dropdowns and inputs
def create_dropdown(id, options, value, label):
    return html.Div([
        html.Label(label, className='text-light'),
        dcc.Dropdown(
            id=id,
            options=[{'label': opt, 'value': opt} for opt in options],
            value=value,
            className='mb-3'
        )
    ])

symbol_dropdown = create_dropdown('symbol-dropdown', get_symbol_names(), 'EURUSD', 'Symbol:')
timeframe_dropdown = create_dropdown('timeframe-dropdown', TIMEFRAMES, 'H1', 'Timeframe:')

num_bars_input = html.Div([
    html.Label('Number of Candles:', className='text-light'),
    dbc.Input(id='num-bar-input', type='number', value=500, min=50, max=10000, step=50, className='mb-3')
])

# Enhanced indicator selection
indicator_checklist = dbc.Checklist(
    id='indicator-checklist',
    options=[
        {'label': 'SMA', 'value': 'SMA'},
        {'label': 'EMA', 'value': 'EMA'},
        {'label': 'Bollinger Bands', 'value': 'BB'},
        {'label': 'MACD', 'value': 'MACD'},
        {'label': 'RSI', 'value': 'RSI'},
        {'label': 'Stochastic', 'value': 'Stoch'},
        {'label': 'Ichimoku Cloud', 'value': 'Ichimoku'},
        {'label': 'ATR', 'value': 'ATR'},
    ],
    value=['SMA', 'EMA'],
    inline=True,
    className='mb-3'
)

period_input = html.Div([
    html.Label('SMA/EMA Period:', className='text-light'),
    dbc.Input(id='period-input', type='number', value=20, min=1, max=200, step=1, className='mb-3')
])

# Chart type selection
chart_type_radio = dbc.RadioItems(
    id='chart-type-radio',
    options=[
        {'label': 'Candlestick', 'value': 'candlestick'},
        {'label': 'OHLC', 'value': 'ohlc'},
        {'label': 'Line', 'value': 'line'},
    ],
    value='candlestick',
    inline=True,
    className='mb-3'
)

# Improved layout
app.layout = dbc.Container([
    html.H1('Advanced Forex Analytics Dashboard', className='text-center text-light mt-4 mb-4'),

    dbc.Row([
        dbc.Col(symbol_dropdown, width=3),
        dbc.Col(timeframe_dropdown, width=3),
        dbc.Col(num_bars_input, width=2),
        dbc.Col(period_input, width=2),
        dbc.Col(chart_type_radio, width=2),
    ], className='mb-4'),

    dbc.Row([
        dbc.Col(html.Label("Select Indicators:", className='text-light'), width=2),
        dbc.Col(indicator_checklist, width=10),
    ], className='mb-4'),

    dcc.Loading(
        id="loading-1",
        type="default",
        children=[dcc.Graph(id='main-chart', config={'displayModeBar': True, 'scrollZoom': True})],
    ),

    html.Div(id='price-info', className='text-light mt-3'),

    dbc.Row([
        dbc.Col(dcc.Graph(id='volume-chart'), width=6),
        dbc.Col(dcc.Graph(id='rsi-chart'), width=6),
    ], className='mt-4'),

    dcc.Interval(id='update-interval', interval=10000),  # Update every 100ms

], fluid=True, style={'backgroundColor': '#222', 'minHeight': '100vh'})

@app.callback(
    Output('symbol-dropdown', 'value'),
    Input('symbol-dropdown', 'value')
)
def update_symbol(value):
    if value:
        ws = websocket.create_connection("ws://localhost:8765")
        ws.send(json.dumps({"symbol": value}))
        ws.close()
    return value

@app.callback(
    [Output('main-chart', 'figure'),
     Output('price-info', 'children'),
     Output('volume-chart', 'figure'),
     Output('rsi-chart', 'figure')],
    [Input('update-interval', 'n_intervals'),
     Input('symbol-dropdown', 'value'),
     Input('timeframe-dropdown', 'value'),
     Input('num-bar-input', 'value'),
     Input('indicator-checklist', 'value'),
     Input('period-input', 'value'),
     Input('chart-type-radio', 'value')]
)
def update_charts(n_intervals, symbol, timeframe, num_bars, indicators, period, chart_type):
    global latest_data

    if not latest_data:
        return {}, "", {}, {}

    df = pd.DataFrame(latest_data['bars'])
    df['time'] = pd.to_datetime(df['time'], unit='s')

    fig = go.Figure()

    # Main chart
    if chart_type == 'candlestick':
        fig.add_trace(go.Candlestick(
            x=df['time'],
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'],
            name='OHLC'
        ))
    elif chart_type == 'ohlc':
        fig.add_trace(go.Ohlc(
            x=df['time'],
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'],
            name='OHLC'
        ))
    else:  # line chart
        fig.add_trace(go.Scatter(
            x=df['time'],
            y=df['close'],
            mode='lines',
            name='Close'
        ))

    # Add indicators
    if 'SMA' in indicators:
        df['SMA'] = df['close'].rolling(window=period).mean()
        fig.add_trace(go.Scatter(x=df['time'], y=df['SMA'], name=f'SMA ({period})', line=dict(color='yellow')))

    if 'EMA' in indicators:
        df['EMA'] = df['close'].ewm(span=period, adjust=False).mean()
        fig.add_trace(go.Scatter(x=df['time'], y=df['EMA'], name=f'EMA ({period})', line=dict(color='magenta')))

    if 'BB' in indicators:
        bb = BollingerBands(df['close'], window=20, window_dev=2)
        df['BB_upper'] = bb.bollinger_hband()
        df['BB_lower'] = bb.bollinger_lband()
        fig.add_trace(go.Scatter(x=df['time'], y=df['BB_upper'], name='Upper BB', line=dict(color='lightblue', dash='dash')))
        fig.add_trace(go.Scatter(x=df['time'], y=df['BB_lower'], name='Lower BB', line=dict(color='lightblue', dash='dash')))

    if 'MACD' in indicators:
        macd = MACD(df['close'])
        df['MACD'] = macd.macd()
        df['MACD_signal'] = macd.macd_signal()
        fig.add_trace(go.Scatter(x=df['time'], y=df['MACD'], name='MACD', line=dict(color='cyan')))
        fig.add_trace(go.Scatter(x=df['time'], y=df['MACD_signal'], name='MACD Signal', line=dict(color='orange')))

    if 'Ichimoku' in indicators:
        ichimoku = IchimokuIndicator(df['high'], df['low'])
        df['ichimoku_a'] = ichimoku.ichimoku_a()
        df['ichimoku_b'] = ichimoku.ichimoku_b()
        fig.add_trace(go.Scatter(x=df['time'], y=df['ichimoku_a'], name='Ichimoku A', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=df['time'], y=df['ichimoku_b'], name='Ichimoku B', line=dict(color='red')))

    if 'ATR' in indicators:
        atr = AverageTrueRange(df['high'], df['low'], df['close'], window=14)
        df['ATR'] = atr.average_true_range()
        fig.add_trace(go.Scatter(x=df['time'], y=df['ATR'], name='ATR', line=dict(color='orange'), yaxis="y3"))

    # Improve main chart layout
    fig.update_layout(
        title=f'{symbol} - {timeframe}',
        yaxis_title='Price',
        xaxis_rangeslider_visible=False,
        legend_title_text='Legend',
        height=600,
        template='plotly_dark',
        hovermode='x unified',
        yaxis=dict(title="Price", side="right", showgrid=False),
        yaxis3=dict(title="ATR", overlaying="y", side="left", showgrid=False)
    )

    fig.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1h", step="hour", stepmode="backward"),
                dict(count=1, label="1d", step="day", stepmode="backward"),
                dict(count=7, label="1w", step="day", stepmode="backward"),
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    # Price information
    last_price = df['close'].iloc[-1]
    price_change = df['close'].iloc[-1] - df['close'].iloc[-2]
    price_change_pct = (price_change / df['close'].iloc[-2]) * 100

    price_info = html.Div([
        html.H3(f"Current Price: {last_price:.5f}"),
        html.P(f"Change: {price_change:.5f} ({price_change_pct:.2f}%)",
               style={'color': 'green' if price_change >= 0 else 'red'})
    ])

    # Volume chart
    volume_fig = go.Figure(go.Bar(x=df['time'], y=df['tick_volume'], name='Volume'))
    volume_fig.update_layout(
        title='Volume',
        height=300,
        template='plotly_dark',
        xaxis_rangeslider_visible=False
    )

    # RSI chart
    rsi = RSIIndicator(df['close'], window=14)
    df['RSI'] = rsi.rsi()
    rsi_fig = go.Figure(go.Scatter(x=df['time'], y=df['RSI'], name='RSI'))
    rsi_fig.add_hline(y=70, line_dash="dash", line_color="red")
    rsi_fig.add_hline(y=30, line_dash="dash", line_color="green")
    rsi_fig.update_layout(
        title='RSI (14)',
        height=300,
        template='plotly_dark',
        yaxis=dict(range=[0, 100]),
        xaxis_rangeslider_visible=False
    )

    return fig, price_info, volume_fig, rsi_fig

if __name__ == '__main__':
    app.run_server(debug=True)
