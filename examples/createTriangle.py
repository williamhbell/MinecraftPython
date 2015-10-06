#!/usr/bin/env python3
#
# Import needed libraries
from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create()  # Connect to Minecraft, running on the local PC
pos = mc.player.getPos() # Get the player position
x = pos.x # Assign the value of the x coordinate to x
y = pos.y # Assign the value of the y coordinate to y
z = pos.z # Assing the value of the x coordinate to z

# Add two to the x and y positions to avoid the player
x += 2
z += 2

# Loop from 0 to 5 to create a triangle in two dimensions
for i in range(6):

  # Set a rectangle of blocks to be ICE
  # As "i" is incremented, the rectangle starts one unit higher
  # The rectangle becomes shorter, when it is created higher in the air  
  mc.setBlocks(x, y+i, z, x, y+i, z+5-i, block.ICE.id)
