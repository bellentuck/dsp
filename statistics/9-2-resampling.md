[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

>> In hypothesis testing, the null hypothesis (H0) represents the assertion that the effect to be tested is due to chance. (More precisely, H0 asserts that an effect as extreme as the one observed is unlikely not to be due to chance.) 

>> There are several ways of modeling H0. As Allen Downey demonstrates in ThinkStats Section 9.3, H0 can be simulated by "permutation": "we 
treated the observed values [of pregnancy length for first-born babies vs. others in the NSFG dataset under examination] as if they represented the entire population [of pregnancy lengths], and randomly assigned the members of the population [that is, dataset members] to the two groups."

>> Alternatively, H0 can be simulated by "resampling." Resampling entails (a) using a sample to estimate population distribution, and then (b) drawing a random sample from the sampled distribution. So, sampling and then sampling again: re-sampling.

>> A simple way to implement resampling is to draw a sample with replacement from the observed values (i.e., from the original sample). "Replacement" in this context means that after a particular value is drawn from the group of observed values, it remains in the group so that the number of values in the group remains the same regardless of how many values have also been drawn into the resampled sample. (See https://www.ma.utexas.edu/users/parker/sampling/repl.htm for more info.)

>> Testing differences in pregnancy length and birth weight for first-borns vs. others, we can compare the resampled model to a permutated one to determine how resampling affects our results.

>>

>> (0) Module and Data Import and Filtering

>>  First, let's import the `thinkstats2` module, as well as `numpy` and the `nsfg` file; and read in and filter the data file for analysis.
```
import thinkstats2
import numpy as np
import nsfg
preg = nsfg.ReadFemPreg()  #read in proper data file
live = preg[preg.outcome == 1]  #filter to subset for analysis
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
```

>> Now we can start building classes to test our data. Credit to Downey; I'm compiling this stuff so that I can look back on a more succint version of his Pythonic approach to hypothesis testing. :)

>> 

>> Downey's Approach to Hypothesis Testing

>> (1) Parent Class: `HypothesisTest`

>> "`HypothesisTest` is an abstract parent class that provides complete definitions for some methods and place-keepers for others. Child classes based on `HypothesisTest` inherit (a) `__init__` and (b) `PValue` and provide (c) `TestStatistic`, (d) `RunModel`, and optionally (e) `MakeModel`" (Downey, 9.2).
```
class HypothesisTest(object):
    # (a)
    def __init__(self, data):
        self.data = data
        self.MakeModel()
        self.actual = self.TestStatistic(data)
    # (b)
    def PValue(self, iters=1000):
        self.test_stats = [self.TestStatistic(self.RunModel()) 
                           for _ in range(iters)]
        count = sum(1 for x in self.test_stats if x >= self.actual)
        return count / iters
    # (c)
    def TestStatistic(self, data):
        raise UnimplementedMethodException()
    # (d)
    def MakeModel(self):
        pass
    # (e)
    def RunModel(self):
        raise UnimplementedMethodException()
```
>> (a) "`__init__` takes the data in whatever form is appropriate. It calls `MakeModel`, which builds a representation of the null hypothesis, then passes the data to `TestStatistic`, which computes the size of the effect in the sample" (Downey, 9.2).

>> (b) "`PValue` computes the probability of the apparent effect under the null hypothesis. It takes as a parameter `iters`, which is the number of simulations to run. The first line generates simulated data, computes test statistics, and stores them in `test_stats`. The result is the fraction of elements in `test_stats` that exceed or equal the observed test statistic, `self.actual`" (Downey, 9.2).

>>

>> (2) Child Class: `CorrelationPermute`
```
class CorrelationPermute(HypothesisTest):
    """Tests correlations by permutation."""
    # (a)
    def TestStatistic(self, data):
        """Computes the test statistic.                                        
        data: tuple of xs and ys                          
         """
        xs, ys = data
        test_stat = abs(thinkstats2.Corr(xs, ys))
        return test_stat
    # (b)
    def RunModel(self):
        """Run the model of the null hypothesis.                               
        returns: simulated data                                   
        """
        xs, ys = self.data
        xs = np.random.permutation(xs)
        return xs, ys
```
>> "`data` is a pair of sequences. (a) `TestStatistic` computes the absolute value of Pearson’s correlation. (b) RunModel shuffles the xs and returns simulated data.

>> "For the test statistic, I use [Downey uses] Pearson’s correlation, but Spearman’s would work as well. If we had reason to expect positive correlation, we would do a one-sided test. But since we have no such reason, I’ll do a two-sided test using the absolute value of correlation.

>> "The null hypothesis is that there is no correlation between mother’s age and birth weight. By shuffling the observed values, we can simulate a world where the distributions of age and birth weight are the same, but where the variables are unrelated" (Downey, 9.5).

>>

>> (3) Child Class: `DiffMeansPermute`
```
class DiffMeansPermute(HypothesisTest):
    """Tests a difference in means by permutation."""
    # (a)
    def TestStatistic(self, data):
        """Computes the test statistic.
        data: data in whatever form is relevant        
        """
        group1, group2 = data
        test_stat = abs(group1.mean() - group2.mean())
        return test_stat
    # (b)
    def MakeModel(self):
        """Build a model of the null hypothesis.
        """
        group1, group2 = self.data
        self.n, self.m = len(group1), len(group2)
        self.pool = np.hstack((group1, group2))
    # (c)
    def RunModel(self):
        """Run the model of the null hypothesis.
        returns: simulated data
        """
        np.random.shuffle(self.pool)
        data = self.pool[:self.n], self.pool[self.n:]
        return data
```
>> (a) `TestStatistic`. "`data` is a pair of sequences, one for each group. `TestStatistic` outputs the absolute difference in the means" (Downey, 9.3). (It's a two-sided test stat because it takes the absolute value of the difference.)

>> (b) "`MakeModel` records the sizes of the groups, `n` and `m`, and combines the groups into one NumPy array, `self.pool`, via `np.hstack`" (Downey, ibid.). `hstack` is a NumPy method that takes a sequence of arrays and stacks them horizontally (column-wise) to make a single array. The method also rebuilds arrays divided by `hsplit` (opposite of `hstack`). 

>> (c) "`RunModel` simulates the null hypothesis by shuffling the pooled values and splitting them into two groups with sizes `n` and `m`. As always, the return value from `RunModel` has the same format as the observed data" (Downey, ibid.). Before splitting them into two groups, the pooled values get shuffled via `np.random.shuffle`. The NumPy method `random.shuffle` modifies a sequence in-place by shuffling its contents.

>>

>> (4) Child of Child Class `DiffMeansPermute`: `DiffMeansResample`

>> Finally, we reach the distinction between permutation and resampling methods:
```
class DiffMeansResample(DiffMeansPermute):
    """Tests a difference in means using resampling."""
    # (a)
    def RunModel(self):
        """Run the model of the null hypothesis.
        returns: simulated data
        """
        group1 = np.random.choice(self.pool, self.n, replace=True)        
        group2 = np.random.choice(self.pool, self.m, replace=True)
        return group1, group2   
```
>> (a) `RunModel`. The extra step in resampling is to draw random samples from the sampled distribution, to create new "re-sampled" samples. This is accomplished in `RunModel` via `np.random.choice`. `random.choice` is a NumPy method generating a random sample from a given 1-D array. The parameters at present are the array to be resampled, `self.pool`; the sizes of the resampled arrays, `self.n` and `self.m`, as set in `DiffMeansPermute` to the length of groups 1 and 2 [so resampling is basically like reshuffling a deck to assure more maximal randomness]; and the argument `replace=True`, denoting whether the resampled sample is to be taken from the original sample with or without replacement (in this case, with replacement).

>>

>> (5) Child Class: `PregLengthTest`
```
class PregLengthTest(HypothesisTest):
    """Tests difference in pregnancy length using a chi-squared statistic."""
    # (a)
    def TestStatistic(self, data):
        """Computes the test statistic.                 
        data: pair of lists of pregnancy lengths   
        """
        firsts, others = data
        stat = self.ChiSquared(firsts) + self.ChiSquared(others)
        return stat
    # (b)
    def ChiSquared(self, lengths):
        """Computes the chi-squared statistic.                 
        lengths: sequence of lengths                                
        returns: float                                            
        """
        hist = thinkstats2.Hist(lengths)
        observed = np.array(hist.Freqs(self.values))
        expected = self.expected_probs * len(lengths)
        stat = sum((observed - expected)**2 / expected)
        return stat
    # (c)
    def MakeModel(self):
        """Build a model of the null hypothesis.  
        """
        firsts, others = self.data
        self.n = len(firsts)
        self.pool = np.hstack((firsts, others))
        pmf = thinkstats2.Pmf(self.pool)
        self.values = range(35, 44)
        self.expected_probs = np.array(pmf.Probs(self.values))
    # (d)
    def RunModel(self):
        """Run the model of the null hypothesis. 
        returns: simulated data                                     
         """
        np.random.shuffle(self.pool)
        data = self.pool[:self.n], self.pool[self.n:]
        return data
```
>> (a) "`TestStatistic` computes the chi-squared statistic for first babies and others, and adds them" (Downey, 9.8).

>> (b) "`ChiSquared` takes a sequence of pregnancy lengths, computes its histogram, and computes observed, which is a list of frequencies corresponding to `self.values`. To compute the list of expected frequencies, it multiplies the pre-computed probabilities, `expected_probs`, by the sample size. It returns the chi-squared statistic, `stat`" (Downey, ibid.).

>> (c) "The data are represented as two lists of pregnancy lengths. The null hypothesis is that both samples are drawn from the same distribution. `MakeModel` models that distribution by pooling the two samples using `hstack`....`MakeModel` also defines `values`, which is the range of weeks we’ll use, and `expected_probs`, which is the probability of each value in the pooled distribution" (Downey, ibid.).

>> (d) "`RunModel` generates simulated data by shuffling the pooled sample and splitting it into two parts" (Downey, ibid.).

>>

>> Now that we've built our hypothesis test structure, we can compare resampling vs. permutation as methods of attaining randomness in H0.

>> I don't understand how the comparison works out in practice. Downey provides the following two functions. I can't really explain what they do. But here they are.
```
# (a) 
def RunResampleTest(firsts, others):
    """Tests differences in means by resampling.
    firsts: DataFrame
    others: DataFrame
    """
    #
    data = firsts.prglngth.values, others.prglngth.values
    ht = DiffMeansResample(data)
    p_value = ht.PValue(iters=10000)
    print('\nmeans permute preglength')
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())
    #
    data = (firsts.totalwgt_lb.dropna().values,
            others.totalwgt_lb.dropna().values)
    ht = DiffMeansPermute(data)
    p_value = ht.PValue(iters=10000)
    print('\nmeans permute birthweight')
    print('p-value =', p_value)
    print('actual =', ht.actual)
    print('ts max =', ht.MaxTestStat())
```
```
# (b)
def RunTests(live, iters=1000):
    """Runs the tests from Chapter 9 with a subset of the data.
    live: DataFrame
    iters: how many iterations to run
    """
    n = len(live)
    firsts = live[live.birthord == 1]
    others = live[live.birthord != 1]
    #
    # compare pregnancy lengths
    data = firsts.prglngth.values, others.prglngth.values
    ht = DiffMeansPermute(data)
    p1 = ht.PValue(iters=iters)
    data = (firsts.totalwgt_lb.dropna().values,
            others.totalwgt_lb.dropna().values)
    ht = DiffMeansPermute(data)
    p2 = ht.PValue(iters=iters)
    #
    # test correlation
    live2 = live.dropna(subset=['agepreg', 'totalwgt_lb'])
    data = live2.agepreg.values, live2.totalwgt_lb.values
    ht = CorrelationPermute(data)
    p3 = ht.PValue(iters=iters)
    #
    # compare pregnancy lengths (chi-squared)
    data = firsts.prglngth.values, others.prglngth.values
    ht = PregLengthTest(data)
    p4 = ht.PValue(iters=iters)
    #
    print('%d\t%0.2f\t%0.2f\t%0.2f\t%0.2f' % (n, p1, p2, p3, p4))
```

>> Well, there we have it: I've hit a wall. But I certainly look forward to learning how to more fully unpack this stuff in order to then be able to carry it out on my own!
