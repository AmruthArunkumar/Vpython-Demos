from vpython import *

# creating a sphere object in the center
# NOTE: the position and size for the objects are from the center so, 
# an box with size.x as 12, means 6 on each side
ball = sphere(pos = vector(0, 0, 0), radius = 0.5, color = color.magenta, make_trail = True, retain = 100)

# creating all 6 walls for a cube, with the front wall transparent
wallR = box(pos = vector(6, 0, 0), size = vector(0.2, 12, 12), color = color.cyan)
wallL = box(pos = vector(-6, 0, 0), size = vector(0.2, 12, 12), color = color.cyan)
wallT = box(pos = vector(0, 6, 0), size = vector(12, 0.2, 12), color = color.cyan)
wallB = box(pos = vector(0, -6, 0), size = vector(12, 0.2, 12), color = color.cyan)
wallBK = box(pos = vector(0, 0, -6), size = vector(12, 12, 0.2), color = color.gray(0.7))
wallFR = box(pos = vector(0, 0, 6), size = vector(12, 12, 0.2), color = color.black, opacity = 0)

# setting the ball's velocity as a vector
ball.velocity = vector(0.15, 0.2, 0.25)

# changing background settings
scene.background = color.white
scene.autoscale = False

# loop to update the ball's position
while True:
    # the while loop will not be updated more than 100 times per second
    rate(100)

    # checking the location of the ball, and if it hits the wall
    # the velocity in that direction will flip
    if (ball.pos.x + ball.radius) > (wallR.pos.x - (0.5 * wallR.size.x)):
        ball.velocity.x = -ball.velocity.x
    elif (ball.pos.x - ball.radius) < (wallL.pos.x + (0.5 * wallL.size.x)):
        ball.velocity.x = -ball.velocity.x
    if (ball.pos.y + ball.radius) > (wallT.pos.y - (0.5 * wallT.size.y)):
        ball.velocity.y = -ball.velocity.y
    elif (ball.pos.y - ball.radius) < (wallB.pos.y + (0.5 * wallB.size.y)):
        ball.velocity.y = -ball.velocity.y
    if (ball.pos.z + ball.radius) > (wallFR.pos.z - (0.5 * wallFR.size.z)):
        ball.velocity.z = -ball.velocity.z
    elif (ball.pos.z - ball.radius) < (wallBK.pos.z + (0.5 * wallBK.size.z)):
        ball.velocity.z = -ball.velocity.z

    # updating the ball's position by adding the velocity to the previous position
    ball.pos = ball.pos + ball.velocity