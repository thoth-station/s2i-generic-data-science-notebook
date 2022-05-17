TEST_NB_TEMPLATE = """
{
"cells": [
{
"cell_type": "code",
"metadata": {},
"outputs": [],
"source": [
    "import TEST_PACKAGE"
]
}
],
"metadata": {
},
"nbformat": 4,
"nbformat_minor": 5
}
"""

test_package_list = [
    "boto3",
    "bokeh",
    "cloudpickle",
    "cython",
    "dask",
    "dill",
    "distributed",
    "h5py",
    "ipywidgets",
    "jupyter_bokeh",
    "jupyterlab_git",
    "jupyterlab_s3_browser",
    "kafka",
    "matplotlib",
    "numpy",
    "pandas",
    "plotly",
    "pre_commit",
    "pyarrow",
    "s3fs",
    "scipy",
    "seaborn",
    "sqlalchemy",
    "statsmodels",
]

for package in test_package_list:
    text_file = open("tests/imports/" + package + ".ipynb", "wt")
    n = text_file.write(TEST_NB_TEMPLATE.replace("TEST_PACKAGE", package))
    text_file.close()
