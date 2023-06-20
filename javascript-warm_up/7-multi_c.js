#!/usr/bin/node
const args = process.argv;
let i = 0;
if (isNaN(args[2])) {
	  console.log('Missing number of occurrences');
} else {
	  for (i = 0; i < Number(args[2]); i++) {
		      let name = '';
		      name += 'C is fun';
		      console.log(name);
		    }
}
