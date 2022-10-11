FROM python:3.8-slim-buster

WORKDIR Example.Python.Api


RUN pip install Flask==2.1.2

COPY main.py /Example.Python.Api

ENTRYPOINT ["python"]

CMD ["main.py"]

EXPOSE 443/tcp 8080/tcp