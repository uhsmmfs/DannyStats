import numpy
from scipy import stats

SIGNIFICANCE_LEVEL = 0.05 # Significance level
SD_SIGNIFICANCE = 2 # Standard deviation significance level

def set_significance(significance_value = 0.05):
    """
    Sets the value of the level of significance (α) used in statistical tests
    """
    
    if significance_value > 1 or significance_value <= 0:
        print("Error: Please input a significance level greater than 0 and less than 1")
        return
        
    global SIGNIFICANCE_LEVEL
    
    SIGNIFICANCE_LEVEL = significance_value
    print("The significance level (α) has been set to " + str(significance_value))
    
def set_sd_significance(significance_value = 2):
    """
    Sets the value of the level of significance (α) used in statistical tests
    """
    
    if  significance_value <= 0:
        print("Error: Please input a significance level greater than 0")
        return
        
    global SD_SIGNIFICANCE
    
    SD_SIGNIFICANCE = significance_value
    print("The standard deviation significance level (α) has been set to " + str(significance_value) + " standard deviations")

def mean(sample):
    """
    Calculate the mean value of a given sample
    """
    
    return numpy.mean(sample)
    
def standard_deviation(sample):
    """
    Calculate the standard deviation of a given sample
    """
    
    return numpy.std(sample)

def shapiro(sample):
    """
    Determines whether or not a sample follows a normal distribution based on the Shapiro-Wilk test. Returns a boolean True or False, the p-value, as well as the test statistic
    """
    
    result = stats.shapiro(sample)
    statistic = result.statistic
    pvalue = result.pvalue
    
    if (pvalue >= SIGNIFICANCE_LEVEL): # Do not reject the null hypothesis
        isNormal = True
        print("YES, your sample appears to be normally distributed.\nThe p-value of the test was " + str(pvalue) + ", which was greater than the significance interval α = " + str(SIGNIFICANCE_LEVEL) + ".\nThis means there is a " + str(pvalue) + "% chance that the observed data could have come from a normal distribution.\nTherefore, you can use parametric methods in your analysis.")
    else: # Reject the null hypothesis
        isNormal = False
        print("NO, your sample does not appear to be normally distributed.\nThe p-value of the test was " + str(pvalue) + ", which was lower than the significance interval α = " + str(SIGNIFICANCE_LEVEL) + ".\nThis means there is a " + str(pvalue) + "% chance that the observed data could have come from a normal distribution.\nTherefore, you should not use any parametric methods in your analysis.")
    
    return isNormal, pvalue, statistic

def anderson(sample):
    """
    Determines whether or not a sample follows a normal distribution based on the Anderson-Darling test. Returns a boolean True or False and the test statistic
    """
    
    result = stats.anderson(sample, dist='norm')
    statistic = result.statistic
    criticalValues = result.critical_values
    significanceLevels = result.significance_level
    
    if (SIGNIFICANCE_LEVEL * 100 in significanceLevels):
        levelIndex = numpy.where(significanceLevels == SIGNIFICANCE_LEVEL * 100)
    else:
        print("Sorry! The set significance level (" + str(SIGNIFICANCE_LEVEL) + ") is not standard, and the critical value for that significance level is unknown. Please try again with one of the following significance levels: 0.01, 0.025, 0.05, 0.1, or 0.15.\n(Tip: You can set the significance level with the set_significance() method!)")
        return
    
    value = criticalValues[levelIndex]
    
    print("The test statistic is " + str(statistic) + ".")
    
    if (statistic < value): # Do not reject the null hypothesis at this significance level
        isNormal = True
        print("YES, your sample appears to be normally distributed. At the " + str(SIGNIFICANCE_LEVEL * 100) + "% significance level, the test statistic is lower than the critical value of " + str(value[0]) + ". Therefore, we do not reject the null hypothesis. The data appears to be normally distributed, and you can use parametric methods in your analysis.")
    else: # Reject the null hypothesis at this significance level
        isNormal = False
        print("NO, your sample does not appear to be normally distributed. At the " + str(SIGNIFICANCE_LEVEL * 100) + "% significance level, the test statistic is greater than or equal to the critical value of " + str(value[0]) + ". Therefore, we reject the null hypothesis. The data does not appear to be normally distributed, and you should not use any parametric methods in your analysis.")
    
    return isNormal, statistic

