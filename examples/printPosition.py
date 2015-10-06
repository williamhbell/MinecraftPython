#!/usr/bin/env python3
#
# Import needed libraries
from mcpi.minecraft import Minecraft
import mcpi.block as block
import time

mc = Minecraft.create()  # Connect to Minecraft, running on the local PC

# A while loop that continues until the program is stopped.
while True:
  pos = mc.player.getPos() # Get the player position
  # Post the position to the local chat
  mc.postToChat("Player pos x=" + str(pos.x) + ", y=" + str(pos.y) + ", z=" + str(pos.z))
  time.sleep(0.5) # Sleep for half a second
