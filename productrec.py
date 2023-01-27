from sklearn.neighbors import NearestNeighbors
import pandas as pd

# Load the data into a pandas DataFrame
data = pd.read_csv("product_data.csv")

# Define the features to be used for recommendation
features = ['product_name', 'price', 'rating', 'category']

# Create a NearestNeighbors model
model = NearestNeighbors(n_neighbors=5, algorithm='brute', metric='cosine')

# Fit the model to the data
model.fit(data[features])

# Define a function to recommend products
def recommend_products(product_name):
    # Find the index of the product in the data
    product_index = data[data.product_name == product_name].index.values[0]
    
    # Find the 5 most similar products
    distances, indices = model.kneighbors(data.iloc[product_index, :].values.reshape(1, -1), n_neighbors=5)
    
    # Print the recommended products
    for i in indices.flatten():
        print(data.iloc[i]['product_name'])
