class Calculator {
    value: number
    constructor(v: number) {
        this.value = v
    }
    
    add(v: number): Calculator {
        this.value += v
        return this
    }
    
    subtract(v: number): Calculator {
        this.value -= v
        return this
    }
    
    multiply(v: number): Calculator {
        this.value *= v
        return this
    }
    
    divide(v: number): Calculator {
        if(!v) throw new Error("Division by zero is not allowed")
        this.value /= v
        return this
    }
    
    power(v: number): Calculator {
        this.value **= v
        return this
    }
    
    getResult(): number {
        return this.value
    }
}