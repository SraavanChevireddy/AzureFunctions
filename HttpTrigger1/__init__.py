import logging
import os
import json
import time
import azure.functions as func #3.8
from azure.storage.blob import BlobClient #3.9 

connectionstring = "DefaultEndpointsProtocol=https;AccountName=demopyfunapp;AccountKey=HuTRl7wzWIvyHTVqt2ENTH/s+2wJaab5hn8CCTcAFbQo+0nioBBO7bB21xHbbsYr+8ADuUvH5rOhmnYYo5VpHA==;EndpointSuffix=core.windows.net"
containername = "demo"
blobname = time.strftime("%Y%m%d-%H%M%S")

print(f'This is connection String{connectionstring}')
print(f'This is Container Name{containername}')

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
            blob = BlobClient.from_connection_string(conn_str=connectionstring, container_name=containername,
                                                     blob_name=blobname + ".json")
            data = json.dumps(req_body)
            blob.upload_blob(data)
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
