from flask import Flask
import pandas as pd 
import json
#data=pd.read_json('DB2.json',orient ='records')
#data = json.loads('DB2.json')

with open('BoyRentQuery.json','r') as fr:
    for line in fr:
        BoyRentdata = line.replace('[','').replace (']','')

with open('phoneQuery.json','r') as fr:
    for line in fr:
        Phpnedata = line.replace('[','').replace (']','')

with open('QueryAgent.json','r') as fr:
    for line in fr:
        Agentdata = line.replace('[','').replace (']','')

with open('QueryMissWuAtTp.json','r') as fr:
    for line in fr:
        MissWudata = line.replace('[','').replace (']','')

app = Flask(__name__)






@app.route('/')
def index():
    
    return 'Welcome'

@app.route('/BoyRentQuery')
def BoyRent():
    return BoyRentdata


@app.route('/phoneQuery')
def phone():
    return Phpnedata
 
@app.route('/QueryAgent')
def Agent():
    return Agentdata

@app.route('/QueryMissWuAtTp')
def MissWuTp():
    return MissWudata
    
  
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)