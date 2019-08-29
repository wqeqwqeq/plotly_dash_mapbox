#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
#import pandas_datareader.data as web # requires v0.6.0 or later
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go
import pymongo
import dns
import json

client = pymongo.MongoClient("mongodb+srv://Alluser:123@cluster0-ujbuf.mongodb.net/test?retryWrites=true&w=majority")
db = client['GlobalAI']
collection = db['old_data'] 

com_name=pd.read_csv('https://raw.githubusercontent.com/knightblackersun/csvtest/master/Company_list.csv')
company_name=com_name['0'].tolist()
indicator=pd.read_csv('https://raw.githubusercontent.com/knightblackersun/csvtest/master/indicators.csv')
indicator_name=indicator['0'].tolist()


app = dash.Dash()

#options = ciss.drop(['COMPANY','Sector','DATE'], axis = 1)
server=app.server

#ciss['DATE'] = pd.to_datetime(ciss.DATE)
#Index dataset by 'Date' column.
#ciss.set_index('DATE', inplace=True)

#options = [{'label': i, 'value': i} for i in ciss.columns]
#options.append({'label':'{}'.format('SPY'), 'value':'SPY'})
#[{'label': i, 'value': i} for i in ciss.columns]


app.layout = html.Div([
    html.H1('SDG Index'),
    html.Div([
    html.H3('Select Company:', style={'paddingRight':'30px'}),
        # replace dcc.Input with dcc.Options, set options=options
        dcc.Dropdown(
            id='company_ticker',
            options=[{'label': i, 'value': i} for i in company_name],
            value=['a o smith'],
            #multi=True
        )
    # widen the Div to fit multiple inputs
    ], style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}), html.Div([
        html.H3('Select indicator:', style={'paddingRight':'30px'}),
        # replace dcc.Input with dcc.Options, set options=options
        dcc.Dropdown(
            id='my_indicator_symbol',
            options = [{'label': i, 'value': i} for i in indicator_name],
            value=['SDG_1'],
            #multi=True
        )
    # widen the Div to fit multiple inputs
    ], style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}),
    
    html.Div([
        html.H3('Select start and end dates:'),
        dcc.DatePickerRange(
            id='my_date_picker',
            min_date_allowed=datetime(2011, 1, 1),
            max_date_allowed=datetime(2019, 1, 2),
            start_date=str(datetime(2015, 2, 19)),
            end_date=str(datetime(2019, 1, 2))
        )
    ], style={'display':'inline-block'}),
    html.Div([
        html.Button(
            id='submit-button',
            n_clicks=0,
            children='Submit',
            style={'fontSize':24, 'marginLeft':'30px'}
        ),
    ], style={'display':'inline-block'}),
    
    dcc.Graph(
        id='my_polar',
    ),
    dcc.Graph(
        id='my_graph',
        figure={
            'data': [
                {'x': [1,2], 'y':[3,1], 'name':'SDG Data'},
            ],
            'layout':go.Layout(
                title = 'Correlation:')
            
        }
    )
])

@app.callback(
    Output('my_polar', 'figure'),
    [Input('company_ticker', 'value')]
)
def update_graph(company_ticker):
    sdg=pd.DataFrame(list(collection.find({"COMPANY" : company_ticker})))
    sdg=sdg.sort_values('date')
    item=[]
    scores=[]
    for i in range(17):
        item.append('SDG_'+str(i+1))
        scores.append(sdg.iloc[-1]['SDG_'+str(i+1)])
    fig = go.Figure(data=go.Scatterpolar(
        r=scores,
        theta=item,
        fill='toself'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True
            ),
        ),
        showlegend=False
    )
    return fig

@app.callback(
    Output('my_graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('company_ticker', 'value'),
     State('my_indicator_symbol', 'value'),
    State('my_date_picker', 'start_date'),
    State('my_date_picker', 'end_date')])
def update_graph(n_clicks, company_ticker, ind_ticker,start_date, end_date):
    # since stock_ticker is now a list of symbols, create a list of traces
    traces0 = []
    #traces1 = []
    #Update figure by indexing datetime strings.
    #Filter data by selected datetime
    sdg=pd.DataFrame(list(collection.find({"COMPANY" : company_ticker})))
    sdg=sdg.sort_values('date')
    sdg.set_index('date', inplace=True)
    sdg_select = sdg.loc[start_date:end_date]
    traces0.append({'x':sdg_select.index, 'y': sdg_select[ind_ticker], 'name': 'Index'})
    fig = {
        # set data equal to traces
        'data': traces0,
        'layout': {'title':'Your selected result:'}
    }
    
    return fig
    

if __name__ == '__main__':
    app.run_server()

