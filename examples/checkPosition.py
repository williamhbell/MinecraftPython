#!/usr/bin/env python3
#
# Import needed libraries
from mcpi.minecraft import Minecraft
import mcpi.block as block
import time

mc = Minecraft.create()  # Connect to Minecraft, running on the local PC

# Create a monolith around the origin
mc.setBlocks(-1, -20, -1, 1, 20, 1, block.GLOWING_OBSIDIAN.id)

# A while loop that continues until the program is stopped.
while True:
  pos = mc.player.getTilePos() # Get the player tile position
 
  # Test if the players tile position is next to the monolith
  if pos.x >= -2 and pos.x <= 2 and pos.y >= -21 and pos.y <= 21 and pos.z >= -2 and pos.z <= 2:
    mc.postToChat("WARNING: next to monolith!") # Post a message to the chat

  # Sleep for a fifth of a second
  time.sleep(0.2)
