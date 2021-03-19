#%%
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import numpy as np
import pandas as pd
#%%
header_list = ["Dato", "Tid", "Temperatur1", "Luftfugtighed1"]
df = pd.read_csv("humidityLog.csv", names=header_list)
#%%

print(df)
# # %%

df.plot("Dato", ["Temperatur1", "Luftfugtighed1"], subplots=True)
# %%
