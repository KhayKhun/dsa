type MultiDimensionalArray = (number | MultiDimensionalArray)[];


var flat = function (arr:  MultiDimensionalArray, n: number):  MultiDimensionalArray {
    if (n === 0) return arr;
    
    const result:any = [];
    arr.forEach(x => {
        if (typeof x === 'number') {
            result.push(x);
        } else {
            result.push(...flat(x, n - 1));
        }
    })

    return result;
};


