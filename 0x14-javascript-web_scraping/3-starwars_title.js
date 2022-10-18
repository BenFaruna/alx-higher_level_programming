#!/usr/bin/node

const request = require('request');
url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`
request(url, (error, response, body) => {
  const data = JSON.parse(body);
	console.log(data["title"]);
});
