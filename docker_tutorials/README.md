Docker Image for Data Science
-----------------------

Create Docker Image
```
docker build --tag='datascience_image' .
```

Run the Container
```
docker run -p 8889:8889  datascience_image

```
Run the Container with Access to database on host machine
```
docker run -p 8889:8889 --network=host   datascience_image

```

Run the Container without database +  host directory
```
docker run -p 8889:8889 --network=host -v <local/directory>:/home/  datascience_image

```
