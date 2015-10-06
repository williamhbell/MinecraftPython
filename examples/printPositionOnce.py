#!/usr/bin/env python3
#
# Import Minecraft and block from associated libraries
from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create()  # Connect to Minecraft, running on the local PC
pos = mc.player.getPos() # Get the player position
x = pos.x # Assign the value of the x coordinate to x
y = pos.y # Assign the value of the y coordinate to y
z = pos.z # Assing the value of the x coordinate to z

# Print the current player position
print("The player is currently at x =", x, ", y =", y, ", z =", z)
