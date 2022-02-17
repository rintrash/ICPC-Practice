//COMPLETE: But had to look at solution for rounding 
package PNW2018;
import java.util.*;
public class T2018 {
    public static void main (String[] args) {
        String input = "4 8 7 8 9 9";
        Scanner scan = new Scanner(input);
        int x = scan.nextInt();
        int y = scan.nextInt();
        int x1 = scan.nextInt();
        int y1 = scan.nextInt();
        int x2 = scan.nextInt();
        int y2 = scan.nextInt();

        //if x < x1, if x > x2
        int dx = 0;
        int dy = 0;
        if(x < x1) {dx = x1 - x;}
        if(x > x2) {dx = x - x2;}
        if(y < y1) {dy = y1 - y;}
        if(y > y2) {dy = y - y2;}

        double rope = Math.hypot(dx, dy);
        System.out.printf("%.3f", rope);
    }
}
