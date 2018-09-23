def getWays(n, coins):
    """Gets the number of ways the desired amount 'n' can
    be made with the given coins.
    
    Arguments:
        n {integer} -- The desired amount.
        coins {list} -- A list of coins.
    
    Returns:
        integer -- The amount of ways.
    """

    # base case of 0 must be 1
    totals = [1] + [0] * n
    for i in range(len(coins)): 
        for j in range(coins[i], n + 1): 
            totals[j] += totals[j-coins[i]]
    return totals[-1]