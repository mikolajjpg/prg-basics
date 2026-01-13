def ms_to_kmh(ms):

    return ms * 3.6

if __name__=="__main__":

    v1 = 10
    v2 = 35

    print(f'{v1} m/s = {int(ms_to_kmh(v1))} km/h')
    print(f'{v2} m/s = {int(ms_to_kmh(v2))} km/h')

