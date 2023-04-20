#基于python:3.8这个基础镜像镜像构建镜像
FROM python:3.8
#  设置环境变量
ENV PYTHONUNBUFFERED 1
#  在容器内创建/var/mydjango 文件夹
RUN mkdir -p /var/mydjango
# 设置容器内工作目录为 /var/mydjango
WORKDIR /var/mydjango
# 将当前目录下所有文件添加至Docker容器内的工作目录中
ADD . /var/mydjango
#安装依赖包
RUN pip3 install -r requirements.txt
# 对外暴露3000端口
EXPOSE 3000
#设置容器执行后自动执行的命令
COPY script.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/script.sh
CMD ["/usr/local/bin/script.sh"]
#CMD ["python3","manage.py","runserver","0.0.0.0:3000"]