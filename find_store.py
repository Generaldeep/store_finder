from docopt import docopt

usage = '''

    Store Finder CLI.

    Usage:
        find_store --address="<address>"
        find_store --address="<address>" [--units=(mi|km)] [--output=text|json]
        find_store --zip=<zip>
        find_store --zip=<zip> [--units=(mi|km)] [--output=text|json]
'''


args = docopt(usage)


if args['--zip']:
    zip = args['--zip']
    print(zip)

if args['--address']:
    store = args['--address']
    print('>>> ', store)
