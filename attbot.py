import pandas as pd
import request

webhook_url='https://hooks.zapier.com/hooks/catch/6891865/b6juuuh/'
data={'name':['Binay','sujan']}
r=requests.post(webhook_url,data=json.dumps(data),
                headers={'Content-Type':'application/json'})