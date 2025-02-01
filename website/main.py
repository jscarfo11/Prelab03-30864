
from django_server import DjangoServer

def main():
    """Server for the website."""

    # run a django server here

    django_server = DjangoServer()
    django_server.create()
    django_server.run()


if __name__ == "__main__":
    main()