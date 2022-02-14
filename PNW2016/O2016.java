package PNW2016;
import java.util.*;
public class O2016 {
    //ignores bad commands
    static char[][] grid;
    static String commands = "";
    public static void main (String[] args) {
        Scanner scan = new Scanner(System.in);
        int rows = scan.nextInt();
        int cols = scan.nextInt();
        grid = new char[rows][cols];

        String str = "";
        for(int r = 0; r < rows; r++) {
            str = scan.nextLine();
            for(int c = 0; c < cols; c++) {
                grid[r][c] = str.charAt(c); 
            }
        }

        commands = scan.nextLine();
    }

    public static void play() {
        
    }
}
