#!/usr/bin/node
class Rectangle {
  constructor (w, l) {
    if ((w > 0) && (l > 0)) {
      this.width = w;
      this.height = l;
    }
  }

  print () {
    for (let m = 0; i < this.height; m++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Rectangle;
