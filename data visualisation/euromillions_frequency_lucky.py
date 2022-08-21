import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

df = pd.read_csv(
    os.path.join(os.path.dirname(__file__), "../EuroMillions_results.csv"),
    delimiter="|",
    header=0,
)
# Lets find the frequency of lucky balls

balls = [x for x in df["Lucky 1"]]
balls += [x for x in df["Lucky 2"]]

frequency_df = pd.DataFrame()
frequency_df["Lucky Balls"] = balls


fig, ax = plt.subplots()

frequency_df["Lucky Balls"].value_counts().plot(
    ax=ax, kind="bar", xlabel="Number", ylabel="Frequency"
)

plt.show()
