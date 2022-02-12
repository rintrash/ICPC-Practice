//COMPLETE
package PNW2016;

import java.util.Scanner;

public class R2016 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        String str = scn.nextLine();
        scn.close();
        
        Scanner scan = new Scanner(str);
        int a = scan.nextInt();
        scan.next();
        int b = scan.nextInt();
        scan.next();
        int c = scan.nextInt();

        if(a + b == c) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

        scan.close();
    }
}
