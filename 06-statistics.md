# Statistics

Read Allen Downey's [Think Stats (second edition)](http://greenteapress.com/thinkstats2/) and [Think Bayes](http://greenteapress.com/thinkbayes/) for getting up to speed with core ideas in statistics and how to approach them programmatically. Both books are completely available online, or you can buy physical copies if you would like.

[<img src="img/think_stats.jpg" title="Think Stats"/>](http://greenteapress.com/thinkstats2/)
[<img src="img/think_bayes.png" title="Think Bayes" style="float: left"; />](http://greenteapress.com/thinkbayes/)  

## Instructions

The ThinkStats book is approximately 200 pages in length.  It is recommended you read the entire book, particularly if you are less familiar with introductory statistical concepts.

The stats exercises have been chosen to introduce/solidify some relevant statistical concepts related to data science.  The solutions for these exercises are available in the ThinkStats repository on GitHub.  You should focus on understanding the statistical concepts, python programming and interpreting the results.  If you are stuck, review the solutions and recode the python in a way that is more understandable to you. 

For example, in the first exercise, the author has already written a function to compute Cohen's D.  You could import it, or you could write your own to practice python and develop a deeper understanding of the concept. 

Complete the following exercises along with the questions in this file. They come from Think Stats, and some can be solved using code provided with the book. The preface of Think Stats [explains](http://greenteapress.com/thinkstats2/html/thinkstats2001.html#toc2) how to use the code.  

Communicate the problem, how you solved it, and the solution, within each of the following [markdown](https://guides.github.com/features/mastering-markdown/) files. (You can include code blocks and images within markdown.)

---

### Instructions for cloning the repo 
Using the code referenced in the book, follow the step-by-step instructions below.  

**Step 1. Create a directory on your computer where you will do the prework.  Below is an example:**

```
(Mac):      /Users/yourname/ds/metis/prework  
(Windows):  C:/ds/metis/prework
```

**Step 2. cd into the prework directory.  Use GitHub to pull this repo to your computer.**

```
$ git clone https://github.com/AllenDowney/ThinkStats2.git
```

**Step 3.  Put your ipython notebook or python code files in this directory (that way, it can pull the needed dependencies):**

```
(Mac):     /Users/yourname/ds/metis/prework/ThinkStats2/code  
(Windows):  C:/ds/metis/prework/ThinkStats2/code
```

---

###Required Exercises

###Q1. [Think Stats Chapter 2 Exercise 4](statistics/2-4-cohens_d.md) (effect size of Cohen's d)  
Cohen's D is an example of effect size.  Other examples of effect size are:  correlation between two variables, mean difference, regression coefficients and standardized test statistics such as: t, Z, F, etc. In this example, you will compute Cohen's D to quantify (or measure) the difference between two groups of data.   

You will see effect size again and again in results of algorithms that are run in data science.  For instance, in the bootcamp, when you run a regression analysis, you will recognize the t-statistic as an example of effect size.

###Q2. [Think Stats Chapter 3 Exercise 1](statistics/3-1-actual_biased.md) (actual vs. biased)
This problem presents a robust example of actual vs biased data.  As a data scientist, it will be important to examine not only the data that is available, but also the data that may be missing but highly relevant.  You will see how the absence of this relevant data will bias a dataset, its distribution, and ultimately, its statistical interpretation.

###Q3. [Think Stats Chapter 4 Exercise 2](statistics/4-2-random_dist.md) (random distribution)  
This questions asks you to examine the function that produces random numbers.  Is it really random?  A good way to test that is to examine the pmf and cdf of the list of random numbers and visualize the distribution.  If you're not sure what pmf is, read more about it in Chapter 3.  

###Q4. [Think Stats Chapter 5 Exercise 1](statistics/5-1-blue_men.md) (normal distribution of blue men)
This is a classic example of hypothesis testing using the normal distribution.  The effect size used here is the Z-statistic. 

As a bonus (optional) step, write out the null hypothesis, alternative hypothesis, critical value for testing, and the associated p-value.  You will see p-values in virtually every algorithm output during the bootcamp.  And from this exercise, you will know how the p-value has been computed and its relationship to a distribution.

###Q5. [Think Stats Chapter 7 Exercise 1](statistics/7-1-weight_vs_age.md) (correlation of weight vs. age)
In this exercise, you will compute the effect size of correlation.  Correlation measures the relationship of two variables, and data science is about exploring relationships in data.    

###Q6. [Think Stats Chapter 8 Exercise 2](statistics/8-2-sampling_dist.md) (sampling distribution)
In the theoretical world, all data related to an experiment or a scientific problem would be available.  In the real world, some subset of that data is available.  This exercise asks you to take samples from an exponential distribution and examine how the standard error and confidence intervals vary with the sample size.

###Q7. Bayesian (Elvis Presley twin) 

Bayes' Theorem is an important tool in understanding what we really know, given evidence of other information we have, in a quantitative way.  It helps incorporate conditional probabilities into our conclusions.

Elvis Presley had a twin brother who died at birth.  What is the probability that Elvis was an identical twin? Assume we observe the following probabilities in the population: fraternal twin is 1/125 and identical twin is 1/300.  

>> (1) Let A = fraternal twins

>> (2) Let B = identical twins

>> (3) Let C = twin brothers

>> (4) p(A) = prior probability for fraternal twins = 1/125

>> (5) p(C|A) = likelihood that fraternal twins are boys 
>> = 1/2 * 1/2 = 1/4, given even chances of a twin's being male or female

>> (6) p(B) = prior probability for identical twins = 1/300

>> (7) p(C|B) = likelihood that identical twins are male 
>> = 1/2 * 1 = 1/2, as identical twins share the same DNA and are therefore the same sex

>> (8) p(C) = normal probability of twin brothers = [p(A) * p(C|A)] + [p(B) * p(C|B)], following from Law of Total Probability = (1/125 * 1/4) + (1/300 * 1/2) = 1/500 + 1/600 = 6/3000 + 5/3000 = 11/3000

>> (9) p(B|C) = posterior probability of identical twins given twin brothers = [p(B) * p(C|B)] / p(C), following from Bayes' Theorem = (1/300 * 1/2) / 11/3000 = 1/600 * 3000/11 = (1/600 * 3000)/11 = 5/11

>> The probability that Elvis was an identical twin is 5/11, or a little over 45%. 5:6 odds--who knew! (probably many).

---

###Q8. Bayesian &amp; Frequentist Comparison  
How do frequentist and Bayesian statistics compare?

>> Probability:
Frequentist probability = normative frequency (frequency over series of trials).
Bayesian probability = subjective degree of belief (updated state of knowledge).

>> Estimation: 
Frequentist confidence intervals = Bayesian probabilities.

>> Sampling:
Frequentist sampling is a repeatable process that can be theoretically iterated infinite times (studies are taken to be repeatable).
Bayesians observe fixed data from already-taken samples (studies are taken to be fixed).

>> Hypothesis Testing:
Frequentist M.O. = probability of data, given hypothesis. Data is random (sample-dependent); hypotheses/parameters are fixed (either true or false). Compare p-hat to a p-level, where p = probability of getting a result as extreme as the observed data if the null hypothesis were true, to determine cause for (a) statistical significance and (b) rejection of the null hypothesis. 
Bayesian M.O. = probability of hypothesis, given data. Data is fixed (observed from a realized sample); hypotheses/parameters are random/unknown (can be described probabilistically). Use Bayes' Theorem to calculate p(H|D). Express the relationship between null and alternative hypotheses in terms of odds (posterior probability). There are no sufficiently "significant" results, just better odds.

>> Results:
Frequentist = statements about the world.
Bayesian = statements about our beliefs.

>> Strengths of frequentist statistics:
Calculations are relatively simple.
Explanations are technically objective.

>> Criticisms of frequentist statistics:
Calculations do not account for prior knowledge.
Explanations are jargony and counter-intuitive.

>> Strengths of Bayesian statistics:
Calculations account for prior knowledge.
Explanations make intuitive sense in natural language.

>> Criticisms of Bayesian statistics:
Calculations are relatively complex.
Explanations are technically subjective (priors lack objectivity in that they don't have to come from anywhere in particular, but rather express subjective states of knowledge. They tend to be drawn from previous studies, published work, researcher intuition, substantive experts, convenience, nonparametric data, and other data sources).

>> "A frequentist basically says, 'The world is a certain way, but I don’t know how it is. Further, I can’t necessarily tell how the world is just by collecting data, because data are always finite and noisy. So I’ll use statistics to line up the alternative possibilities, and see which ones the data more or less rule out.' A Bayesian basically says, 'I don’t know how the world is. All I have to go on is finite data. So I’ll use statistics to infer something from those data about how probable different possible states of the world are.'" -- Jeremy Fox, "Frequentist vs. Bayesian Statistics: Resources to Help You Choose"

>> "Bayes [1] makes the additional assumption of a prior over θ [some underlying world state for which p(X1, . . . , Xn | θ) expresses a likelihood function over possible observations], and [2] optimizes for average-case performance rather than worst-case performance. It follows, then, that Bayes is the superior method whenever we can obtain a good prior and when good average-case performance is sufficient. However, if we have no way of obtaining a good prior, or when we need guaranteed performance, frequentist methods are the way to go.

>> "A nice middle-ground between purely Bayesian and purely frequentist methods is to use a Bayesian model coupled with frequentist model-checking techniques; this gives us the freedom in modeling afforded by a prior but also gives us some degree of confidence that our model is correct." -- Jacob Steinhardt, "Beyond Bayesians and Frequentists"

>> Also see: 

>> Ben-Gal, "Bayesian Networks" (2007) --- Encyclopedia of Statistics in Quality and Reliability entry; BNs look a lot like OOP class-based structures --- http://www.eng.tau.ac.il/~bengal/BN.pdf

>> Steinhardt, "Beyond Bayesians and Frequentists" (2012) --- short piece tying approaches to machine learning use cases --- http://cs.stanford.edu/~jsteinhardt/stats-essay.pdf 

>> [links don't seem to link so google titles]

---

###Optional Exercises

The following exercises are optional, but we highly encourage you to complete them if you have the time.

###Q9. [Think Stats Chapter 6 Exercise 1](statistics/6-1-household_income.md) (skewness of household income)
###Q10. [Think Stats Chapter 8 Exercise 3](statistics/8-3-scoring.md) (scoring)
###Q11. [Think Stats Chapter 9 Exercise 2](statistics/9-2-resampling.md) (resampling)

## More Resources

Some people enjoy video content such as Khan Academy's [Probability and Statistics](https://www.khanacademy.org/math/probability) or the much longer and more in-depth Harvard [Statistics 110](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo). You might also be interested in the book [Statistics Done Wrong](http://www.statisticsdonewrong.com/) or a very short [overview](http://schoolofdata.org/handbook/courses/the-math-you-need-to-start/) from School of Data.







