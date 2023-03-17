import csv
import os

from rich.console import Console
from rich.table import Table
from datetime import date, timedelta, datetime
from arguments import arguments

from make_pdf_report import make_pdf_report
import date

def make_report(args):
    with open('stock.csv', 'r') as file_reader, open('report.csv' , 'w', newline= '') as file_writer:
        bought_report = csv.reader(file_reader)
        new_csv_file = csv.writer(file_writer)

        table_bought = Table(show_header=True, header_style="bold", show_lines=True)
        table_sold = Table(show_header=True, header_style="bold", show_lines=True)
        table_profit = Table (show_header=True, header_style="bold", show_lines=True)
        table_revenue = Table (show_header=True, header_style="bold", show_lines=True)
        console = Console()

        table_bought.add_column('ID')
        table_bought.add_column('Date')
        table_bought.add_column('Product')
        table_bought.add_column('Buy price')
        table_bought.add_column('Amount')
        table_bought.add_column('Expiration date')

        table_sold.add_column('ID')
        table_sold.add_column('Date')
        table_sold.add_column('Product')
        table_sold.add_column('Buy price')
        table_sold.add_column('Amount')
        table_sold.add_column('Expiration date')

        table_profit.add_column('Profit')
        
        table_revenue.add_column('Revenue')

        #report today
        if args.Subcommand == 'inventory' and args.time =='today':
            for line in bought_report:
                if args.file == 'true':
                    new_csv_file.writerow(line)
                elif args.pdf == 'true':
                    try:
                        make_pdf_report()
                    except:
                        None
                else:
                    table_bought.add_row(
                        line[0], line[1], line[2], line[3], line[4], line[5]
                    )
            console.print(table_bought)
        
        #report yesterday
        if args.subcommand == 'inventory' and args.time == 'yesterday':
            for line in bought_report:
                if (datetime.strptime(line[1], "%d-%m-%y")) < datetime.strptime(
                    date.display_yesterday, "%d-%m-%y"
                ):
                    if args.file == 'true':
                        new_csv_file.writerow(line)
                    else: 
                        table_bought.add_row(
                            line[0], line[1], line[2], line[3], line[4], line[5]
                        )
            console.print(table_bought)

        #report last week
        if args.subcommand == 'inventory' and args.time == 'lastweek':
            display_last_week = datetime.strptime(args.date, "%d-%m-%y")

            for line in bought_report:
                if (datetime.strftime(display_last_week, "%d-%m-%y")
                   < datetime.strptime(line[1], "%d-%m-%y")
                   < datetime.strptime(date.display_today, "%d-%m-%y")
                    ):
                    if args.file == 'true':
                        new_csv_file.writerow(line)
                    else:
                        table_bought.add_row(
                            line[0], line[1], line[2], line[3], line[4], line[5]
                        )
            console.print(table_bought)
        
        #report specific date
        if args.subcommand == 'inventory' and args.time == 'date':
            display_date = datetime.strptime(args.date, "%d-%m-%y")

            for line in bought_report:
                if (datetime.strptime(line[1], "%d-%m-%y")) <= display_date:
                    if args.file == 'true':
                        new_csv_file.writerow(line)
                    else:
                        table_bought.add_row(
                            line[0], line[1], line[2], line[3], line[4], line[5]
                        )
            console.print(table_bought)

        if args.subcommand == 'expiredates' and args.time == 'today':
            for line in bought_report:
                if (datetime.strptime(line[5], "%d-%m-%y")) <= datetime.strptime(
                    date.display_yesterday, "%d-%m-%y"
                ):
                    if args.file == 'true':
                        new_csv_file.writerow(line)
                    else:
                        table_bought.add_row(
                            line[0], line[1], line[2], line[3], line[4], line[5]
                        )
            console.print(table_bought)
          
        if args.subcommand ==  'expiredates' and args.time == 'date':
            display_date = datetime.strptime(args.date, "%d-%m-%y")
            for line in bought_report:
                if (datetime.strptime(line[5], "%d-%m-%y")) <= display_date:
                    if args.file == 'true':
                        new_csv_file.writerow(line)
                    else: 
                        table_bought.add_row(
                            line[0], line[1], line[2], line[3], line[4], line[5]
                        )
            console.print(table_bought)

    with open('selling.csv', 'r') as sold_file:
        sold_report = csv.reader(sold_file)

        if args.subcommand == 'sold':
            for line in sold_report:
                if (datetime.strptime(line[1], "%d-%m-%y")) <= date.display_today:
                    
                    if args.file == 'true':
                        new_csv_file.writerow(line)
                    else:
                        table_sold.add_row(
                            line[0], line[1], line[2], line[3], line[4], line[5]
                        )
            console.print(table_sold)
        
        if args.subcommand == 'revenue' and args.time == 'today':
            sum_revenue = 0
            for line in sold_report:
                if (datetime.strptime(line[1], "%d-%m-%y")) == date.display_today:
                    
                    total_revenue_per_product = float(line[3]) * float(line[4])
                    sum_revenue += total_revenue_per_product
                    if args.file == 'true':
                        new_csv_file.writerow(sum_revenue)
                    else:
                        None
                else:
                    table_revenue.add_row(str(sum_revenue))
                console.print (table_revenue)

        if args.subcommand == 'revenue' and args.time == 'date':
            display_date = datetime.strptime(args.date, "%d-%m-%y")
            sum_revenue = 0
            for line in sold_report:
                if (datetime.strptime(line[1], "%d-%m-%y")) <= display_date:
                    total_revenue_per_product = float(line[3]) * float(line[4])
                    sum_revenue += total_revenue_per_product
                    if args.file == 'true':
                        new_csv_file.writerow(sum_revenue)
                    else:
                        None
                else:
                    table_revenue.add_row(str(sum_revenue))
            console.print(table_revenue)

        if args.subcommand == 'profit' and args.time == 'today':
            sum_profit = 0
            for line in sold_report:
                sum_profit += float(line[5])
                if args.file == 'true':
                    new_csv_file.writerow(sum_profit)
                else:
                    None
            else:
                table_profit.add_row(str(sum_profit))
            console.print(table_profit)

        if args.subcommand == 'profit' and args.time == 'date':
            display_date = datetime.strptime(args.date, "%d-%m-%y")
            sum_profit = 0
            for line in sold_report:
                if (datetime.strptime(line[1], "%d-%m-%y")) <= display_date:
                    sum_profit += float(line[5])
                    if args.file == 'true':
                        new_csv_file.writerow(sum_profit)
                    else:
                        None
                else:
                    table_profit.add_row(str(sum_profit))
            console.print(table_profit)

if __name__ == '__main__':
    pass

                    