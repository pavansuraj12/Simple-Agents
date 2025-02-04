#Air Purifier Controller: Develop a Simple Reflex Agent for an air purifier. If the air quality index
#exceeds a threshold value, the agent should turn on the purifier; otherwise, it should remain off.

import random

threshold = 30

def environment():
    airqualityindex=random.uniform(0,60)
    return airqualityindex
    
def senseairqualityindex():
    airqualityindex=environment()
    return airqualityindex
    
def decide(airqualityindex):
    if airqualityindex<=30:
        action="Purifier ON"
    else:
        action="Purifier OFF"
    return action
        
def agent():
    airqualityindex=senseairqualityindex()
    action=decide(airqualityindex)
    print(f"Air Quality Index : {airqualityindex:.2f}")
    print(f"Action : {action}")
for i in range(10):
    agent()