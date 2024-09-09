import glassflow
import os

pipeline_id = os.getenv("PIPELINE_ID")
pipeline_access_token = os.getenv("ACCESS_TOKEN")


client = glassflow.GlassFlowClient()
pipeline_client = client.pipeline_client(
    pipeline_id=pipeline_id, pipeline_access_token=pipeline_access_token
)

data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "123-456-7890",
    "ssn": "123-45-6789",
}

response = pipeline_client.publish(request_body=data)
if response.status_code == 200:
    print(f"Data sent to GlassFlow: {data}")
else:
    print(f"Failed to send data: {response.text}")
