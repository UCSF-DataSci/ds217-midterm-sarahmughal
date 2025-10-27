#!/usr/bin/env python3

# Assignment 5, Question 2: Python Data Processing
# Process configuration files for data generation.


def parse_config(filepath: str) -> dict:
    """
    Parse config file (key=value format) into dictionary.

    Args:
        filepath: Path to q2_config.txt

    Returns:
        dict: Configuration as key-value pairs

    Example:
        >>> config = parse_config('q2_config.txt')
        >>> config['sample_data_rows']
        '100'
    """
    # TODO: Read file, split on '=', create dict
    config = {}

    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if line and "=" in line:
                key, value = line.split("=")
                config[key] = value

    return config


def validate_config(config: dict) -> dict:
    """
    Validate configuration values using if/elif/else logic.

    Rules:
    - sample_data_rows must be an int and > 0
    - sample_data_min must be an int and >= 1
    - sample_data_max must be an int and > sample_data_min

    Args:
        config: Configuration dictionary

    Returns:
        dict: Validation results {key: True/False}

    Example:
        >>> config = {'sample_data_rows': '100', 'sample_data_min': '18', 'sample_data_max': '75'}
        >>> results = validate_config(config)
        >>> results['sample_data_rows']
        True
    """
    # TODO: Implement with if/elif/else
    rows = int(config.get("sample_data_rows", 0))
    vmin = int(config.get("sample_data_min", 0))
    vmax = int(config.get("sample_data_max", 0))

    results = {}

    if rows > 0:
        results["sample_data_rows"] = True
    else:
        results["sample_data_rows"] = False

    if vmin >= 1:
        results["sample_data_min"] = True
    else:
        results["sample_data_min"] = False

    if vmax > vmin:
        results["sample_data_max"] = True
    else:
        results["sample_data_max"] = False

    return results


def generate_sample_data(filename: str, config: dict) -> None:
    """
    Generate a file with random numbers for testing, one number per row with no header.
    Uses config parameters for number of rows and range.

    Args:
        filename: Output filename (e.g., 'sample_data.csv')
        config: Configuration dictionary with sample_data_rows, sample_data_min, sample_data_max

    Returns:
        None: Creates file on disk

    Example:
        >>> config = {'sample_data_rows': '100', 'sample_data_min': '18', 'sample_data_max': '75'}
        >>> generate_sample_data('sample_data.csv', config)
        # Creates file with 100 random numbers between 18-75, one per row
        >>> import random
        >>> random.randint(18, 75)  # Returns random integer between 18-75
    """
    # TODO: Parse config values (convert strings to int)
    rows = int(config.get("sample_data_rows", 0))
    low = int(config.get("sample_data_min", 0))
    high = int(config.get("sample_data_max", 0))

    # TODO: Generate random numbers and save to file
    # TODO: Use random module with config-specified range
    import random

    with open(filename, "w") as f:
        for _ in range(rows):
            f.write(str(random.randint(low, high)) + "\n")


def calculate_statistics(data: list) -> dict:
    """
    Calculate basic statistics.

    Args:
        data: List of numbers

    Returns:
        dict: {mean, median, sum, count}

    Example:
        >>> stats = calculate_statistics([10, 20, 30, 40, 50])
        >>> stats['mean']
        30.0
    """
    # TODO: Calculate stats
    n = len(data)
    total = sum(data)
    mean = total / n if n else 0
    s = sorted(data)
    mid = n // 2
    median = s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2
    return {"mean": mean, "median": median, "sum": total, "count": n}


if __name__ == "__main__":
    # TODO: Test your functions with sample data
    # Example:
    # config = parse_config('q2_config.txt')
    # validation = validate_config(config)
    # generate_sample_data('data/sample_data.csv', config)
    #
    # TODO: Read the generated file and calculate statistics
    # TODO: Save statistics to output/statistics.txt
    config = parse_config("q2_config.txt")
    validation = validate_config(config)
    print("Validation:", validation)

    generate_sample_data("data/sample_data.csv", config)

    with open("data/sample_data.csv") as f:
        numbers = [int(line.strip()) for line in f if line.strip()]

    stats = calculate_statistics(numbers)
    print("Statistics:", stats)

    with open("output/statistics.txt", "w") as f:
        for k, v in stats.items():
            f.write(f"{k}: {v}\n")
