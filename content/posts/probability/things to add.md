---
title: Probability todo
date: 2020-01-01
---
# The standard deviation as a measure of spread
bessel correction - proof 3 on wikipedia page

<http://www.crataegus.me.uk/thoughts/bessel_correction.html>

Samuelson's inequality : For N samples, all lie within $\sqrt {N-1}$ standard deviations of the sample mean

Chebyshev's Inequality : only $1 \over k^2$ of data lie beyond $k\sigma$ of $\mu$
.

Cramer-Rao bound - varience of any unbiased estimator is at least the inverse of the fisher information

(see also Chapman-Robbins bound)

Bhatia-Davis inequality : For a sample with maximum $M$ and minumum $m$, we have $\sigma ^2 \le ( M - \mu ) (\mu - m)$

Popoviciu's inequality $\sigma^2 \le {1 \over 4} (M-m)^2$

von Szokefalvi Nagy inequality $\sigma^2 \ge {{(M-m)^2} \over 2n}$

<https://stats.stackexchange.com/questions/317502/tightest-bounds-on-sample-variance-given-sample-size-mean-minimum-and-maximum>

<http://files.ele-math.com/articles/jmi-04-32.pdf>

# error analysis

<https://stats.stackexchange.com/questions/93316/parameter-uncertainty-after-non-linear-least-squares-estimation>

the least squares routine in SciPy returns the Jacobian for the system. First estimate the Hessian $H=J^TJ$. The covariance matrix is the inverse of the Hessian. The unbiased covariance matrix $\sigma_{xy} = cov (RSS/(m-n))$ where RSS is the residual sum of square, m is the number of measurements, and n is the number of parameters. The diagonal of $\sigma_{xy}$ gives the parameter uncertainties.

# Nice presentations on parameter estimation
<https://www.phas.ubc.ca/~oser/p509/>
<https://www.phas.ubc.ca/~oser/p509/Lec_08.pdf>
<https://www.phas.ubc.ca/~oser/p509/Lec_09.pdf>