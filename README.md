# 2dv515-A3

#### Run

To run the project, download docker:
* [Docker för Mac](https://docs.docker.com/docker-for-mac/install/#download-docker-for-mac)  
* [Docker för Windows](https://docs.docker.com/toolbox/toolbox_install_windows/)  
* [Docker för Ubuntu](https://www.docker.com/docker-ubuntu) samt [docker-compose](https://docs.docker.com/compose/install/)

Start the project with `docker-compose up -d --build`.
Visit `localhost:80`.

#### API
`http://localhost/api/searchengine?query=<query>`

```
{
    {frequency: 1, link: "/wiki/Nintendo", location: 0.8, pageRa...
}
```
