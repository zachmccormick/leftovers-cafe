from functools import wraps

from ddtrace import tracer
from ddtrace.constants import SERVICE_KEY


def for_service(service_name):
    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            root_span = tracer.current_root_span()
            if root_span:
                root_span.set_tag(SERVICE_KEY, service_name)
            return func(request, *args, **kwargs)

        return inner

    return decorator
