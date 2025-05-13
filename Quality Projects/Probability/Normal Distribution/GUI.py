import tkinter as tk
from tkinter import messagebox
from scipy.stats import norm

def calculate():
    try:
        mean = float(mean_entry.get())
        std_dev = float(std_dev_entry.get())
        value = float(value_entry.get())

        # Calculate Z-score
        z_score = (value - mean) / std_dev

        # Calculate probability
        probability = norm.cdf(z_score)

        # Display results
        z_score_label.config(text=f"Z-Score: {z_score:.4f}")
        probability_label.config(text=f"Probability: {probability:.4f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("Normal Distribution Calculator")

# Mean input
tk.Label(root, text="Mean:").grid(row=0, column=0, padx=10, pady=5)
mean_entry = tk.Entry(root)
mean_entry.grid(row=0, column=1, padx=10, pady=5)

# Standard deviation input
tk.Label(root, text="Standard Deviation:").grid(row=1, column=0, padx=10, pady=5)
std_dev_entry = tk.Entry(root)
std_dev_entry.grid(row=1, column=1, padx=10, pady=5)

# Value input
tk.Label(root, text="Value:").grid(row=2, column=0, padx=10, pady=5)
value_entry = tk.Entry(root)
value_entry.grid(row=2, column=1, padx=10, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Results
z_score_label = tk.Label(root, text="Z-Score: ")
z_score_label.grid(row=4, column=0, columnspan=2, pady=5)

probability_label = tk.Label(root, text="Probability: ")
probability_label.grid(row=5, column=0, columnspan=2, pady=5)

# Run the application
root.mainloop()

