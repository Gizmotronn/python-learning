https://www.coursera.org/learn/machine-learning/lecture/Ujm7v/what-is-machine-learning

## Modern Definition of Machine Learning

A computer program is said to *learn* from experience *E* with respect to a task *T* and some performance measure *P*. For it to be ML, the performance on the task, as measured by P, improves with experience.

### Example of ML parts

Gmail Spam Filter:

* The computer program/software improves over time with marking things as spam. At the start, it may make mistakes, for example putting the wrong thing in the spam folder or not marking spam messages as spam. 
* At the start (well actually throughout the lifetime, but this is more important at the start) of your account, the program will watch what emails you mark as spam, and learn from this. For example, if you mark an email from a real person as spam multiple times, Gmail will learn that although it is a legitimate email address, you don't want it in your inbox. This is the experience part of Gmail.
* The task is classifying emails as spam/not spam
* The number of emails correctly classified is the performance measure



## Machine Learning Algorithms

**Supervised Learning**

We teach the computer how to do something

**Unsupervised Learning**

We let it learn by itself



### Supervised Learning

* Right answers given - data set with examples with values
* Task - Produce more right answers based on the data sets given
* AKA Regression problem - 
  * Predict continuous valued output

In **machine learning** and statistics, **classification** is the **problem** of identifying to which of a set of categories (sub-populations) a new observation belongs, on the basis of a training set of data containing observations (or instances) whose category membership is known.

**Regression** prediction **problems** are usually quantities or sizes. For example, when provided with a dataset about houses, and you are asked to predict their prices, that is a **regression** task because price will be a continuous output.