#Pretty brute force, but works
#Used to determine the probability of an offspring with the
#dominant trait. 
def mendel(dom, het, rec):
    pop = dom + het + rec
    #Dominance
    prob_D = dom/pop
    #Het dom
    prob_HD = (het/pop * dom/(pop-1))
    #Het het
    prob_HH = (het/pop * (het-1)/(pop-1)) * .75
    #het_recessive
    prob_HR = (het/pop * rec/(pop-1)) * .5
    #Recessive dom
    prob_RD = (rec/pop * dom/(pop-1))
    #Recessive het
    prob_RH = (rec/pop * het/(pop-1)) * .5
    prob =prob_D + prob_HD + prob_HH + prob_HR + prob_RD + prob_RH
    return prob

mendel(18, 21, 26)

##Other example by Myke which is 1000x simpler
def firstLaw(k,m,n):
    #Get sum
   N = float(k+m+n)
   #Uses the probability of getting no dominant alleles
   return(1 - 1/N/(N-1)*(n*(n-1) + n*m + m*(m-1)/4.))