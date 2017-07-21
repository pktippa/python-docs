# All basic usage of numpy
import numpy as np
# prints the version of numpy
print(np.__version__)

# Whether element is a numpy array
el = np.array(list())
# Below command resolves to true
if isinstance(el, np.ndarray):
    print("Element is a numpy array.")