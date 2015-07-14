#!/usr/local/bin/python

# Calculates the binomial population proportion
#
# Reference: "On the Estimation of Confidence Intervals for Binomial Population
# Proportions in Astronomy: The Simplicity and Superiority
# of the Bayesian Approach" by Ewan Cameron

import math
import numpy as np
import scipy.stats.distributions as dist
from scipy.special import erf

def fac(x):
  return math.factorial(x)

def main():

        N = int(raw_input('\nTotal number of observed objects? '))
        k = int(raw_input('Number of variables? '))
        c = erf(1./np.sqrt(2))                          # How many standard deviations?

        p_upper = dist.beta.ppf(1-(1-c)/2.,k+1,N-k+1)
        p_lower = dist.beta.ppf((1-c)/2.,k+1,N-k+1)

        print "\nProbability of finding",k,"variable objects amongst",N,"observed objects:"
        print "\n\t+",round(100.*(p_upper-float(k)/N),1),"%"
        print "    ",round(float(k)/N*100.,1)
        print "\t-",round(100.*(float(k)/N-p_lower),1),"%\n"

if __name__ == '__main__':
        main()
