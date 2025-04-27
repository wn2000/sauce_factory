#!/bin/sh

cp ./boxart/addon.z.png /tmp
echo -e "[Property]\nBezelPath=/tmp/addon.z.png" > /tmp/gameinfo.ini

set -x
/emulator/retroplayer ./emu/mame2003_plus_libretro.so "./roms/area51mx.zip"

rm -f /tmp/gameinfo.ini