def kolmogorov(sample):
    """
    Determines whether or not a sample follows a normal distribution based on the Kolmogorov-Smirnov test. Returns a boolean True or False, the p-value, as well as the test statistic
    """
    
    sampleMean, sd = mean(sample), standard_deviation(sample)
    result = stats.kstest(sample, 'norm', args=(sampleMean, sd))
    statistic = result.statistic
    pvalue = result.pvalue
    
    if (pvalue >= SIGNIFICANCE_LEVEL): # Do not reject the null hypothesis
        isNormal = True
        print("YES, your sample appears to be normally distributed.\nThe p-value of the test was " + str(pvalue) + ", which was greater than the significance interval α = " + str(SIGNIFICANCE_LEVEL) + ".\nThis means there is a " + str(pvalue) + "% chance that the observed data could have come from a normal distribution.\nTherefore, you can use parametric methods in your analysis.")
    else: # Reject the null hypothesis
        isNormal = False
        print("NO, your sample does not appear to be normally distributed.\nThe p-value of the test was " + str(pvalue) + ", which was lower than the significance interval α = " + str(SIGNIFICANCE_LEVEL) + ".\nThis means there is a " + str(pvalue) + "% chance that the observed data could have come from a normal distribution.\nTherefore, you should not use any parametric methods in your analysis.")
    
    return isNormal, pvalue, statistic

def d_agostino(sample):
    """
    Determines whether or not a sample follows a normal distribution based on D'Agostino's K-squared test. Returns a boolean True or False, the p-value, as well as the test statistic
    """
    
    result = stats.normaltest(sample)
    statistic = result.statistic
    pvalue = result.pvalue
    
    if (pvalue >= SIGNIFICANCE_LEVEL): # Do not reject the null hypothesis
        isNormal = True
        print("YES, your sample appears to be normally distributed.\nThe p-value of the test was " + str(pvalue) + ", which was greater than the significance interval α = " + str(SIGNIFICANCE_LEVEL) + ".\nThis means there is a " + str(pvalue) + "% chance that the observed data could have come from a normal distribution.\nTherefore, you can use parametric methods in your analysis.")
    else: # Reject the null hypothesis
        isNormal = False
        print("NO, your sample does not appear to be normally distributed.\nThe p-value of the test was " + str(pvalue) + ", which was lower than the significance interval α = " + str(SIGNIFICANCE_LEVEL) + ".\nThis means there is a " + str(pvalue) + "% chance that the observed data could have come from a normal distribution.\nTherefore, you should not use any parametric methods in your analysis.")
    
    return isNormal, pvalue, statistic
    
def test_normality(sample):
    """
    Test if a sample typically follows a normal distribution. Returns a boolean True or False, the p-value, as well as the test statistic
    """
    
    # Check sample size to determine which test to perform
    n = len(sample)
    
    if n < 50: # Small sample size
        
        print("Your sample size was relatively small (n < 50), so I decided to run the Shapiro-Wilk test on your sample to test for normality.")
        shapiro(sample)
    elif n < 2000: # Moderate sample size
        
        print("Your sample size was moderately sized (n < 2000), so it was a choice between the Shapiro-Wilk test and the Anderson-Darling test. (Tip: Note that D'Agostino's K-squared test may also be suitable for this situation! However, the test requires a sufficiently large sample size in order to produce accurate results, so I decided to omit it from consideration this time)\n")
        
        if (SIGNIFICANCE_LEVEL not in {0.01, 0.025, 0.05, 0.1, 0.15}): # If significance level isn't standard
            print("The set significance level (" + str(SD_SIGNIFICANCE) + ") isn't a standard value, so I decided to use the Shapiro-Wilk test.\n")
            shapiro(sample)
        else:
            sd = standard_deviation(sample) # Calculate the standard deviation to decide which test to use
            
            if (sd > SD_SIGNIFICANCE): # Anderson-Darling test
                print("I calculated the standard deviation of your sample to be " + str(sd) + ", which was greater than the significance level of " + str(SD_SIGNIFICANCE) + " standard deviations.\nTherefore, I decided to use the Anderson-Darling test for additional sensitivity to tail deviations.\n")
                anderson(sample)
            else: # Shapiro-Wilk test
                print("I calculated the standard deviation of your sample to be " + str(sd) + ", which was less than the significance level of " + str(SD_SIGNIFICANCE) + " standard deviations.\nTherefore, I decided to use the Shapiro-Wilk test for high sensitivity to deviation.\n")
                shapiro(sample)

    else: # Large sample size
        
        print("Your sample size was relatively large (n >= 2000), so it was a choice between the Kolmogorov-Smirnov test (K-S test) and D'Agostino's K-squared test.\n")
        
        sd = standard_deviation(sample) # Calculate the standard deviation to decide which test to use
        
        if (sd > SD_SIGNIFICANCE): # D'Agostino's K-squared test
            print("I calculated the standard deviation of your sample to be " + str(sd) + ", which was greater than the significance level of " + str(SD_SIGNIFICANCE) + " standard deviations.\nTherefore, I decided to use D'Agostino's K-squared test for additional sensitivity to tail deviations.\n")
            d_agostino(sample)
        else: # Kolmogorov-Smirnov test
            print("I calculated the standard deviation of your sample to be " + str(sd) + ", which was less than the significance level of " + str(SD_SIGNIFICANCE) + " standard deviations.\nTherefore, I decided to use the Kolmogorov-Smirnov test for emphasis on the center of the distribution.\n")
            kolmogorov(sample)