
const mongoose = require('mongoose');
//mongoose.connect('mongodb+srv://dashin:colatOnBat@cluster0.coywt.mongodb.net/test?authSource=admin&replicaSet=atlas-10vxuo-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true');


let repeat = 20000

 function _test()  {
  const shape = Math.random(50)
  const tiredness = Math.random(50)

  const data = [];
    const avgMinHr = 25;
    const avgMaxHr = 90;
  
    const originalAvgHR = Math.round(
      (avgMinHr + (avgMaxHr - avgMinHr) * (1 - shape)) * (1 + tiredness * 0.2),
    );
  
    const originalRR = Math.round((60 / originalAvgHR) * 1000);
  
    for (let index = 0; index < 1000; index++) {
      const rr = (60 / originalAvgHR) * 1000;
      const plusOrMinus = Math.random() < 0.5 ? -1 : 1;
      const variability = Math.round(
        plusOrMinus * rr * Math.random() * 0.2 * (1 - tiredness),
      );
      const total = rr + variability;
  
      data.push(Math.round(total));
    }
  
    let total = data.reduce(function (acc, val) {
      return acc + val;
    }, 0);
  
    const simulatedRR = Math.round(total / data.length);
    const simulatedAvgHR = Math.round(60000 / simulatedRR);
  
    const dataHR = {
      shape,
      tiredness,
      originalAvgHR,
      originalRR,
      simulatedAvgHR,
      simulatedRR,
      data,
    };

   // const Test = mongoose.model('test', dataHR);
//Test.insertMany(dataHR)
    return dataHR
}


const testData = []
while(repeat > 0) {

 testData.push(_test())
 repeat = repeat-1
}

JSON.stringify(testData)

console.log(testData)
var fs = require('fs');

fs.writeFileSync('test.json', JSON.stringify(testData));


  console.log(testData)