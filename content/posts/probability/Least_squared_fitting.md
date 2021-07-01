---
title: An Introduction to Maximum Liklihood Estimation
slug: Least Squares
date: 2018-06-09
modified: 2018-06-09

---

# Overview

We'll first review the simple straight line fitting you're already familiar with. Then we'll look at why it works and how it can be extended to fit arbitrary functions with constraints on teh parameters.

# Linear Least Squared Error Fitting

## Fitting a Straight Line to Data

At some point in your education, you've learned about fitting a straight line to a data set. We'll start with this case you've already seen and then look at extensions.

Assume that you've collected a set of *m* data points $(\tilde{x}_i, \tilde{y}_i)$ You believe that the *y* measurements are corrupted by additive noise, while the *x* values are essentially noise free and you wish to find the line 

$y_ i = a_ 0 + a_ 1 \cdot x_ i$

Minimize $S = \sum_ {i=1} ^m (\tilde{y}_ i - y_ i)^2$

To simplify the notation, we'll assume the summations are from *1* to *m* and drop the subscripts from *x* and *y*. Substituting and expanding, we have $S= \sum \tilde{y}^2 - 2a_ 0 \sum \tilde{y} + a_ 0^2 + 2a_ 0 a_ 1 \sum x -2 a_ 1 \sum x \tilde{y} + a_ 1 ^2 \sum x^2$

Recall that at local extrema, the partial derivatives of a function go to zero, so to find the values of $a_ 0$ and $a_ 1$ that minimize *S* we take the partial derivatives of $S$ with respect to those variables and set them equal to zero. Note that by itself this doesn't guarantee that the extremum we find will be a minimum, but we'll see later that it is.

Taking the partials and setting them equal to zero, we get the two equations

${{\partial S} \over {\partial a_ 0}} = 
-2 \sum \tilde{y} + 2 a_ 0 + 2 a_ 1 \sum x = 0$

and

${{\partial S} \over {\partial a_1}} = 
2 a_0 \sum x -2 \sum x \tilde{y} + 2 a_ 1 \sum x^2 = 0$

Writing this as a matrix equation, we have

$\begin{bmatrix} 1 & \sum x \\ \sum x & \sum x^2 \end{bmatrix} \begin{pmatrix} a_ 0 \\ a_ 1 \end{pmatrix} = \begin{pmatrix} \sum \tilde{y} \\ \sum x \tilde{y} \end{pmatrix}$

Since $\sum x^2 \ge (\sum x)^2$ the matrix of coefficients is not singular and the system of equations has a unique solution. Since *S* cannot be negative, and can get arbitrarily large for large values of the *a*s, we know the extremum we find by solving this matrix equaiton is the global minimum for S.

## Linear Least Squared Error Fits to non-linear functions

Notice that we were able to solve our system of equations because they were linear in the parameters *a*. What if instead of a straight line, our model is given by

$y_ i = \sum_ {j=1} ^n a_ j f_ j (x_ i)$

Our new *S* is given by

$S = \sum_ {i=1} ^m (\tilde{y}_ i - (\sum_ {j=1} ^n a_ j f_ j (x_ i)))^2$

Let's take the partial derivative of our new *S* with respect to one of the parameters $a_ k$.

$\begin{array}{ll}
{{\partial s} \over {\partial a_ k}} & = 
  \sum_ {i=1} ^m  \left( 2 \left(\tilde{y}_ i - \left(\sum_ {j=1} ^n a_ j f_ j (x_ i)\right)\right)(-1) f_ k (x_ i)\right) \\
& = -2 \sum (\tilde{y} f_ k (x)) + 2  \left( 
	    \sum_ {j=1} ^n a_ j \sum   \left( f_ j (x) f_ k (x)   \right)   \right) \\
& = 0 
\end{array}$

Writing this as a matrix equation, we have 

$M a = d$

where 

$M_ {jk} = \sum \left(f_ j (x) f_ k (x) \right)$

and 

$d_ k = \sum \left(\tilde{y} f_ k (x)\right)$

Once again, we can solve this system of linear equations to find values of the parameters *a* that minimize *S*.

It should be clear that nothing in our analysis limits the functions *f* to being functions of a single independent variable. We could use the same approach to fit data points to a surface or some more complicated multivariable function.

# Uncertainties and Why Least Squares Fitting Works

## From Optimal Estimation to Least Squares

Let's say we're trying to estimate some unknown vector of parameters, *a*. Ideally, we have some way of quantifying the quality of our estimate. A common way of doing this is to specify a loss function that tells us the cost of being wrong.The loss function $\mathscr{L}(\hat{a},a)$ gives us the cost of choosing the estimate $\hat{a}$ when the actual values are $a$). Ideally we would choose an estimate that minimizes the expected value of the loss function given any information we have about the actual paramtersThere must In estimating an unknown parameter, *a* we would ideally minimize the expected value of some loss function

$\hat{a} = \underset{\hat{a}}{\operatorname{argmin}} \left( \int \mathscr{L} (\hat{a},a)p(a|x)da \right)$

a\
a\
a\
that's all folks...

