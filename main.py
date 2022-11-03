import os
import pandas as pd
import cfbd
from sklearn import linear_model
# @jbuddavis
# https://github.com/jbuddavis
pd.options.mode.chained_assignment = None

try:
    SOME_SECRET = os.environ["CFBD_SECRET"]
except KeyError:
    SOME_SECRET = "key not available!"

print(SOME_SECRET)
