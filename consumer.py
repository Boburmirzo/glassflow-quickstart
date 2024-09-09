import glassflow
import os

pipeline_id = os.getenv("PIPELINE_ID")
pipeline_access_token = os.getenv("ACCESS_TOKEN")

client = glassflow.GlassFlowClient()
pipeline_client = client.pipeline_client(pipeline_id=pipeline_id,
                                         pipeline_access_token=pipeline_access_token)

while True:
    res = pipeline_client.consume()
    if res.status_code == 200:
        event_data = res.body.event
        print(f"Data received from GlassFlow: {event_data}")
