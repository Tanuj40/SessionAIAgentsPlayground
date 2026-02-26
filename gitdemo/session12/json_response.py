import json

response = '''
 {
    "id": "req123",
    "status": "success",
    "result": {
        "text": "hello world",
        "confidence" : 0.08
    }  
 }
'''


### { " n a m e " :}
## Breaks into plece.  { --> start object , name --> saring : --> seperator , 30 --> number } --> end onject
## structure validation:
## convert it into dict
print(type(response))

parsed = json.loads(response)
print(type(parsed))
 
print(parsed["id"])