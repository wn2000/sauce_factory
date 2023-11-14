echo script started on `date`.

UCE_PATH=$(tr -d '\0' < /sys/block/loop1/loop/backing_file)
UCE_DIR=$(dirname -- "$UCE_PATH")
UCE_DIR_ON_USB=${UCE_DIR#/media/usb[0-9]}
UCE_NAME=$(basename -- "$UCE_PATH")
UCE_NAME="${UCE_NAME%.*}"
echo UCE_DIR: $UCE_DIR
echo UCE_NAME: $UCE_NAME

model=$(tr -d '\0' < /proc/device-tree/model)
echo Model: $model

export AUDIODEV="hw:2,0"
if [ -f "$UCE_DIR/gamecontrollerdb_$model.txt" ]; then
  export SDL_GAMECONTROLLERCONFIG_FILE="$UCE_DIR/gamecontrollerdb_$model.txt"
elif [ -f "$UCE_DIR/gamecontrollerdb.txt" ]; then
  export SDL_GAMECONTROLLERCONFIG_FILE="$UCE_DIR/gamecontrollerdb.txt"
elif [ -f "/userdata/customer_controller_db_3rd.txt" ]; then
  export SDL_GAMECONTROLLERCONFIG_FILE="/userdata/customer_controller_db_3rd.txt"
elif [ -f "/malibu/CarbonClient/Mas/gamecontrollerdb.txt" ]; then
  export SDL_GAMECONTROLLERCONFIG_FILE="/malibu/CarbonClient/Mas/gamecontrollerdb.txt"
fi
echo SDL_GAMECONTROLLERCONFIG_FILE: $SDL_GAMECONTROLLERCONFIG_FILE

cp emu/fs/usr/lib/ld-linux-armhf.so.3 /tmp
mkdir -p /tmp/fs/usr/lib /tmp/fs/usr/bin
cp -R emu/fs/usr/lib/libasound* /tmp/fs/usr/lib
cp -R emu/fs/usr/lib/alsa-lib /tmp/fs/usr/lib
cp -R emu/fs/usr/bin/bgdi /tmp/fs/usr/bin

cd save
mkdir -p savegame
ln -sf ../roms/gamedata/* .

export LD_LIBRARY_PATH=/tmp/fs/usr/lib:../emu/fs/usr/lib
case "$model" in
  HA8819|HA2818|HA2819)
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:../emu/fs/usr/lib/rk3399
    ;;
  *)
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:../emu/fs/usr/lib/rk3328
    ;;
esac

/tmp/fs/usr/bin/bgdi SorR.dat

if [ $? -ne 0 ]; then
  msg="
Game did not run successfully.
You can create a 'log' folder at the USB root and relaunch, a log will then be generated there.
Check the log for any error messages."
  echo "$msg" | ../emu/fs/usr/bin/messagebox -t 20
fi

sync

rm -rf /tmp/ld-linux-armhf.so.3 /tmp/fs

