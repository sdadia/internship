#!/bin/sh
sudo $SPARK_HOME/sbin/start-master.sh  --host localhost
sudo cat /usr/local/spark-2.4.1-bin-hadoop2.7/logs/spark-root-org.apache.spark.deploy.master*
#sudo cat /usr/local/spark-2.4.1-bin-hadoop2.7/logs/spark-org.apache.spark.deploy.master.*
sudo $SPARK_HOME/sbin/start-slave.sh spark://localhost:7077 --cores 4 --memory 4G
sudo cat /usr/local/spark-2.4.1-bin-hadoop2.7/logs/spark-root-org.apache.spark.deploy.worker*
#sudo cat /usr/local/spark-2.4.1-bin-hadoop2.7/logs/spark-org.apache.spark.deploy.worker.*

jupyter notebook --port=8889 --ip=0.0.0.0 




	




# su - docker
