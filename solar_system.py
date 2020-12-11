from vpython import *

# creating an earth object and setting it's 23.5 degree rotation
earth = sphere(pos = vector(2, 0, 0), radius = 0.25, texture = {'file':textures.earth})
earth.rotate(angle = radians(23.5), axis = vector(0, 0, 0.5))

# creating the sun and the light object
sunlight = local_light(pos = vector(0, 0, 0), color = color.white)
sun = sphere(pos = vector(0, 0, 0), radius = 0.5, emissive = True, color = color.orange)

# creating the moon object
moon = sphere(pos = vector(2.5, 0.22, 0), radius = 0.1, color = color.white, texture = {'file':textures.metal})

# loop to update the position of all the objects
while True:
    # the while loop will not be updated more than 100 times per second
    rate(100)

    # rotating all the objects
    earth.rotate(axis = vector(-0.22, 0.5, 0), angle = radians(1))
    earth.rotate(origin = sun.pos, axis = vector(0, 0.5, 0), angle = radians(1))
    moon.rotate(origin = earth.pos, axis = vector(-0.22, 0.5, 0), angle = radians(8))
    moon.rotate(origin = sun.pos, axis = vector(0, 0.5, 0), angle = radians(1))