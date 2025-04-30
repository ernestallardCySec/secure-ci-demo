from app import app # imports app from app.py. This is going to allow me to test it's endpoints. 
def test_list_empty():
    client = app.test_client() # creates Flasks built in test client. This should simulate http requests without actually running a real server. 
    resp = client.get('/tasks') # sends a HTTP GET request to the /tasks endpoint. 
    assert resp.status_code == 200
    assert resp.get_json == [] # These two lines check that the response status code is 200 - meaning okay. Also checks that the JSON body is an empty list since no task has been created yet. Will throw an error is either assert fails.add()
