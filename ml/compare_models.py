
import pandas as pd
import joblib
import time

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import (
    RandomForestRegressor,
    ExtraTreesRegressor,
    GradientBoostingRegressor
)
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("dataset/cleaned_cars.csv")

# Separate features and target
X = df.drop("Price", axis=1)
y = df["Price"]

# Identify columns
categorical_cols = X.select_dtypes(include=["object", "str"]).columns.tolist()
numerical_cols = X.select_dtypes(include=["number"]).columns.tolist()

# Preprocessing
numerical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
])

preprocessor = ColumnTransformer(transformers=[
    ("num", numerical_transformer, numerical_cols),
    ("cat", categorical_transformer, categorical_cols)
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Models
models = {
    "Linear Regression": LinearRegression(),

    "Ridge Regression": Ridge(alpha=1.0),

    "Decision Tree": DecisionTreeRegressor(
        random_state=42
    ),

    "Random Forest": RandomForestRegressor(
        n_estimators=200,
        random_state=42,
        n_jobs=-1
    ),

    "Extra Trees": ExtraTreesRegressor(
        n_estimators=200,
        random_state=42,
        n_jobs=-1
    ),

    "Gradient Boosting": GradientBoostingRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=3,
        random_state=42
    )
}

results = []
trained_models = {}

# Train and evaluate each model
for name, regressor in models.items():

    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("regressor", regressor)
    ])

    start_time = time.time()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    training_time = time.time() - start_time

    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    r2 = r2_score(y_test, predictions)

    results.append({
        "Model": name,
        "MAE": round(mae, 3),
        "RMSE": round(rmse, 3),
        "R2 Score": round(r2, 3),
        "Training Time": round(training_time, 2)
    })

    trained_models[name] = model

    print(f"\n{name}")
    print("MAE:", round(mae, 3))
    print("RMSE:", round(rmse, 3))
    print("R2 Score:", round(r2, 3))
    print("Training Time:", round(training_time, 2), "seconds")

# Compare results
results_df = pd.DataFrame(results)
results_df = results_df.sort_values(by="RMSE")

print("\n========== MODEL COMPARISON ==========")
print(results_df.to_string(index=False))

# Select model with lowest RMSE
best_model_name = results_df.iloc[0]["Model"]
best_model = trained_models[best_model_name]

# Save best model
joblib.dump(best_model, "ml/car_price_model.pkl")

# Save comparison results
results_df.to_csv("ml/model_comparison.csv", index=False)

print("\nBest Model:", best_model_name)
print("Best model saved successfully!")
