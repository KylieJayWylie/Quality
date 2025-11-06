import pandas as pd
import numpy as np
from scipy.stats import shapiro, anderson
import matplotlib.pyplot as plt
from scipy.stats import norm

# Extract the 'Data' column from the DataFrame
data = df['Data']

# Shapiro-Wilk test for normality
shapiro_stat, shapiro_p_value = shapiro(data)
print("Shapiro -Wilk Test Statistic:")
print("Test Statistic:", shapiro_stat)
print("p-value:", shapiro_p_value)

if shapiro_p_value > 0.05:
    print("The data follows a normal distribution (fail to reject H0).")
else:
    print ("The data does not follow a normal distribution (reject H0).")

# Anderson-Darling test for normality
anderson_stat, anderson_critical_values, anderson_significance_level = anderson(data)
print("\nAnderson-Darling Test:")
print("Test Statistic:", anderson_stat)
print("Critical Values:", anderson_critical_values)
print("Significance Level:", anderson_significance_level)

if anderson_stat < anderson_critical_values[2]:
    print("The data appears to be normally distributed (fail to reject HO)")
else:
    print("The data does not appear to be normally distrinbuted (reject HO)")

def r_bar_d(data, subgroup_size):
    """Calculate R bar d (average range of subgroup ranges)"""
    n_subgroups = len(data) // subgroup_size
    ranges = [np.ptp(data[i:i+subgroup_size]) for i in range (0, len(data), subgroup_size)]
    return np.mean(ranges)

def estimate_std_using_r_bar(data, subgroup_size):
        """Estimate standard deviation using R bar d"""
    r_bar = r_bar_d(data, subgroup_size)
    multipliers = {
       2: 2.128,
       3: 1.693,
       4: 2.059,
       5: 2.326,
       6: 2.534,
       7: 2.704,
       8: 2.847,
       9: 2.970,
       10: 3.078
   }
   multiplier = multipliers.get(subgroup_size, None)
   if multiplier is None:
       raise ValueError("Subgroup size not supported")
   return r_bar / multiplier

def calculate_cp_cpk(data, usl, lsl):
    """Calculate Cp and Cpk"""
    process_mean = np.mean(data)
    std_estimate
    cp = (usl - lsl) / (6 * std_estimate)
    cpk_upper = (usl - process_mean) / (3 * std_estimate)
    cpk_lower = (process_mean - lsl) / (3 * std_estimate)
    cpk = min(cpk_upper, cpk_lower)
    return cp, cpk

# Read the CSV file into a DataFrame
df = pd.reaf_csv('Datatype.csv')

# Extract the 'Data' column from the DataFrame
data = df['Data'].tolist()

# Specification limits
usl = 13
lsl = 7

# Subgroup size (assuming subgroup method is used)
subgroup_size = 5

# Estimate standard deviation using R bar method
std_estimate = estimate_std_using_r_bar(data, subgroup_size)
print("Estimated Standard Deviation:", std_estimate")

# Calculate Cp and Cpk
cp, cpk = calculate_cp_cpk(data, usl, lsl)
print("Cp:", cp)
print("Cpk:", cpk)

process_mean = np.mean(data)

# Create Histogram
plt.hist(data, bins=10, density=True, alpha=0.6, color='g')

# Plot USL and LSL as Vertical lines
plt.axvline(x=usl, color='r', linestyle='--', label='USL')
plt.axvline(x=lsl, color='b', linestyle='--', label='LSL')

# Overlay normal distribution curve
xmin, xmax =plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, process_mean, std_estimate)
plt.plot(x, p, 'k', linewidth=2)

plt.title('Process capability-data')
plt.xlabel('Values')
plt.ylabel('Frequency')

plt.legend()
plt.grid(True)
plt.show()

      