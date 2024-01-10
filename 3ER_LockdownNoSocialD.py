import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap, Normalize

# Example Data
data1 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [17, 9, 0],
    '25': [28, 17, 9],
    '50': [31, 27, 16]
}

data2 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [27, 22, 14],
    '25': [32, 29, 16],
    '50': [39, 30, 26]
}

data3 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [34, 31, 22],
    '25': [44, 35, 28],
    '50': [47, 40, 35]
}

# Create a custom colormap (yellow to dark red)
colors = ["yellow", "orange", "red", "darkred"]
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
