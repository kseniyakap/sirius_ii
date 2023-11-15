import json
from rapidfuzz import fuzz

a = input()

with open('res/test_00.json', 'r') as myfile:
    data = myfile.read()
with open('res/test_01.json', 'r') as myfile2:
    data2 = myfile2.read()

obj = json.loads(data)
obj2 = []

for item in obj:
    msg = ""
    for i2 in item['dialogue']:
        if i2['share_photo']:
            break
        msg = msg + " " + i2['message']
    if len(msg) > 0:
        obj2.append({'msg': msg, 'pu': item['photo_url']})

obj = json.loads(data2)

for item in obj:
    msg = ""
    for i2 in item['dialogue']:
        if i2['share_photo']:
            break
        msg = msg + " " + i2['message']
    if len(msg) > 0:
        obj2.append({'msg': msg, 'pu': item['photo_url']})

pr = []
pr2 = {}
for x in obj2:
    w = fuzz.partial_token_ratio(a,x['msg'])
    pr.append({'weight' : w, 'pu' : x['pu']})
    pr2[x['pu']] = w

sorted_pr = sorted(pr2.items(), key=lambda x:x[1], reverse=True)[:10:]

for i in sorted_pr:
    print(i[0])

