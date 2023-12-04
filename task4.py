import numpy as np

def k_transactions_dynamic(stock_matrix, k):
    solution_array = [0, 0, 0, 0]
    row_dim, col_dim = np.shape(stock_matrix)
    dynamic_table = [[[0, []] for _ in range(col_dim)] for _ in range(k + 1)]
    
    for transactions in range(2, k + 1):
        for sell_day in range(1, col_dim):
            previous = dynamic_table[transactions][sell_day - 1]
            dynamic_table[transactions][sell_day] = previous.copy()
            
            for stock_index in range(row_dim):
                for buy_day in range(sell_day):
                    buy_price = stock_matrix[stock_index][buy_day]
                    sell_price = stock_matrix[stock_index][sell_day]
                    profit = sell_price - buy_price
                    
                    previous_profit = dynamic_table[transactions - 1][buy_day][0]
                    previous_transactions = dynamic_table[transactions - 1][buy_day][1]
                    net_profit = profit + previous_profit
                    
                    if net_profit > dynamic_table[transactions][sell_day][0]:
                        dynamic_table[transactions][sell_day][0] = net_profit
                        dynamic_table[transactions][sell_day][1] = previous_transactions + [[stock_index, buy_day, sell_day]]
    
    return dynamic_table[k][col_dim - 1][1]