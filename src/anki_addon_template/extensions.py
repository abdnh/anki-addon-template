import re
from typing import Callable

from jinja2.environment import Environment
from jinja2.ext import Extension


def simple_filter(filter_function: Callable) -> Callable:
    """Decorate a function to wrap it in a simplified jinja2 extension."""

    class SimpleFilterExtension(Extension):
        def __init__(self, environment: Environment):
            super().__init__(environment)
            environment.filters[filter_function.__name__] = filter_function

    SimpleFilterExtension.__name__ = filter_function.__name__
    return SimpleFilterExtension


@simple_filter
def github_pages_from_repo(url: str) -> str:
    m = re.match("https://github.com/(?P<user>.*?)/(?P<repo>.*)", url)
    if not m:
        return url
    return f"https://{m.group(1)}.github.io/{m.group(2)}"
