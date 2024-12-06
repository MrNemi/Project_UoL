import cv2
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, f1_score, confusion_matrix, roc_curve, auc, classification_report
)
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# Declare path for recorded video data
video_path = "C:\\Users\\manny\\Downloads\\data"

# Step 1: Extract Features from Video
def extract_features(video_path):
    """
    Extract features from a video for binary classification.
    Features include mean and variance of frame differences.
    """
    cap = cv2.VideoCapture(video_path)
    prev_frame = None
    motion_features = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if prev_frame is not None:
            # Compute absolute difference between consecutive frames
            diff = cv2.absdiff(prev_frame, gray_frame)
            motion_features.append(np.sum(diff))

        prev_frame = gray_frame

    cap.release()

    # Summarize features: mean and variance of motion
    motion_features = np.array(motion_features)
    if motion_features.size > 0:
        return np.mean(motion_features), np.var(motion_features)
    else:
        return 0, 0

# Step 2: Load Data and Extract Features
def load_vid_data(data_folder):
    """
    Load video data, extract features, and prepare labels for classification.
    """
    features = []
    labels = []

    for label_folder in ['viscous', 'non_viscous']:
        folder_path = os.path.join(data_folder, label_folder)
        label = 1 if label_folder == 'viscous' else 0
        for video_file in os.listdir(folder_path):
            video_path = os.path.join(folder_path, video_file)
            feature = extract_features(video_path)
            features.append(feature)
            labels.append(label)

    return np.array(features), np.array(labels)

# Step 3: Train Model with Hyperparameter Tuning
def train_with_tuning(X_train, y_train):
    """
    Train a binary classifier with hyperparameter tuning using GridSearchCV.
    """
    model = RandomForestClassifier(random_state=42)
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5, 10]
    }
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='f1', verbose=2)
    grid_search.fit(X_train, y_train)

    print(f"Best Parameters: {grid_search.best_params_}")
    return grid_search.best_estimator_

# Step 4: Model Evaluation
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model using various metrics.
    """
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]

    # Accuracy and F1 Score
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    print(f"F1 Score: {f1:.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # Confusion Matrix
    conf_matrix = confusion_matrix(y_test, y_pred)
    plt.figure(1, figsize=(6, 4))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")

    # ROC Curve
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
    roc_auc = auc(fpr, tpr)
    plt.figure(2, figsize=(6, 4))
    plt.plot(fpr, tpr, color='blue', label=f'ROC Curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
    plt.title("ROC Curve")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend()

    # Show all figures
    plt.show()

# Main Workflow
if __name__ == "__main__":
    # Step 1: Load and preprocess video data
    # Folder structure: data/viscous/*.avi, data/non_viscous/*.avi
    data_folder = "data"
    features, labels = load_vid_data(data_folder)

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.8, random_state=42)

    # Step 2: Train the model with hyperparameter tuning
    best_model = train_with_tuning(X_train, y_train)

    # Step 3: Evaluate the model
    evaluate_model(best_model, X_test, y_test)
