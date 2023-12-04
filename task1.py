import numpy as np

def single_transaction_brute_force(stock_matrix):
    max_profit = -float('inf')
    solution_array = [0, 0, 0, 0]
    row_dim, col_dim = np.shape(stock_matrix)
    
    for stock_index in range(row_dim):
        for buy_day_index in range(col_dim - 1):
            for sell_day_index in range(buy_day_index + 1, col_dim):
                buy_price = stock_matrix[stock_index][buy_day_index]
                sell_price = stock_matrix[stock_index][sell_day_index]
                profit = sell_price - buy_price
                
                if profit > max_profit:
                    max_profit = profit
                    solution_array = [stock_index, buy_day_index, sell_day_index, profit]
    
    return solution_array