# Importing function from a module
from topackage.importme import theimportedFunction
# Importing whole module
from topackage.packager import ucanimportme 

# Invoking particular function from imported module
print(ucanimportme.anotherimportedfunc("Sekhar"))
# Invoking imported function directly
print(theimportedFunction("Sappa"))