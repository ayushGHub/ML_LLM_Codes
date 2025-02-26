Clarifying Questions:
1. What's the current process look like:
    -  How does amazon currently calculate CLV of their shoppers?
    -  What's the average lifespan of a customer of Amazon?
    -  What's Amazon's profit percentage from a single sale?

👉 “Great questions to start off. The only thing I would advise is that I would generally avoid questions that the interviewer would presume that you would already know. This is to demonstrate expertise from the gecko. For instance, if you are a practitioner in the field, or you’ve already done some research, you would anticipate that CLV is calculated based on some fixed horizon, let’s say 1, month, 3 months, 6 months, 12 months. I would provide some info up front then confirm with the interviewer.”

2. What's the business objective:
    -  Is the goal to improve CLV considering the latter half of the prompt?
3. Data sources:
    -Customer-specific data: (number of purchases, whether they were a prime member (month-to-month vs annual), total spent,, time duration, address (including city and country)

👉 “Great list of signals!”

Fleshing out the ML Pipeline:
1) EDA: 
   - Observe distributions of the features
   - Correlation analysis between Xs and Y using something like Pearson's correlation 
2) Data Pre-processing
   - Handle missing values: 1) If they account for +50% of data remove feature. 2) Build a classifier and use that feature as your target variable 3) You can use clustering
   - Encode categorical features: 1) If that feature has few categories then you can do one-hot/dummy encoding. 2) If high amount of categories you can do numerical target encoding
   - Normalize data (no need to if using decision tree based model like Random Forest
3) Feature Engineering
   - If we had more detailed purchase history with timestamps we can break it do some time decomposition: month - day - hour - minute - second
   - Can't think of anything else
4) Feature Selection
   - To avoid curse of dimensionality we can try PCA, Random Forest variable Importance or L1 Regression

👉 “Agreed, but remember interpretation matters for the latter case. So, I’d stick to L1 Regression or RF.”

5) Model Selection
   - Since we are predicting continuous, real-value we will be doing Regression
   - Random Forest Regressor comes to mind or XGBoost Regressor given their robust reputation
   - Hyperparameter tuning: (depth of trees, number of trees, min number of sample per leaf, pruning, learning rate in 

👉 “+1”

case of XGBoost)
6) Model Evaluation
   - MSE and possibly try MAE since it is less sensitive to outliers and we don't want our model necessarily to sensitive to them
   - K-fold cross validation to make sure our model generalizes well

👉 “+1”

7) Productionalize
  - Not too experienced here other than using a REST API using one of the cloud service providers like AWS, Azure or even something like Databricks which I know has that functionality

👉 “Depending on the level of depth the interviewer expects, follow-up questions may vary. But, generally the framework works like this - you need to build an ETL, establish a Cron job (not sure what Amazon readily uses, but you could use Airflow), wrap your model in a REST API that includes preprocessing, training and prediction. The result should be stored in DBs for prediction, monitoring and so and so”
