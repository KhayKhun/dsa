function mergeSort(list){
    if(list.length <=1) return list;
    
    const mid = Math.round(list.length / 2);

    const leftHalf = list.slice(0, mid);
    const rightHalf = list.slice(mid);

    const left = mergeSort(leftHalf);
    const right = mergeSort(rightHalf);

    return merge(left, right);
}
function merge(list1,list2){
    const both = [];
    let i=0;
    let j=0
    while(i<list1.length && j<list2.length){
        if(list1[i] < list2[j]){
            both.push(list1[i]);
            i++;
        }else{
            both.push(list2[j]);
            j++;
        }
    }
    while(i<list1.length){
        both.push(list1[i]);
        i++;
    }
    while(j<list2.length){
        both.push(list2[j]);
        j++;
    }
    return both;
}
const l = [33,1,2,6,3,66,0,0,877]

console.log(mergeSort(l));