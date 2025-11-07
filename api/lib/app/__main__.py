if __name__ == '__main__':
    from . import App
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('-d', action='store_true', help='enable debug')
    parser.add_argument('-b', default='127.0.0.1', help='bind address')
    parser.add_argument('port', default='8000', help='listening port', nargs='?')
    args = parser.parse_args()
    App().to_wsgi_app().run(debug=args.d, host=args.b, port=args.port)
