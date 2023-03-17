from arguments import arguments
from make_report import make_report
from buy_products import buy_products
from sell_products import sell_products
from rich.console import Console

def main (args):
    args = arguments()
    if args.Subcommand == 'report':
        make_report(args)
    elif args.Subcommand == 'buying':
        buy_products(args)
    elif args.Subcommand == 'selling':
        sell_products(args)

if __name__ == '__main__':
    myconsole = Console ()
    myconsole.print('-' * 70)

    args = arguments()
    main(args)

    myconsole.print('-' * 70)
    myconsole.print('# Arguments', args)
    myconsole.print('-' * 70)
