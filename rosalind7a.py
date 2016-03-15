def prob(k,m,n):
    total = k+m+n
    domPercent=k/total
    heteroPercent=m/total
    recesivePercent=n/total
    
    twoDoms=domPercent*((k-1)/(total-1))
    domHet=domPercent*((m)/(total-1))
    domR=domPercent*((n)/(total-1))
    
    hetDom=heteroPercent*((k)/(total-1))
    hetHet=heteroPercent*((m-1)/(total-1))
    hetR=heteroPercent*((n)/(total-1))
    
    rDom=recesivePercent*((k)/(total-1))
    rHet=recesivePercent*((m)/(total-1))
    
    totalP=twoDoms+domHet+domR+hetDom+(.75*hetHet)+(.5*hetR)+rDom+(.5*rHet)
    print(totalP)

prob(2,2,2)