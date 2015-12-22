[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> The National Survey of Family Growth (NSFG) 2002 data from the Think Stats repo includes mothers' responses to the question, "How many children under 18 live in your household?" The probability mass function (PMF) of this data, revealing what percentage of households contain what number of children, provides statisticians with an actual distribution of kids per house. The distribution is basically unbiased because one and only one respondent accounts for each out of the vast majority of households: the ratio between households and mothers who account for them is more or less 1:1. (More or less: non-traditional parents--lesbian, polygamous, polyamorous, trans--pose interesting if statistically trivial counterexamples.)

>> Compare the unbiased, actual distribution of number of children under 18 in a household, constructed using NSFG data, to a biased distribution. Let's say the NSFG surveyed kids instead of expectant mothers and asked these kids how many kids lived in their households, including themselves. Or, say the NSFG asked respondents to report the number of children under 18 in the households they grew up in, as opposed to the ones they currently occupy. How would the actual distribution differ from a biased one like these, in which the ratio of respondents to households is not 1:1?

>> Fortunately, we can intentionally bias the actual PMF for minors per house in order to compute the biased distribution. 

>> First, let's import modules `nsfg` and `thinkstats2` from the Think Stats repo; then, let's use the former to unpack the data from `ReadFemResp` and the latter to make us a histogram for the particular survey question about number of minors per household (`numkdhh`). (N.B.: `nsfg.py` has to be updated with appropriate functions to accommodate `2002FemResp` files. These functions are available in `chap01soln.py`.) 
```
import nsfg
import thinkstats2
import thinkplot
fam = nsfg.ReadFemResp()
kids_hist = thinkstats2.Hist(fam.numkdhh)
```
>> Now we can construct the actual distribution for `numkdhh`. `actual_pmf` is a dictionary linking numbers of children to percentages of responses:
```
actual_pmf = thinkstats2.Pmf(kids_hist)
```
>> Finally, we'll compute the biased distribution for `numkdhh` by manipulating a copy of the actual distribution (step 1). We'll throw off or "bias" each household size by the number of children under 18 in the household (step 2--this is what the `.Mult()` method call is about). We normalize the new distribution so that the decimalized percentages will add up to 1 (step 3). (This function courtesy Think Stats, chapter 3.)
```
#step 1
def BiasPmf(pmf):
    new_pmf = pmf.Copy()
#step 2
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)  
#step 3
    new_pmf.Normalize()
    return new_pmf
```
>> Let's call up our biased distribution, `biased_pmf`, in order to compare the two distributions side by side.
```
biased_pmf = BiasPmf(actual_pmf)
```
>> We have two basic options for comparing PMFs, courtesy Think Stats' module `thinkplot`: bar graph and step function. As the number of values in the PMFs is not small, a bar graph already seems like a bad idea. Compounding the problem is the fact that in order to display actual vs. biased data for zero children, we need to bring the bar graph's x-axis range down to -1 (because one of the bars needs to go to the left of zero, which is visually not possible unless we extend the range of the graph below zero). But extending the possible number of children under 18 in a household down below zero makes no sense; there are, generally speaking, no negative numbers of people. (Which raises an interesting point: what about households that've lost more children than've gained? Strictly speaking, this is not the matter at hand.) For these reasons, a step function is the way to go.

>> Here's the code to get us the desired step function:
```
thinkplot.PrePlot(2)
thinkplot.SubPlot(2)
thinkplot.Pmfs([actual_pmf, biased_pmf])
thinkplot.Show(xlabel='number of minors in household',
               ylabel='probability',
               axis=[0, 6, 0, 0.5])
```
>> Notably, I've extended the x-axis only to 6 and the y-axis only to 0.5 in order to highlight the relevant distinction between the actual and biased distributions. The purplish line in the step function represents `actual_pmf`, while the blueish one represents `biased_pmf`.

<a href="https://github.com/bellentuck/dsp/commit/4178ecf79c094e9fd3c0853986b76928e43f3c91"><img src="img/thinkstats_actual_and_biased_pmfs.png" style="width: 100px;" target="_blank"></a>

>> Don't pay attention to the vertical lines: picture, rather, a dotted line extending from each number on the x-axis up to the purplish and blueish lines. As we can see, both actual (purplish) and biased (blueish) lines show a probability of a little over 0.2 for a household with 1 child under 18. This makes sense: the ratio of respondent:children is going to be 1:1 in the biased distribution because a house with an only child only gets reported once, viz., by that single child. (To reiterate, the respondent:children ratio for the actual distribution is always 1:1.) 

>> Differences between the distributions emerge when we consider what percentage of households contain any number of children other than 1, however. In the case of 0, the biased distribution tells us that there are no households with 0 children under 18--clearly ridiculous yet sound, considering there is no set of children who do not count themselves as members of their own households (strictly speaking--not accounting for, say, children who have been disowned or emancipated minors who may not *consider* themselves members of their families' households, a very interesting problem to do with how people answer surveys). In the case of numbers > 1, the biased distribution consistently overcounts because the ratio between respondents and children will be 1:>1. Interestingly, the biased distribution is off by about the same amount for households with 2 children and households with 3, which has to do with there being fewer households with 3 children than with 2.

>> This is one of those stories where a single statistic may very well say it all: the mean number of children under 18 per household in the biased distribution is 2.4x that in the actual one. Here's the code:
```
# Print means for actual and biased PMFs
print 'actual mean:', actual_pmf.Mean()
print 'biased mean:', biased_pmf.Mean()
```
>> and output:
```
actual mean: 1.02420515504
biased mean: 2.40367910066
```

>> However we may tend to assume that bias "matters", we now have shown just how much havoc a simple form of bias can statistically wreak. The biased distribution of number of children under 18 in a given household is a whopping 240% greater than the actual distribution of the same.