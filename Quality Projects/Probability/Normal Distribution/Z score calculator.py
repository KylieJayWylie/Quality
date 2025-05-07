def calculate_z_score(value, mean, standard_deviation):
    """
    Calculate the Z Score for a given value in a normal distribution.

    Parameters:
    value (float): The value for which the Z Score is to be calculated.
    mean (float): The mean of the distribution.
    standard_deviation (float): The standard deviation of the distribution.

    Returns:
    float: The Z Score of the value.
    """
    if standard_deviation == 0:
        raise ValueError("Standard deviation cannot be zero.")
    
    z_score = (value - mean) / standard_deviation
    return z_score

# Example usage
if __name__ == "__main__":
    value = float(input("Enter the value: "))
    mean = float(input("Enter the mean: "))
    standard_deviation = float(input("Enter the standard deviation: "))

    try:
        z_score = calculate_z_score(value, mean, standard_deviation)
        print(f"The Z Score is: {z_score}")
    except ValueError as e:
        print(e)
