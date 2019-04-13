# Run this file as docker build --tag='jupyter_stack' .
# Run the container as docker run -p 8889:8889  jupyter_stack

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
RUN pip install --upgrade awscli boto3 flintrock s3fs

# Install new jupyter notebook theme : https://github.com/dunovank/jupyter-themes
#RUN pip install --upgrade jupyterthemes
#RUN jt -t chesterish -fs 95 -altp -tfs 11 -nfs 115 -cellw 88% -T 

# bash completion
RUN apt install bash-completion -y

RUN pip install findspark

# start jupyter notebook on 8889
ENTRYPOINT jupyter notebook --port=8889 --ip=0.0.0.0 --allow-root 
