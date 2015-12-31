[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

>> "Standard error (SE) is a measure of how far we expect the estimate to be off, on average. For each simulated experiment, we compute the error, x − µ, and then compute the root mean squared error (RMSE).

>> "A confidence interval (CI) is a range that includes a given fraction of the sampling distribution. For example, the 90% confidence interval is the range from the 5th to the 95th percentile."

>> -- Allen Downey, ThinkStats, 8.3 

>> 

>> How do SE and CIs vary according to sample size? To attack this problem, let's vary the sample size of an exponential distribution and see what happens. 

>> What are we going to test? Let's say the parameter of this distribution, lambda, is equal to 2. What will the sampling distribution of `L`, an estimation of the exponential parameter for a given sample (thus "lambda-hat"), look like given a particular sample size? 

>> I imported modules to help code up an answer to the previous question as follows:
```
import math
import numpy as np
import thinkplot
import thinkstats2
import matplotlib.pyplot as plt
```
>> First things first: we'll need to be able to compute the RMSE. Next things next: we'll want to simulate samples (say, 1000 of them) to gain a basic sense of the sampling distribution of `L`. From there, we can figure out how the SE and CIs for `L` vary depending on sample size.

>> As far as code goes, these first functions `RMSE` and `SimulateSample` are taken/adapted from Downey. 
```
def RMSE(estimates, actual):
    """Root mean squared error formula.
    estimates: list of estimates in exponential distribution (estimate = L)
    actual: actual value being estimated (lambda parameter, e.g.)
    """
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)
```
>>
```
def SimulateSample(lam, n, m):
    """Sampling distribution of L as an estimator of exponential parameter.
    lam: parameter of an exponential distribution
    n: sample size                                                          
    m: number of iterations                                                   
    """
    def VertLine(x, y=1):
        """Plots CI lines.
        """
        thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)
    #
    estimates = []
    for j in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1.0 / np.mean(xs)  # L, aka "lamda-hat"
        estimates.append(L)
    #
    stderr = RMSE(estimates, lam)
    print('standard error', stderr)
    #
    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print('confidence interval', ci)
    VertLine(ci[0])
    VertLine(ci[1])
    #
    # plot the CDF                                                             
    thinkplot.Cdf(cdf)
    thinkplot.Config(root='estimation2',
                   xlabel='estimate',
                   ylabel='CDF',
                   title='Sampling distribution')
```
>> Here's a sample output for lambda=2 and a sample size of 10 (`SimulateSample(2, 10, 1000)`):
```
('standard error', 0.8077354609638567)
('confidence interval', (1.2539059715743179, 3.5499397034956872))
```
>> [1] + link

>> Calling `SimulateSample` a few more times with the same arguments generated the following SE and CI outputs:
```
('standard error', 0.8257051881004289)
('confidence interval', (1.2674399798297786, 3.6448100997033417))
('standard error', 0.8477018707931915)
('confidence interval', (1.2623663340301843, 3.7214363095971783))
('standard error', 0.7933457941809067)
('confidence interval', (1.2603254845165561, 3.6024606778933079))
```
>> So, some slight variations on SE and miniscule ones for CI, but we're getting consistent enough results to move on. The task now is to vary the sample size and see what effect this has on the SE and CIs.

>> To do this, I supplemented `SimulateSample` with two variants: one that would return the SE for a given sample size, `n`, over a given number of simulations, `m`; and one that would return the CIs. (Determining how the number of simulations effects the SE and CIs is notso relevant a relevant concern, as I can pretty much run as many simulations as I like. But I can't necessarily increase the size of a given sample. I'm doing so now to demonstrate precisely how varying sample sizes can affect the SE and CIs.)   
```
def SimulateSample2(lam, n, m):
    """A pared-down version of SimulateSample, which returns
    SE to be plotted against sample size.
    """
    estimates = []
    for j in range(m):
        xs = np.random.exponential(1.0/lam, n)
        lamhat = 1.0 / np.mean(xs)
        estimates.append(lamhat)
    stderr = RMSE(estimates, lam)
    return stderr
```
>>
```
def SimulateSample3(lam, n, m):
    """A pared-down version of SimulateSample, which returns
    CI to be plotted against sample size.
    """
    estimates = []
    for j in range(m):
        xs = np.random.exponential(1.0/lam, n)
        lamhat = 1.0 / np.mean(xs)
        estimates.append(lamhat)
    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.Percentile(95) - cdf.Percentile(5) 
    return ci
```
>> I now utilize `SimulateSample2` and `SimulateSample3` in the following function, `make_plots`, to be able to make line graphs of SE vs. sample size and 90% CI vs. sample size. `make_plots` takes arguments `start`, `stop`, and `step` as parameters for a range of sample sizes (beginning with `start` and ending with `stop - step`).
```
def make_plots(start, stop, step):
    """Plots SE vs. sample size and CIs vs. sample size.
    start: where to start the given distribution
    stop - step: where to end the given distribution
    stderr_list = standard errors across the given distribution
    ci_list = 90% confidence intervals across the given distribution
    n_list = sample sizes across given distribution
    """
    stderr_list = []
    ci_list = []
    n_list = []  
    for i in range(start, stop, step):
        n_list.append(i)
        stderr_list.append(SimulateSample2(2, i, 1000))
        ci_list.append(SimulateSample3(2, i, 1000))
    #plot SE vs. sample size
    plt.plot(n_list, stderr_list)
    plt.xlabel('sample size')
    plt.ylabel('standard error')
    plt.show()
    #plot CI vs. sample size
    plt.plot(n_list, ci_list)
    plt.xlabel('sample size')
    plt.ylabel('90% confidence interval')
    plt.show()
```
>> Let's start simple, by looking at sample sizes from 10 to 100, increasing by increments of 10:
```
make_plots(10, 110, 10)
```
>> [2] + link

>> It appears that a sample size of 10 is significantly more error-prone, and has a significantly greater 90% CI than larger sample sizes. Values progressively stabilize as we move from n=20 to n=70 (a sample size of 40, in particular, appears to be a small sample size worth aiming for), and for sample sizes >= 70 SE and CIs appear to be relatively stable. Of course these are rough estimates; increasing the sample size by 10 at a time gives us only a rough picture of what's going on.

>> Let's increase the sample size by an increment of 1 instead of 10 this time, and see what happens:
```
make_plots(10, 101, 1)
```
>> [3] + link

>> While we appear to be getting about the same picture of what's going on here, incrementing the sample size by 1 gives us a somewhat smoother graph. 

>> Increasing the maximum sample size to 1000, we observe the same half-parabolically-downward-sloping trend:
```
make_plots(100, 1001, 10)
```
>> [4] + link

>> And again from 1000-10000:

>> [5] + link

>> This is all to say that an intriguing pattern appears to have surfaced. 10^1 samples generate about a 3x greater level of error, and about a 3x larger confidence interval, than 10^2 samples. In turn, 10^2 samples generate about 3x greater SE and CI levels than 10^3 samples. Only at 10^4 samples does the sample size begin to have less of an effect on error (10000 samples generates more like 2x as much error as 1000 samples); yet 10^4 samples still bears the same 3:1 relation to 10^3 samples as far as the 90% CI goes.

>> While I don't have the mathematical vocabulary to abstract further from here, I get the sense that there's a broader, possibly logarithmic lesson to be taken on some level. 