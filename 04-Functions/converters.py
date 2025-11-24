def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_inch(n):
    return n/2.54

def feet_and_inch_to_cm(f,i):
    return f*30.48 + i*2.54

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'182cm = {cm_inch(182)}inch')
    print(f'5feet 11,67inch = {feet_and_inch_to_cm(5,11.67)}cm')

