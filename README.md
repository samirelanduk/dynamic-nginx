# dynamic-nginx

To run normally, serving the contents of a folder called public on the host machine home directory:

`$ docker run -p 80:80 -v /home/myusername/public:/usr/share/nginx/html samirelanduk/dynamic-nginx`

To dynamically serve particular files:

`$ docker run -p 80:80 -e "DYNAMIC_DOCUMENT_MYDOMAIN_COM=document.pdf" -v /home/myusername/public:/usr/share/nginx/html samirelanduk/dynamic-nginx`

Now `http://document.mydomain.com/` will serve document.pdf