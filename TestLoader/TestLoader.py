import json
from os import path
import datetime 

#date = datetime.datetime.now()
#date = date.strftime("%d/%m/%Y")
filename = 'c:/users/thoma/source/repos/testloader/testloader/test_results.json'
listObj = []

if path.isfile(filename) is False:
  raise Exception("File not found")

name = 'nome_' + input("Inserire nome utente: ")
no_test = 'no_test_' + input("Inserire il numero del test: ")
while True:
    device_ans = input("Inserire il device usato dall'utente (Ar, Hololens, Manuale): ")
    if device_ans in ['a', 'h', 'm']:
        break
if device_ans == 'a':
    device = 'AR'
if device_ans == 'h':
    device = 'hololens'
if device_ans == 'm':
    device = 'manuale'
time = int(input("Inserire il tempo impiegato per sostenere il test: "))

with open(filename, 'r') as fp:
  listObj = json.load(fp)

listObj.append(
    {'28042022': 
        [
            {
            name: 
                [
                    {
                    no_test: 
                           [
                               {
                                'device': device,
                                'time': time
                                }
                           ]
                    }
                ]
            }
        ]
     }
)

with open(filename, 'w') as json_file:
    json.dump(listObj, json_file)



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
