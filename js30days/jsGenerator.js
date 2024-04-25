function* fibGenerator() {
    let vals = []
    while(true){
        if(vals.length === 0) {
            vals.push(0)
            yield 0
        }
        if(vals.length === 1) {
            vals.push(1)
            yield 1
        }

        const n = vals[vals.length - 2] + vals[vals.length - 1]
        vals.push(n)
        yield n
    }
};

const gen = fibGenerator();
console.log(gen.next().value)
console.log(gen.next().value)
console.log(gen.next().value)
console.log(gen.next().value)
console.log(gen.next().value)
console.log(gen.next().value)
console.log(gen.next().value)
console.log(gen.next().value)
console.log(gen.next().value)
console.log(gen.next().value)
