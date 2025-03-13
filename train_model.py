import pandas as pd
import zipfile
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Path to ZIP file
zip_path = r"C:\Users\anils\OneDrive\Desktop\MY\Student Performance Dataset.zip"
extract_dir = "extracted"

# Extract ZIP
if not os.path.exists(extract_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
        print("✅ Dataset extracted!")

# Locate CSV
csv_file = None
for file in os.listdir(extract_dir):
    if file.endswith(".csv"):
        csv_file = os.path.join(extract_dir, file)
        break

if csv_file is None:
    raise FileNotFoundError("❌ No CSV file found!")

# Load CSV
df = pd.read_csv(csv_file)
print("✅ Columns in dataset:", df.columns.tolist())

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convert relevant columns to numeric after stripping whitespace
for col in ['math_score', 'reading_score', 'writing_score', 'total_score']:
    df[col] = df[col].astype(str).str.strip().str.replace(r'\t', '', regex=True)
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop any rows with missing or non-numeric values
df = df.dropna(subset=['math_score', 'reading_score', 'writing_score', 'total_score'])

# Define features and target
features = ['math_score', 'reading_score', 'writing_score']
target = 'total_score'

# Prepare data
X = df[features]
y = df[target]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained successfully and saved as model.pkl")






