[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> What percentage of the U.S. male population is eligable to join the Blue Man Group (BMG), based on height alone? For consistency's sake, BMG requires applicants to be between 5'10" and 6'1". So what our initial question actually requires us to figure out is the percentage of the U.S. male population between 5'10" and 6'1".  

>> To find out what the distribution of U.S. male heights might look like, we've got help from the Behavioral Risk Factor Surveillance System (BRFSS), a survey of hundreds of thousands of U.S. residents that includes a height statistic. If this statistic doesn't give us an exact answer, it at least points us in the right direction. (We can later perform a hypothesis test to get a better idea of how accurate the sample is.) 

>> In the BRFSS (Allen Downey helpfully hints), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men. Recall that we want to figure out the *percentage* of the U.S. male population between 5'10" (177.8 cm) and 6'1" (185.4 cm). We can model the empirical distribution of BRFSS data with a cumulative distribution function (CDF) in order express the difference between high and low height limits as a difference between percentiles. Data modelled via CDF is analytically distributed. By constructing an analytic distribution, we can express the number of eligable blue men out of U.S. males as a percent of U.S. males.

>> (1) To get started, let's import the `norm` class from the SciPy module `stats`. (`scipy.stats` contains objects that represent analytic distributions.)
```
from scipy.stats import norm
```
>> `norm` represents the normal/Gaussian distribution.

>> (2) With the ability to represent analytic normal distributions, let's create one with mean and standard deviation parameters specifically set to 178 cm and 7.7 cm, respectively. This is done by setting parameter "keywords" associated with `norm` appropriately. As the keyword `loc` has to do with centrality (think "locus") and the keyword `scale` to do with, well, scale, `loc` and `scale` should in a normal distribution be set, respectively, to values for µ and σ. 
```
dist = norm(loc=178, scale=7.7)
```
>> Querying the type of our distribution--`type(dist)`--we see that `dist` is a "frozen random variable" (`scipy.stats._distn_infrastructure.rv_frozen`). "Frozen random variable" is another way of saying that `dist` represents the normal distribution for µ and σ as a cumulative mass function (CMF). The computed mean equals µ (`dist.mean()` outputs `178.0`) and the computed standard deviation basically equals σ (`dist.std()` outputs `7.7000000000000002`).

>> (3) Next, we need to convert our two BMG hight limits from the normally-distributed CMF `dist` into CDF values; i.e., percentiles. 
```
high = dist.cdf(185.4)
# high = 0.83173371081078573 = 83rd percentile
low = dist.cdf(177.8)    
# low = 0.48963902786483265 = 49th percentile
```
>> (4) Finally, we can calculate the difference between `high` and `low` height limits as the number of percentiles falling in between. This will give us the percentage of U.S. males eligable, based on height alone, to become members of the BMG.
```
high - low
# output = Z-statistic? = 0.34209468294595308
```
>> From this analysis, it appears that 34.2% of U.S. males are eligable to become blue men based on height.

>> To test our hypothesis that about 1/3 of U.S. males are eligible to become members of the BMG, we'll need to come up with null and alternative hypotheses to test. The null hypothesis will be the hypothesis that we came up with 0.342 by chance and that, due to various biases, this percentage is not representative of the U.S. male population between 5'10" and 6'1" as a whole. The alternative hypothesis will be the hypothesis that our result is statistically significant; that is, unlikely due to chance. How unlikely is sufficiently unlikely? Traditionally, <5%. In our test, we'll need to set the p-value accordingly. I'd like to say our critical value for testing will be the Z-statistic, but I'm not sure. (Upon further developing my statistical know-how, I'll be able to know where to take it from here.)