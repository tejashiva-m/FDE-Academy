# Virtual Environments (day11 notes)

What is a virtual environment?

A virtual environment is a project-specific Python environment that keeps packages and interpreter settings isolated from other projects and the system Python.

Why use one?

- Avoid dependency conflicts between projects.
- Reproduce a stable development environment across machines.

What is pip?

`pip` is the package installer for Python. It downloads and installs packages from PyPI into the active environment.

What does `pip install` do?

Installs a package and its dependencies into the current environment so your code can import it.

What does `pip freeze` do?

Outputs exact package versions installed in the environment; useful for creating `requirements.txt`.

Why use `requirements.txt`?

It lists dependencies so other developers (or CI) can install the same packages with `pip install -r requirements.txt`.

Difference between `pip list` and `pip freeze`:

- `pip list` shows installed packages in a human-friendly table.
- `pip freeze` shows exact versions suitable for `requirements.txt`.

Why not install packages globally?

Global installs can lead to version collisions and make projects harder to reproduce; virtual envs avoid this.

What is an API?

An API exposes functionality or data from a service (like GitHub) over HTTP so programs can interact with it.

Why use `requests` instead of raw sockets?

`requests` handles HTTP details (methods, headers, redirects, TLS) and returns convenient objects (like `.json()`), letting you work at a higher level.
