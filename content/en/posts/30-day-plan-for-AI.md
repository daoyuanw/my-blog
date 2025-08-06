---
title: "30-Day AI Study Plan for Beginners"
date: 2025-08-06T08:55:40+08:00
author: "Daoyuan"
slug:
draft: false
toc: false
---
This plan is designed for a zero-foundation learner to build a basic understanding of Artificial Intelligence (AI) in 30 days. It covers foundational math, Python programming, machine learning, and introductory AI concepts through theory, practice, and projects. 

---

## Week 1: Foundations of Math and Programming
**Goal**: Learn basic math (linear algebra, statistics) and Python programming, which are essential for AI.

### Day 1-2: Introduction to AI and Math Basics
- **Objective**: Understand what AI is and learn basic math concepts.
- **Topics**:
  - Overview of AI, machine learning (ML), and deep learning (DL).
  - Basic linear algebra: vectors, matrices, and operations (addition, multiplication).
- **Tasks**:
  - [What is Artificial Intelligence?](https://www.youtube.com/watch?v=uMzUB89uSxU).
  - [Essence of linear algebra](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
  - [Khan Academy: Linear Algebra](https://www.khanacademy.org/math/linear-algebra)(focus on vectors and matrices).

### Day 3-4: Statistics and Probability Basics
- **Objective**: Learn core statistics and probability for AI.
- **Topics**:
  - Mean, median, variance, standard deviation.
  - Probability basics: events, probability distributions (normal, binomial).
- **Tasks**:
  - [CrashCourse Statistics](https://thecrashcourse.com/topic/statistics/) (Episodes 1-3).
  - [StatQuest’s "Statistics Fundamentals"](https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9) 

### Day 5-7: Python Programming Basics
- **Objective**: Learn Python, the primary language for AI development.
- **Topics**:
  - Variables, data types, loops, conditionals, functions.
  - Python libraries: NumPy (for arrays), Pandas (for data handling).
- **Tasks**:
  - Install Python and Jupyter Notebook (via Anaconda).
  - [AI python for Beginners by Andrew Ng](https://learn.deeplearning.ai/courses/ai-python-for-beginners/lesson/z57gn/introduction)
  - [NumPy Quickstart](numpy.org/doc/stable/user/quickstart.html.)

---

## Week 2: Introduction to Machine Learning
**Goal**: Understand machine learning concepts and start applying them in Python.

### Day 8-10: Machine Learning Fundamentals
- **Objective**: Learn core ML concepts and algorithms.
- **Topics**:
  - Supervised vs. unsupervised learning.
  - Linear regression, classification, overfitting, underfitting.
- **Tasks**:
  - Watch: Andrew Ng’s Coursera ML course (Week 1, free audit, ~2 hours).
  - Read: “An Introduction to Machine Learning” by Scikit-learn (scikit-learn.org, ~1 hour).
  - Practice: Implement linear regression in Python using Scikit-learn on a small dataset (e.g., predict house prices).
- **Resources**:
  - Coursera: Andrew Ng’s Machine Learning (audit free).
  - Scikit-learn: scikit-learn.org/stable/getting_started.html.

### Day 11-13: Data Preprocessing and Model Evaluation
- **Objective**: Learn how to prepare data and evaluate ML models.
- **Topics**:
  - Data cleaning, normalization, splitting (train/test).
  - Metrics: accuracy, mean squared error, confusion matrix.
- **Tasks**:
  - Watch: StatQuest’s “Data Preprocessing” (YouTube, ~20 mins).
  - Practice: Use Pandas to clean a dataset (e.g., remove missing values) and split it into train/test sets.
  - Experiment: Train a logistic regression model on a simple dataset (e.g., Iris dataset) and compute accuracy.
- **Resources**:
  - Kaggle: Iris dataset (kaggle.com/datasets/uciml/iris).
  - StatQuest YouTube.

### Day 14: Mini Project - Linear Regression
- **Objective**: Apply Week 2 knowledge in a small project.
- **Task**:
  - Build a linear regression model to predict a numerical value (e.g., house prices or student grades) using a Kaggle dataset.
  - Steps: Load data with Pandas, preprocess (handle missing values, normalize), train model, evaluate using mean squared error.
  - Write a short summary (100 words) of your findings.
- **Resources**:
  - Kaggle: Search for “house prices” dataset.
  - Scikit-learn Linear Regression: scikit-learn.org/stable/modules/linear_model.html.

---

## Week 3: Intermediate Machine Learning and Tools
**Goal**: Explore more ML algorithms and tools for AI development.

### Day 15-17: Decision Trees and Ensemble Methods
- **Objective**: Learn tree-based algorithms and ensemble techniques.
- **Topics**:
  - Decision trees, random forests, gradient boosting.
  - Hyperparameter tuning (e.g., max depth, number of trees).
- **Tasks**:
  - Watch: StatQuest’s “Decision Trees” and “Random Forests” (YouTube, ~40 mins).
  - Practice: Implement a decision tree classifier on a classification dataset (e.g., Titanic dataset).
  - Experiment: Compare random forest vs. decision tree performance.
- **Resources**:
  - Kaggle: Titanic dataset (kaggle.com/competitions/titanic).
  - StatQuest YouTube.

### Day 18-20: Introduction to Deep Learning
- **Objective**: Understand neural networks and deep learning basics.
- **Topics**:
  - Neural networks, activation functions, backpropagation.
  - Introduction to TensorFlow/Keras.
- **Tasks**:
  - Watch: 3Blue1Brown’s “Neural Networks” (YouTube, ~20 mins).
  - Read: TensorFlow’s “Basic Classification” tutorial (~1 hour).
  - Practice: Build a simple neural network in Keras to classify a dataset (e.g., MNIST digits).
- **Resources**:
  - 3Blue1Brown YouTube.
  - TensorFlow: tensorflow.org/tutorials/keras/classification.

### Day 21: Mini Project - Classification Model
- **Objective**: Build and evaluate a classification model.
- **Task**:
  - Use the Titanic dataset to predict passenger survival using a random forest or neural network.
  - Steps: Preprocess data, train model, evaluate using accuracy and confusion matrix, tune one hyperparameter (e.g., max depth).
  - Write a 100-word summary of results.
- **Resources**:
  - Kaggle: Titanic dataset.

---

## Week 4: Advanced Topics and Capstone Project
**Goal**: Explore advanced AI concepts and complete a capstone project.

### Day 22-24: Natural Language Processing (NLP) Basics
- **Objective**: Learn NLP and its applications.
- **Topics**:
  - Text preprocessing, tokenization, word embeddings.
  - Simple NLP models (e.g., sentiment analysis).
- **Tasks**:
  - Watch: “NLP Introduction” by freeCodeCamp (YouTube, ~30 mins).
  - Practice: Use NLTK or SpaCy to preprocess text (e.g., tokenize, remove stop words).
  - Experiment: Build a sentiment analysis model using a dataset (e.g., IMDB reviews).
- **Resources**:
  - NLTK: nltk.org.
  - Kaggle: IMDB dataset (kaggle.com/datasets/lakshmi25n/imdb-dataset-of-50k-movie-reviews).

### Day 25-27: Computer Vision Basics
- **Objective**: Understand computer vision and convolutional neural networks (CNNs).
- **Topics**:
  - Image preprocessing, CNNs, transfer learning.
- **Tasks**:
  - Watch: “Convolutional Neural Networks” by DeepLearning.AI (YouTube, ~30 mins).
  - Practice: Use TensorFlow to build a CNN for image classification (e.g., CIFAR-10 dataset).
  - Experiment: Apply transfer learning with a pre-trained model (e.g., MobileNet).
- **Resources**:
  - TensorFlow: tensorflow.org/tutorials/images/cnn.
  - Kaggle: CIFAR-10 dataset.

### Day 28-30: Capstone Project - AI Application
- **Objective**: Build a complete AI project combining learned skills.
- **Task**:
  - Choose one:
    1. **Sentiment Analysis**: Build a model to classify movie reviews as positive/negative.
    2. **Image Classification**: Create a model to classify images (e.g., cats vs. dogs).
    3. **Predictive Model**: Predict numerical values (e.g., house prices) with regression.
  - Steps:
    - Collect data (use Kaggle datasets).
    - Preprocess data (clean, normalize, split).
    - Train and evaluate a model (e.g., random forest, neural network).
    - Present results in a 200-word report and visualize performance (e.g., plot accuracy or loss).
- **Resources**:
  - Kaggle: Search for relevant datasets (e.g., “cats and dogs”, “house prices”).
  - Matplotlib: matplotlib.org for visualization.

---

## Tips for Success
- **Daily Routine**: Spend 1 hour on theory (videos/readings), 1 hour on practice (coding/exercises), and 30 mins reviewing or summarizing.
- **Tools**: Use Jupyter Notebook for Python coding. Install libraries via pip (e.g., `pip install numpy pandas scikit-learn tensorflow`).
- **Community**: Join Kaggle or Reddit’s r/learnmachinelearning for support.
- **Track Progress**: Keep a notebook to summarize daily learnings and code snippets.
- **Next Steps**: After 30 days, explore advanced topics (e.g., reinforcement learning, GANs) or take a full course like Andrew Ng’s Deep Learning Specialization.
