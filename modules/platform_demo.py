# Importing necessary functions from the platform module
from platform import platform as p, machine as m, processor, system
from platform import version
from platform import python_implementation, python_version_tuple

# Print the platform details
print(p())             # Full platform information
print(p(1))            # Aliased version of platform information
print(p(0, 1))         # Information with specific terse and aliased options

# Print the machine type
print(m())             # Machine type (e.g., x86_64)

# Print processor information
print(processor())     # Processor details (e.g., Intel64 Family 6 Model 142)

# Print the operating system name
print(system())        # Operating system (e.g., Windows, Linux, etc.)

# Print the OS version
print(version())       # Version of the operating system

# Print the Python implementation being used
print(python_implementation())  # Python implementation (e.g., CPython, PyPy)

# Print the Python version tuple details
for attr in python_version_tuple():
    print(attr)        # Python version details (e.g., major, minor, patch level)
