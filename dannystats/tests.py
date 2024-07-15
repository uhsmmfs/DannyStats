from scipy import stats

ALPHA_SIGNIFICANCE = 0.05

def set_significance(significance_value = 0.05):
    """
    Sets the value of the level of significance (α) used in statistical tests
    """
    
    if significance_value > 1 or significance_value <= 0:
        print("Error: Please input a significance level greater than 0 and less than 1")
        return
        
    global ALPHA_SIGNIFICANCE
    
    ALPHA_SIGNIFICANCE = significance_value
    print("The significance level (α) has been set to " + str(significance_value))