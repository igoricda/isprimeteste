import json

def handle(req):
    
    data = json.loads(req)
    
    num = int(data["n1"])
    
    if num < 2:
            return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

