import pandas as pd
import json
import scipy
import scipy.stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load data from JSON file
with open("your_data.json", "r") as file:
    data = json.load(file)

# Convert JSON data to pandas DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Prepare features and labels
X = df["Question"]
y = df["Answer"]

# Encode available answer options for dropdown questions
X_encoded = pd.get_dummies(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Save trained model
joblib.dump(model, "question_answering_model.joblib")

# Load trained model
model = joblib.load("question_answering_model.joblib")

# Input new question
new_question = "Are you age 18 or over?"

# Predict answer for new question
predicted_answer = model.predict([new_question])
print("Predicted answer:", predicted_answer)

