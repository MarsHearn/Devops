
FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /var/mydjango

WORKDIR /var/mydjango

ADD . /var/mydjango

RUN pip3 install -r requirements.txt

EXPOSE 3000

COPY script.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/script.sh
CMD ["/usr/local/bin/script.sh"]
#CMD ["python3","manage.py","runserver","0.0.0.0:3000"]