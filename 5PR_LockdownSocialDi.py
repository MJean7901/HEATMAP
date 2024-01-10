import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap, Normalize

# Example Data
data1 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [28, 22, 13],
    '25': [34, 25, 26],
    '50': [39, 33, 26]
}

data2 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [24, 21, 12],
    '25': [32, 25, 20],
    '50': [34, 31, 23]
}

data3 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [20, 13, 6],
    '25': [28, 19, 16],
    '50': [33, 28, 21]
}

data4 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [19, 10, 4],
    '25': [24, 17, 12],
    '50': [28, 25, 17]
}

data5 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [13, 7, 0],
    '25': [18, 13, 7],
    '50': [25, 18, 13]
}

# Create a custom colormap (yellow to dark red)
colors = ["yellow", "orange", "red", "darkred"]
n_bins = 50
cmap = LinearSegmentedColormap.from_list(name='Custom', colors=colors, N=n_bins)

# Create subplots
fig, axes = plt.subplots(1, 5, figsize=(18, 6))

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
