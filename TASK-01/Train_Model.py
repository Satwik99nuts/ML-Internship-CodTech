from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()

# Convert to DataFrame for better visualization
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target
