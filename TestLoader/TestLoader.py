import json
from os import path

filename = 'c:/users/thoma/source/repos/testloader/testloader/test_results.json'
listObj = []

if path.isfile(filename) is False:
  raise Exception("File not found")

name = input("Inserire nome utente: ")
no_test = input("Inserire il numero del test: ")
device = input("Inserire il device usato dall'utente: ")
time = input("Inserire il tempo impiegato per sostenere il test: ")

with open(filename, 'r') as fp:
  listObj = json.loads(fp)

listObj.append({
        'name': name,
        'no_test': no_test,
        'device': device,
        'time': time
})

with open(filename, 'w') as json_file:
    json.dumps(listObj, json_file, 
                        indent=4,  
                        separators=(',',': '))



#data = {
#    '27042022' : [
#        {
#            'name' : 'u1',
#            'no_test' : '1',
#            'device' : 'hololens',
#            'time' : '57'
#        },
#        {
#            'name' : 'u2',
#            'no_test' : '3',
#            'device' : 'ar',
#            'time' : '64'
#        },
#        {
#            'name' : name,
#            'no_test' : no_test,
#            'device' : device,
#            'time' : time
#        }
#    ]
#}


#json_string = json.dumps(data)

#with open(filename, 'w') as outfile:
#    json.dump(json_string, outfile)
