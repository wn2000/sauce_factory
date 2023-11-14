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
  - To build a single sauce, type  
    `make out/Sauce_Name.uce`  
    e.g.  
    `make out/AddOn_Air_Rescue.uce`
    Currently this does not work if the recipe folder contains files with space in their names.
  - Alternatively, you can use
    `./build_uce.sh /path/to/recipe /path/to/output.uce`
    This approach works for all recipes.

