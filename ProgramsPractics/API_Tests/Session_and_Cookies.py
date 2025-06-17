import requests
cooki = {'session_id': 'abc123', 'time_out': '3000'}
response = requests.get('https://httpbin.org/get')
# print(response.json())
# cookies = response.cookies
# print(cookies)
# cookies = {'session_id': 'abc123'}
# requests.post('https://httpbin.org/post', cookies=cookies)
# response = requests.get('https://httpbin.org/cookies')
# print(response.json())
session = requests.Session()
response = session.get('https://httpbin.org/cookies', cookies=cooki)
print(response.json())
response = session.get('https://httpbin.org/cookies/delete', cookies=cooki)
print(response.json())
# import requests
# response1 = session.get('https://httpbin.org/get')
# print(response1.json())
New_cooki = {'Name': 'Shakti', 'Age': '30'}
response = session.get('https://httpbin.org/cookies', cookies=New_cooki)
print(response.json())
# Create a session to persist cookies
# session = requests.Session()

# cooki = {'session_id': 'abc123', 'time_out': '3000'}
# # Set a cookie by making a request
# response = session.get('https://httpbin.org/cookies', cookies=cooki)

# # Show cookies before deletion
# print("Cookies before delete:", response.cookies)# # Delete a specific cookie by clearing it from the cookie jar
# # session.get('https://httpbin.org/cookies/delete', cookies={'session_id': 'abc123'})

# # # Show cookies after deletion
# # print("Cookies after delete:", session.cookies.get_dict())
