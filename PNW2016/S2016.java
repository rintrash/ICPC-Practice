//COMPLETE
package PNW2016;

import java.util.Map;
import java.util.Scanner;
import java.util.concurrent.ConcurrentHashMap;

public class S2016 {
    public static void main (String[] args) {
        Scanner scan = new Scanner(System.in); 
        int rows = scan.nextInt();
        int cols = scan.nextInt();
        scan.nextLine();
        char[][] grid = new char[rows][cols];
        Map<Integer, int[]> apples = new ConcurrentHashMap<>();
        
        int numApples = 0; 
        for(int i = 0; i < rows; i++) {
            String str = scan.nextLine();
            for(int j = 0; j < cols; j++) {
                char c = str.charAt(j);
                grid[i][j] = c; //adds to grid
                if(c == 'o') {
                    apples.put(numApples, new int[]{i, j}); //adds apple position
                    numApples++; 
                }
            }
        }

        scan.close();

        //while(!blocked(grid, apples)) {
          //  fall(grid, apples);
        //}
        fall(grid,apples);
        fall(grid,apples);
        fall(grid,apples);
        fall(grid,apples);
        System.out.println();
        for(int i = 0; i < rows; i++) {
            for(int j = 0; j < cols; j++) {
                System.out.print(grid[i][j]);
            }
            System.out.println();
        }
    }

    //apple falls
    public static void fall(char[][] grid, Map<Integer, int[]> apples) {
        for(int[] pos : apples.values()) {
            if(empty(pos, grid)) {
                int r = pos[0];
                int c = pos[1];
                grid[r][c] = '.';
                grid[r + 1][c] = 'o';
                pos[0] = r + 1; //update position
            }
        }
    }

    public static boolean empty(int[] pos, char[][]grid) {
        int r = pos[0];
        int c = pos[1];

        if(r + 1 != grid.length && grid[r + 1][c] == '.') { //not bottom or wall/object
            return true;
        }
        return false;
    }

    //so i got the positions of apples
    public static boolean blocked(char[][]grid, Map<Integer, int[]> apples) {
        for(int[] pos : apples.values()) {
            if(empty(pos, grid)) { 
                return false;
            } 
        }
        return true;
    }
}
