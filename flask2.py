from flask import Flask #Importing the Flask module

app = Flask(__name__) #Creating a application

@app.route('/') #Creating a default route
def home():
    return "change url for greeting with name = <b> port/greet/yourname</b> </br> change url for performing string operation =  <b>port/stringoperation/word1/word2</b> <u>(replace word1 and word2 with your words )</u>" #Returning the string to the browser

@app.route('/greet/<name> <lastname>') 
#Creating a route with a variable name
def greet(name , lastname):
    return f"<b> Hello {name} {lastname}</b>"#Returning the string to the browser

@app.route('/stringoperation/<string:word>/<string:word2>')
def stringoperation(word , word2):
    return f"<b> {word} + {word2} :-  {word + word2} </b>" #performing string concatnation operation 

@app.route('/add/<int:num1>/<int:num2>') 
def add(num1 , num2):
    return f"<b> {num1} + {num2} :- {num1 + num2} </b>" #performing addition operation

if __name__ == '__main__': #Running the application
    app.run(port='2506' , debug=True)