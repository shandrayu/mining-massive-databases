# Homework Report

**Team:**

- Diana Kapatsyn
- Yuliia Sandra
- Oleksandr Shevchenko
- Nazariy Vysokinskyi

## Barcelona dataset recommendation system

### Goal
Recommend similar apartments (items) based on input query (apartment description).

### Tasks

- Convert text feature with TF-IDF to vector of features
- Grid search for parameters
- Grid search for number of features
- Calculate ground truth
- Choose metrics. Explain choice

### Results
#### Metrics for different sets of hyperparameters
| num_features | bucket_lenght | num_hash_tables | num_neighbours | F1-score    |
|--------------|---------------|-----------------|----------------|----------|
| 20           | 2.0           | 1               | 5              | 0.006398 |
| 20           | 2.0           | 1               | 15             | 0.004784 |
| 20           | 2.0           | 1               | 50             | 0.009361 |
| 20           | 2.0           | 1               | 100            | 0.009900 |
| 30           | 2.0           | 1               | 5              | 0.017937 |
| 30           | 2.0           | 1               | 15             | 0.007176 |
| 30           | 2.0           | 1               | 50             | 0.009225 |
| 30           | 2.0           | 1               | 100            | 0.009005 |

#### Computation time

#### Machine characteristics

## Ukrainian Wikipedia recommendation system

### Tasks

- Convert text feature with TF-IDF to vector of features
- Grid search for parameters
- Grid search for number of features
- Calculate ground truth
- Choose metrics. Explain choice

### Results
#### Metrics for different sets of hyperparameters
#### Computation time
#### Machine characteristics

## Run Airbnb-trained model on Wikipedia data
### Observations
#### Metrics for different sets of hyperparameters
#### Comparison with native data learning
#### Difference explanation
