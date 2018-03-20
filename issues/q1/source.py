import requests
import json
url = 'https://localhost:8081/login'
data = {'username': 'admin', 'password': 'admin'}
try:
  # Issue is here, gives the error
  token = requests.post(url, data = json.dumps(data), headers = {'Content-type':'application/json'})
  print('Status Code: ', token.status_code)
  token_json = json.loads(token.content)
  print(token_json)
except Exception as ex:
  # Exception [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749)
  print('Exception', ex)

try:
  # give verify=False now the issue didnt coime up and doesnt go to Exception block
  token = requests.post(url, verify = False, data = json.dumps(data), headers = {'Content-type':'application/json'})
  print('Status Code: ', token.status_code)
  token_json = json.loads(token.content)
  print(token_json)
except Exception as ex:
  print('Exception', ex)