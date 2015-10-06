#!/bin/bash
mount /dev/sdb2 /mnt
if [[ $? != 0 ]]; then
  echo "Error: mount failed"
  exit 1
fi

destdir="/mnt/home/pi/minecraft_examples"
mkdir -p $destdir
if [[ $? != 0 ]]; then
  echo "Error: mkdir failed"
  exit 1
fi

cp /home/wbell/Documents/raspberrypi/Minecraft/examples/*.py $destdir
if [[ $? != 0 ]]; then
  echo "Error: cp command failed"
  exit 1
fi

chown 1000:1000 -R $destdir
if [[ $? != 0 ]]; then
  echo "Error: chown command failed"
  exit 1
fi

umount /mnt
if [[ $? != 0 ]]; then
  echo "Error: umount failed"
  exit 1
fi
echo ">> Copy completed"
