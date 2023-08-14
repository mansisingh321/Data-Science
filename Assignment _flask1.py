############# ASSIGNMENT - FLASK 
"""
Que1 : What is Flask Framework? What are the advantages of Flask Framework?

Ans : Flask is a web framework for Python that provides the essential needed to create web applications or APIs with minimal code and complexity.
 Advantages of Flask: 
 1. Flask keeps things simple, focuses on routing HTTP requests, and support the basics of web applications.
 2. Flask is flexible. It give us the freedom to structure our code in our way that makes sense for our project.
 3. Modularity : Flask is built with extensions. These are xtra packages developers can pick and and choose to integrate their applications according to them.
 4. Flask's concise and intuitive API makes easy to develop web applications fir beginners.
 5. As Flask is widely use in the industry, so its resources are available easily.


 Que2 : Create a simple Flask application to display ‘Hello World!!’. Attach the screenshot of the output in Jupyter Notebook.
 Ans : 
"""
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World !!"

"""
Que3 : What is App routing in Flask? Why do we use app routes?

Ans : In Flask, app routing refers to the process of defining URL patterns (routes) that corresponds to specific functions or views in our application. 
It allows us to map URLs to pythonic functions, enable to create different pages or endpoints for our web applications.

We use app routes for several important purposes like 
1. It organize URLs of our web application. We can create meaningful URLs for different pages.
2. By defining seperate functions for different routes, we handle specific tasks related to associated page.
3. It enhances readibility of the function instead of writing all logic in single function we can define seperate functions and their corresponding app routes.
4. We can easily change the behaviour of specific pages without affecting the rest of the application.


Que4 : Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/”
route to show the following details:
Company Name: ABC Corporation
Location: India
Contact Detail: 999-999-9999

Ans : 
"""

@app.route('/welcome')
def welcome():
    return "Welcome to ABC Corporation"

@app.route('/')
def details():
    det = """
    #Company Name : ABC Corporation /n
    #Location : India
    #Contact Detail : 999-999-9999"
"""
    return det
    

"""
Que5. What function is used in Flask for URL Building? Write a Python code to demonstrate the working of the
url_for() function. 

Ans : In Flask, the "url_for()" function is used to generate URLs for routes defined in your application. 
The function takes the name of the route function and returns the URL that corresponds to that route
 """
@app.route('/')
def index():
    return "Welcome to the homepage !"
@app.route('/about')
def about():
    return "This is the about page." 

if __name__ == "__main__":
    with app.test_request_context():
        index_url = url_for('index') # This will give the url for index function
        about_url = url_for('about') # This will give the url for about function
        print("Index URL : ", index_url)
        print("About URL : ", about_url)
    app.run(host="0.0.0.0")    
     
