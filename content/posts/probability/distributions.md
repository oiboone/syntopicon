---
title: Common Probability Distributions and their relationships
slug: distributions
date: 2018-06-09
modified: 2018-06-09

bibliography: [support/MyLibrary.bib]
csl: [support/ieee.csl]
---

# Uniform Distributions and the Principle of Indifference

## Discrete Uniform Distribution

In a situation with N possible outcomes with complete symmetry between them, there is no reason for the probability of any outcome to be greater or less than the others. In this case each outcome has a probability of 1/N.

## Continuous Uniform Distribution

Similarly, if a random variable has a finite range from *a* to *b* and there is no reason to prefer any value over another in this range, the probability density function is $1 \over {b-a}$

# Distributions arising from Bernoulli experiments

A Bernoulli experiment is one that has two outcomes (success and failure) and a probability of success p and failure (1-p)

## Bernoulli Distribution

Probability of a success in a single trial.

## Binomial Distribution

Probability of k successes in n trials. $P _k (k)= {{n!} \over {k!(n-k)!}} p^k (1-p)^{(n-k)}$ Note that ${{n!} \over {k!(n-k)!}} = {n \choose k}$ are the binomial coefficients (hence the name).

## Geometric

Probability that first success occurs on n'th trial $P _n (n) = (1-p)^{(n-1)}p$

## Negative binomial

Probability that k'th success occurs on n'th trial. Generalization of geometric distribution. $P _n (n) = {{n-1}\over{k-1}}(1-p)^{(n-k)}p^{k}$. $X _1 , X _2 , ..., X _{n-k} \sim \mathrm{GEOM}(1-p) \implies \sum X _i \sim \mathrm{NB}(r,p)$ for *X* independent.

# Experiments with shrinking pools

Starting with a finite pool of N consisting of K successes and (N-K) failures and sampling without replacement.

## Hypergeometric

Probability of k successes in n trials without replacement. $P _k (k) = {{{K \choose k}{{N-K} \choose {n-k}}}\over{N\choose n}}$

## Negative Hypergeometric

Probability that k successes occur before r failures. $P _k (k) = {{{{k+r-1}\choose k}{{N-r-k}\choose {K-k}}\over{N \choose K}}}$

# Poisson processes

Poisson processes are the limiting continuum case of a large number of Bernoulli trails in an interval such that p decreases as N increases with $\lambda = n \cdot p$ remaining constant. $\lambda$ is the average number of successes in the interval. Note that if we know the average number of successes in a unit interval, the average in an interval *t* is $\lambda \cdot t$

## Poisson

Probability of k successes in an interval. $P _k (k) = e^{-\lambda} {{\lambda^k}\over{k!}}$ Limit of the binomial distribuiton as n approaches $\infty$ with np held constant. Also the limit of a negative binomial distribution for $\lambda = (n-k)p/(1-p)$ as p goes to 0 while keeping $\lambda$ comstant.

## Exponential

Probability of next success occuring in an interval t. $P _t (t) = \lambda e^{-\lambda t}$ for $t \ge 0$. Continuous analog of the geometric distribution.

## Rayleigh

$X \sim \mathrm{Exp}(\lambda) \implies \sqrt {X} \sim \mathrm{Rayleigh}(1/\sqrt{2\lambda})$

## Erlang

Probability of N successes occuring in an interval T. This is also the distribuiton of the sum of N independent and identically distributed exponential variables.

# Normal Distributions and their relatives

## Normal Distributions

Fully specified by mean and variance. Normals have infinite extent. A normal with zero mean and variance 1 is called a standard normal distribution. For any normally distributed variable, $X$, ${X-\mu} \over \sigma$is a standardized normal.

Sums of normal distributions are also normal.

## Chi Squared Distributions

Also known as Chi Square and $\chi ^2$ is
fully specified by degrees of freedom, $\nu$. A sum of Chi Squared distributions is another Chi squared distribution with $\nu$ equal to the sum of degrees of freedom of the component distributions.

If $X _1 ... X _n$ are independent, identically distributed normal variables, then $Y = \sum _ {i=1}^n ({{X _ i - \mu}\over \sigma})$ is chi squared distributed with n degrees of freedom.

## Student's t Distribution

If Z is a standard normal and V has a Chi square distribution with $\nu$ degrees of freedom, then
$T = {Z \over \sqrt {V/\nu}}$ has a student's t distribution with $\nu$ degrees of freedom.

## F distribution 

If U, V ~ $\chi^2$ with $\nu _ 1$ and $\nu _ 2$ degrees of freedom,$F = {{U/ \nu _ U} \over {V/\nu _ V}}$has an F distribution. This distribution is useful in comparing two random 
variables [@walpole1978] and so on.

Include beta and gamma distributions...
Also lognormal and other derived distributions...