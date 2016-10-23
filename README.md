# flask-api-key
Simple API Key authN using decarators via HTTPS using TLS.

This is a proof of concept (POC) of a RESTful end point using Flask.
Flask uses TLS for HTTPS connections.
Sample self-signed certs and keys are provided.
As writen, you can send a GET and POST.

The POST is authenticated using an API Key as a parameter.
Where the key is stored in a file, so the key value is not stored in code.
Be sure to change the value in api.key when deploying.

##GET Test
curl -k https://127.0.0.1

##POST Test
curl -k -H "Content-Type: application/json" -X POST -d '{"username":"xyz","password":"xyz"}' https://127.0.0.1/json/?key=eiWee8ep9due4deeshoa8Peichai8Ei2
