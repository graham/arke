def flask_serve(service):
    pass


if __name__ == '__main__':
    from service import Service

    def my_index(service):
        return "Hello World"

    s = Service()
    s.register(path='/', func=my_index)

    flask_serve(s)
