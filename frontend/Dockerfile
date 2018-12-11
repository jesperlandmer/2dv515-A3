FROM node:10.8.0-alpine

# Set application folder path
ENV PATH_APP=/app/
RUN mkdir $PATH_APP

# Install dependencies
COPY package*.json $PATH_APP
WORKDIR $PATH_APP
RUN npm install

COPY . $PATH_APP

CMD ["npm", "start"]
