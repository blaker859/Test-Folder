import requests

# Define the URL you want to send the POST request to
# url = 'https://example.com/api'

# # Define the data you want to include in the POST request
# data = {
#     'key1': 'value1',
#     'key2': 'value2'
# }

# # Send a POST request to the URL with the data
# response = requests.post(url, data=data)

# # Check the status code of the response to ensure it was successful
# if response.status_code == 200:
#     # The request was successful
#     # You can access the response content as text or in other formats
#     content = response.text
#     print(content)
# else:
#     # The request was not successful, handle the error as needed
#     print(f"Request failed with status code {response.status_code}")



# Define the URL you want to make a GET request to
url = 'https://google.com'

# Send a GET request to the URL
response = requests.get(url)

# Check the status code of the response to ensure it was successful
if response.status_code == 200:
    # The request was successful
    # You can access the response content as text or in other formats
    # For example, to get the response content as text:
    content = response.text
    print(content)
else:
    # The request was not successful, handle the error as needed
    print(f"Request failed with status code {response.status_code}")