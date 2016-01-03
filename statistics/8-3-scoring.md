[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

---

>> What might a team's goal-scoring rate look like for a sport like soccer or hockey? So few goals are scored per game in these types of sports that the time between goals is roughly exponential (i.e., there is an arbitrary amount of time between each goal scored). This allows us to estimate a team's goal-scoring rate by observing the number of goals the team scores in a given game and then compiling a sample of number of goals given number of games. 

>> Because the intervals between goal-scoring in sports like hockey and soccer is roughly exponential, the distribution of goals per game will be roughly exponential as well. This means that the parameter we're trying to calculate, goal-scoring rate, will be the exponential distribution parameter *lambda*.

>> (1) Downey's `SimulateGame` function

>> First, we're going to need a function that takes the goal-scoring rate, lambda, as an expression of goals per game, `lam`, and simulates a single game. This function, `SimulateGame`, will generate the time between goals, `time_between_goals`, via the `random` module method `random.expovariate`. 

>> `random.expovariate` takes one argument, equal to 1.0 / desired mean. We're going to feed it `lam`; `desired mean = 1.0 / lam`. `random.expovariate` returns a value from 0 to positive infinity if `lam` is positive. (It would return a value from negative infinity to 0 if `lam` were negative, but in this example we won't be entering negative values for `lam`.)  

>> At each interval, we'll add a single goal to a `goals` variable. We'll add `time_between_goals` to a time variable, `t` until `t` as the sum of `random.expovariate` outputs exceeds `1` (i.e., 1 game). We'll then return the number of goals scored as the estimate `L`. (Prior to running `SimulateGame`, we estimate `L = 1/lam`.) So, if `random.expovariate` returns a value > 1, the game is over before a single goal has been scored: `L = 0`. 
```
import random
def SimulateGame(lam):
    """Simulates a game and returns the estimated goal-scoring rate.
    lam: actual goal scoring rate in goals per game
    """
    goals = 0
    t = 0
    while True:
        time_between_goals = random.expovariate(lam)  # lam = 1.0/desired mean
        t += time_between_goals                       # desired mean = 1.0/lam
        if t > 1:
            break
        goals += 1
    # estimated goal-scoring rate is the actual number of goals scored
    L = goals
    return L
```

>> (2) Downey's `Estimate` function

>> Having created a function that simulates a single game and returns a goal-scoring rate for that game, we can now call this function in another function, `Estimate` that will simulate many games and append estimates for `lam` (i.e., the return values of `L` from `SimluateGame`) to a list of estimates.

>> `Estimate` takes two arguments, `lam` and `m`. `lam` will be our baseline estimate for goals per game; we'll feed it into `SimulateGame`. We'll call the function `m` times, and then we'll have a goal-scoring rate estimates list of length `m`.

>> We'll want to know how accurate our estimation list is. This will help us determine whether this way of making an estimate is biased or not, as well. So it seems as though we'll want to have `Estimate` compute and print the Mean Squared Error (MSE) and Root Mean Squared Error (RMSE) based on the `estimates` and `lam`. Recall that `MSE = (1/m) * sum(L - lam)^2`, and that `RMSE = (MSE)^(1/2)`.

>> Question, though: I'm not sure we're actually using the MSE in these calculations. I think there's a separate value, "Mean Error" that Downey uses instead, and that this is why Mean Error outputs are/can be negative. I'm unclear about what the formula for Mean Error is vs. MSE.

>> Plotting a Probability Mass Function (PMF) as a sampling distribution of our `estimates` will give us a way of visualizing most common values for `L`. We would expect them to congregate around whatever initial value we input for `lam`. 

>> Finally, we can get the Cumulative Distribution Function (CDF) for the estiamtes in order to compute the 90% confidence interval for our data. The 90% CI will give us a sense of the range of goal-scoring rates in a more succint way than the visualization. (But the visualization is nice to have something to think with.)
```
import thinkstats2
def Estimate(lam, m):
    """Estimates a goal-scoring rate from a sample of simulated games, given
    an initial goals per game estimate. Returns a graphed PMF for estimates, as
    well as the Mean Error and Root Mean Squared Error for the rate estimate.
    Arguments:    
    lam = initial goal-scoring rate estimation of goals per game
    m = number of games to be simulated
    """
    # Compute list of goal-scoring rate estimates:    
    estimates = []
    for i in range(m):
        L = SimulateGame(lam)
        estimates.append(L)
    # Print mean error and rmse for estimate list:
    print('rmse L', RMSE(estimates, lam))
    print('mean error L', MeanError(estimates, lam))  
    # Make pmf from estimate list:    
    pmf = thinkstats2.Pmf(estimates)
    thinkplot.Hist(pmf)
    thinkplot.Show(xlabel='goal-scoring rate (i.e., goals per game)',
                  ylabel='PMF')
    # Calculate 90% CI from estimate list:
    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print('confidence interval', ci)
```
>> Here are some outputs for `Estimate(2, 1000000)`; i.e., `lam = 2` and `m = 1000000` (that's right: 1 million simulated games).
```
('rmse L', 1.4133106523337322)
('mean error L', -0.001521)
```
>> <a href="https://github.com/bellentuck/dsp/blob/e507c8c93d42a7dabb302d13853ebc65e83346ef/thinkstats_scoring_pmf.png"><img src="img/thinkstats_scoring_pmf.png" style="width: 100px;" target="_blank"></a>
```
('confidence interval', (0, 5))
```
>> Running this experiment multiple times, it appears that RMSE and mean error stay consistent enough to say that, given the initial setting `lam=2`, the RMSE is 1.4, and the mean error is nearly 0.

>> Interestingly, when we increase `lam` to `3`, the RMSE increases to 1.7, and when `lam = 4`, the RMSE increases again to just about 2.0. For `lam = 5`, there is not quite so big a jump--this time from RMSE=2.0 to RMSE=2.2. However, for `lam = 1`, RMSE=1.0. We could simulate many values of `lam` and see what this does to the RMSE, but I'm not sure what exactly we would get from seeing the distribution of RMSE across different goal-scoring rates, as RMSE stays relatively small all the while. Still, it does appear that in general `Estimator` is a more accurate predictor for smaller goal-scoring rates. The 90% CI may be able to fill in the gap here: 90% of goal-scoring rate values range from 0-5 given `lam = 2`, and from 1-6 given `lam = 3`; however, for `lam = 4`, they range from 1-8, and from 2-9 for `lam = 5`. By contrast the range is 0-3 for `lam = 1`. I'm not exactly sure what this tells us specifically, but generally it seems to imply that a larger range of goal-scoring rates is more difficult to accurately predict for, which seems commonsensical enough. 

>> Mean error remains epsilonically small (+/- 0.001) regardless what we assign `lam` to, suggesting that `Estimator` is unbiased. The consistency of the RMSE value given a set value for `lam` may also suggest this.

---