car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]

def bubblesort(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

if __name__ == "__main__":
    print(bubblesort(car_fuel_consumption))
    
                
        
    