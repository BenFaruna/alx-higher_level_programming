#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const character = 'https://swapi-api.hbtn.io/api/people/18/';
let moviesCount = 0;

request(url, (error, response, body) => {
  const data = JSON.parse(body);
  if (error) {
    console.log(error);
    return;
  }

  for (const film of data.results) {
    if (film.characters.includes(character)) {
      moviesCount = moviesCount + 1;
    }
  }
  console.log(moviesCount);
});
