//COMPLETE: had to look at solution
package PNW2016;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class T2016 {
    static char[][]grid; 
    public static void main (String[] args) {
        /**
         * 1. pick a land 
         * 2. clear all surrounding land (recursion)
         * 3. repeat. 
         */
        Scanner scan = new Scanner(System.in);
        int rows = scan.nextInt();
        int cols = scan.nextInt();
        scan.nextLine();

        grid = new char[rows][cols];
        //List<int[]> cloudPos = new ArrayList<int[]>();
        //build grid
        for(int i = 0; i < rows; i++) {
            String str = scan.nextLine();
            for(int j = 0; j < cols; j++) {
                char c = str.charAt(j);
                grid[i][j] = c; 
            }
        }

        int numIslands = 0;
        for(int r = 0; r < rows; r++) {
            for(int c = 0; c < cols; c++) {
                if(grid[r][c] == 'L' || grid[r][c] == 'C') {
                    numIslands++;
                    makeIsland(r, c);
                }
            }
        }

        System.out.println(numIslands);

    }

    //accounts for all surrounding land
    public static void makeIsland(int r, int c) {
        if(r >= grid.length || r < 0 || c >= grid[r].length || c < 0 ||
            grid[r][c] == 'X' || grid[r][c] == 'W') {
            return;
        }

        grid[r][c] = 'X';

        for(int i = -1; i <= 1; i++) {
            makeIsland(r+i, c); 
            makeIsland(r, c+i);
        } 
    }
}
