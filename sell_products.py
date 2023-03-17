import os
import csv
from arguments import arguments
import date

def sell_products(args):
    with open('stock.csv', 'r') as input, open ('stock_edit.csv', 'w', newline= ' ') as output, open(
        'selling.csv', 'a', newline= ' ') as sold:
        reader = csv.reader(input)
        writer = csv.writer(output)
        sold_writer = csv.writer(sold)
        is_added = False

        for line in reader:
            id_buy = line[0]
            if args.products == line[2]:
                if int(line[4]) >= args.amount:
                    new_amount = int(line[4]) - int(args.amount)
                    profit_product = (args.sell_price - float(line[3])) * int (
                        args.amount
                    )

                    new_amount_arr_for_csv_file = [line[0], line[1], line[2], line[3], new_amount, line[5]]

                    is_added = True

                    if new_amount == 0:
                        None
                    else:
                        writer.writerow(new_amount_arr_for_csv_file)
                      
                    arr_for_soldfile = [
                        id_buy,
                        date.display_today,
                        args.product,
                        args.amount,
                        args.sell_price,
                        profit_product,
                    ]
                    sold_writer.writerow(arr_for_soldfile)
                    try:
                       os.rename('Stock_edit.csv' 'stock.csv')
                    except:
                       None
                else:
                    print('Number of sold itmens is more than available in stock.')
            elif args.product != line[2]:
                writer.writerow(line)
          
        if not is_added:
          writer.writerow(line)
          try:
              os.rename('Stock_edit.csv', 'stock.csv')
          except:
              None

if __name__ == '__main__':
    pass


