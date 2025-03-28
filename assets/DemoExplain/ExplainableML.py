import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib as mpl

# Set global font size
mpl.rcParams['font.size'] = 25  # Set to desired size (e.g., 14)
mpl.rcParams['axes.titlesize'] = 25  # Title font size
mpl.rcParams['axes.labelsize'] = 25  # Axis label font size
mpl.rcParams['legend.fontsize'] = 25  # Legend font size
mpl.rcParams['xtick.labelsize'] = 25  # X-axis tick label size
mpl.rcParams['ytick.labelsize'] = 25  # Y-axis tick label size

# Load the data from the CSV file
file_path = "KustaviIsokari.csv"  # Replace with the actual file path
data = pd.read_csv(file_path)

# Extract relevant columns
data = data[["Maximum temperature [°C]", "Minimum temperature [°C]"]]

# Randomly select a specified number of data points
num_data_points = 10  # Specify the number of data points to select
data = data.sample(n=num_data_points, random_state=42)

# build feature matrix (with one column in this case) and label vector
X = data[["Minimum temperature [°C]"]]  # feature of a data point is min.temp during a day
y = data["Maximum temperature [°C]"]    # label of data point is max.temp during a day 

# Train a Decision Tree Regressor
maxdep=5
dt_model = DecisionTreeRegressor(random_state=42, max_depth=maxdep)
dt_model.fit(X, y)

# Train a Polynomial Regression model
poly_degree = 7  # Specify the degree of the polynomial
poly_features = PolynomialFeatures(degree=poly_degree)
X_train_poly = poly_features.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y)

# Generate a range of values for the predictor with the same column name as training data
min_temp_range = pd.DataFrame(
    np.linspace(X["Minimum temperature [°C]"].min(), X["Minimum temperature [°C]"].max(), 500),
    columns=["Minimum temperature [°C]"]
)

# Predict maximum temperatures for the range using both models
predicted_max_temp_dt = dt_model.predict(min_temp_range)
min_temp_range_poly = poly_features.transform(min_temp_range)
predicted_max_temp_poly = poly_model.predict(min_temp_range_poly)


# Generate scatter plot with original and augmented data
plt.figure(figsize=(10, 6))

# Plot the original data points
plt.scatter(
    X, y, color='blue', label="training data", marker='o', s=500
)


# Plot the prediction lines
#plt.plot(min_temp_range, predicted_max_temp_dt, color='red', label=f"dec. tree (max.dept. {maxdep})", linewidth=6)
plt.plot(min_temp_range, predicted_max_temp_poly, color='black',linestyle='--',  label=f"PolyReg. (degree {poly_degree})", linewidth=6)

# Add axis labels, title, and legend
plt.xlabel("mintemp [°C]")
plt.ylabel("maxtemp [°C]")
#plt.title("trained models and training data")
plt.legend()
# Save the plot before showing it
plt.savefig("dtpolyreg.png", dpi=100, bbox_inches='tight')
plt.show()



#########
# now we augment the dataset using user signals as pseudo-labels for perturbed data points 
#########


# Augment the training set
augmented_data = data.copy()
augmented_data["Minimum temperature [°C]"] = data["Minimum temperature [°C]"] + 1
augmented_data["Maximum temperature [°C]"] = data["Maximum temperature [°C]"] + 1

augmented_data_minus = data.copy()
augmented_data_minus["Minimum temperature [°C]"] = data["Minimum temperature [°C]"] - 1
augmented_data_minus["Maximum temperature [°C]"] = data["Maximum temperature [°C]"] - 1

# Combine original and augmented data
data_augmented = pd.concat([data, augmented_data, augmented_data_minus], ignore_index=True)

# Split augmented data into predictors and target
X_augmented = data_augmented[["Minimum temperature [°C]"]]
y_augmented = data_augmented["Maximum temperature [°C]"]

# Train a Decision Tree Regressor
dt_model = DecisionTreeRegressor(random_state=42, max_depth=3)
dt_model.fit(X_augmented, y_augmented)

# Train a Polynomial Regression model
poly_degree = 7  # Specify the degree of the polynomial
poly_features = PolynomialFeatures(degree=poly_degree)
X_train_poly = poly_features.fit_transform(X_augmented)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_augmented)

# Generate a range of values for the predictor with the same column name as training data
min_temp_range = pd.DataFrame(
    np.linspace(X_augmented["Minimum temperature [°C]"].min(), X_augmented["Minimum temperature [°C]"].max(), 500),
    columns=["Minimum temperature [°C]"]
)

# Predict maximum temperatures for the range using both models
predicted_max_temp_dt = dt_model.predict(min_temp_range)
min_temp_range_poly = poly_features.transform(min_temp_range)
predicted_max_temp_poly = poly_model.predict(min_temp_range_poly)


# Generate scatter plot with original and augmented data
plt.figure(figsize=(10, 6))

# Plot the original data points
plt.scatter(
    X, y, color='blue', label="orig. data", marker='o',s=500
)

# Plot the augmented data points with +1 shifts
plt.scatter(
    augmented_data["Minimum temperature [°C]"],
    augmented_data["Maximum temperature [°C]"],
    color='orange', label="+1", marker='^',s=500
)

# Plot the augmented data points with -1 shifts
plt.scatter(
    augmented_data_minus["Minimum temperature [°C]"],
    augmented_data_minus["Maximum temperature [°C]"],
    color='green', label="-1", marker='v', s=500
)

# Plot the prediction lines
#plt.plot(min_temp_range, predicted_max_temp_dt, color='red', label="dec. tree", linewidth=6)
plt.plot(min_temp_range, predicted_max_temp_poly, linestyle = "--",color='black', label=f"PolyReg", linewidth=6)

# Add axis labels, title, and legend
plt.xlabel("mintemp [°C]")
plt.ylabel("maxtemp [°C]")
plt.title("explainable PolyReg")
plt.legend(loc='upper left')
plt.savefig("dtpolyregexplainable.png", dpi=100)
plt.show()
""

