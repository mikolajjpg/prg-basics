
def avg_speed(distance,hours,minutes):

    return distance / (hours + ((minutes*(10/6)))*0.01)

if __name__=="__main__":
    x = int(input('Enter distance in km: '))
    y = int(input('Enter number of travel hours: '))
    z = int(input('Enter number of travel minutes '))

    result = avg_speed(x,y,z)

    print( f'Average speed: {result:.1f} km/h')
