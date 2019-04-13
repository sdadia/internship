#!/bin/sh
$SPARK_HOME/sbin/start-master.sh  --host localhost
cat /usr/local/spark-2.4.1-bin-hadoop2.7/logs/spark--org.apache.spark.deploy.master.*
$SPARK_HOME/sbin/start-slave.sh spark://localhost:7077 --cores 4 --memory 4G
cat /usr/local/spark-2.4.1-bin-hadoop2.7/logs/spark--org.apache.spark.deploy.worker.*

jupyter notebook --port=8889 --ip=0.0.0.0 --allow-root 