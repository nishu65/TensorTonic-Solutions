def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    x = values[:]  # copy to avoid modifying original

    min_val = min(x)
    max_val = max(x)

    # Edge case: all values same
    if max_val == min_val:
        return [0] * len(x)

    w = (max_val - min_val) / num_bins

    result = []
    for i in range(len(x)):
        bin_index = int((x[i] - min_val) / w)

        # Handle max value edge case
        if bin_index == num_bins:
            bin_index = num_bins - 1

        result.append(bin_index)

    return result