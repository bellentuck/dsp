[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

>> "The distribution of income is famously skewed to the right" (Downey). In other words: mean household income is greater than median household income, influenced by a minute number of highest earners. The extent to which income distribution is right-skewed is thus dependent on the assumed upper bound.

>> We can visualize these trends using household income ("hinc") data from the Current Population Survey (CPS). Downey has converted 2013 CPS hinc data from `hinc06.xls`, an Excel spreadsheet, to `hinc06.csv`. `hinc2.py` reads the file nand transforms the data.
```
import numpy as np
import density
import hinc
import hinc2
import thinkstats2
df = hinc.ReadData()
```
>> "The dataset is in the form of a series of income ranges and the number of 
respondents who fell in each range. The lowest range includes respondents who 
reported annual household income 'Under $5000.' The highest range includes 
respondents who made '$250,000 or more.'

>> "To estimate mean and other statistics from these data, we have to make some assumptions about the lower and upper bounds, and how the values are distributed in each range. `hinc2.py provides `InterpolateSample`, which shows one 
way to model this data. It takes a DataFrame with a column, income, that 
contains the upper bound of each range, and freq, which contains the number of 
respondents in each frame.

>> "It also takes log_upper, which is an assumed upper bound on the highest range, expressed in log10 dollars. The default value, log_upper=6.0 represents the assumption that the largest income among the respondents is 10^6, or one million dollars" (Downey).
```
log_sample = hinc2.InterpolateSample(df, log_upper=6.0)
```
>> "`InterpolateSample` generates a pseudo-sample; that is, a sample of household incomes that yields the same number of respondents in each range as the actual data. It assumes that incomes in each range are equally spaced on a log10 scale" (Downey).

>> (1) Household income vs. CDF for `log_upper=6.0`: Here's how to plot household income (x-axis) against CDF (y-axis), following Downey's code:
```
log_cdf = thinkstats2.Cdf(log_sample)
thinkplot.Cdf(log_cdf)
thinkplot.Show(xlabel='household income',
                   ylabel='CDF')
sample = np.power(10, log_sample)
mean, median = density.Summarize(sample)
```
>> `np.power` is a NumPy method that raises the first argument to powers from the second. (Arguments can be individual numbers or groups like arrays.) In the case of our sample, `np.power` converts the x-axis household income exponents back to actual income levels.

>> Here's the graph and output:

>> [1] <a href="https://github.com/bellentuck/dsp/blob/20c20065643d8ee1543a94660f70955c3dd3ad58/.thinkstats_skewness_1.png"><img src="img/.thinkstats_skewness_1.png" style="width: 100px;" target="_blank"></a>
```
mean 74278.7075312
std 93946.9299635
median 51226.4544789
skewness 4.94992024443
pearson skewness 0.736125801914
```
>> Following Downey, let's figure out the fraction of households reporting a taxable income below the mean.
```
cdf = thinkstats2.Cdf(sample)
print('cdf[mean]', cdf[mean])
```
>> Here's the output:
```
('cdf[mean]', 0.66000587956687196)
```
>> 2/3 of households report incomes below the mean.

>> (2) Household income vs. PDF for `log_upper=6.0`:
```
pdf = thinkstats2.EstimatedPdf(sample)
thinkplot.Pdf(pdf)
thinkplot.Show(xlabel='household income',
               ylabel='PDF')
```
>> [2] <a href="https://github.com/bellentuck/dsp/blob/20c20065643d8ee1543a94660f70955c3dd3ad58/.thinkstats_skewness_2.png"><img src="img/.thinkstats_skewness_2.png" style="width: 100px;" target="_blank"></a>

>> Next, let's observe what happens when we change the upper bound. 

>> (3) Household income vs. CDF for `log_upper=5.5`: 

>> [3] <a href="https://github.com/bellentuck/dsp/blob/20c20065643d8ee1543a94660f70955c3dd3ad58/.thinkstats_skewness_3.png"><img src="img/.thinkstats_skewness_3.png" style="width: 100px;" target="_blank"></a>

>> (4) Household income vs. PDF for `log_upper=5.5`:

>> [4] <a href="https://github.com/bellentuck/dsp/blob/20c20065643d8ee1543a94660f70955c3dd3ad58/.thinkstats_skewness_4.png"><img src="img/.thinkstats_skewness_4.png" style="width: 100px;" target="_blank"></a>

>> Here are the outputs:
```
mean 65308.9999054
std 52150.9795657
median 51226.4544789
skewness 1.17955077982
pearson skewness 0.810102449294
('cdf[mean]', 0.60345587875026541)
```
>> With a maximum income of $250,000, 60% of households report incomes below the mean (compared with 67% from a $1,000,000 income upper bound).

>> Interestingly, moment-based skewness reveals more about the difference in the PDF graphs than does Pearson's skewness. Moment-based skewness is almost 3x greater given an upper bound of 10^6 than 10^5.5, which reflects the stark skewness of graph (2) compared to (4).

>> Why does Pearson's skewness go slightly down given a higher upper bound? Downey hypothesizes that "increasing the upper bound has a modest effect on the mean, and a stronger effect on standard deviation.  Since std is in the denominator with exponent 3, it has a stronger effect on the result."

>> Downey adds that, as opposed to Pearson's skewness, "A better choice [for elucidating income distribution] is a statistic that has meaning in context, like the fraction of people with income below the mean.  Or something like the Gini coefficient designed to quantify a property of the distribution (like the relative difference we expect between two random people)" (`chap06soln.py`).