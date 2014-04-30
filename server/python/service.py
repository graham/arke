import json
import pprint

class Service(object):
    def __init__(self):
        self.live_version = '0'
        self.api_calls = []
        self.pre_call = []
        self.post_call = []
        self.error_handler = lambda *x, **y: "error"
        self.gets = {}

    def get(self, key, default=None):
        if key in self.gets:
            return self.gets[key]()
        else:
            if default == None:
                raise Exception("No such value.")
            else:
                return default
    
    def register(self, path, func, options=None):
        if options == None:
            options = {}
        
        version = options.get('version', self.live_version)

        self.api_calls = list(filter(
            lambda x: False if path == x[4] else True, 
            self.api_calls))
        
        self.api_calls.insert(0, [
            func,
            version,
            options.get('method', "GET"),
            options.get('host', ''),
            path,
            path.rsplit('/')[-1] or "index",
            []
        ])

    def dispatch(self, path, options=None):
        if options == None:
            options = {}

        hits = list(filter(
            lambda x: True if path == x[4] else False,
            self.api_calls))

        num = len(hits)

        if num == 0:
            return None
        elif num == 1:
            return hits[0][0]
        else:
            for endpoint in hits:
                if any([fn(path, options) for fn in endpoint[6]]):
                    return endpoint[0]
            return None
            
    def serialize(self, pretty=1):
        output = []
        output.append(["version", "method", "host", "path", "func_name", "validators"])

        for endpoint in self.api_calls:
            output.append(endpoint[1:])

        if pretty:
            return '[\n' + ',\n'.join(map(lambda x: '  ' + json.dumps(x), output)) + '\n]'
        else:
            return json.dumps(output)


if __name__ == '__main__':
    def myfunc():
        return "Hello World"

    s = Service()
    s.register(path='/', func=myfunc)
    s.register(path='/asdf', func=myfunc)
    s.register(path='/', func=int)
    print(s.serialize(pretty=True))

    print(s.dispatch(path='/'))
