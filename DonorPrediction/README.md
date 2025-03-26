# DonorPrediction: Predicting Future Donations Using Machine Learning

## Overview
The **DonorPrediction** project aims to analyze donor behavior and predict whether a donor will make a future donation. By leveraging machine learning techniques, we can understand donation patterns and help organizations personalize outreach to their community. This project focuses on predicting donor behavior based on features like **Donation Frequency, Amount, Recency**, and clustering donor data to uncover hidden patterns.

## Problem Statement
Our goal is to predict whether a donor is likely to donate again, based on past donation behaviors. By identifying patterns in the data, we can tailor strategies to encourage recurring donations. Key features used include:

- **Donation Frequency**: How often a donor gives.
- **Donation Amount**: The average size of their donation.
- **Recency**: How recent their last donation was.
- **Cluster Label**: Derived from K-Means clustering to group donors with similar donation patterns.

## Approach
1. **Data Preprocessing**:
   - Clean the dataset, handle missing values, and prepare features for analysis.
   
2. **Clustering**:
   - Applied K-Means clustering to group donors into similar behavior clusters (e.g., frequent donors, occasional donors).
   - The optimal number of clusters was determined using the Elbow Method.

3. **Feature Importance**:
   - Trained a **Random Forest Classifier** to predict whether a donor will donate again.
   - **Recency** was found to be the most important feature, strongly influencing whether a donor will donate again.

4. **Classification**:
   - A **Random Forest Classifier** was used to predict the binary outcome: **Will Donate Again**.
   - Model evaluation metrics such as **Accuracy, Precision, Recall, and F1-Score** were calculated to assess performance.

5. **Results**:
   - The classification model showed that recency is the most important predictor for future donations, meaning that donors who donate recently are more likely to donate again, regardless of the amount or frequency.

## Steps Taken
1. **Clustering**:
   - Used **K-Means** clustering to group donors based on donation behavior.
   
2. **Modeling**:
   - Built a **Random Forest Classifier** to predict future donations.
   - Evaluated the model's performance with various metrics.

3. **Feature Importance**:
   - Visualized feature importance and found that **Recency** is the most influential feature in predicting future donations.

## Requirements
- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/DonorFlow.git
   cd DonorFlow
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Open the Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

4. Run each cell step-by-step to recreate the project from data exploration to model training.

## Future Improvements
- **Model Optimization**: Further hyperparameter tuning to improve model accuracy.
- **Additional Features**: Incorporate other features such as donor engagement (e.g., event attendance) to improve prediction accuracy.
- **Model Deployment**: Implement the model in a production environment to make real-time predictions.

## Conclusion
This project demonstrates how to use machine learning to understand and predict donor behavior. The most valuable insight was that **Recency** is a strong indicator of whether a donor will give again. With this model, organizations can personalize outreach efforts to maximize the likelihood of securing future donations.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

