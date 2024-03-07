// Beats98.04%of users with TypeScript
function letterCombinations(digits){
    let dummy = [
        ["a","b","c"], 
        ["d","e","f"], 
        ["g","h","i"],
        ["j","k","l"],
        ["m","n","o"],
        ["p","q","r","s"],
        ["t","u","v"],
        ["w","x","y","z"]
    ]
    let temp = []
    for(let i =0;i<digits.length;i++){
        temp.push(dummy[parseInt(digits[i]) - 2]);
    }
    let result = temp[0] || []

    for(let i = 1;i<temp.length;i++){
        let samp = []
        for(let j = 0;j < result.length;j++){
            for(let k = 0;k < temp[i].length;k++){
                samp.push(result[j] + temp[i][k])
            }
        }
        result = samp
    }
    return result;
};

let digits = ""
console.log(letterCombinations(digits))