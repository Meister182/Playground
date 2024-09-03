import importlib
import sys

spec = importlib.util.spec_from_file_location("cursed", "./some-cursed-lib.py")
cursed = importlib.util.module_from_spec(spec)
sys.modules["cursed"] = cursed
spec.loader.exec_module(cursed)


cursed.print_cursed()
