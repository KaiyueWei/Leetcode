class Solution {
    public void addCell(int r, int c, Queue<int[]> queue, int[][] visited, int[][] grid, int rows, int cols){
        if(r<0 || r>= rows || c <0 || c >= cols || visited[r][c] == 1 || grid[r][c] == -1){
            return;
        }
        visited[r][c] = 1;
        queue.offer(new int[]{r, c});
    }
    public void islandsAndTreasure(int[][] grid) {

        int rows = grid.length;
        int cols = grid[0].length;
        int[][] visited = new int[rows][cols];
        Queue<int[]> queue = new ArrayDeque<>();

        for(int i = 0; i<rows;i++){
            for(int j = 0; j<cols;j++){
                if (grid[i][j] == 0){
                    visited[i][j] = 1;
                    queue.offer(new int[]{i, j});
                }else{
                    visited[i][j] = 0;
                }
            }
        }

        int distance = 0;
        while (!queue.isEmpty()){
            int size = queue.size();
            for(int i = 0; i<size;i++){
                int[] cell = queue.remove();
                int r = cell[0];
                int c = cell[1];

                if(grid[r][c] == Integer.MAX_VALUE){
                    grid[r][c] = distance;
                }
                addCell(r+1, c, queue, visited, grid, rows, cols);
                addCell(r-1, c, queue, visited, grid, rows, cols);
                addCell(r, c-1, queue, visited, grid, rows, cols);
                addCell(r, c+1, queue, visited, grid, rows, cols);
            }
            distance += 1;
        }
        
    }
}
