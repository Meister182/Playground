# Create & install a `setuptools` package

```
$ python3 -m venv venv && . ./venv/bin/activate
$ python3 ./my_py_pkg/setup.py install
```

# Use the package

```
$ my_py_pkg
> My python package!
```

``` python3
import my_py_pkg
my_py_pkg.main()

> My python package!
```

# Run the code directly

When directly running the code, python won't know that `my_py_pkg` is a **sub-package**, and will
look for a module of the same name instead and it will fail with the error:
`ModuleNotFoundError: No module named 'my_py_pkg'`

In order for `my_py_pkg` to be found, we need a way to make sure the package directory is in the
`PYTHONPATH`.

> **CONCLUSION:** Approach 3 seems to be the best way to go about it.

### 1) Explicit `PYTHONPATH` approach

```
$ PYTHONPATH=. python3 my_py_pkg

# Calling it from another place
$ PYTHONPATH=./packaging_setuptools/ python3 packaging_setuptools/my_py_pkg
```

- **CON** Harder on the eyes
- **CON** We need to path an absolute path to the package
- **CON** More boiler plate code
- **CON** More room for errors

### 2) Run as python module approach

```
$ python3 -m my_py_pkg
```

- **CON** Only works when run in the package directory
- **CON** Causes some weird sys.modules loading warnings

### 3) Using a dedicated python script

``` python3
#! /usr/bin/env python3
from my_py_pkg.__main__ import main

if __name__ == "__main__":
    main()
```

- **CON** Needs an extra script.
- **PRO** Works flawlessly from anywhere
- **PRO** No warning, errors or tweaks to environments variables
