# Create a new file: daym/middleware.py

class CorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Get the origin from the request
        origin = request.META.get('HTTP_ORIGIN')
        
        # List of allowed origins
        allowed_origins = [
            'https://daymate-s7gj.onrender.com',
            'http://localhost:3000',
            'http://localhost:5173',
            'http://127.0.0.1:3000',
        ]
        
        # Check if origin is allowed
        if origin in allowed_origins:
            response['Access-Control-Allow-Origin'] = origin
        elif origin and 'daymate' in origin and 'onrender.com' in origin:
            # Allow any daymate subdomain on render
            response['Access-Control-Allow-Origin'] = origin
        
        response['Access-Control-Allow-Credentials'] = 'true'
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept, Authorization, X-CSRFToken, X-Requested-With'
        response['Access-Control-Expose-Headers'] = 'Content-Type, X-CSRFToken'
        response['Access-Control-Max-Age'] = '3600'
        
        return response

    def process_request(self, request):
        # Handle preflight OPTIONS requests
        if request.method == 'OPTIONS':
            from django.http import HttpResponse
            response = HttpResponse()
            
            origin = request.META.get('HTTP_ORIGIN')
            allowed_origins = [
                'https://daymate-s7gj.onrender.com',
                'http://localhost:3000',
                'http://localhost:5173',
                'http://127.0.0.1:3000',
            ]
            
            if origin in allowed_origins:
                response['Access-Control-Allow-Origin'] = origin
            elif origin and 'daymate' in origin and 'onrender.com' in origin:
                response['Access-Control-Allow-Origin'] = origin
            
            response['Access-Control-Allow-Credentials'] = 'true'
            response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
            response['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept, Authorization, X-CSRFToken, X-Requested-With'
            response['Access-Control-Max-Age'] = '3600'
            response['Content-Length'] = '0'
            
            return response
        
        return None
