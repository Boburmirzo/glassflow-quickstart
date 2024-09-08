import os

pipeline_id = input("Enter your GlassFlow Pipeline ID: ")
access_token = input("Enter your GlassFlow Access Token: ")

with open(".env", "w") as f:
    f.write(f"PIPELINE_ID={pipeline_id}\n")
    f.write(f"ACCESS_TOKEN={access_token}\n")

print("✅ Pipeline ID and Access Token saved to .env")
