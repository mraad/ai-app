# AI APP

Install [uv](https://github.com/astral-sh/uv).

- Create a virtual environment at `.venv`.
```shell
rm -rf .venv && uv venv --python=python3.11 --seed
```

- Activate the environment.
```shell
source .venv/bin/activate
```

- Install modules
```
uv pip compile pyproject.toml -q -o requirements.txt && uv pip install -q -r requirements.txt
```

### References
- https://github.com/astral-sh/uv
- https://pub.towardsai.net/performing-data-science-tasks-with-llm-based-agents-crewai-71f8eadb0a6d
- https://www.esri.com/arcgis-blog/products/experience-builder/natural-resources/recreating-near-me-workflows-in-experience-builder/
