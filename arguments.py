import argparse
def arguments():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    #buy parser
    buy_parser = subparser.add_parser('buy', help='Add the bought products to the stock')
    
    buy_parser.add_argument(
        '-p', '--products', type=str.lower, help='Fill in the name of the product!'
    )

    buy_parser.add_argument(
        '-a', '--amount', type=int, help='How many did you bought?'
    )

    buy_parser.add_argument(
        '-bp', '--bought_price', type=float, help='Fill in the price like: 1,25'
    )

    buy_parser.add_argument(
        '-exp', '--expiration', type=str, help='Fill in the expiration date like: dd-mm-yy'
    )

    buy_parser.add_argument(
        '-d', '--date', type=str, help="Fill in the date like: dd-mm-yy"
    )

    #reporting parser
    reporting_parser = subparser.add_parser('report', help = 'Make a report')
    reporting_parser.add_argument('Subcommand',
        choices=['inventory','revenues', 'sold', 'profit','expired'],
        help= 'Please make a choice for the full report'
    )

    reporting_parser.add_argument('time',
        choices= ['today', 'yesterday', 'lastweek','date'],
        help = 'Please pick a for the report like: today, yesterday, lastweek or date')
    
    reporting_parser.add_argument(
        '-d', '--date', type=str, help="Fill in the date like: dd-mm-yy"
    )

    reporting_parser.add_argument(
        '-f', '--file', type=str, help='When exported to a CSV file, type: -f true'
    )

    reporting_parser.add_argument(
        '-pdf','--pdf', type=str, help='When exported to a PDF file, type: -pdf true'
    )

    #Selling parser
    selling_parser = subparser.add_parser('sell', help= 'Add the sold item')
    selling_parser.add_argument(
        '-p', '--product', type=str.lower, help='Fill in the sold product:'
    )

    selling_parser.add_argument(
        '-a', '--amount', type=int, help='How many did we sold?'
    )
    
    selling_parser.add_argument(
        '-s', '--sold', type=float, help='For how many did we sold? Fill in like: 2.75'
    )

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    pass