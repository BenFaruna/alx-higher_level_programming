#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const character = "https://swapi-api.hbtn.io/api/people/18/";
let moviesCount = 0;

request(url, (error, response, body) => {
  data = JSON.parse(body);
	for (const film of data["results"]) {
		if (film["characters"].includes(character)) {
			moviesCount = moviesCount + 1;
		}
	}
	console.log(moviesCount);
});
