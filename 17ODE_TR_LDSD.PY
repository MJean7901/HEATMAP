import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap, Normalize

# Example Data
data1 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [44, 33, 23],
    '25': [47, 44, 34],
    '50': [48, 45, 45]
}

data2 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [41, 34, 18],
    '25': [45, 42,34],
    '50': [45, 43, 43]
}

data3 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [41, 31, 16],
    '25': [45, 42, 31],
    '50': [45, 44, 42]
}
data4 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [39, 32, 15],
    '25': [43, 40, 32],
    '50': [44, 43, 49]
}
data5 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [40, 33, 12],
    '25': [40, 39, 31],
    '50': [43, 40, 47]
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
