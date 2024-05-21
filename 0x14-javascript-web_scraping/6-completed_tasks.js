#!/usr/bin/node
// a script that computes the number of tasks completed by user id

const req = require('request');
const url = process.argv[2];

req.get(url, { json: true }, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const completedTasks = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 1;
      } else {
        completedTasks[todo.userId] += 1;
      }
    }
  });
  console.log(completedTasks);
});
