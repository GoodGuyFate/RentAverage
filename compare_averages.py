import csv
from statistics import mean
import matplotlib.pyplot as plt


def calculate_average_rent(filename):
    """
    Calculates the average rent price from a CSV file.

    Args:
        filename (str): Name of the CSV file containing rent prices (assumed to be in the second column).

    Returns:
        float: The average rent price.
    """

    prices = []
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row (assuming it exists)
        for row in reader:
            price = float(row[1])  # Assuming price is in the second column
            prices.append(price)
    return mean(prices)


def main():
    # List of your filtered CSV filenames
    csv_filenames = [
       
    ]

    average_rents = {}
    for filename in csv_filenames:
        average_rent = calculate_average_rent(filename)
        area_name = filename.split("_")[2].replace(
            ".csv", ""
        )  # Extract area name (assuming filename format)
        average_rents[area_name] = average_rent

    # Print the calculated averages
    print("Average Apartment Rents by Area:")
    areas = list(average_rents.keys())
    rents = list(average_rents.values())

    # Create the bar graph
    plt.figure(figsize=(10, 6))  # Adjust figure size as needed
    bars = plt.bar(areas, rents, color="skyblue")  # Create bars and store them

    # Add data labels above each bar
    for bar, rent in zip(bars, rents):
        yval = bar.get_height()  # Get the height of each bar
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 50, f"{rent:.2f}", ha='center', va='bottom')  # Add label with offset and format

    plt.xlabel("Neighborhood")
    plt.ylabel("Average Rent (EGP)")
    plt.title("Comparison of Average Apartment Rent Prices")
    plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
