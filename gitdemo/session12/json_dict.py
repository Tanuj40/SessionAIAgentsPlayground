import json


data = {
    "name": "Tanuj",
    "age": 27
}

json_string  = json.dumps(data)


## To write json into a file, config.json

with open("config.json", "w") as f:
    json.dump(data, f)
    
    
    
# dumps vs dump
# writes json directly to a file
# dumps : Return json as string