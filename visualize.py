import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

gdp = pd.read_csv("gdp.csv", index_col="Country")
cpi = pd.read_csv("cpi.csv", index_col="Country")

fig, axes = plt.subplots(2, 2, figsize=(14, 9))
fig.suptitle("Post-COVID Global Economic Recovery", fontsize=15, fontweight="bold")

# Plot 1: GDP line chart
ax1 = axes[0, 0]
for country in gdp.index:
    ax1.plot(gdp.columns, gdp.loc[country], marker="o", label=country)
ax1.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax1.set_title("GDP Growth (%)")
ax1.set_ylabel("%")
ax1.legend(fontsize=7)
ax1.tick_params(axis="x", rotation=45)

# Plot 2: Inflation line chart
ax2 = axes[0, 1]
for country in cpi.index:
    ax2.plot(cpi.columns, cpi.loc[country], marker="s", linestyle="--", label=country)
ax2.set_title("CPI Inflation (%)")
ax2.set_ylabel("%")
ax2.legend(fontsize=7)
ax2.tick_params(axis="x", rotation=45)

# Plot 3: Mean GDP bar chart
ax3 = axes[1, 0]
means = gdp.mean(axis=1)
stds  = gdp.std(axis=1)
ax3.bar(means.index, means.values, yerr=stds.values, capsize=4, color="steelblue", alpha=0.8)
ax3.set_title("Mean GDP Growth with Std Dev")
ax3.set_ylabel("%")
ax3.tick_params(axis="x", rotation=30)

# Plot 4: Correlation heatmap
ax4 = axes[1, 1]
corr = gdp.T.corr()
sns.heatmap(corr, ax=ax4, annot=True, fmt=".2f", cmap="coolwarm", center=0)
ax4.set_title("GDP Correlation Matrix")

plt.tight_layout()
plt.savefig("dashboard.png", dpi=150)
plt.show()