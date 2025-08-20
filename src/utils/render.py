import re
import typing as t

def render_vars(v: t.Any, vars: dict):
    if isinstance(v, str):
        return re.sub(r"{{\s*([a-zA-Z0-9_]+)\s*}}", lambda m: str(vars.get(m.group(1), "")), v)
    if isinstance(v, list):
        return [render_vars(x, vars) for x in v]
    if isinstance(v, dict):
        return {k: render_vars(val, vars) for k, val in v.items()}
    return v
