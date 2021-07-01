---
# This is a YAML Header (1st line must not be blank, but must be preceeded by blank line)
#
# parse with pandoc -s -S --filter pandoc-citeproc --toc --number-sections pandoc.md -o pandoc.tex
# for pandoc versions < 2
# or parse with pandoc -s --filter pandoc-citeproc --toc --number-sections pandoc.md -o pandoc.tex
# for pandoc version => 2
# Note that comments in YAML header don't appear in output files (even HTML)
#
title: Introduction to Measurement Uncertainty
author: Jeffrey A. Jalkio
date: 2018-03-08

bibliography: [support/MyLibrary.bib]
csl: support/ieee.csl
---
# Main text???

## An individual Direct Measurement

A measurement is a comparison to a standard unit. All measurements are ratios (i.e. only rational numbers needed not reals.)

We can use anything we want as a standard unit, but it should be stable, easy to compare to, and for communication purposes should be agreed upon. That's why we have metric convention, BIPM and units defined in terms of natural constants. This document does not cover details of SI, please refer to NIST's guide to SI

## Uncertainty

Individual measurements cannot provide perfect knowledge of physical quantities. We must find ways of expressing uncertainty. At the very least, we must specify the range of possible true values that are compatible with the measurement. Even better, we could consider how likely any possible value is based on our prior knowledge and all measurements we've made.

Cox [@cox1946] showed that probability or something essentially equivalent to it is the only way to extend Boolean logic to situations where we do not have certainty of truth or falsehood. So we will need to review probability.


## Summary

We briefly summarize our approach for three different cases:

### Direct single measurements

If we can directly measure the quantity of interest, but can't make more than one measurement, we must determine our faith in our measurement process based on our knowledge of our instruments and environment. In section 3 we will look at how this is done.

### Direct Repeated Measurement

If we can make multiple direct measurements, we can combine those measurements to reduce our uncertainty and use the variability of those measurements to calculate the repeatability of our measurements, one portion of our uncertainty. We also have a portion of uncertainty that must be calculated as above because our measurements may contain a constant unknown bias undetectable by repeated measurement. We must use our knowledge of the measurement process to bound such biases. Accuracy is a term sometimes used for the range of this unknown bias, and sometimes the term is used for a combination of repeatability and bias.

### Indirect Measurements

If the quantity we wish to determine cannot be measured directly, but must be calculated from some combination of known and measured quantities, we must consider how the uncertainties in these quantities propagates through to the result. We will consider several ways of doing this, depending on the complexity of the problem we're trying to solve.

In each of these three cases, after making the measurement and calculating the uncertainty, we must report the result. We will look at several ways to communicate the value and uncertainty of a measurement. Including consideration of significant figures in numerical values, meaning of uncertainty specified via $\pm$, correct use of SI units, and reporting of uncertainties in graphs.

## Review of Probability

### Basics of probability

Using Boolean logic, we can determine the truth or falsehood of complex statements given the truth or falsehood of the simpler statements of which they are composed. For example A and B, A or B have known truth values if the truth values of of A and B are known. If we are uncertain of the truth of A and B, we have a more difficult problem. If we want to describe our level of certainty in a proposition with a single number, Cox showed that the only way we can do this while maintaining both internal consistency and consistency with Boolean logic is to use a representation that is equivalent to probability. Therefore, we will start by reviewing some key points from probability.

If *A* represents an arbitrary statement, we represent the probability that *A* is true by *P(A)*. *P(A)* lies between 0 and 1, with 0 representing certainty that A is false and 1 representing a certainty that A is true. In many cases, our knowledge of one proposition affects our belief in the truth of a second proposition. We write *P(A|B)* to represent the probability of *A* given the knowledge that *B* is true. Note that in all these cases, P() is not a function but simply a notation for the probability of a statement.

In Boolean logic, symbols are often used to represent logical operations. Unfortunately, different fields use different symbols. In this document, we'll use the symbols common in logic $A \wedge B$ to represent A and B, $A \vee B$ to represent A or B, and $\neg A$ for not A.

$P(A \wedge B) = P(A|B)P(B) = P(B|A)P(A)$ gives the probability for conjunction, $P(A \vee B)= P(A) + P(B) - P(A \wedge B)$ gives the probability for disjunction and $P(\neg A)=1-P(A)$ gives the probability for negation.

