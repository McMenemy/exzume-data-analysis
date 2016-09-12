var data = [];

var f1 = [{ x: '2016-11-10', y: 4 }, { x: '2016-12-10', y: 2 }];
var f2 = [{ x: '2016-11-10', y: 5 }, { x: '2016-13-10', y: 4 }];

var i1 = 0;
var i2 = 0;
while (i1 < f1.length && i2 < f2.length) {
  var dateF1 = new Date(f1[i1].x).getTime();
  var dateF2 = new Date(f2[i2].x).getTime();

  if (dateF1 == dateF2) {
    var row = {};
    row.f1 = f1[i1].y;
    row.f2 = f2[i2].y;
    data.push(row);
    i1++;
    i2++;
  } else if (dateF1 < dateF2) {
    var row = {};
    row.f1 = f1[i1].y;
    row.f2 = 'None';
    data.push(row);
    i1++;
  } else {
    var row = {};
    row.f1 = 'None';
    row.f2 = f2[i2].y;
    data.push(row);
    i2++;
  }

  console.log(data);
}

console.log(data);

// if (i1 < f1.length) {
//   data = data.concat(f1.slice(i1));
// } else {
//   data = data.concat(f1.slice(i2));
// }

