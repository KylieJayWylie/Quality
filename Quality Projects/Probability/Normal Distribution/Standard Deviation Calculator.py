import math

def calculate_standard_deviation(data):
    if len(data) == 0:
        return float('nan')
    
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    standard_deviation = math.sqrt(variance)
    
    return standard_deviation

def get_user_input_and_calculate_sd():
    """
    Prompts the user to input a list of numbers and calculates the standard deviation.
    """
    try:
        user_input = input("Enter numbers separated by spaces: ")
        data = list(map(float, user_input.split()))
        
        if len(data) == 0:
            print("No data provided. Please enter at least one number.")
            return
        
        standard_deviation = calculate_standard_deviation(data)
        print(f"The standard deviation of the given data is: {standard_deviation}")
    except ValueError:
        print("Invalid input. Please enter numeric values only.")

# Example usage
if __name__ == "__main__":
    get_user_input_and_calculate_sd()

