FROM docker.m.daocloud.io/python:3.10

WORKDIR /opt/karuha
COPY . .
COPY ./examples/welcome_docker/config.json .

RUN pip install .[all] -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD [ "python" , "-m" , "karuha", "./config.json", "-m", "examples.welcome"]
