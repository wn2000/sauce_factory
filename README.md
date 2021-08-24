# saUCE Factory 

Scripts and tools to automate saUCE cooking.

## Usage
- First clone the repo  
  ```
  git clone https://github.com/wn2000/sauce_factory
  cd sauce_factory
  ```
- Set ROM and core directories by setting the following env variable (assuming Bash):
  ```
  export ROMDIR=/my/rom/directory
  export COREDIR=/my/core/directory
  ```
- Build  
  - To build all sauces, type  
  `make`  
  This will turn each recipe in the `recipes` folder into a sauce in the `out` folder. The Makefile will only process a recipe if the corresponding sauce does not exist, or the recipe has recently been updated.
  - To build a single sauce, type  
    `make out/Sauce_Name.uce`  
    e.g.  
    `make out/AddOn_Air_Rescue.uce`

## Notes on pre-generated save partition
- Some recipes include a `save.zip` file. This is a pre-generated save partition, which can contain core options overrides, custom control mappings, and save states of the game.
- To generate such a file yourself, or to simply view the content of this file, refer to the following steps:
  - Generate an ext4 partition file with necessary folder structures
    ```
    truncate -s 4M save.bin
    mkfs.ext4 save.bin
    debugfs -R 'mkdir upper' -w save.bin
    debugfs -R 'mkdir work' -w save.bin
    ```
    This creates a 4MB file `save.bin` that has an ext4 partition in it.
    Alternatively, you can also get such a file by stripping the last 4MB from an existing UCE:
    ```
    tail -c 4M existing.uce > save.bin
    ```
  - Once the `save.bin` file is ready, we need to mount it to a directory to access its content:
    ```bash
    # First create the mount point directory
    mkdir mnt
    # Mount it
    sudo mount -o loop save.bin mnt
    ```
    Note that the `mount` command needs `sudo` access. So make sure your user account is in the `sudoers` group.
  - Once "mounted", the content of `save.bin` can be accessed from the `mnt` folder. There you can add/remove/edit files of interest, which may include the following:
    - `retroplayer.ini`: This can be used to override many core options, and frontend video / control settings
    - `cfg` folder: This has custom control mappings made in the MAME menu
    - `hi` and `nvram`: May contain hi-scores
    - Game save files and their screenshots
  - Once done editting the `mnt` folder, go out of the folder and do
    ```
    sudo umount /path/to/mnt
    ```
    This unmounts the `save.bin` file and flushes all changes to the file.
  - Finally, zip the `save.bin` file as `save.zip` and place it inside the recipe folder. The build script will unzip it and put it into the UCE.
