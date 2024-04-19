function numIslands(grid: string[][]): number {
    let count = 0;
    for(let r = 0; r < grid.length; r++){
        for(let c = 0; c < grid[0].length; c++){
            if(grid[r][c] === '1'){
                dfs(grid,r,c)
                count++;
            }
        };
    };
    return count
};

function dfs(grid,r,c){
    if(r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] === '0') return
    grid[r][c] = '0'
    dfs(grid,r + 1, c)
    dfs(grid,r - 1, c)
    dfs(grid,r, c + 1)
    dfs(grid,r, c - 1)
}