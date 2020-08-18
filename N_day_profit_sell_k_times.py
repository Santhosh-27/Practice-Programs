'''
Stock Buy Sell to Maximize Profit
The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days. 
For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by buying on day 0, selling on day 3. 
Again buy on day 4 and sell on day 6. If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.
'''

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def stockBuySell(price, n): 
      
    # Prices must be given for at least two days 
    if (n == 1): 
        return
      
    i=0
    profit = 0
    while(i<n-1):
        while(i<n-1 and price[i+1]<=price[i]):
            i += 1
          
        buy = i
        i += 1
        
        while(i<n and price[i]>=price[i-1]):
            i += 1
        
        sell = i-1
        
        profit = price[buy]+price[sell]
        
        print("Buy on day:"+str(buy)+" and sell on day:"+str(sell))
        
    print("Total Profit:"+str(profit))    
          
# Driver code 
  
# Stock prices on consecutive days 
#price = [100, 180, 260, 310, 40, 535, 695] 
price = [1,5,2,3,7,6,4,5]
n = len(price) 
  
# Fucntion call 
stockBuySell(price, n) 
  