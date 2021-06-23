# S2I Generic Data Science Notebook

Custom Notebook built with Thoth s2i-minimal-notebook.

This custom notebook contains [SciPy](https://www.scipy.org/) , Boto3, Pandas, Kafka-python related packages installed with minimal notebook for Data Science usage. This image can be directly used if user needed these package while using the minimal jupyter notebook.

We have configured this repository to use pipenv and micropipenv python dependency managers.

# List of packages in generic-data-science-notebook

```
- beautifulsoup4
- bokeh
- cloudpickle
- cython
- dask
- dill
- distributed
- h5py
- ipywidgets
- matplotlib
- numpy
- pandas
- plotly
- pyarrow
- s3fs
- scikit-image
- scikit-learn
- scipy
- seaborn
- sqlalchemy
- statsmodels
- boto3
- kafka-python
```

# List of extensions

```
- jupyter-bokeh
- jupyterlab-git
- jupyterlab-s3-browser
```

## Importing the Generic Data Science Notebook

A pre-built version of the Generic data science notebook based on [Thoth s2i-minimal-notebook](https://github.com/thoth-station/s2i-minimal-notebook), can be found at quay.io:

- <https://quay.io/repository/thoth-station/s2i-generic-data-science-notebook>

This image could be imported into an OpenShift cluster using OpenShift ImageStream:

```yaml
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  # (Below label is needed for Opendatahub.io/JupyterHub)
  # labels:
  #   opendatahub.io/notebook-image: "true"
  name: s2i-generic-data-science-notebook
spec:
  lookupPolicy:
    local: true
  tags:
  - name: latest
    from:
      kind: DockerImage
      name: quay.io/thoth-station/s2i-generic-data-science-notebook:latest
```

## Building the Generic Data Science Notebook

Instead of using the pre-built version of the minimal notebook, you can build the minimal notebook from source code.

With [Thoth](https://thoth-station.ninja/) advise

```bash
s2i build . quay.io/thoth-station/s2i-minimal-notebook:latest \
--env THAMOS_RUNTIME_ENVIRONMENT="" \
--env ENABLE_MICROPIPENV=1 \
--env THOTH_ADVISE=1 \
--env THOTH_DRY_RUN=0 \
--env THOTH_PROVENANCE_CHECK=1 \
s2i-generic-data-science-notebook
```

Without [Thoth](https://thoth-station.ninja/) advise

```bash
s2i build . quay.io/thoth-station/s2i-minimal-notebook:latest \
--env THAMOS_RUNTIME_ENVIRONMENT="" \
--env ENABLE_MICROPIPENV=1 \
--env THOTH_ADVISE=0 \
--env THOTH_ERROR_FALLBACK=1 \
--env THOTH_DRY_RUN=1 \
--env THOTH_PROVENANCE_CHECK=0 \
s2i-generic-data-science-notebook
```
