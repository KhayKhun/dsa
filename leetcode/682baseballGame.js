// beats 90.17%
function calPoints(operations){
    let records = [];
    operations.forEach((o)=>{
        if(Number(o)) records.push(Number(o));
        else if(o === '+')records.push(records[records.length - 1] + records[records.length - 2]);
        else if(o === 'C')records.pop();
        else if(o === 'D')records.push(records[records.length - 1] * 2);
    })
    return records.reduce((acc, curr) => acc + curr, 0);
}

const ops = ["5", "-2", "4", "C", "D", "9", "+", "+"];

console.log(calPoints(ops));