Frequently, we are interested in the probability that a random variable (denoted by a capital letter) takes a particular numerical value, e.g. P(X=5) would denote the probability that a die comes up 5. This can also be written $P _ X (5)$.  For real variables we need to consider the probability density $p _ X (x)$ and can only consider the probability that X lies in an interval.
$P(a < X < b) = \int_ a ^b p_X (x) dx$. Notice that $P( a < X < b )$ is the probability of the proposition that the random variable X lies between a and b.

### Expected values of variables

Given a random variable, X, that can take on values $x _ 1 ,...,x _ n$. The expected value of X is simply the weighted average of possible values of X weighted by their probabilities, $E  _  X \{ X \} = \sum  _  {i=1} ^{n} x  _  i P  _  X (x  _  i)$. Similarly the expected value of some quantity that depends on X, e.g. h(x) is $E _  X \{f(X)\}=\sum _  {i=1} ^{n} f(x _  i) P _  X (x _  i)$. For continuous variables, this becomes $E _ X \{f(X)\}=\int _  {-\infty} ^{\infty} f(x _ i) p _ X (x) dx$. Note that we write $E _ X{}$ rather than $E{}$ to make it clear which random variable we are averaging over. In some situations we might have more than one random variable.

Two expected values show  up so frequently, we give them names. The mean $\bar{X}=E _ X\{X\}$ and the variance $var(X) = E _ X\{(X-\bar{X})^2\}$.

Mention moment generating function?

### Adding random variables

Convolution integral for adding variables $p _  {x+y}(s)=\int _  {-\infty}^\infty p _  x (x')p _ y (s-x') dx'$

For a linear combination of random variables, the means and variances add linearly. I.e. if$Y=a _ 1 X _ 1 + a _ 2 X _ 2 + ... + a _ n X _ n$then$\mu _ Y = a _ 1 \mu _ {X _ 1} + ... a _ n \mu _ {X _ n}$ and $\sigma _ Y^2 = a _ 1^2 \sigma _ {X _ 1}^2 + ... a _ n^2 \sigma _ {X _ n}^2$ This does not hold for higher moments, but there are linear combinations of moments called cumulants that do add for linear combinations of random variables.


If $Y=X _ 1 + X _ 2$ then 
$M _ Y (t) = M _ {X _ 1 + M _ 2} (t) = M _ {X _ 1} (t) M _ {X _ 2} (t)$

### Common Probability Distributions and their relationships

#### Normal Distributions

Fully specified by mean and variance. Normals have infinite extent. A normal with zero mean and variance 1 is called a standard normal distribution. For any normally distributed variable, $X$, ${X-\mu} \over \sigma$is a standardized normal.

Sums of normal distributions are also normal.

#### Chi Squared Distributions

Also known as Chi Square and $\chi _ 2$ is
fully specified by degrees of freedom, $\nu$. A sum of Chi Squared distributions is another Chi squared distribution with $\nu$ equal to the sum of degrees of freedom of the component distributions.

If $X _ 1 ... X _ n$ are independent, identically distributed normal variables, then $Y = \sum _ {i=1}^n ({{X _ i - \mu}\over \sigma})$ is chi squared distributed with n degrees of freedom.

#### Student's t Distribution

If Z is a standard normal and V has a Chi square distribution with $\nu$ degrees of freedom, then
$T = {Z \over \sqrt {V/\nu}}$ has a student's t distribution with $\nu$ degrees of freedom.

#### F distribution

If U, V ~ $\chi^2$ with $\nu _ 1$ and $\nu _ 2$ degrees of freedom,$F = {{U/ \nu _ U} \over {V/\nu _ V}}$has an F distribution. This distribution is useful in comparing two random variables [@walpole1978]

### Choosing a probability distribution appropriate to describe ignorance in a particular situation

Assigning probabilities or probability densities must be done in such a way as to accurately reflect the plausibility of various possible statements or variable values. In the case of N equally plausible alternatives, each should be assigned a probability 1/N. Similarly, if a variable is constrained to an interval of width, w, and nothing else is known about it, one should assign a probability density p(x)=1/w for values in the interval and a density of 0 outside the interval.

For more complex situations, we must take advantage of

#### Maximum Entropy Distributions

1. Constrained to finite interval -> uniform
2. Positive and known mean -> exponential
3. Known mean and variance -> normal
