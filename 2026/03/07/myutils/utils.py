from functools import wraps
import sys
import dill

def dump_runtime_environment(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        captured = {}

        def profiler(frame, event, arg):
            if event == "return" and frame.f_code is func.__code__:
                captured["locals"] = frame.f_locals.copy()
                captured["globals"] = {
                    k: v for k, v in frame.f_globals.items()
                    if not k.startswith("__") and not callable(v)
                }
            return profiler

        old_profiler = sys.getprofile()
        sys.setprofile(profiler)

        result = None
        exc = None

        try:
            result = func(*args, **kwargs)
        except Exception as e:
            exc = e
            raise
        finally:
            sys.setprofile(old_profiler)

            run_info = {
                "args": args,
                "kwargs": kwargs,
                "result": result,
                "func": captured,
                "exception": exc,
            }

            with open(f"{func.__name__}.dill", "wb") as f:
                dill.dump(run_info, f, byref=True, recurse=True)

        return result

    return decorator

def load_runtime_environment(dill_file):
    with open(dill_file, 'rb') as f:
        runtime_environment = dill.load(f)
        return runtime_environment


def load_into_namespace(dill_file, namespace):
    env = load_runtime_environment(dill_file)

    namespace.update(env)

    if "func" in env:
        namespace.update(env["func"].get("globals", {}))
        namespace.update(env["func"].get("locals", {}))

def ex_hook(type_, value, tb):
    import ipdb, traceback

    if type_ is KeyboardInterrupt:
        sys.__excepthook__(type_, value, tb)
        return

    traceback.print_exception(type_, value, tb)
    ipdb.post_mortem(tb)
