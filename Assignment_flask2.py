########### ASSIGNMENT - FLASK 

"""  
Que1 : Q1. Explain GET and POST methods.

Ans : GET and POST methods are two most commonly used HTTP methods used for communication between a client(such as web browser) and a server. 
1. GET Method : GET method is used to request data from a specified resource, typically identified by a URL. When a client sends a GET request, it asks the server to retrieve 
and send back from a resource, which can be a web page, an image, file etc. GET requests can have parameters included in the URL, often as query parameters. It is not secure.

2. POST Method : POST methods are used to submit data to be processed to a specified resource. When a clent sends a POST request, it includes data in the request body. 
This data can be used to update, create, or modify resources on the server. The data sent in the POST request is not visible in the URL and is instead included in the request body.


Que 2 : Why is request used in Flask?

Ans : The 'request' object is a global object that allows you to access data sent by the client as part of an HTTP request. This object is provided by Flask to enable you to interact and extract the relevant data for processing. 
Why it is used? 
'request' object allow us to access the sent data in the form of HTTP request and process in our Flask application.
When a url contains query parameters, then the 'request' method allows you to retrieve and work with these parameters.


Que 3 : Why is redirect() used in Flask?

Ans : In Flask, the 'redirect()' function is used to perform client-side redirect from one URL to another.It's a way to send an HTTP response that tells the cleint's browser to request a different URL, 
which can be on the same or a different domain.
Redirects are commonly used for various purposes in web development, including after form submissions, handling routes and many more.


Que 4 : What are templates in Flask? Why is the render_template() function used?

Ans : In Flask, templates are used to seperate the presentation layer from the application logic. Templates are the files that contains HTML structure of web pages along with dynamical content.
This seperation allows developers to keep the python code seperate from the HTML code making the application more maintainale and scalable.

The 'render_template()' function is used to render HTML templates in Flask. This function reads the template file, processes it and returns the HTML to be sent to the client's browser.


Que 5 : Create a simple API. Use Postman to test it. Attach the screenshot of the output in the Jupyter Notebook.

Ans :
"""
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api', methods = ['POST'])
def hello():
    data = {
        'message': 'Hello, world !'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0")  


