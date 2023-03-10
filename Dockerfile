FROM python
RUN apt-get update -y \
  && apt-get install -y gdal-bin
ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
