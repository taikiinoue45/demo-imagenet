FROM node as base
WORKDIR /app
COPY compose/local/frontend/entrypoint.sh /root/entrypoint.sh
RUN yarn global add @vue/cli
ENTRYPOINT /root/entrypoint.sh
