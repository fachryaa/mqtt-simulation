const payload = require('../payload.json')
const keys = Object.keys(payload);

const splitToJson = (str) => {
  const values = str.toString().split('*');
  var result =  JSON.stringify(Object.assign.apply({}, keys.map( (v, i) => ( {[v]: values[i]} ) ) ));
  
  return (JSON.parse(result));
}

console.log((splitToJson('1*15:40:47*5*4*5*72.28*True')));

module.exports = { splitToJson };