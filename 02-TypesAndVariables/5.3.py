###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
cube_volume = int(a*b*c)
cube_surface_area = int(a*b*2 + a*c*2 + b*c*2)
print(f'The volume of a cube is {cube_volume}.')
print(f'The surface area of a cube is {cube_surface_area}.')