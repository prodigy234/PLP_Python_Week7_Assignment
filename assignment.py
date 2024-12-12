import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load the dataset
    file_path = 'airbnb_price.csv'
    data = pd.read_csv(file_path)
    
    # Display the first few rows
    print("First five rows of the dataset:")
    print(data.head())
    
    # Check the structure of the dataset
    print("\nDataset Info:")
    print(data.info())
    
    # Check for missing values
    print("\nMissing Values:")
    print(data.isnull().sum())
    
    # Clean the dataset (fill or drop missing values)
    data = data.dropna()  # Dropping missing values for simplicity
    print("\nData after dropping missing values:")
    print(data.info())

except FileNotFoundError:
    print("The file was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")

# Task 2: Basic Data Analysis
try:
    # Compute basic statistics of numerical columns
    print("\nBasic Statistics of Numerical Columns:")
    print(data.describe())
    
    # Perform grouping on a categorical column and compute mean of a numerical column
    if 'room_type' in data.columns and 'price' in data.columns:
        grouped_data = data.groupby('room_type')['price'].mean()
        print("\nAverage Price by Room Type:")
        print(grouped_data)
    else:
        print("Columns 'room_type' or 'price' not found in the dataset.")

except Exception as e:
    print(f"An error occurred during analysis: {e}")

# Task 3: Data Visualization
try:
    # Line Chart: Time-Series Data
    if 'date' in data.columns and 'price' in data.columns:
        data['date'] = pd.to_datetime(data['date'])
        time_series_data = data.groupby('date')['price'].mean()
        plt.figure(figsize=(10, 6))
        plt.plot(time_series_data, label='Average Price')
        plt.title('Time-Series of Average Price')
        plt.xlabel('Date')
        plt.ylabel('Average Price')
        plt.legend()
        plt.show()
    
    # Bar Chart: Comparison of Numerical Value Across Categories
    if 'room_type' in data.columns and 'price' in data.columns:
        plt.figure(figsize=(8, 6))
        sns.barplot(x=grouped_data.index, y=grouped_data.values, palette='viridis')
        plt.title('Average Price by Room Type')
        plt.xlabel('Room Type')
        plt.ylabel('Average Price')
        plt.show()

    # Histogram: Distribution of a Numerical Column
    if 'price' in data.columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(data['price'], kde=True, bins=30, color='blue')
        plt.title('Distribution of Price')
        plt.xlabel('Price')
        plt.ylabel('Frequency')
        plt.show()

    # Scatter Plot: Relationship Between Two Numerical Columns
    if 'price' in data.columns and 'minimum_nights' in data.columns:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=data['minimum_nights'], y=data['price'], alpha=0.6, color='green')
        plt.title('Price vs Minimum Nights')
        plt.xlabel('Minimum Nights')
        plt.ylabel('Price')
        plt.show()

except Exception as e:
    print(f"An error occurred during visualization: {e}")
