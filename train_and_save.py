import pickle
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassfier

wine = load_wine()

X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

cat_model = CatBoostClassfier(iterations=100, depth=4, learning_rate=0.05, verbose=0, random_state=42)
cat_model.fit(X_train, y_train)

model_package = {
    "model": cat_model,
    "feature_names": wine.feature_names,
    "target_names": wine.target_names
}

filename = "catboost_wine_model.pkl"
with open(filename, "wb") as file:
    pickle.dump(model_package, file)

print(f"Model successfully trained and saved as {filename}")