#Basic hello world program using flask
from flask import Flask #Importing the Flask module

app = Flask(__name__) #Creating a application 

@app.route('/') #Creating a default route

def home():
    return "<b>Hello Flask</b>" #Returning the string to the browser

if __name__ == '__main__': #Running the application
    app.run(host='0.0.0.0'  , port='2007' , debug=True) 
    #Running the application on port 2007 and debug = true means it will show the error on the browser