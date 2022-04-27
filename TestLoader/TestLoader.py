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

with open('test_results.json', 'w') as outfile:
    json.dump(json_string, outfile)
