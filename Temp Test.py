import pandas as pd
import numpy as np
import glob
import os

# My Folder Location : C:\Users\joy43\Desktop\New folder\Assignment 2\Qus 3\temperatures

FOLDER = r"C:\Users\joy43\Desktop\New folder\Assignment 2\Qus 2\temperatures"

# Output files saved in the same folder
OUTPUT_AVG   = os.path.join(FOLDER, "average_temp.txt")
OUTPUT_RANGE = os.path.join(FOLDER, "largest_temp_range_station.txt")
OUTPUT_STD   = os.path.join(FOLDER, "temperature_stability_stations.txt")

# Map months to numbers and seasons

months = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]
month_to_num = {m: i+1 for i, m in enumerate(months)}

def get_season(month_num):
    if month_num in (12,1,2): return "Summer"
    if month_num in (3,4,5): return "Autumn"
    if month_num in (6,7,8): return "Winter"
    return "Spring"

# Read and combine all CSV files

files = glob.glob(os.path.join(FOLDER, "*.csv"))
if not files:
    raise FileNotFoundError(f"No CSV files found in {FOLDER}")

df_list = [pd.read_csv(f) for f in files]
data = pd.concat(df_list, ignore_index=True)

# Melt months into rows

long_df = data.melt(
    id_vars=["STATION_NAME","STN_ID"],
    value_vars=months,
    var_name="Month",
    value_name="Temp"
).dropna(subset=["Temp"])

long_df["MonthNum"] = long_df["Month"].map(month_to_num)
long_df["Season"] = long_df["MonthNum"].map(get_season)
long_df["Station"] = long_df["STATION_NAME"] + " (" + long_df["STN_ID"].astype(str) + ")"

# Seasonal Average

season_avg = long_df.groupby("Season")["Temp"].mean()
with open(OUTPUT_AVG,"w",encoding="utf-8") as f:
    for season in ["Summer","Autumn","Winter","Spring"]:
        if season in season_avg:
            f.write(f"{season}: {season_avg[season]:.1f}°C\n")

# Largest Temp Range

station_stats = long_df.groupby("Station")["Temp"].agg(["min","max"])
station_stats["range"] = station_stats["max"] - station_stats["min"]
max_range = station_stats["range"].max()
leaders = station_stats[station_stats["range"]==max_range]

with open(OUTPUT_RANGE,"w",encoding="utf-8") as f:
    for st, row in leaders.iterrows():
        f.write(f"{st}: Range {row['range']:.1f}°C (Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n")

# Temperature Stability

stds = long_df.groupby("Station")["Temp"].std()
min_std, max_std = stds.min(), stds.max()
stable = stds[stds==min_std]
variable = stds[stds==max_std]

with open(OUTPUT_STD,"w",encoding="utf-8") as f:
    for st, val in stable.items():
        f.write(f"Most Stable: {st}: StdDev {val:.1f}°C\n")
    for st, val in variable.items():
        f.write(f"Most Variable: {st}: StdDev {val:.1f}°C\n")

print("Done, files saved in:", FOLDER)
