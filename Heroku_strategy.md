This file is for the function that generates the graph. It will go into the Heroku folder and be used to create the website. We're allowed to pull some pickle files, but others we want to rewrite into here.

Method to get the price data
function to get the search data
function to graph the search data with the price data together
function (obj is one of the inputs) to calculate and graph the correlation bar chart
function (obj is one of the inputs) to calculate the profit graph

In the Heroku folder, we'll have the Crypto Class, all the objects stored, and all the pickle files stored. 

When the Generate button is pressed, it will find if that object extists. If it does, it will call the object. If not, it will create the object.
Then it will do the same thing for the price data and the search data, check if they already exist, if not, it will search for them.
It will feed the search data and the price data into 1st graph function, which is rather simple.
Then feed the search data into the correlation bar chart method
Then feed the search data into the profit graph method

So the files that will be in the Heroku folder are: Crypto Class (including Method to get the price data), Pickles (including the objects), Methods and Functions to generate graph, Function to get the search data, Function to get or initiate object

0 Pickles

1 Class File: Contains the Crypto Class, the method to get the price data, and the function to call or initiate an object if it doesn't already exist

2 Function File: Function to get the search data

3 Function File: Functions to generate the graphs