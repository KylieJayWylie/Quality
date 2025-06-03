import math
def calculate_reliability(failure_rate, repair_rate, time):
    """
    Calculate the reliability of a system given its failure rate, repair rate, and time.
    Parameters:
    failure_rate (float): The failure rate of the system (failures per unit time).
    repair_rate (float): The repair rate of the system (repairs per unit time).
    time (float): The time period over which to calculate reliability.
    Returns:
    float: The reliability of the system at the given time.
    """
    # Calculate the reliability using the formula
    reliability = math.exp(-(failure_rate - repair_rate) * time)
    return reliability

if __name__ == "__main__":
    try:
        failure_rate = float(input("Enter the failure rate (failures per unit time): "))
        time = float(input("enter the time period in (hours): "))
        repair_rate = float(input("Enter the repair rate (repairs per unit time): "))
        reliability = calculate_reliability(failure_rate, repair_rate, time)
        print(f"Reliability of the process over {time} hours: {reliability:.4f}")
    except ValueError:
        print("Please enter valid numeric value. ")