import streamlit as st
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Streamlit UI
st.title("k-Nearest Neighbors (KNN) vLab Simulation")
st.sidebar.image("https://vlabcomp.kjsieit.in/uploads/Somaiya1.png", caption="Computer Department-2024", use_column_width=True)
st.sidebar.header("Simulation Settings")

# User input: Choose the value of k
k = st.sidebar.slider("Select the value of k", 1, 15, 3)

# User input: Upload a custom dataset (CSV file)
custom_dataset = st.sidebar.file_uploader("Upload a custom dataset (CSV)", type=["csv"])

if custom_dataset is not None:
    # Use the custom dataset if provided
    df = pd.read_csv(custom_dataset)
    
    # Identify the columns with string values
    string_columns = df.select_dtypes(include=['object'])

    # Apply label encoding to string columns
    label_encoder = LabelEncoder()

    for col in string_columns:
        df[col] = label_encoder.fit_transform(df[col])

    # Save the preprocessed dataset
    # df.to_csv('preprocessed_dataset.csv', index=False)

    # Assuming the last column contains the target class
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
    
    st.write("Using custom dataset:")
    st.write(df)
    
    # Analyze the number of features in the dataset
    num_features = X.shape[1]
else:
    # Use the default Iris dataset if no custom dataset provided
    from sklearn import datasets
    iris = datasets.load_iris()
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_df['Class'] = iris.target
    X = iris.data
    y = iris.target
    st.write("Using default Iris dataset:")
    st.write(iris_df)
    num_features = X.shape[1]

# Reduce the number of features to 2 using PCA if needed
if num_features > 2:
    pca = PCA(n_components=2)
    X = pca.fit_transform(X)

# Create a KNN classifier
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)

# Display a scatter plot of the data with colors based on classes
st.header("Dataset (2D Projection)")
st.write("Scatter plot of the dataset:")

# Group the data by class for different colors
fig, ax = plt.subplots()
for class_label in np.unique(y):
    data = X[y == class_label]
    ax.scatter(data[:, 0], data[:, 1], label=f"Class {class_label}")

ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")
ax.legend(title="Classes")

# User input: Add a new point
st.sidebar.header("Add a New Point")
new_x = st.sidebar.number_input("Enter X-coordinate", min_value=np.min(X[:, 0]), max_value=np.max(X[:, 0]))
new_y = st.sidebar.number_input("Enter Y-coordinate", min_value=np.min(X[:, 1]), max_value=np.max(X[:, 1]))

# Predict the class of the new point
new_point = np.array([[new_x, new_y]])
predicted_class = knn.predict(new_point)[0]

# Plot the new point with the predicted class color
colors = ["blue", "orange", "green"]  # Assume classes 0, 1, and 2 correspond to blue, green, and red
ax.scatter(new_x, new_y, marker='o', color=colors[predicted_class], label=f"New Point (Class {predicted_class})")

# Annotate the new point with its predicted class
ax.annotate(f"Class {predicted_class}", (new_x, new_y), textcoords="offset points", xytext=(5, 5), ha='center')

# Calculate and display the accuracy of the KNN model
accuracy = knn.score(X, y)
st.subheader(f"Accuracy for k = {k}: {accuracy * 100:.2f}%")

st.pyplot(fig)

# footer
st.markdown(
    """
    ***
    <div class="footer" style='text-align:center; color:#9b2928;font-weight: bold;'>
    Department Of Computer Engineering\n
    <b>Guided by: Prof.Kavita Bathe\n
    Developed by: Arvind Patel, Dev Shah, Avisha Shah</b>
    </div>
    """,
    unsafe_allow_html=True
)
