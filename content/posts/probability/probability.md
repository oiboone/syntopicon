---
# This is a YAML Header (1st line must not be blank, but must be preceeded by blank line)
#
title: Probability
author: Jeffrey A. Jalkio
date: 2018-03-08

bibliography: [support/MyLibrary.bib]
csl: support/ieee.csl
---
# Review of Probability

## Basics of probability

Using Boolean logic, we can determine the truth or falsehood of complex statements given the truth or falsehood of the simpler statements of which they are composed. For example A and B, A or B have known truth values if the truth values of of A and B are known. If we are uncertain of the truth of A and B, we have a more difficult problem. If we want to describe our level of certainty in a proposition with a single number, Cox showed that the only way we can do this while maintaining both internal consistency and consistency with Boolean logic is to use a representation that is equivalent to probability. Therefore, we will start by reviewing some key points from probability. 

If *A* represents an arbitrary statement, we represent the probability that *A* is true by *P(A)*. *P(A)* lies between 0 and 1, with 0 representing certainty that A is false and 1 representing a certainty that A is true. In many cases, our knowledge of one proposition affects our belief in the truth of a second proposition. We write *P(A|B)* to represent the probability of *A* given the knowledge that *B* is true. This is called the conditional probability of *A* given *B*. Note that in all these cases, P() is not a function but simply a notation for the probability of a statement.

In Boolean logic, symbols are often used to represent logical operations. Unfortunately, different fields use different symbols. In this document, we'll use the symbols common in logic. $A \wedge B$ represents A and B, $A \vee B$ represents A or B, and $\neg A$ represents not A.

$P(A \wedge B) = P(A|B)P(B) = P(B|A)P(A)$ gives the probability for conjunction, $P(A \vee B)= P(A) + P(B) - P(A \wedge B)$ gives the probability for disjunction and $P(\neg A)=1-P(A)$ gives the probability for negation.

Frequently, we are interested in the probability that a random variable (denoted by a capital letter) takes a particular numerical value, e.g. P(X=5) would denote the probability that a die comes up 5. This can also be written $P _ X (5)$.  For continuous variables we need to consider the probability density $p _X (y)$ and can only consider the probability that X lies in an interval.
$P(a < X \le b) = \int_ a ^b p_X (y) dy$. Notice that $P( a < X \le b )$ is the probability of the proposition that the random variable X lies between a and b.


## Expected values of variables

Given a random variable, X, that can take on values $x _ 1 ,...,x _ n$. The expected value of X is simply the weighted average of possible values of X weighted by their probabilities, $E  _  X \{ X \} = \sum  _  {i=1} ^{n} x  _  i P  _  X (x  _  i)$. Similarly the expected value of some quantity that depends on X, e.g. $f(x)$ is $E _  X \{f(X)\}=\sum _  {i=1} ^{n} f(x _  i) P _  X (x _  i)$. For continuous variables, this becomes $E _ X \{f(X)\}=\int _  {-\infty} ^{\infty} f(x _ i) p _ X (x) dx$. Note that we write $E _ X{}$ rather than $E{}$ to make it clear which random variable we are averaging over. In some situations we might have more than one random variable.

The expected value of the N'th power of a random variable is called the variable's N'th moment. The first moment, denoted $\mu$ is the only one commonly used. For higher moments, central moments are more commonly encountered. The N'th central moment, denoted $\mu _n$ is the expected value of $(X - \mu)^2$.
Two expected values show  up so frequently, we give them names. The mean $\bar{X}=E _ X\{X\}$ and the variance $var(X) = E _ X\{(X-\bar{X})^2\}$.

Mention moment generating function? Yes, it's relevant in the next section. Also point out similarity to F.T. of probability distribution. Instead, use characteristic function and second cumulant generating function (log of characteristic function) Mention hteir usefulness in proving results about combinations of distributions.

## Adding random variables

Consider a pair of dice. We'll call them $X$ and $Y$. The value of a single die can be an integer between 1 and 6 inclusive with equal probability. The probability that the sum of two dice will have a value $v$ is $P_{X+Y} (v) = \sum_{i=1} ^6 P_X (i) P_Y (v-i)$. This is a discrete convoluiton of the two probability distributions. Similarly a Convolution integral is used to find the probability distribution for the sum of two continuous random $p _  {x+y}(s)=\int _  {-\infty}^\infty p _  x (x')p _ y (s-x') dx'$

For a linear combination of random variables, the means and variances add linearly. I.e. if $Y=a _ 1 X _ 1 + a _ 2 X _ 2 + ... + a _ n X _ n$ then $\mu _ Y = a _ 1 \mu _ {X _ 1} + ... a _ n \mu _ {X _ n}$ and $\sigma _ Y^2 = a _ 1^2 \sigma _ {X _ 1}^2 + ... a _ n^2 \sigma _ {X _ n}^2$ This does not hold for higher moments, but there are linear combinations of moments called cumulants that do add for linear combinations of random variables.


If $Y=X _ 1 + X _ 2$ then 
$M _ Y (t) = M _ {X _ 1 + X _ 2} (t) = M _ {X _ 1} (t) M _ {X _ 2} (t)$

## Choosing a probability distribution appropriate to describe ignorance in a particular situation

Assigning probabilities or probability densities must be done in such a way as to accurately reflect the plausibility of various possible statements or variable values. In the case of N equally plausible alternatives, each should be assigned a probability 1/N. Similarly, if a variable is constrained to an interval of width, w, and nothing else is known about it, one should assign a probability density p(x)=1/w for values in the interval and a density of 0 outside the interval.

For more complex situations, we must take advantage of

### Maximum Entropy Distributions

1. Constrained to finite interval -> uniform
2. Positive and known mean -> exponential
3. Known mean and variance -> normal

