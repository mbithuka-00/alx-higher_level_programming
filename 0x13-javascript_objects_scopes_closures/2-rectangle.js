#!/usr/bin/node
class Rectangle {
  constructor (w, l) {
    if ((w > 0) && (l > 0)) {
      this.width = w;
      this.height = l;
    }
  }
}

module.exports = Rectangle;
