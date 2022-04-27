import json

data = {
    '27042022' : [
        {
            'name' : 'U1',
            'device' : 'hololens',
            'time' : '57'
        }
    ]
}


json_string = json.dumps(data)
print(json_string)
