FROM ubuntu:latest


#RUN apt update
RUN useradd -u 8877 newuser
#RUN apt install yes
WORKDIR /home/newuser
COPY print_colleagues_loop.sh .

USER newuser

CMD [ "bash" ,"./print_colleagues_loop.sh" ]