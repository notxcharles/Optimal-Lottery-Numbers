import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

# df = pd.read_csv("../EuroMillions_results.csv", delimiter="|", header=0)

df = pd.read_csv(
    os.path.join(os.path.dirname(__file__), "../EuroMillions_results.csv"),
    delimiter="|",
    header=0,
)

df = df.dropna()

# Lets find the frequency the regular balls * by 1/7 of the jackpot to find the most valuable ball


ball_value = dict()

for row, ball in df["Ball 1"].items():
    # print("Roll", b, "Jackpot", df.at[a,"Jackpot"])
    ball_value[ball] = ball_value.get(ball, 0) + (df.at[row, "Jackpot"] / 7)

for row, ball in df["Ball 2"].items():
    ball_value[ball] = ball_value.get(ball, 0) + (df.at[row, "Jackpot"] / 7)

for row, ball in df["Ball 3"].items():
    ball_value[ball] = ball_value.get(ball, 0) + (df.at[row, "Jackpot"] / 7)

for row, ball in df["Ball 4"].items():
    ball_value[ball] = ball_value.get(ball, 0) + (df.at[row, "Jackpot"] / 7)

for row, ball in df["Ball 5"].items():
    ball_value[ball] = ball_value.get(ball, 0) + (df.at[row, "Jackpot"] / 7)

# print(len(ball_value))


value_df = pd.DataFrame(data=ball_value.items(), columns=["Ball", "Value"])
value_df.set_index("Ball", inplace=True)
value_df = value_df.sort_values("Value")
print(value_df)

fig, ax = plt.subplots()
value_df["Value"].plot(ax=ax, kind="bar", xlabel="Number", ylabel="Value")
plt.grid(axis="y")
plt.show()
