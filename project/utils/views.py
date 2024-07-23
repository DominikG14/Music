import inspect


def get_template(template_name: str = '', *, path: str = '', app: str) -> str:
    """Setups view template to render"""

    if not template_name:
        template_name = inspect.stack()[1][3] # Gets name of the function that this was called in
        template_name = template_name.replace('_', '-')

    if path:
        path = path.strip('/')
        return f'{app}/{path}/{template_name}.html'

    return f'{app}/{template_name}.html'