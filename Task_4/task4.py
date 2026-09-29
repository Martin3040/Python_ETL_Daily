import json
import csv
def extracting_from_api():
    with open('new_data.json','r',newline='',encoding='utf-8') as file:
        data=json.load(file)
        mobiles=[]
    for row in data:
        if(row['data'] is not None):
            color=None
            capacity=None
            for key, value in row["data"].items():
                if "color" in key.lower():
                    color = value
                elif "capacity" in key.lower():
                    capacity = value
            mobiles.append({
                "id":row['id'],
                'name':row['name'],
                'color':color,
                'capacity':capacity
            })
        else:
            mobiles.append({'id':row['id'],'name':row['name'],'color':None,'capacity':None})
    return mobiles
def validation_mob():
    mob=extracting_from_api()
    ##handle the capacity_GB column
    for row in mob:
        if isinstance(row['capacity'], int):
            row['capacity'] = str(row['capacity']) + ' GB'
    return mob

data=validation_mob()
for row in data:
    if(',' in row['name']):
        print(row['name'])


    
        