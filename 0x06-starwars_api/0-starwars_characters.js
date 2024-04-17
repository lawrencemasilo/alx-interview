#!/usr/bin/node

const axios = require('axios');

function getCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  axios.get(url)
    .then(response => {
      response.data.characters.forEach(characterUrl => {
        axios.get(characterUrl)
          .then(characterResponse => {
            console.log(characterResponse.data.name);
          })
          .catch(error => {
            console.error('Error: ', error);
          });
      });
    })
    .catch(error => {
      console.error('Error: ', error);
    });
}

if (process.argv.length !== 3) {
  console.log('Usage: node 0-starwars_characters.js [Movie ID]');
  process.exit(1);
}

getCharacters(process.argv[2]);
