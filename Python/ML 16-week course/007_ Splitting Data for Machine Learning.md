# Day 7 
How Do We Split Data for Machine Learning ?

Before training the model , we need to divide the data into different groups . But here's the important question :

**Can we just randomly divide the data?**

Sometimes yes. Sometimes **absolutely not.**

The way we split data depends on the type of data and the problem we’re solving. Today, let’s understand the most common approaches:

- Random Split

- Stratified Split

- Time-Based Split

- Group-Based Split

- Training, Validation & Test Split

1. **Random Split**

The simplest approach is to randomly distribute data into different sets. Suppose we have 100 customer records. We might randomly split them:

80 records → Training

10 records → Validation

10 records → Test

Each customer has a random chance of ending up in any pile.

This works well when your data is:

Large enough

Randomly collected

Not dependent on time

Fairly balanced

For example:

Predicting clothes on features based on size , material , art , brand .

Randomly splitting the clothes can work well.
 


**But Random Splitting Has a Problem **

Imagine you’re building a model to detect a rare disease. Out of 10,000 patients:

9,900 → Don’t have the disease

100 → Have the disease

Only 1% of the data belongs to the positive class.

Now imagine we randomly split the data.

By chance, one of the smaller datasets might contain very few or even no positive examples. That creates a problem. The training and test datasets may no longer represent the real distribution properly.

This is where Stratified Splitting helps.


2.**Stratified Split** 
