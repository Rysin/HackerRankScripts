# import pandas as pd
import pandas as pd

# import numpy as np
import numpy as np

# simple array
data = np.array(["s", "c", "a", "l", "a", "r"])

_index = (i for i in range(10, 22, 2))

# providing an index
ser = pd.Series(data, index=_index)
print(ser)
