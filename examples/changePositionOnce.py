#!/usr/bin/env python3
#
# Import needed libraries
from mcpi.minecraft import Minecraft
import mcpi.block as block

# Connect to Minecraft, running on the local PC
mc = Minecraft.create()

# Move the player to x=0., y=20., z=0.
mc.player.setPos(0.,20.,0.)
