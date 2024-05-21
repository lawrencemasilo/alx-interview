#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

const fetchCharacterName = (url) => {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (err, res, body) => {
      if (err) {
        return reject(err);
      }
      resolve(body.name);
    });
  });
};

request(apiUrl, { json: true }, async (err, res, body) => {
  if (err) {
    console.error('Error fetching movie data:', err);
    process.exit(1);
  }

  if (!body.characters || body.characters.length === 0) {
    console.error('No characters found for this movie');
    process.exit(1);
  }

  try {
    const characterNames = await Promise.all(body.characters.map(fetchCharacterName));
    characterNames.forEach((name) => console.log(name));
  } catch (error) {
    console.error('Error fetching character names:', error);
  }
});
