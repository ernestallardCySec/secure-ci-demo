from flask import Flask, request, jsonify
# Flask is creating the web app, request gives the incoming http data (JSON, headers, etc), jsonify converts Python dictionarys and lists to proper json HTTP responses. 
app = Flask(__name__)
# This instaniates the Flash application, telling Flask where to look for static files and templates.
tasks = [] # This creates an plain python list to keep my tasks. 

@app.route('/tasks', methods=['POST'])
def create_task(): #Registers the create task function to handle HTTP post requests to the /tasks URL.
    data = request.get_json() # This will parse the request body as JSON into a dictionary called data.
    #! Intentionally insecure, not checking to make sure that data['title'] exists and is a string.  
    tasks.append({'id': len(tasks) + 1, 'title': data['title']}) # This appends a new task dictionary to the tasks list. Also uses len(tasks) to create a simple ID. 
    return jsonify(tasks[-1]), 201 # Responds with the newly created task as json, the 201 HTTP code means created. 

@app.root('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(tasks), 200 # Registers list_tasks for HTTP GET on /tasks. Returns the full tasks list as JSON, with a HTTP 200 OK status code. 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
