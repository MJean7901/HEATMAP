import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap, Normalize

# Example Data
data1 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [48, 36, 35],
    '25': [47, 45, 48],
    '50': [46, 47, 46]
}

data2 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [46,34, 22],
    '25': [45, 42,30],
    '50': [45, 43, 43]
}

data3 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [48, 32, 17],
    '25': [48, 44, 28],
    '50': [47, 44, 47]
}
data4 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [44, 29, 14],
    '25': [45, 40, 26],
    '50': [42, 41, 47]
}
data5 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [35, 23, 10],
    '25': [40, 28, 31],
    '50': [43, 40, 33]
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
