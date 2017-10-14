import requests
params = {apikey: '-YOUR API KEY HERE-'}
files = {file: ('myfile.exe', open('myfile.exe', 'rb'))}
response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
json_response = response.json()

params = {apikey: '-YOUR API KEY HERE-', resource: '7657fcb7d772448a6d8504e4b20168b8'}
headers = {
  Accept-Encoding: "gzip, deflate",
  User-Agent : "gzip,  My Python requests library example client or username"
  }
response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
  params=params, headers=headers)
json_response = response.json()
 
print (json)      