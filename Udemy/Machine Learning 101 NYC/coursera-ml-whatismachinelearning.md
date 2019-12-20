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



### Unsupervised Learning

* Same labels for data set
* Not told what to do with it
* UL algorithms can create clusters of data - clustering algorithms

Google News is an example of clustering algorithms:

* Searches the internet and clusters thousands of stories into cohesive news articles
* There are multiple different links (for example, news.com.au, news.abc.net.au); however if they are about the same story, they will be classed under the same header (or clustered)

Google News example:

![image-20191220084700137](C:\Users\arbuc\AppData\Roaming\Typora\typora-user-images\image-20191220084700137.png)

* We aren't telling the algorithm in advance that these news articles are part of the same category; this is why it is unsupervised learning

**Model Representation**

Key:

* x^(i) refers the "input variables"/input features
* y^(i) refers to the output, or target variable that we are trying to predict
* A pair (x,y) refers to a **training example**
* m refers to a list of training examples - training set
* The subscript (i) is only used for notation - does not refer to exponentials

The supervised learning problem:

* The goal is - given a training set - to learn a function h:X-->Y so that h(x) is a good predictor for the corresponding value of y
* The function h is referred to as a hypothesis:

![img](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/H6qTdZmYEeaagxL7xdFKxA_2f0f671110e8f7446bb2b5b2f75a8874_Screenshot-2016-10-23-20.14.58.png?expiry=1576972800000&hmac=SWnrvXOkdYbrt3vzwguvVRiRlLRa9lUtkfshuqCYkFw)

When the target variable that we’re trying to predict is continuous, such as in our housing example, we call the learning problem a regression problem. When y can take on only a small number of discrete values (such as if, given the living area, we wanted to predict if a dwelling is a house or an apartment, say), we call it a classification problem.



## Cost Function

* Hypothesis: h(theta)(x) = (theta.0) + (theta.1)x
* Theta.i - Parameters

Example:

* Theta 1 = 1.5
* Theta 2 = 0:
* ![image-20191220172958013](C:\Users\arbuc\AppData\Roaming\Typora\typora-user-images\image-20191220172958013.png)

* ![image-20191220173026729](C:\Users\arbuc\AppData\Roaming\Typora\typora-user-images\image-20191220173026729.png)



Linear regression:

![image-20191220173225174](C:\Users\arbuc\AppData\Roaming\Typora\typora-user-images\image-20191220173225174.png)

Choose the values of theta so that h(x) is as close to y for our training examples (x,y) as possible (see blue line going through the data set/training examples)

Equation for this: ![image-20191220173753721](C:\Users\arbuc\AppData\Roaming\Typora\typora-user-images\image-20191220173753721.png)

![image-20191220173934902](C:\Users\arbuc\AppData\Roaming\Typora\typora-user-images\image-20191220173934902.png)