import os
import pandas as pd

# Define paths to the dataset
train_dir = "aclImdb/train"
test_dir = "aclImdb/test"

# Function to load data from positive and negative folders
def load_data_from_folder(folder_path):
    data = []
    labels = []
    for label_type in ["pos", "neg"]:
        label_dir = os.path.join(folder_path, label_type)
        for filename in os.listdir(label_dir):
            if filename.endswith(".txt"):
                # Read review text
                with open(os.path.join(label_dir, filename), encoding="utf-8") as f:
                    data.append(f.read())
                # Assign label (1 for positive, 0 for negative)
                labels.append(1 if label_type == "pos" else 0)
    return pd.DataFrame({"review": data, "label": labels})

# Load training and testing data
train_data = load_data_from_folder(train_dir)
test_data = load_data_from_folder(test_dir)

# Show the first few rows of the training data
print(train_data.head())

# Optional: Save data to CSV for later use
train_data.to_csv("imdb_train.csv", index=False)
test_data.to_csv("imdb_test.csv", index=False)
