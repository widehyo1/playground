import dill
from IPython import start_ipython

def load_runtime_environment(dill_file):
    with open(dill_file, "rb") as f:
        return dill.load(f)

env = load_runtime_environment("main.dill")

# inject into ipython namespace
ns = {}
ns.update(env)

# optionally expose locals/globals if you saved them
if "func" in env:
    ns.update(env["func"].get("locals", {}))

start_ipython(argv=[], user_ns=ns)
