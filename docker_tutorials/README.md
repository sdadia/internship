Docker Image for Data Science
-----------------------

This Docker sets up a Jupyter-Spark Notebook with all the dependencies

With Docker Compose
```bash
docker-compose  up --build
```

Without Docker Compose
```bash
docker build --tag='spark_stack' .
```

```bash
docker run -it --net=host -v /home/:/home/   spark_stack
```
