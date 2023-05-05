#!/usr/bin/node
// Prints all characters in a Star Wars movie
const { argv } = require('node:process');
const filename = require('path').basename(__filename);
const request = require('request');

const apiEndpoint = 'https://swapi-api.alx-tools.com/api/films';

if (argv.length !== 3) {
  console.log(`Usage: ${filename} <film-number>`);
} else {
  request(`${apiEndpoint}/${argv[2]}`, (err, res, body) => {
    if (err) {
      console.error(err);
    } else {
      const characters = JSON.parse(body).characters;
      characters.forEach(character => {
        request(character, (err, res, body) => {
          if (err) {
            console.error(err);
          } else {
            const characterName = JSON.parse(body).name;
            console.log(characterName);
          }
        });
      });
    }
  });

  // Promise.all(
  //     characters.map((character => {
  //         console.log(character)
  //         request(character, (err, res, body) => {
  //             character_name = JSON.parse(body).name;
  //             return character_name;
  //         });
  //     }))
  // ).then(data => {
  //     data.forEach(character_name => console.log(character_name))
  // });
}
