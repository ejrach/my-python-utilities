# There are two ways to import modules, as seen below. In each case, Module1 and Module2
# is a self defined module that you can use to store related functions in.
#
# Here is the import configuration:
# if you do: "import Module1", then you actually import all methods in it
# if you do "from Module1 import lbs_to_kg", then you only import that specific method

# Method 1
import Module1
# Method 2
from Module2 import kg_to_lbs

# Method 1 call
print(Module1.lbs_to_kg(70))

# Method 2 call
print(kg_to_lbs(70))
