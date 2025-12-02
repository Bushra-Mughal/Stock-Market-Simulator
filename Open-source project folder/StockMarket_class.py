from collections import deque
import Hashmap_class as hm_class
class stock_market:
    def __init__(self):
        self.stock_market = deque()  #--> queue | for realtime stock updates
        self.buy_stocks = hm_class #--> hashmap | for O(1) searching/insertion
        self.sell_stocks = deque()  #--> stack | for tracking last sold 
        self.ownership = False        #--> to check kya atleast 1 stock buy kya ya nhn
        stocks = {
            1 : ['Google', f"slots:{2}" , "time: 7:00 am" ] ,
            2 : ['Tesla' , f"slots:{15}" , "time: 7:02 am"] ,
            3 : ['Amazon b' , f"slots:{17}" , "time: 7:05 am"] ,
            4 : ['Daraz', f"slots:{34}" , "time: 7:08 am" ] ,
            5 : ['Gormet' , f"slots:{90}" , "time: 7:10 am"] ,
            6 : ['Amazon c' , f"slots:{4}" , "time: 7:12 am"] ,
        }
        for stock in stocks:
            self.stock_market.append( stocks[stock] )

    def sell_stock(self, name):
        name = name.capitalize()
        if not self.ownership:
            return "Can't sell stock, buy atleast one"
        ind = self.buy_stocks.hash_function(name)
        if self.buy_stocks.list[ind] != None:
            your_stock = self.buy_stocks.list[ind]
            self.sell_stocks.append(your_stock)
            self.buy_stocks.list[ind] = None
            if all(x is None for x in self.buy_stocks.list):
                self.ownership = False
            return f"===== Stock {your_stock} successfully sold! ====="
        else:
            return "Stock not owned"
    
    def buy_stock(self, num):
        index = num - 1
        if 0 <= index < len(self.stock_market):
            selected = self.stock_market[index]
            name = selected[0]
            self.buy_stocks.add_item(name, selected)
            self.ownership = True
            return f"===== Stock successfully owned: {selected} ====="
        else:
            return "Stock number doesn't exist!"

    def show_buy_stocks(self):
        if not self.ownership:
            return "You haven't owned any stock"
        result = "======= Bought stocks =======\n"
        for stock in self.buy_stocks.list:
            if stock != None:
                result += f"{stock}\n"
        result += "======= ========== ======="
        return result
            
    def show_last_sold_stock(self):
        if self.sell_stocks:
            return str(self.sell_stocks[-1])
        else:
            return "You haven't sold the stock yet"

    def show_stock_market(self):
        result = "*****==== Real-time stock market ====*****\n\n"
        if self.stock_market:
            for i, stocks in enumerate(self.stock_market):
                result += f"\t{i+1}: {stocks}\n"
            result += "\n*****=============*****"
        else:
            result += "Stock market not active"
        return result
    
    def stock_market_info(self):
        return """
- **Stock** = A tiny piece of ownership in a company (e.g., 1 Apple stock = 0.0000001% of Apple).
- **Stock Market** = A digital marketplace (like NYSE, Nasdaq) where people buy/sell stocks.
- **Why Companies Sell Stocks**:
  - Raise money to grow (build factories, hire, invent).
  - No need to repay (unlike loans).
- **Why People Buy Stocks**:
  - **Price Growth**: If company does well → stock price ↑ → sell for profit.
  - **Dividends**: Some companies pay you cash yearly.
- **Stock Price Changes**:
  - Up: Good news, high demand.
  - Down: Bad news, low demand.
- **Real-Time Data** = Live prices updated every few seconds (via APIs like Polygon.io).
- **Risk** = Stock price can fall → you lose money.
- **Reward** = Company grows → you earn big!
        """.strip()