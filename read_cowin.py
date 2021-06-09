import json

with open('vaccine.json') as f:
  data = json.load(f)

for i in range(len(data["sessions"])):
    if data["sessions"][i]["available_capacity_dose1"] > 0:
        #do something
        print("#alert")


