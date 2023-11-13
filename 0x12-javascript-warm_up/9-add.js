#!/usr/bin/node
function add (m, n) {
  const x = m + n;
  console.log(x);
}

add(Number(process.argv[2]), Number(process.argv[3]));
