# The IP Gods

This project was created by "The IP Gods" for GovHack 2017. It is a Django app, which allows users to check on the status of patent and trademark applications. It is hosted on heroku and can be accessed through the custom domain [ipgod.tech](http://ipgod.tech)

## Project Links

- [Project Page](https://2017.hackerspace.govhack.org/project/ip-gods)
- [GitHub Org](https://github.com/The-IP-Gods)
- [Video](https://youtube.com/somewhere)

## Data Sets

We made extensive use of the [Intellectual Property Government Open Data](https://2017.hackerspace.govhack.org/dataset/intellectual-property-government-open-data-2017-govhack) from 2017

## Running Locally

```bash
$ git clone https://github.com/The-IP-Gods/The-IP-Gods.git
$ cd The-IP-Gods
$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

Deployment to Heroku is achieved through Continuious Integration on Semaphore. This means all pushes to master on github will result in a deploy to the Heroku server.

[![Build Status](https://semaphoreci.com/api/v1/puzzleduck/the-ip-gods/branches/master/badge.svg)](https://semaphoreci.com/puzzleduck/the-ip-gods)

## The IP Gods Team

The IP Gods are:

- Trent Torkar,
- Riley Baird,
- Ben Minerds, and
- Jake Pringle
