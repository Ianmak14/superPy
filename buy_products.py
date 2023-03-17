import os
import csv
from arguments import arguments
import date

def buy_products(args):
    with open('Stock.csv', 'r') as inp, open('Stock_edit.csv', 'a', newline='') as out:
      reader = csv.reader(inp)
      writer = csv.writer(out)
      id_buy = id(1)

      is_added = False
      for line in reader:
         if args.product == line[2]:
            new_amount = int(args.amount) + int(line[4])
          
            if args.date == None:
               new_amount_arr_for_csvfile = [
                  id_buy, date.display_today, args.products, args.buy_price, new_amount, args.expiration_date
               ] 
               is_added = True
               writer.writerow(new_amount_arr_for_csvfile)
            
            elif len(args.date) > 2:
               new_amount_and_date_arr_for_csvfile = [
                  id_buy, date.display_today, args.products, args.buy_price, new_amount, args.expiration_date
               ] 
               is_added = True

               writer.writerow(new_amount_and_date_arr_for_csvfile)
               try:
                  os.rename('stock_edit.csv', 'stock.csv')
               except:
                  None

            else:
              writer.writerow(line)
              try:
                  os.rename('stock_edit.csv', 'stock.csv')
              except:
                  None

      if not is_added:
         if args.date == None:
            new_arr_for_csvfile = [
                    id_buy, date.display_today, args.product, args.buy_price, args.amount, args.expiration_date
                ]
            writer.writerow(new_arr_for_csvfile)

         elif len(args.date) > 2:
            new_amount = int(args.amount) + int(line[4])
            new_amount_and_date_arr_for_csvfile = [
                    id_buy, args.date , args.product, args.buy_price, args.amount, args.expiration_date, new_amount
                ] 
            writer.writerow(new_amount_and_date_arr_for_csvfile)
            try:
               os.rename ('stock_edit.csv', 'stock.cs')
            except:
               None

if __name__ == '__main__':
   pass

