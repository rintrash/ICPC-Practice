//INCOMPLETE
package PNW2016;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class T2016 {
    final static char WATER = 'W';
    final static char LAND = 'L';
    final static char CLOUD = 'C';
    public static void main (String[] args) {
        Scanner scan = new Scanner(System.in);
        int rows = scan.nextInt();
        int cols = scan.nextInt();
        scan.nextLine();

        char[][] grid = new char[rows][cols];
        List<int[]> cloudPos = new ArrayList<int[]>();
        //build grid
        for(int i = 0; i < rows; i++) {
            String str = scan.nextLine();
            for(int j = 0; j < cols; j++) {
                char c = str.charAt(j);
                if(c == CLOUD) {
                    cloudPos.add(new int[]{i, j});
                }
                grid[i][j] = c; 
            }
        }

        //convert all clouds
        //if C is next to L then it is L 
            //else it is W
        //check if island. Check L surroundings, if has water and connected to a L then it's edge 
        //

    }

    public static void convertClouds(char[][] grid, List<int[]> cloud) {
        for(int i = 0; i < cloud.size(); i++) {
            int row = cloud.get(i)[0];
            int col = cloud.get(i)[1]; 
            boolean land = false;
            boolean water = false;
            if(row + 1 != grid.length && grid[row + 1][col] == LAND) {
                land = true;
            }
        }
    }
}
