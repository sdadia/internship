# Run this file as docker build --tag='my_spark_dist' .
# Run the container as docker run -it -p 4040:4040 -p 8080:8080 -p 7070:7070  my_spark_dist
FROM ubuntu:18.04

RUN apt-get update && \
        apt-get install -y  vim
RUN apt-get update -y

# install ultility tools
RUN apt install -y curl

# install python 3.6
RUN apt update
RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv && \
        apt-get install -y git

# insall pip
RUN python3.6 -m pip install pip --upgrade && \
        python3.6 -m pip install wheel

# install jupyter stack
RUN pip install jupyter ipython
RUN pip install scikit-learn matplotlib pandas numpy scipy

# install visualization stack
RUN pip install seaborn bokeh plotly holoviews hvplot folium

# install data-science stack
RUN pip install kaggle pytest

# install database stack
RUN pip install SQLAlchemy psycopg2-binary PyMySQL pymssql

# install cloud stack
RUN pip install --upgrade awscli boto3 s3fs findspark


RUN apt-get update && \
        apt-get install -y  vim curl git wget
RUN apt-get update -y

# install java for spark
RUN apt install -y openjdk-8-jre-headless

#Download the Spark binaries from the repo
WORKDIR /usr/local/
RUN wget --no-verbose https://www-eu.apache.org/dist/spark/spark-2.4.1/spark-2.4.1-bin-hadoop2.7.tgz 

# Untar the downloaded binaries, move them the folder name spark 
RUN tar xf spark-2.4.1-bin-hadoop2.7.tgz

# set path of java and spark
ENV SPARK_HOME=/usr/local/spark-2.4.1-bin-hadoop2.7
RUN echo "export SPARK_HOME=/usr/local/spark-2.4.1-bin-hadoop2.7" >> ~/.bashrc
RUN echo "export PATH=$PATH:$SPARK_HOME/bin" >> ~/.bashrc
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> ~/.bashrc

# Use python3 as runtime environment
RUN echo "export PYSPARK_PYTHON=/usr/bin/python3" >> ~/.bashrc
RUN echo "export PYSPARK_DRIVER_PYTHON=/usr/bin/python3" >> ~/.bashrc

# install for getting ipconfig
RUN apt install net-tools

# Start master and worker
WORKDIR /
# set master URL
COPY ./entrypoint.sh /
ENTRYPOINT ["bash", "entrypoint.sh"]

EXPOSE 8889 8080 7070 4040