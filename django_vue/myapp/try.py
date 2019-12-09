import json

a = {'data1':{'name':'fuck','value':10},
     'data2':{'name':'you','value':15}}
j = json.dumps(a)
print(j)
