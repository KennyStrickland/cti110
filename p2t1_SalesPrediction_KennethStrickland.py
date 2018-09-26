#Sales Predictor
#9/25/18
#Kenny Strickland
#

#Ask for total sales

TotalSales= int(input ("What are the total sales for the year?"))

#Multiply total sales by 23% to determine profits

profit= TotalSales*.23

#Display profits

print("Total profit is" , (format(profit,'.2f')))
