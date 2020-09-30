
# Summary
  - I have written two main function **find_by_zip** and **find_by_address** and one helper function called **find_distance_to_stores** 
  - **find_by_zip** takes **--zip** as a required argument and **units** and **output** as optional argument.
  - **find_by_address** takes **address** as a required argument and **units** and **output** as optional argument.
  - **find_distance_to_stores** reads csv file, sort the stores in the csv and returns the closest store to the provided zip or adress

# Requirments.txt file
- I am using **docopt**, **pandas**, **uszipcode**, **haversinegeopy**. Please run **Pip install** after cloning the repo in order to install required libraries. 

# Testing and Running Functions
- To run test (in test_find_stores.py) please run **python3 test_find_store.py** 
- To find a store by zip, in the command line please run **python3 find_store.py  --zip=95670 --units=km**
- To find a store by an address, in the command line please run **python3 find_store.py  --address="1122 14th, oakland" --units="km"**
- Expected result **{'dist': 2.7137721756187703, 'key': 1758, 'Address': '2700 Fifth Street'}** 