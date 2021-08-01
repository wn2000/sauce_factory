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
