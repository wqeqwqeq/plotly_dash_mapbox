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
#### Please wait for 30 seconds after click on the link, cause the code need to be launched on a remote server on heroku, it takes time.
#### If nothing show up initially, try to play with the bars and hit submit, then your are good to go. You can hover on the graph to find more insights about out data. Isn't it really cool? 


1. Macro CISS: https://cissploty.herokuapp.com

![alt text](https://github.com/wqeqwqeq/plotly_dash_mapbox/blob/master/pic/CISS%20signal.png)

2. World bank. https://shuyidashapp.herokuapp.com  (Username: stanley, Password yuan)

![alt text](https://github.com/wqeqwqeq/plotly_dash_mapbox/blob/master/pic/Worldbank.png)


3. Political risk: http://gai-test1-app.herokuapp.com

![alt text](https://github.com/wqeqwqeq/plotly_dash_mapbox/blob/master/pic/Political%20risk.png)


4. Anomalies：https://anomlies.herokuapp.com

![alt text](https://github.com/wqeqwqeq/plotly_dash_mapbox/blob/master/pic/Anomalies.png)


5. SDG: https://sdgcom.herokuapp.com 

![alt text](https://github.com/wqeqwqeq/plotly_dash_mapbox/blob/master/pic/SDG_Radar.png)


6. Turbulence: https://gai-tb-test.herokuapp.com/

![alt text](https://github.com/wqeqwqeq/plotly_dash_mapbox/blob/master/pic/turbulance.png)

7. Powerplant by Mapbox: https://my-powerplant.herokuapp.com/

![alt text](https://github.com/wqeqwqeq/plotly_dash_mapbox/blob/master/pic/powerplant.png)


## Authors

* **Zhehui Yuan** - *Initial work* - [GitHub](https://github.com/wqeqwqeq) [LinkedIn](https://www.linkedin.com/in/stanley-yuan-6093a317a/)

See also the list of [contributors](https://github.com/wqeqwqeq/plotly_dash_mapbox/blob/master/Contributor.md) who participated in this project.

