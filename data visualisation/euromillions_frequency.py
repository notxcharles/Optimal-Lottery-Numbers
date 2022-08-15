import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

df = pd.read_csv(
    os.path.join(os.path.dirname(__file__), "../EuroMillions_results.csv"),
    delimiter="|",
    header=0,
)
# Lets find the frequency of regular balls

balls = [x for x in df["Ball 1"]]
balls += [x for x in df["Ball 2"]]
balls += [x for x in df["Ball 3"]]
balls += [x for x in df["Ball 4"]]
balls += [x for x in df["Ball 5"]]

frequency_df = pd.DataFrame()
frequency_df["Balls"] = balls


fig, ax = plt.subplots()

frequency_df["Balls"].value_counts().plot(
    ax=ax, kind="bar", xlabel="Number", ylabel="Frequency"
)

plt.show()
