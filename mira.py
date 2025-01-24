from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})

version = "1.0.1"
input_data = {
    "brand": "",
    "types": "",
    "budget": "",
    "engine": ""
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@shamgagan/car-detailer/{version}"
else:
    flow_name = "@shamgagan/car-detailer"

result = client.flow.execute(flow_name, input_data)
print(result)