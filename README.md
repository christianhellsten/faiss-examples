Build the image:

```bash
$ docker build . -t faiss-examples
```

Run the image:

```bash
$ docker run --rm -it --mount type=bind,source="$(pwd)",target="/app/" --env-file=envrc.docker faiss-examples
```

Play around with faiss inside the running Docker container:

```bash
$ python flat_index_example.py
$ python ivf_index_example.py
```
