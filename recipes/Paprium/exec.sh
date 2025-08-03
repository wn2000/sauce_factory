#!/bin/sh

cp ./boxart/addon.z.png /tmp
echo -e "[Property]\nBezelPath=/tmp/addon.z.png" > /tmp/gameinfo.ini

set -x
/emulator/retroplayer ./emu/fbneo_libretro_md.so "./roms/md_paprium.zip"

rm -f /tmp/gameinfo.ini

