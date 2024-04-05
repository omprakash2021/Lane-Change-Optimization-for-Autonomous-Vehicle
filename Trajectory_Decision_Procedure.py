
def trajectoryDecision(x_fo, x_nr, lowerBound, upperBound):
    
    if(x_nr <= lowerBound):
        if(lowerBound <= x_fo and x_fo <= upperBound):
            # the current velocity and weight value do not need to change
            return ["optimal", lowerBound, upperBound]

        elif(x_fo >= upperBound):
            # reducing the speed if not warks then decrease the weight value
            return ["more than upperBound", lowerBound, upperBound]

        elif(x_fo <= lowerBound):
            # should accelerate and increase speed or if not work increase weight
            return ["less than lowerBound", lowerBound, upperBound]

    elif(lowerBound <= x_nr and x_nr <= upperBound):
        if(x_fo >= upperBound):
            # decelerate to decrease speed and if not work decrease weight value
            return ["more than upperBound", lowerBound, upperBound]
        
        elif(x_nr <= x_fo and x_fo <= upperBound):
            # the current velocity and weight value do not need to change
            return ["optimal", lowerBound, upperBound]
    
    elif(x_nr >= upperBound):
        # decelerate to decrease speed and if not work decrease the weight value
        return ["more than upperBound", lowerBound, upperBound]
    
    # print(7)
    # print(lowerBound < x_nr)
    # print(x_nr < upperBound)
    # print(lowerBound < x_nr and x_nr < upperBound)
    print(f"2) x_fo: {x_fo :.3f}, x_nr: {x_nr :.3f}, lb: {lowerBound :.3f}, ub: {upperBound :.3f}\n")