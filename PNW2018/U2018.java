//COMPLETED: outside test
package PNW2018;
import java.util.Scanner;
public class U2018 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int x = scan.nextInt();
        scan.close();
        int q = 0, p = 0; 
    
        int count = 0;
        while(x >= 4) {
          //p iterates from 3 to max 
          //q iterates from max to 3
    
          for(int i = 3; i <= x - 3; i++) {
            if(isPrime(i) && isPrime(x - i)) {
              p = i;
              q = x - i;
              x = q - p; //:)?
              break;
            } 
          }
          count++; //????? why :(
          //f 
        }
        System.out.println(count);
  
      }
    
      public static boolean isPrime(int n) {
        // Corner case
        if (n <= 1)
            return false;
    
        // Check from 2 to n-1
        for (int i = 2; i < n; i++)
            if (n % i == 0)
                return false;
        return true;
      }
}
