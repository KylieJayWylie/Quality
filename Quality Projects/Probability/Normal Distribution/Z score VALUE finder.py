def get_z_score_from_table(cumulative_probability, z_score_table):
    """
    Retrieve the Z score corresponding to a given cumulative probability from a Z score table.

    Parameters:
    cumulative_probability (float): The cumulative probability (area under the curve) to look up.
    z_score_table (dict): A dictionary representing the Z score table, where keys are Z scores
                          and values are cumulative probabilities.

    Returns:
    float: The Z score corresponding to the given cumulative probability.

    Raises:
    ValueError: If the cumulative probability is not found in the table.
    """
    # Find the closest match in the Z score table
    closest_z_score = None
    closest_difference = float('inf')

    for z_score, probability in z_score_table.items():
        difference = abs(probability - cumulative_probability)
        if difference < closest_difference:
            closest_difference = difference
            closest_z_score = z_score

    if closest_z_score is None:
        raise ValueError("Cumulative probability not found in the Z score table.")

    return closest_z_score


# Example usage
if __name__ == "__main__":
    # Example Z score table (partial, for demonstration purposes)
    z_score_table = {
        -3.4: 0.0003,
        -3.3: 0.0005,
        -3.2: 0.0007,
        -3.1: 0.0010,
        -3.0: 0.0013,
        -2.9: 0.0019,
        -2.8: 0.0026,
        -2.7: 0.0035,
        -2.6: 0.0047,
        -2.5: 0.0062,
        # Add more entries as needed
    }

    cumulative_probability = float(input("Enter the cumulative probability: "))

    try:
        z_score = get_z_score_from_table(cumulative_probability, z_score_table)
        print(f"The Z score corresponding to the cumulative probability {cumulative_probability} is: {z_score}")
    except ValueError as e:
        print(e)

