import matplotlib.pyplot as plt

def plot_data_with_median_mode(array, median, mode):
    plt.figure(figsize=(10, 5))

    # Plotting histogram
    plt.hist(array, bins=10, color='blue', alpha=0.7, label='Data Distribution')

    # Adding vertical lines for median and mode
    plt.axvline(median, color='green', linestyle='dashed', linewidth=2, label=f'Median: {median}')
    plt.axvline(mode, color='red', linestyle='dashed', linewidth=2, label=f'Mode: {mode}')

    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram with Median and Mode')
    plt.legend()
    plt.show()

# Example usage
data = [1, 2, 2, 3, 4]
median, mode = 2, 2
plot_data_with_median_mode(data, median, mode)
