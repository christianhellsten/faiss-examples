FROM continuumio/anaconda3

RUN conda install faiss-cpu -c pytorch

WORKDIR /app

RUN pip install --upgrade pip
ADD requirements.txt /app/
RUN pip install -r requirements.txt
