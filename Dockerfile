FROM python:alpine
VOLUME data
COPY ./docker-conf.py ./data/config.py
WORKDIR data
RUN pip install --index-url https://git.glebmail.xyz/api/packages/PythonPrograms/pypi/simple pds
CMD pds
EXPOSE 4011