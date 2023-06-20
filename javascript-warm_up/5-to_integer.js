#!/usr/bin/node
const args = process.argv;
if (isNaN(args[2])) {
	  console.log('Not a number');
} else if (Number(args[2]) !== isNaN) {
	  console.log('My number:', Number(args[2]));
} else {
	  console.log('Not a number');
}
