To create the environment (Poetry)

```
poetry init -n 
```

This will create a project specific virtual environment and the pyproject.toml file

---
To add dependencies

```
poetry add <pip dependencies>
```

This will pip install any dependencies on the project virtual environment and update the poetry.lock file 

---

To run the project

```
poetry run python runner.py
```

This is the same as activating the virtual environment and then running `python runner.py`.