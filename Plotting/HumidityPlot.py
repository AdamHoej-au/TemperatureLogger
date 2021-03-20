#%%
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import numpy as np
import pandas as pd
#%%
fileInput = "../Logs/humidityLog.csv"

header_list = ["Dato", "Tid", "Temperatur1", "Luftfugtighed1"]
df = pd.read_csv(fileInput, names=header_list)
#%%

print(df)
# # %%

df.plot("Tid", ["Temperatur1", "Luftfugtighed1"], subplots=True)
plt.savefig('Plot.png',dpi=300)
# %%
