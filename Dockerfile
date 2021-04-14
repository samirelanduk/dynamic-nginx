FROM nginx:alpine

RUN apk add python3

COPY ./update-conf.py ./
COPY ./template.conf ./
RUN sed -i '/*.conf;/a include \/etc\/nginx\/sites-enabled\/*;' /etc/nginx/nginx.conf
RUN mkdir /etc/nginx/sites-enabled

CMD python3 update-conf.py && nginx -g 'daemon off;'