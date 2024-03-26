class Node{
    constructor(val){
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

const a = new Node('a');
const b = new Node('b');
const c = new Node('c');
const d = new Node('d');
const e = new Node('e');
const f = new Node('f');
  
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
    console.log(root.val,target)
    if(root.val === target) return true
    const left = root.left ? isInTreeReursive(root.left,target) : false
    const right = root.right ? isInTreeReursive(root.right,target) : false
    return left || right
}

console.log(isInTreeReursive(a,'x'))
