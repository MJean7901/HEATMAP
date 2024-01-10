import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap, Normalize

# Example Data
data1 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [42, 39, 31],
    '25': [46, 40, 39],
    '50': [50, 47, 42]
}

data2 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [38, 35, 28],
    '25': [41, 33, 35],
    '50': [42, 40, 37]
}

data3 = {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [29, 22, 10],
    '25': [32, 26, 15],
    '50': [38, 29, 24]
}

data4= {
    'Initial Inf in City2': ['50', '25', '0'],
    '0': [22, 14, 4],
    '25': [26, 22, 14],
    '50': [30, 25, 18]
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
