[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> Are first babies lighter or heavier than others? To investigate this question I analyzed data from the National Survey of Family Growth, provided by Allan Downey's `nsfg` module from Think Stats. First, I used the `nsfg` method `nsfg.ReadFemPreg()` to read in the data. I then filtered the data two times: first, I kept only data partaining to live births in play; second, I filtered data on live births into `firsts` and `others` for first-borns and others, respectively.
```
import nsfg  #import set of data files 
preg = nsfg.ReadFemPreg()  #read in proper data file
live = preg[preg.outcome == 1]  #filter to subset for analysis
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
```
>> Plotting a histogram of `totalwgt_lb` frequencies for `firsts` against that of those of `others`, using Downey's `thinkstats2` and `thinkplot` modules, I observed that the two histograms were shaped more or less analogously. 
```
import thinkstats2  #variation on pandas
import thinkplot  #variation on matplotlib
first_hist = thinkstats2.Hist(firsts.totalwgt_lb)
other_hist = thinkstats2.Hist(others.totalwgt_lb)
thinkplot.Hist(first_hist)
thinkplot.Show(xlabel='weight', ylabel='frequency')
thinkplot.Hist(other_hist)
thinkplot.Show(xlabel='weight', ylabel='frequency')
```
>> First babies would appear not to be significantly lighter or heavier than others. But can we know this more precisely? We can quantify the difference between these two groups (first babies, others) using "Cohen's d," a formula comparing (a) the difference between firsts and others to (b) the variability within these groups. The greater (a) is compared to (b), the greater the difference effectively is between weights of first babies compared to those of others.
```
import math
def cohensD(group1, group2):
    diff = group1.mean() - group2.mean()  # numerator
    var1 = group1.var()  # variance
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)  # denominator
    d = diff / math.sqrt(pooled_var)  # compares the difference between groups
    return d  
```
>> Feeding `cohensD` the arguments `others.totalwgt_lb` and `firsts.totalwgt_lb`, I got the output `0.0886729270726`. The difference between weights for firsts and others is about 0.089 standard deviations, which is trivial (0.2 = small, 0.5 = medium, 0.8 = large effect). Notably, however, the difference in pregnancy length for first babies versus others is 0.029 SDs (as calculated by Downey in chap02). So, while still in a small way, whether a baby is a first-born or not will have statistically effected that baby's birth weight about 3x more thanwill have effected length of pregnancy.