import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Create sample datasets
np.random.seed(42)
normal_dist = np.random.normal(100, 15, 1000)
skewed_dist = np.concatenate([
    np.random.normal(50, 10, 800),  # Bulk of data
    np.random.normal(150, 20, 200)  # Some extreme values
])
outlier_dist = np.random.normal(100, 15, 1000)
outlier_dist[-10:] = [250, 260, 270, 280, 290, 300, 310, 320, 330, 340]  # Add extreme outliers

# Create figure
plt.figure(figsize=(15, 5))

# Normal Distribution Boxplot
plt.subplot(1, 3, 1)
sns.boxplot(x=normal_dist)
plt.title('Normal Distribution')
plt.xlabel('Values')

# Skewed Distribution Boxplot
plt.subplot(1, 3, 2)
sns.boxplot(x=skewed_dist)
plt.title('Skewed Distribution')
plt.xlabel('Values')

# Distribution with Outliers Boxplot
plt.subplot(1, 3, 3)
sns.boxplot(x=outlier_dist)
plt.title('Distribution with Outliers')
plt.xlabel('Values')

plt.tight_layout()
plt.show()

# Detailed statistical breakdown
def describe_boxplot(data, name):
    q1 = np.percentile(data, 25)
    median = np.median(data)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    
    # Identify outliers
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    
    print(f"\n{name} Distribution Analysis:")
    print(f"Median: {median:.2f}")
    print(f"25th Percentile (Q1): {q1:.2f}")
    print(f"75th Percentile (Q3): {q3:.2f}")
    print(f"Interquartile Range (IQR): {iqr:.2f}")
    print(f"Number of Outliers: {len(outliers)}")
    print(f"Outlier Range: {lower_bound:.2f} to {upper_bound:.2f}")

describe_boxplot(normal_dist, "Normal")
describe_boxplot(skewed_dist, "Skewed")
describe_boxplot(outlier_dist, "Outlier")