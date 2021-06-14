#!/bin/sh

cp ./boxart/addon.z.png /tmp
echo -e "[Property]\nBezelPath=/tmp/addon.z.png" > /tmp/gameinfo.ini

/emulator/retroplayer ./emu/mame2003_plus_libretro_20210521.4.so "./roms/arabfgt.zip"

rm -f /tmp/gameinfo.ini

