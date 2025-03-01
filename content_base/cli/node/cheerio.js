const cheerio = require('cheerio');
const fs = require('fs');
const buffer = fs.readFileSync('temp.html');
const $ = cheerio.loadBuffer(buffer);

console.log($.html());
