import numpy as np

def single_transaction_dynamic(stock_matrix):
    max_profit = 0
    solution_array = [0, 0, 0, 0]
    row_dim, col_dim = np.shape(stock_matrix)
    
    for stock_index in range(row_dim):
        potential_profit = 0
        buy_day = 0
        
        for sell_day in range(1, col_dim):
            buy_price = stock_matrix[stock_index][buy_day]
            sell_price = stock_matrix[stock_index][sell_day]
            
            if buy_price < sell_price:
                potential_profit = sell_price - buy_price
                
                if potential_profit > max_profit:
                    max_profit = potential_profit
                    solution_array = [stock_index, buy_day, sell_day, max_profit]
            else:
                buy_day = sell_day
    
    return solution_array
