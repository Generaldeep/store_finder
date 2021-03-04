
# Summary
  - Two main functions **find_by_zip** and **find_by_address** and one helper function called **find_distance_to_stores** are defined. 
  - **find_by_zip** takes **--zip** as a required argument. **units** and **output** are optional arguments.
  - **find_by_address** takes **address** as a required argument. **units** and **output** are optional arguments.
  - **find_distance_to_stores** reads a csv file, sort the stores in the csv and returns the closest store to the provided zip or adress. 

# Requirments.txt file
- Using **docopt**, **pandas**, **uszipcode**, **haversinegeopy**. Please run **Pip install** after cloning the repo in order to install required libraries. 

# Testing and Running Functions
- To run tests (in test_find_stores.py) please run **python3 test_find_store.py** 
- To find a store near a zip, in the command line please run **python3 find_store.py  --zip=95670 --units=km**
- To find a store near an address, in the command line please run **python3 find_store.py  --address="1122 14th, oakland" --units="km"**
- Expected result **{'dist': 2.7137721756187703, 'key': 1758, 'Address': '2700 Fifth Street'}** 
- In this example, kilometers are return, but you can specify **--units="mi"** to return miles as distance instead.
