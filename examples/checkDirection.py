#!/usr/bin/env python3
#
# Import needed libraries
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
import mcpi.block as block
import time
import math

def calculateVelocity(mc, ntimes = 5): # Try 5 times before giving up
  pos1 = mc.player.getPos() # Get the player position
  while ntimes > 0:
    time.sleep(0.2) # Sleep for a fifth of a second
    pos2 = mc.player.getPos() # Get another player position  
    xdiff = pos2.x - pos1.x  # Calculate the difference
    ydiff = pos2.y - pos1.y  # Calculate the difference
    zdiff = pos2.z - pos1.z  # Calculate the difference
    if (math.fabs(xdiff) + math.fabs(ydiff) + math.fabs(zdiff)) > 0.:  # If the player has moved
      break  # Break out of the loop
    else:
      ntimes = ntimes - 1 # Decrement the number of times to check
  return (Vec3(xdiff, ydiff, zdiff), pos2) # Return the velocity and last position


mc = Minecraft.create()  # Connect to Minecraft, running on the local PC
while True:
  (direction, pos) = calculateVelocity(mc)  # Get the direction the player is moving  
  print(direction)

  # Sleep for half a second
  time.sleep(0.5)
