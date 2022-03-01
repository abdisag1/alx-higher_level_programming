#!/usr/bin/node
'use strict';
let arguments = process.argv;
if (arguments[2] === undefined)
console.log('No argument');
else {
console.log(arguments[2]);
}
