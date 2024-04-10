#!/usr/bin/node
//  a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
//  script must import dict from the file 101-data.js
//  In the new dictionary:
//  A key is a number of occurrences
//  A value is the list of user ids
//  Print the new dictionary at the end
const dic = require('./101-data.js').dict;
const dicList = Object.entries(dic);
const dicValues = Object.values(dic);
const newValues = [...new Set(dicValues)];
const newDic = {};
for (const n in newValues) {
  const nList = [];
  for (const m in dicList) {
    if (dicList[m][1] === newValues[n]) {
      nList.unshift(dicList[m][0]);
    }
  }
  newDic[newValues[n]] = nList;
}
console.log(newDic);
