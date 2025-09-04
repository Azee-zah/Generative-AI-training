import math             #importing a pre-built python module

print(math.sqrt(9))

#importing as an alias
import math as m

print(m.sqrt(25))

# to import specific function or variable from a module
from math import sqrt, pi
print(sqrt(36))
print(pi)

# to import evrything from the module
from math import *
print(sqrt(49))
print(pi)


#