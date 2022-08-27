import time

class mySimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.perf_counter()
        response = self.get_response(request)
        end = time.perf_counter()
        print("the request '" + str(request.path) + "' took", end - start, "seconds to complete.")
        return response