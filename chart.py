import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------
# Generate synthetic data
# -----------------------
np.random.seed(42)
months = pd.date_range("2023-01-01", periods=12, freq="ME").strftime("%b")

segments = ["Premium", "Standard", "Budget"]
data = []

for seg in segments:
    base = np.linspace(80, 200, 12)  # baseline upward trend
    seasonal = 20 * np.sin(np.linspace(0, 2 * np.pi, 12))  # seasonality
    noise = np.random.normal(0, 8, 12)  # random noise
    revenue = base + seasonal + noise
    
    # Adjust per segment
    if seg == "Premium":
        revenue *= 1.8
    elif seg == "Standard":
        revenue *= 1.2
    else:  # Budget
        revenue *= 0.9
    
    for m, r in zip(months, revenue):
        data.append([m, seg, r])

df = pd.DataFrame(data, columns=["Month", "Segment", "Revenue"])

# -----------------------
# Create visualization
# -----------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# IMPORTANT: dpi * figsize = 512
fig = plt.figure(figsize=(8, 8), dpi=64)

sns.lineplot(
    data=df,
    x="Month",
    y="Revenue",
    hue="Segment",
    palette="deep",
    marker="o"
)

plt.title("Monthly Revenue Trends by Customer Segment", fontsize=16, weight="bold")
plt.xlabel("Month")
plt.ylabel("Revenue (in $000s)")
plt.xticks(rotation=45)
plt.legend(title="Customer Segment", loc="upper left")

# -----------------------
# Save chart (force exact size)
# -----------------------
# bbox_inches="tight" can shrink canvas → remove it
plt.savefig("chart.png", dpi=64, pad_inches=0)
plt.close()
