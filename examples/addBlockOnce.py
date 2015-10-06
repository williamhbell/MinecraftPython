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

# Set the block where the player is to be Spruce 
mc.setBlock(x, y, z, block.WOOD.id, 1)
