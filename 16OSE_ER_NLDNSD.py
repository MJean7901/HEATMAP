import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap, Normalize

# Example Data
data1 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [42, 32, 0],
    '25': [45, 40, 32],
    '50': [48, 45, 43]
}

data2 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [43, 37, 36],
    '25': [46, 42, 37],
    '50': [50, 48, 47]
}

data3 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [45, 44, 41],
    '25': [46, 44, 42],
    '50': [50, 50, 49]
}

# Create a custom colormap (yellow to dark red)
colors = ["lemonchiffon", "aquamarine", "deepskyblue", "navy", "midnightblue"]
n_bins = 50
cmap = LinearSegmentedColormap.from_list(name='Custom', colors=colors, N=n_bins)

# Create subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

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

# Adjust layout
plt.tight_layout()
plt.show()
