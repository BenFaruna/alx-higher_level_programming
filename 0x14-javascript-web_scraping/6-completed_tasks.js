#!/usr/bin/node

const request = require("request");
const url = process.argv[2];
let completedTasks = {};

request(url, (error, response, body) => {
  let data = JSON.parse(body);
  for (const todo of data) {
    if (todo.completed == true) {
      if (todo.userId in completedTasks) {
        completedTasks[todo.userId] = completedTasks[todo.userId] + 1;
      } else {
        completedTasks[todo.userId] = 1;
      }
    }
  }
	console.log(completedTasks);
});
