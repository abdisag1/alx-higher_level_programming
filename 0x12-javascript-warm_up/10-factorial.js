#!/usr/bin/node
let first_arg = process.argv[2];
function factorial (first_arg) {
    if (isNaN(first_arg) || first_arg === 1) {
	return (1);
    } else {
	return (first_arg * factorial(first_arg-1));
    }
}
console.log(factorial(parseInt(first_arg)));
