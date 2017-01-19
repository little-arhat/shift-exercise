#!/usr/bin/python

import random, json, uuid


def get_shift():
    result = {}
    result['driverId'] = str(uuid.uuid4())
    result['start'] = random.randint(0, 10000000)
    result['end'] = result['start'] + random.randint(10, 1000)
    return result


with open('test-shifts.txt', 'w') as shift_file:
    with open('test-trips.txt', 'w') as trip_file:
        shifts = [get_shift() for i in range(100000)]
        trips = []

        for i in range(100000):
            trip = {}
            trip['uuid'] = str(uuid.uuid4())
            shift = shifts[random.randint(0, len(shifts) - 1)]
            if random.randint(0,1000) == 1:
                trip['driverId'] = shift['driverId']
                trip['start'] = (shift['start'] + shift['end']) // 2
                trip['end'] = shift['end']
            else:
                trip['driverId'] = shift['driverId']
                trip['start'] = random.randint(0, 10000000)
                trip['end'] = trip['start'] + 100

            trips.append(trip)

        shifts = sorted(shifts, key=lambda x:x['start'])
        trips = sorted(trips, key=lambda x:x['start'])
        shift_file.writelines([json.dumps(shift) + '\n' for shift in shifts])
        trip_file.writelines([json.dumps(trip) + '\n' for trip in trips])
