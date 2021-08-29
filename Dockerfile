FROM public.ecr.aws/z9d2n7e1/nginx:1.19.5
EXPOSE 80
echo "Test" > index.html
COPY index.html /usr/share/nginx/html
