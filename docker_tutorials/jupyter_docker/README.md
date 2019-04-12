Docker Image for Data Science
-----------------------

This Docker sets up a Jupyter Notebook with all the dependencies

Create Docker Image
```bash
docker build --tag='datascience_image' .
```

Run the Container
```bash
docker run -p 8889:8889  datascience_image

```
Run the Container with Access to database on host machine
```bash
docker run -p 8889:8889 --network=host   datascience_image

```

Run the Container without database +  host directory
```bash
docker run -p 8889:8889 --network=host -v <local/directory>:/home/  datascience_image

```

Run the Container with aws credentials with environemnt variables
```bash
docker run -p 8889:8889 \
		   -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
		   -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY  \
		   datascience_image 

```