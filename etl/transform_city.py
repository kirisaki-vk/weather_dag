import os
import pandas as pd
import numpy as np

DATA_OUTPUT_PATH = os.getenv("OUTPUT_FILES_PATH")

DEMOGRAPHIC_DATA = pd.read_csv(os.getenv("DEMOGRAPHIC_DATA_PATH"))
GEOGRAPHIC_DATA = pd.read_csv(os.getenv("GEOGRAPHIC_DATA_PATH"))

