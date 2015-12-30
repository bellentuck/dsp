[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

>> Based on National Survey of Family Growth (NSFG) data from ThinkStats, let's explore the relationship between the birth weight of babies and the ages of their mothers. What might the correlation between birth weight and mother's age look like? To what degree, in other words, do birth weight and mother's age vary together (exhibit covariance), and what is the scope or *effect size* of this relationship?

>> (1) First, let's extract, transform, and load up the data into a nice dataframe, beginning by importing modules:
```
import nsfg
import thinkstats2
import first
```
>> Next, I'm not sure what the `RandomSeed` method is good for in this context (from what I can gather it seeds a NumPy Mersenne Twister pseudo-random number generator, but this doesn't seem to affect scatter-plotting one way or the other), but here it is so I remember to ask about it at some point, because Downey certainly likes to use it:
```
thinkstats2.RandomSeed(17)
```
>> Next, let's make dataframes for live births, as well as for `firsts` and `others`--I'm not sure why including the latter two categories is necessary but if I don't include them I get an Attribute Error ("'tuple' object has no attribute 'dropna'"). Then, we drop the rows without values via `first`'s `dropna` method, analagous to pandas', as far as I can tell.
```
live, firsts, others = first.MakeFrames()
live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
```

>> (2) Now that we've loaded up the data we can go about making determining the extent to which birth weight and mother's age vary together. We can do this by computing Pearson's and Spearman's correlations. 

>> Pearson's ranges from -1.0 to +1.0, and from what I can gather Spearman's does as well. The higher the absolute value, the stronger the correlation. 
```
ages = live.agepreg
weights = live.totalwgt_lb
print('thinkstats2 Corr', thinkstats2.Corr(ages, weights))
print('thinkstats2 SpearmanCorr',
      thinkstats2.SpearmanCorr(ages, weights))
```
>> Here's the output for Pearson's and Spearman's correlations, respectively:
```
('thinkstats2 Corr', 0.068833970354109056)
('thinkstats2 SpearmanCorr', 0.094610041096582262)
```
>> So Pearson's correlation is a little less than 0.07, while Spearman's is a bit greater than 0.09: both are quite small. So the relationship between the variables is weak. The ~0.02 difference between the values suggests possible outliers and/or a non-linear relationship.

>> (3) The numbers do not tell a full enough story by themselves, however. We want a more dynamic representation of the data. Answering questions about correlation entails getting in the right mindset to be able to think through questions about correlation. And getting into this sweet spot entails visualizing our data in ways that will be good to think with. What we need are what have been philosophically dubbed "perspicuous representations" (following from Wittgenstein and more indirectly from Marx): shorthand sum-ups of info that are going to allow us to "get" what's going on. Basically we need effective strategies to get into an analytic mindset from which to derive our insights, and data visualization is one such sort of practice that will make the numbers stick with us.

>> (If I learned one lesson doing this exercise it's that being able to quickly chalk up a bunch of visualizations is far more significant than coming up with an eloquently-coded "solution," at least at this stage of the game.)

>> One of the simplest visualizations, and the one I'll be using to derive some elementary insights about the relationship between birth weight and mother's age, is the scatter plot--a smattering of data-points across a graph. 

>> Here's the (possibly redundant; I'm trying to scrape something together here from Downey) code for a ScatterPlot function, taken from Downey:
```
import thinkplot
def ScatterPlot(ages, weights, alpha=1.0):
    """                              
    ages: sequence of float                                                    
    weights: sequence of float                                                 
    alpha: float (makes points partly transparent)                         
    """
    thinkplot.Scatter(ages, weights, alpha=alpha)
    thinkplot.Config(xlabel='age (years)',
                     ylabel='weight (lbs)',
                     xlim=[10, 45],
                     ylim=[0, 15], 
                     legend=False)
```
>> Calling `ScatterPlot` on `ages` and `weights`, with `alpha` set to `0.1`--`ScatterPlot(ages, weights, alpha=0.1)`--we get the following plot:

>> [1] + link

>> Calling Downey's method `BinnedPercentiles` on `live`--`BinnedPercentiles(live)`--in between steps (1) and (2) adds lines the the plot representing 25th, 50th, and 75th percentiles:
```
def BinnedPercentiles(df):
    #Bin the data by age and plot percentiles of weight for each bin.          
    #df: DataFrame                                                             
    bins = np.arange(10, 48, 3)
    indices = np.digitize(df.agepreg, bins)
    groups = df.groupby(indices)
    ages = [group.agepreg.mean() for i, group in groups][1:-1]
    cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups][1:-1]
    thinkplot.PrePlot(3)
    for percent in [75, 50, 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        thinkplot.Plot(ages, weights, label=label)
```
>> [2] + link

>> Birth weight seems slightly to increase as mother's age increases, but the effect is miniscule and, as a result, the slope of the data (and that of the percentile lines) seems nearly flat; i.e., 0.

>> Most of the data appears to hover between 15-40 years on the x-axis and between 5-10 lbs on the y-axis. Let's zoom in to get a better look by changing the values of `xlim` and `ylim` in `ScatterPlot`:
```
    thinkplot.Config(xlabel='age (years)',
                     ylabel='weight (lbs)',
                     xlim=[15, 40], #was [10,45]
                     ylim=[5, 10],  #was [0,15]
                     legend=False)
```
>> [3] + link

>> At this level the data appears to concentrate around whole numbers on the y-axis: 6, 7, 8, 9. Probably this is because weights near whole numbers get rounded to whole numbers. But we're tracking a very subtle increase in weight, so the rounding is a problem. Fortunately, we can fix it by jittering the data:
```
ages = thinkstats2.Jitter(ages, 1.3)
weights = thinkstats2.Jitter(weights, 0.5)
```
>> Here's how things shape up without `BinnedPercentiles`:

>> [4] + link

>> And with `BinnedPercentiles`:

>> [5] + link

>> Personally I think the lines are a bit distracting. They seem to each be subtle variations on the theme of there tending to be a slight increase in average birth weight as mothers' ages go up, a conclusion we can already gather from the picture without the binned percentile lines, especially in conjunction with Pearson's and Spearman's correlations. The scatter plot gives us the big picture, and Pearson's and Spearman's correlations give us a more precise (read: mathematical) sense of how strong the correlation between birth weight and mother's age is. 