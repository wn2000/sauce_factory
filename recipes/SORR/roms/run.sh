echo script started on `date`.

model=$(tr -d '\0' < /proc/device-tree/model)
echo Model: $model

export AUDIODEV="hw:2,0"
export SDL_GAMECONTROLLERCONFIG_FILE="/malibu/CarbonClient/Mas/gamecontrollerdb.txt"
UCE_DIR=$(dirname "$UCE_NAME")
for ((i=0; i<=9; i++))
do
  filename="/media/usb${i}/${UCE_DIR}/gamecontrollerdb.txt"
  echo trying $filename
  if [ -f "$filename" ]; then
      echo using $filename
      export SDL_GAMECONTROLLERCONFIG_FILE="$filename"
      break
  fi
done

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

