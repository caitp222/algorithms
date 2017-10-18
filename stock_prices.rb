# greedy solution
def get_max_profit(arr)
  i = 0
  profit = 0
  while i < arr.length
    w = i
    while w < arr.length
      x = arr[w] - arr[i]
      if x > profit
        profit = x
      end
      w += 1
    end
    i += 1
  end
  profit
end

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
p get_max_profit(stock_prices_yesterday)
