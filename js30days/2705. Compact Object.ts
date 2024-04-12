type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | JSONValue[];

function compactObject(obj: Obj): Obj {
    console.log(obj)
    if(Array.isArray(obj)){
        for (let index = 0; index < obj.length; index++) {
            const x = obj[index];
            if (x === null || x === false || x === 0 || x === '') {
                obj.splice(index, 1);
                index--; // Decrement index to account for the removed element
            } else if (typeof x === 'object') {
                compactObject(x as Obj); // Type assertion
            }
        }
    } else {
        Object.keys(obj).forEach(x => {
            if(obj[x] === null || obj[x] === false || obj[x] === 0 || obj[x] === '') delete obj[x];
            else if(typeof(obj[x]) === 'object') compactObject(obj[x] as Obj); // Type assertion
        });
    }
    return obj;
};
