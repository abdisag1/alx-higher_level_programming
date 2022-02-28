#!/usr/bin/node
let number_of_arg = process.argv.length;
if (number_of_arg === 2) {
  console.log('No argument');
} else if (number_of_arg === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
