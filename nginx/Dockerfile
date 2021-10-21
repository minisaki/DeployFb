FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
RUN export DJANGO_SETTINGS_MODULE=mysite.settings.pro
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf
# COPY nginx/supervisor.conf /etc/supervisor/conf.d/