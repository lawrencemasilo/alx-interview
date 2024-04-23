#!/usr/bin/node

const request = require('request');
const url = `https://swapi.dev/api/films/${process.argv[2]}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;

    getCharacterNames(characters);
  }
});

function getCharacterNames (characters) {
  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
      } else if (response.statusCode !== 200) {
        console.error('Status:', response.statusCode);
      } else {
        const character = JSON.parse(body);
        console.log(character.name);
      }
    });
  });
}
