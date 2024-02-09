class Router:
    routes = {
        'post': [],
        'put': [],
        'get': [],
        'delete': []
    }

    def callback(self, method, path) -> callable:
        if method not in ['post', 'put', 'get', 'delete']:
            raise Exception('Método inválido')
        if path == '': 
            path = '/'
        callback_fn = None
        for route in self.routes[method]:
            if 'path' in route and route['path'] == path:
                return route['callback']
        return callback_fn

    def post(self, path: str, callback: callable):
        if path == '': 
            path = '/'
        self.routes['post'].append({
            "path": path,
            "callback": callback
        })
    
    def put(self, path: str, callback: callable):
        if path == '': 
            path = '/'
        self.routes['put'].append({
            "path": path,
            "callback": callback
        })
    def get(self, path: str, callback: callable):
        if path == '': 
            path = '/'
        self.routes['get'].append({
            "path": path,
            "callback": callback
        })
    def delete(self, path: str, callback: callable):
        if path == '': 
            path = '/'
        self.routes['delete'].append({
            "path": path,
            "callback": callback
        })
