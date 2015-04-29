#!/usr/bin/python

import random, json, uuid

shift_file = open('test-shifts.txt', 'w')
trip_file = open('test-trips.txt', 'w')

def get_shift():
    result = {}
    result['driverId'] = str(uuid.uuid4())
    result['start'] = random.randint(0, 10000000)
    result['end'] = result['start'] + random.randint(10, 1000)
    return result


shifts = [get_shift() for i in xrange(100000)]
trips = []
for i in xrange(100000):
    trip = {}
    trip['uuid'] = str(uuid.uuid4())
    shift = shifts[random.randint(0, len(shifts) - 1)]
    if random.randint(0,1000) == 1:
        trip['driverId'] = shift['driverId']
        trip['start'] = shift['start'] + shift['end'] / 2
        trip['end'] = shift['end']
    else:
        trip['driverId'] = shift['driverId']
        trip['start'] = random.randint(0, 10000000)
        trip['end'] = trip['start'] + 100
        
    trips.append(trip)

shift_file.writelines([json.dumps(shift) + '\n' for shift in shifts])
shift_file.close()
trip_file.writelines([json.dumps(trip) + '\n' for trip in trips])
trip_file.close()

