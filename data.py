import json
import requests

def getTrain():
    r = requests.get('https://store.piemadd.com/passio_go/rutgers')
    a = r.json()

    # dictionary to keep record of the live bus times
    trains = dict()

    for i, j in a.items():
        if i == "trains":
            for a, b in j.items(): 
                trains[a] = b

    # removing the unneccesary keys from trains
    for key, val in trains.items():
        del trains[key]['heading']
        del trains[key]['lineCode']
        del trains[key]['lineColor']
        del trains[key]['lineTextColor']
        for i in trains[key]['predictions']:
            del i['noETA']
        del trains[key]['extra']['info']

    return trains


def getStaton():

    r = requests.get('https://store.piemadd.com/passio_go/rutgers')

    a = r.json()

    # dictionary to keep record of the bus stops and the busses coming to them 
    stations = dict()

    for i, j in a.items(): 
        if i == "stations":
            for a, b in j.items(): 
                stations[a] = b

    return stations

print(getTrain())
print()
print(getStaton())
