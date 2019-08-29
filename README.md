# Python Interactive Visualization project 
This repository includes python interactive visualization methonds by using plotly and dash package.

Plot types include line chart, radar chart, map, etc. 

Features include automatically refresh in given time, get data from database daily and live updating, hover around map to get detailed data, and connect with mapbox api to have a fancier visualization

The plot has generic feature, basically for the same type of plot, we just change the data source and apply some basic panads function then it works fine with a new plot. AKA template. 
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3 environment 
```

### Installing

The main packages drawing the graph is plotly and dash, we read https://dash.plot.ly/ as reference 
To install, simply type 

```
pip install dash
pip install plotly
```
To import, one thing might be different is 

```
import plotly.graph_objs as go
```
sometimes work but sometimes doesn't work on some computer, try
```
import plotly.graph_objects as go
```
instead 


## Deployment
We follow the tutorial on this document: https://docs.google.com/document/d/1DjWL2DxLiRaBrlD3ELyQlCBRu7UQuuWfgjv9LncNp_M/edit.
All of our code is deployed on heroku.


## Result of deployment and sample pic
1. Macro CISS: https://cissploty.herokuapp.com
https://entrepreneurship.columbia.edu/wp-content/uploads/2017/06/GlobalAILogoName.jpg


2. World bank. https://shuyidashapp.herokuapp.com  (Username: stanley, Password yuan)

3. Political risk: http://gai-test1-app.herokuapp.com

4. Anomalies：https://anomlies.herokuapp.com

5. SDG: https://sdgcom.herokuapp.com 

6. Turbulence: https://gai-tb-test.herokuapp.com/

7. Mapbox: https://my-powerplant.herokuapp.com/

## Authors

* **Zhehui Yuan** - *Initial work* - [GitHub](https://github.com/wqeqwqeq) [LinkedIn](https://www.linkedin.com/in/stanley-yuan-6093a317a/)

See also the list of [contributors](https://github.com/wqeqwqeq/plotly_dash_mapbox/contributor.md) who participated in this project.

