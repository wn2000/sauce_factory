#/bin/bash

set -e

lnkfile="$1"

if [ -z "$lnkfile" ]; then
  exit 0
fi

echo resolving link $lnkfile

folder="$(dirname "$lnkfile")"
echo $folder

eval actualfile=\"$(cat $lnkfile)\"

if [ -f "$actualfile" ]; then
  cp "$actualfile" $folder
else
  echo ERROR: $lnkfile resolved to $actualfile but it is not found. Original file name: $(cat $lnkfile)
  exit 1
fi

