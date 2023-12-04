import numpy as np

def single_transaction_greedy(stock_matrix):
    max_profit = 0
    solution_array = [0, 0, 0, 0]
    row_dim, col_dim = np.shape(stock_matrix)
    
    for stock_index in range(row_dim):
        min_price = float('inf')
        min_price_date = 0
        potential_profit = 0
        
        for day_index in range(col_dim):
            current_price = stock_matrix[stock_index][day_index]
            
            if current_price < min_price:
                min_price = current_price
                min_price_date = day_index
            
            potential_profit = current_price - min_price
            
            if potential_profit > max_profit:
                max_profit = potential_profit
                solution_array = [stock_index, min_price_date, day_index, max_profit]
    
    return solution_array


