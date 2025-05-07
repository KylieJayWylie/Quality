import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

def oc_curve(sample_size, acceptance_number, defect_rates):
    """
    Calculate and plot the OC curve.
    
    Parameters:
    sample_size (int): Number of items sampled.
    acceptance_number (int): Maximum number of defective items allowed for acceptance.
    defect_rates (list): List of defect rates to evaluate.
    
    Returns:
    None
    """
    probabilities = [binom.cdf(acceptance_number, sample_size, p) for p in defect_rates]

    plt.figure(figsize=(8, 6))
    plt.plot(defect_rates, probabilities, marker='o', linestyle='-')
    plt.xlabel("Defect Rate (p)")
    plt.ylabel("Probability of Acceptance")
    plt.title("Operating Characteristic (OC) Curve")
    plt.grid(True)
    plt.show()

# Example usage
sample_size = 50  # Sample size
acceptance_number = 3  # Acceptance number
defect_rates = np.linspace(0, 0.2, 50)  # Range of defect rates

oc_curve(sample_size, acceptance_number, defect_rates)
