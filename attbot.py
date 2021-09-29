import json
import requests

webhook_url='https://hooks.zapier.com/hooks/catch/6871459/b6vht3q'
data={'name':['Binay','sujan']}
r=requests.post(webhook_url,data=json.dumps(data),
                headers={'Content-Type':'application/json'})
print(r.status_code)