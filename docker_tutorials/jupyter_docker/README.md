Docker Image for Data Science
-----------------------

This Docker sets up a Jupyter Notebook with all the dependencies

Create Docker Image
```bash
docker build --tag='spark_stack' .
```

Run the Container
```bash
docker run -p 8889:8889 -p 7077:7077 -p 4040:4040 -v /home/:/home/ --net=host  spark_stack

```

Run the following commands
```bash
#!/bin/bash
$SPARK_HOME/sbin/start-master.sh --host 172.17.0.1
cat /usr/local/spark-2.4.1-bin-hadoop2.7/logs/spark--org.apache.spark.deploy.master.Master-1-09a1121ed833.out
$SPARK_HOME/sbin/start-slave.sh spark://localhost:7077
cat /usr/local/spark-2.4.1-bin-hadoop2.7/logs/spark--org.apache.spark.deploy.worker.Worker-1-09a1121ed833.out

jupyter notebook --port=8889 --ip=0.0.0.0 --allow-root 
```

Run the Container with aws credentials with environemnt variables
```bash
docker run --name='spark_stack' -p 8889:8889 \
		   -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
		   -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY  \
		   spark_stack 

```