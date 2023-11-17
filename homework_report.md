# Homework Report

**Team:**

- Diana Kapatsyn
- Yuliia Sandra
- Oleksandr Korniienko
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
| n_features | metric    | n_trees | num_neighbours | subsample_size | accuracy | time  |
|------------|-----------|---------|----------------|----------------|----------|-------|
| 30         | manhattan | 30      | 50             | 500            | 0.920    | 3.8571|
| 15         | manhattan | 10      | 50             | 500            | 0.946    | 3.8157|
| 5          | euclidian | 5       | 50             | 1000           | 0.967    | 4.1279|
| 15         | euclidian | 30      | 50             | 1000           | 0.999    | 6.8460|

#### Computation time
Computation time ranges from 3.6457 to 9.8337 seconds.

#### Machine characteristics
Google Colab free tier machine.

## Ukrainian Wikipedia recommendation system

### Tasks

- Convert text feature with TF-IDF to vector of features
- Grid search for parameters
- Grid search for number of features
- Calculate ground truth
- Choose metrics. Explain choice

### Results
#### Metrics for different sets of hyperparameters
Here are some of the best accuracies from *results_gridsearch_wikipedia.csv*:

| n_features | metric    | n_trees | num_neighbours | subsample_size | accuracy | time  |
|------------|-----------|---------|----------------|----------------|----------|-------|
| 15         | manhattan | 10      | 50             | 200            | 0.990    | 0.8994|
| 5          | euclidian | 5       | 50             | 200            | 0.995    | 1.1943|
| 15         | euclidian | 10      | 50             | 500            | 0.998    | 0.9103|
| 15         | euclidian | 30      | 50             | 1000           | 0.999    | 2.1558|
#### Computation time
Computation time ranges from 0.6298 to 2.691 seconds.

#### Machine characteristics
Google Colab free tier machine.

## Run Airbnb-trained model on Wikipedia data
### Observations
Running the best hyperparameters from the Barcelona dataset on the Wikipedia data yielded subefficient results.
While still having accuracy > 0.8, learning the native set of hyperparameters is superior.

#### Metrics for different sets of hyperparameters
| n_features | metric    | n_trees | num_neighbours | subsample_size | accuracy | time  |
|------------|-----------|---------|----------------|----------------|----------|-------|
| 30         | manhattan | 30      | 50             | 500            | 0.966    | 1.2503|
| 15         | manhattan | 10      | 50             | 500            | 0.872    | 1.4998|
| 5          | euclidian | 5       | 50             | 1000           | 0.803    | 2.0977|
| 15         | euclidian | 30      | 50             | 1000           | 0.999    | 2.1558|

#### Comparison with native data learning
There are some notable differences between native hyperparameters. 
* Native hyperparameter models tend to lower computation time with mean computation time ≈1.29 (versus 1.7509 with borrowed hyperparameters).
* Native hyperparameter models have higher, near perfect, accuracies (versus 0.91 on borrowed sets)

#### Difference explanation
The difference in accuracy between tuning parameters on the Airbnb dataset and applying them to the Wikipedia
dataset can be attributed to the inherent variations in data distribution and characteristics between the two
domains.

The model could be overfitting to the peculiarities of the training dataset during parameter tuning, and when
applied to a different dataset like Wikipedia, it may not generalize well due to the dissimilarities in the
underlying data distribution.
