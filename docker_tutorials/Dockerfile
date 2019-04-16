# Run this file as docker build --tag='my_spark_dist' .
# Run the container as :
#    docker run -v /home/sahil/:/home/ --net=host -it -p 8889:8889 -p 4040:4040 -p 8080:8080 -p 7070:7070  my_spark_dist
FROM ubuntu:18.04

RUN apt-get update && \
    apt install -y curl vim git wget net-tools
RUN apt-get update -y

#####
# Python Jupyter Stack
#####

# install python 3.6
RUN apt-get install -y python3.6 python3.6-dev python3-pip python3.6-venv

# upgrade pip
RUN python3.6 -m pip install pip --upgrade && \
        python3.6 -m pip install wheel

# install jupyter stack
RUN pip install --upgrade jupyter ipython
RUN pip install --upgrade scikit-learn matplotlib pandas numpy scipy pytest

# install visualization stack
RUN pip install --upgrade seaborn bokeh plotly holoviews hvplot folium

# install data-science stack
RUN pip install --upgrade kaggle

# install database stack
RUN pip install --upgrade SQLAlchemy psycopg2-binary PyMySQL pymssql


#####
# Cloud Stack
#####

# install cloud stack
RUN pip install --upgrade awscli boto3 s3fs findspark


#####
# Big Data Stack
#####


# install java for spark
RUN apt install -y openjdk-8-jre-headless

#Download the Spark binaries from the repo
WORKDIR /usr/local/
RUN wget --no-verbose https://www-eu.apache.org/dist/spark/spark-2.4.1/spark-2.4.1-bin-hadoop2.7.tgz 

# Untar the downloaded binaries, move them the folder name spark  and remove the tar repo
RUN tar xf spark-2.4.1-bin-hadoop2.7.tgz
RUN rm spark-2.4.1-bin-hadoop2.7.tgz 

# set path of java and spark
ENV SPARK_HOME=/usr/local/spark-2.4.1-bin-hadoop2.7
RUN echo "export SPARK_HOME=/usr/local/spark-2.4.1-bin-hadoop2.7" >> ~/.bashrc
RUN echo "export PATH=$PATH:$SPARK_HOME/bin" >> ~/.bashrc
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> ~/.bashrc

# Use python3 as runtime environment
RUN echo "export PYSPARK_PYTHON=/usr/bin/python3" >> ~/.bashrc
RUN echo "export PYSPARK_DRIVER_PYTHON=/usr/bin/python3" >> ~/.bashrc


# add new user monkey to sudo group
RUN apt install sudo
RUN adduser --disabled-password --gecos '' monkey
RUN adduser monkey sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER monkey

# add entrypoint to /opt folder
WORKDIR /opt/
COPY ./entrypoint.sh ./

# start from /home/
WORKDIR /home/

# start the etnry point
ENTRYPOINT ["bash", "/opt/entrypoint.sh"]

EXPOSE 8889 8080 7070 4040
