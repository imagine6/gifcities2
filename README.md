# Coding Challenge - GIFCities


<p>
  <br>
  <img width="600" src="https://cl.ly/72c755d3da1b/%255Bb6065d8232df0e6d2c0219b4284ecf3a%255D_Image%2525202018-09-06%252520at%25252011.22.36%252520PM.png" alt="logo of repository">
  <br>
  <br>
</p>

## Description
Find the best GIFs on the web

**Stay tuned**

## Result

![Demo](https://cl.ly/a755423b91ba/Screen%252520Recording%2525202018-09-06%252520at%25252011.43%252520PM.gif)



## Getting Started

Build the image and spin up the containers:

```sh
$ docker-compose up -d --build
```
Access the application at the address [http://localhost:5002/](http://localhost:5002/)

### Testing

Test without coverage:

```sh
$ docker-compose run web python manage.py test
```

Test with coverage:

```sh
$ docker-compose run web python manage.py cov
```

Lint:

```sh
$ docker-compose run web flake8 project
```
