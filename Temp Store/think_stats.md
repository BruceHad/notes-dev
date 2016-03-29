## ThinkStats Chapter 2 - Descriptive Statistics

### Summary Stats

Mean - μ = 1/n * Σxi
Median
Variance - σ**2 = 1/n * Σ(xi - μ)**2
Standard Deviation = √σ

Median and Mean are two measures of the average, expected value or central tendancy of a data set. How well they represent the expected, central tendancies depends on the data. And they don't tell the full story. 

Variance helps get a picture of the data by describing how far it spreads from the centre. It is the average (mean) of the squared sum of the 'deviations from the mean'. Squaring the deviations of the mean get's rid of the sign. The square root of the variance is called Standard Deviation.

### Distributions

Summary stats like those described above can obscure the data, simplifying it too much. It can be better to look at the distribution instead, which gives a fuller picture of the data.

Distribution is commonly represented by a histogram, which charts the frequency that each value appears in the data set or probability that it will appear, which is the frequence divided by the sample size (n).

In python we can calculate the histogram for a dataset like so:

    hist = {}
    for x in dataset:
        hist[x] = hist.get(x,0)+1

This sets up a dictionary and populates it with each value in the dataset and the number of times it occurs.

Converting from frequency to probability (by dividing by sample size) is known as normalisation. Normalising the dataset lets you compare datasets that have different sample sizes.

The normalised histogram is sometimes called the PDF (probability mass function).