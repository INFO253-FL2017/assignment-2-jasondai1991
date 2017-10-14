1. What is the function of the following technologies in your assignment:
HTML--It builds the outline of the webpage, infrastructure
CSS--It defines what each block/part of the webpage looks like
JavaScript--It provides the webpage the ability to interact with the end users
Python--It is the language  in which the web server is written
Flask--It is the web application framework which we use to build a web server from scratch
HTTP--HTTP functions as a request–response protocol between a client and server. The client(web browser) submits an HTTP request message to the server. The server, which provides resources such as HTML files and other content, or performs other functions on behalf of the client, returns a response message to the client. The response contains completion status information about the request and may also contain requested content in its message body.
GET and POST requests:
GET - Requests data from a specified resource
POST - Submits data to be processed to a specified resource

2. How does HTML, CSS, and JavaScript work together in the browser for this assignment?
So after I write the HTML as the content outline of the webpage, each of the section has either an ID, tag or name. In CSS, I defined the detailed external look for each block by linking their ID or names. In the Javascript, I write functions by associating them to the HTML block IDs, Names or Tags etc to provide them the functionality and interactivity in the front end.

3. How does Python and Flask work together in the server for this assignment?
Python is the language which Flask Framework is programmed in. All the webserver is written in Python language. In the webserver file, we import various modules from Flask-- an existing web application framework, and these modules provides us ability to create a web server which can communicate with the front-end website we constructed previously.

4. List all of the possible GET and POST requests that your server returns a response for and describes what happens for each GET and POST request

Get Requests and their behavior:
@app.route('/')
--After hearing this get request when users type localhost:5000/, the server returns the "homepage.html" in the templates folder as a response. 

@app.route('/index')
--After hearing this get request when users type localhost:5000/index, the server returns the "homepage.html" in the templates folder as a response.


@app.route('/about')
--After hearing this get request when users type localhost:5000/about, the server returns the "aboutus.html" in the templates folder as a response.

@app.route('/contact',methods=['GET'])
--After hearing this get request when users type localhost:5000/contact, the server returns the "contactus.html" in the templates folder as a response.

@app.route('/blog/8-experiments-in-motivation')
--After hearing this get request when users type localhost:5000/blog/8-experiments-in-motivation, the server returns the "blog1.html" in the templates folder as a response.

@app.route('/blog/a-mindful-shift-of-focus')
--After hearing this get request when users type localhost:5000/blog/a-mindful-shift-of-focus, the server returns the "blog2.html" in the templates folder as a response.


@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
--After hearing this get request when users type localhost:5000/blog/how-to-develop-an-awesome-sense-of-direction, the server returns the "blog3.html" in the templates folder as a response.

@app.route('/blog/training-to-be-a-good-writer')
--After hearing this get request when users type localhost:5000/blog/training-to-be-a-good-writer, the server returns the "blog4.html" in the templates folder as a response.

@app.route('/blog/what-productivity-systems-wont-solve')
--After hearing this get request when users type localhost:5000/blog/what-productivity-systems-wont-solve', the server returns the "blog5.html" in the templates folder as a response.


Post Requests and their behavior:
@app.route('/contact',methods=['POST'])
--When the user submits a form on localhost:5000/contact url, the webserver gets the information which are passed through the form, process the information and send an email to the receiver. It also passes information to the "contactus.html" and evokes that html together with the information passed.




