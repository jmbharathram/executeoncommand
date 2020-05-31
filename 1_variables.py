'''
Let's assume you have a small ecommerce/shopify website. 
You just had your first day of sale. At the end of the day,you want to calculate your total sales amount and the profit you made that day.
'''
number_of_orders_today = 200
average_price_of_orders = 25
profit_margin = 0.10
end_of_line_statement = "The End"

print("Total Sale Amount: ")
total_sales = number_of_orders_today*average_price_of_orders
print(total_sales)
print("My profit margin is: ")
print(profit_margin)
print("Profit: ")
print(total_sales*profit_margin)
print(end_of_line_statement)
