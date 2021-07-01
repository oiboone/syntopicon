---
title: Potential Future Topics
date: 2020-01-01
---

# Entropy and Information

KL Divergence measures distance between distributions $D _{KL} (p,q) = \sum _{i=1} ^ N p(i)log({{p(i)}\over{q(i)}})$

For any two distributions $D_{KL} \ge 0$ where equality is only when they are the same distribution.

Because of this, we can show that the maximum entropy distribution is the uniform discrete distribution, since if $q(i)={1 \over N}$, we have 

$$ D_{KL}(p,q)=\sum _{i=1} ^N p(i)log({{p(i)}\over{q(i)}})$$
$$ = \sum _{i=1} ^N p(i)log(p(i)) - \sum _{i=1} ^N p(i)log(q(i) = -H(p)+log(N)$$ 
so $H(p) = log(N) - D _{KL} (p,q)$

# Sig figs in uncertainty

1. Assume normally distributed errors
2. Calculate mean and variance of sample $\hat{\mu}$ and $\hat{\sigma} ^2$
3. Best point estimate of true value is the mean
4. Best value of uncertainty (1 sigma) is standard deviation of the mean $\hat{\sigma} / \sqrt{N}$ for large N. For small N, we should use the standard deviation of the scaled t distribution, i.e. $ {\hat{\sigma} \over{\sqrt{N}}} \sqrt{N \over N-2} = {\hat{\sigma} \over{\sqrt{N-2}}}$.
5. Our uncertainty in the uncertainty is based on the variance of the chi squared distribution
Assuming Normally distributed errors, our best estimate of uncertainty is based on measured variance

Since the sample variance, $S^2 = \hat{\sigma}^2$ has a chi square distribution $(n-1){{S^2}\over{\sigma^2}} \sim \chi ^2 (n-1)$ the variance is $var((n-1){{S^2}\over{\sigma^2}}) = 2(n-1)$ which implies $var({S^2}) = {{2 \sigma^4} \over {n-1}}$.

But $var(f(x))\approx (df/dx)^2 var(x)$ so $var(S) \approx {{Var(S^2)} \over {4S^2}} \approx {{Var(S^2)} \over {4\sigma^2}}$

so $\sigma _S \approx {1 \over {\sqrt{2(n-1)}}}\sigma _x$



that's all folks
