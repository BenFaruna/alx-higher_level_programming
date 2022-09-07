#!/usr/bin/node

const { readFileSync } = require('fs');

function concat (firstFile, secondFile) {
  const content1 = readFileSync(firstFile);
  const content2 = readFileSync(secondFile);

  return (content1 + content2);
}

const file1 = process.argv[2];
const file2 = process.argv[3];

if (process.argv.length > 2) {
  console.log(concat(file1, file2));
}
