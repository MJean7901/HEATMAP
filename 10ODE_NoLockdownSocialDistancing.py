import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap, Normalize

# Example Data
data1 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [45, 36, 25],
    '25': [48, 45, 35],
    '50': [48, 47, 46]
}

data2 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [42, 34, 22],
    '25': [45, 42,30],
    '50': [45, 43, 43]
}

data3 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [35, 30, 18],
    '25': [45, 32, 28],
    '50': [45, 44, 32]
}
data4 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [32, 26, 15],
    '25': [43, 30, 26],
    '50': [44, 43, 29]
}
data5 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [30, 23, 12],
    '25': [40, 28, 31],
    '50': [43, 40, 27]
}

# Create a custom colormap (yellow to dark red)
colors = ["lemonchiffon", "aquamarine", "deepskyblue", "navy", "midnightblue"]
n_bins = 50
cmap = LinearSegmentedColormap.from_list(name='Custom', colors=colors, N=n_bins)

# Create subplots
fig, axes = plt.subplots(1, 5, figsize=(25, 6))

# Function to create heatmap for each dataset
def create_heatmap(data, ax, title):
    df = pd.DataFrame(data)
    df.set_index('Initial Inf in City2', inplace=True)
    sns.heatmap(df, annot=False, cmap=cmap, norm=Normalize(vmin=0, vmax=50), ax=ax)
    ax.set_title(title)
    for _, spine in ax.spines.items():
        spine.set_visible(True)
        spine.set_color('black')
        spine.set_linewidth(2)

# Create heatmaps
create_heatmap(data1, axes[0], '(0)')
create_heatmap(data2, axes[1], '(25)')
create_heatmap(data3, axes[2], '(50)')
create_heatmap(data4, axes[3], '(75)')
create_heatmap(data5, axes[4], '(100)')
# Adjust layout
plt.tight_layout()
plt.show()
