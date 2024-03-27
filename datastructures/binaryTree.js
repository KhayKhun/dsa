class Node{
    constructor(val){
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

const a = new Node(1);
const b = new Node(2);
const c = new Node(3);
const d = new Node(4);
const e = new Node(5);
const f = new Node(0);
  
a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

function depthFirstValues(root){
    if(!root) return;
    let v = []
    let stack = [root]
    while(stack.length > 0){
        const current = stack.pop();
        v.push(current.val)
        if(current.left)stack.push(current.left)
        if(current.right)stack.push(current.right)
    }
    return v
}
function depthFirstValuesRecursive(root){
    if(!root) return [];
    return [root.val,...depthFirstValuesRecursive(root.left),...depthFirstValuesRecursive(root.right)]
}
function isSameTree(p,q){
    console.log(p?.val,q?.val)
    if(!p && !q) return true
    
    if(p && q && p.val === q.val){
        return isSameTree(p.left,q.left) && isSameTree(p.right,q.right)
    }
    return false
};
function breadthFirstValues(root){
    if(!root) return;
    let v = []
    let stack = [root]
    while(stack.length > 0){
        const current = stack.shift();
        v.push(current.val)

        if(current.left)stack.push(current.left)
        if(current.right)stack.push(current.right)
    }
    return v
}

function isInTree(root,target){
    if(!root) return false;
    let stack = [root]
    while(stack.length > 0){
        const current = stack.pop()
        if(current.val == target){
            return true
        }
        if(current.left) stack.push(current.left)
        if(current.right) stack.push(current.right)
    }
    return false
}
function isInTreeReursive(root,target){
    if(!root) return false;
    if(root.val === target) return true
    return isInTreeReursive(root.left,target) || isInTreeReursive(root.right,target)
}

function sum(root){
    if(!root) return 0;
    let sum = 0
    let stack = [root]
    while(stack.length > 0){
        const current = stack.pop()
        sum += current.val;
        if(current.left) stack.push(current.left)
        if(current.right) stack.push(current.right)
    }
return sum
}

function sumRecursive(root){
    if(!root) return 0;
    return root.val + sum(root.left) + sum(root.right)
}

function smallest(root){
    if(!root) return;
    let min = root.val;
    let stack = [root];
    while(stack.length > 0){
        console.log(stack)
        let current = stack.pop()
        if(current.val < min) min = current.val
        if(current.left) stack.push(current.left)
        if(current.right) stack.push(current.right)
    }
return min
}
function smallestRecursive(root){
    if(!root) return;
    const left = root.left ? smallestRecursive(root.left) : root.val;
    const right = root.right ? smallestRecursive(root.right) : root.val;
    return Math.min(root.val, left, right);
}

function smallestRecursiveUsingInfinity(root){
    if(!root) return Infinity;
    return Math.min(root.val, smallestRecursive(root.left),smallestRecursive(root.right) )
}

function maxPath(root){
    if(!root) return 0;
    let max = root.val

    function sumTilLeaf(root,sum = 0){
        let current_sum = root.val + sum
        if(!root.left && !root.right){
            if(current_sum > max) max = current_sum
        }
        if(root.left){
            sumTilLeaf(root.left,current_sum)
        }
        if(root.right){
            sumTilLeaf(root.right,current_sum)
        }
    }
    sumTilLeaf(root)
    return max

}

function maxPath2(root){
    if(!root) return -Infinity;
    const maxChild = Math.max(maxPath2(root.left), maxPath2(root.right))
    return root.val + (maxChild != -Infinity ? maxChild : 0);
}

console.log(maxPath2(a))