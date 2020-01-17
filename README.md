# maximum-rectilinear-crossing-number-of-uniform-hypergraphs
Complete source code for generating all results published in the paper.

This repository contains all the source code along with the outputs.

For running the programs yourself -

1. Make sure to have read, wrie and execute access in the directory you are cloning this repository to and have the following installed -

  ```
  python 3.5+
  pandas 0.20+
  ```
  
  For Debian derivatives the package `glpk-utils` is needed.
  
  For RHEL and Arch Linux derivatives the package `glpk` is needed.
  
  
  2. Create a new directory and copy `all_point_sets.txt` and all the `.py` files in it.
  
      ```
      mkdir test
      
      cp code1_convert_hex_to_int.py \
      code2_generate_feasible_points.py \
      code3_check_for_balanced_set.py \
      code4_1_check_for_ptset_details_where_max_feasible_colorings_is_12.py \
      code4_2_check_for_max_balanced_colors_without_M_or_I_aka_neighbourly_polytopes.py \
      point_set_hex.txt \
      run.py
      
      cd test
      
      python run.py
      ```
