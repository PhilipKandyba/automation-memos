FROM python:3.10
ENV PYTEST_MEMOS /automation-memos

WORKDIR $PYTEST_MEMOS

COPY . $PYTEST_MEMOS/

RUN apt-get update
RUN apt-get install default-jre -y
RUN curl -o allure-2.24.0.tgz -OLs https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.24.0/allure-commandline-2.24.0.tgz
RUN tar -zxvf allure-2.24.0.tgz -C /opt/
RUN ln -s /opt/allure-2.24.0/bin/allure /usr/bin/allure


COPY requirements.txt .
RUN pip install -r requirements.txt

CMD tail -f /dev/null