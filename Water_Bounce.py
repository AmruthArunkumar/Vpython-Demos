from vpython import *

oxygen_color = color.red
oxygen_radius = 1
oxygen_pos = vec(0, 0, 0)

hydrogen_color = color.white
hydrogen_radius = 0.5
hydrogen_1_pos = vec(0.7, 0.7, 0)
hydrogen_2_pos = vec(-0.7, 0.7, 0)

range = 6
wall_thk = 0.2
side_length = 12

wallR = box(pos = vector(range, 0, 0), size = vector(wall_thk, side_length, side_length), color = color.gray(0.7), opacity = 0)
wallL = box(pos = vector(-range, 0, 0), size = vector(wall_thk, side_length, side_length), color = color.gray(0.7), opacity = 0)
wallT = box(pos = vector(0, range, 0), size = vector(side_length, wall_thk, side_length), color = color.gray(0.7), opacity = 0)
wallB = box(pos = vector(0, -range, 0), size = vector(side_length, wall_thk, side_length), color = color.gray(0.7), opacity = 0)

Oxygen = sphere(pos = oxygen_pos, radius = oxygen_radius, color = oxygen_color, make_trail = True, retain = 50)
Hydrogen_1 = sphere(pos = hydrogen_1_pos, radius = hydrogen_radius, color = hydrogen_color, make_trail = True, retain = 50)
Hydrogen_2 = sphere(pos = hydrogen_2_pos, radius = hydrogen_radius, color = hydrogen_color, make_trail = True, retain = 50)

Water = compound([Oxygen,  Hydrogen_1, Hydrogen_2], velocity = vec(-0.104, 0.092, 0))

scene.autoscale = False

while True:
    rate(100)

    Water.rotate(axis = vec(0, 1, 0), angle = radians(0.1))
    Water.rotate(axis = vec(1, 0, 0), angle = radians(0.2))
    Water.rotate(axis = vec(0, 0, 1), angle = radians(0.3))
    hydrogen_1_pos += Water.velocity
    hydrogen_2_pos += Water.velocity
    oxygen_pos += Water.velocity
    Water.pos += Water.velocity

    water_max_x = max((oxygen_pos.x + oxygen_radius), (hydrogen_2_pos.x + hydrogen_radius), (hydrogen_1_pos.x + hydrogen_radius))
    water_min_x = min((oxygen_pos.x - oxygen_radius), (hydrogen_2_pos.x - hydrogen_radius), (hydrogen_1_pos.x - hydrogen_radius))
    water_max_y = max((oxygen_pos.y + oxygen_radius), (hydrogen_2_pos.y + hydrogen_radius), (hydrogen_1_pos.y + hydrogen_radius))
    water_min_y = min((oxygen_pos.y - oxygen_radius), (hydrogen_2_pos.y - hydrogen_radius), (hydrogen_1_pos.y - hydrogen_radius))

    if water_max_x > (wallR.pos.x - wall_thk):
        Water.velocity.x = -Water.velocity.x
    elif water_min_x < (wallL.pos.x + wall_thk):
        Water.velocity.x = -Water.velocity.x
    if water_max_y > (wallT.pos.y - wall_thk):
        Water.velocity.y = -Water.velocity.y
    elif water_min_y < (wallB.pos.y + wall_thk):
        Water.velocity.y = -Water.velocity.y
    
    wallR.opacity = 1 - ((wallR.pos.x - Water.pos.x) / range)
    wallL.opacity = 1 - ((Water.pos.x - wallL.pos.x) / range)
    wallT.opacity = 1 - ((wallT.pos.y - Water.pos.y) / range)
    wallB.opacity = 1 - ((Water.pos.y - wallB.pos.y) / range)