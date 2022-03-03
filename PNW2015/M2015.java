
import java.util.*;
public class M2015 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int numOperations = scan.nextInt();
        int invalid = 0;
        for(int i = 0; i < numOperations; i++) {
            String operation = scan.next();
            int num2 = scan.nextInt();
            scan.nextLine();
            for(int num = 1; num <= 100; num++) {
                double num1 = num;   
                if(!operate(operation, num1, num2)) {
                    invalid++;
                    break;
                }
                num1 = operateNum(operation, num1, num2); 
            }
        }   

        System.out.println(invalid);
    }
    //so I go through all the numbers 1 to 100 
    private static boolean operate(String op, double num1, double num2) {
        switch(op) {
            case "SUBTRACT":
                if(num1 - num2 < 0) {
                    return false;
                }
                return true;
            case "DIVIDE":
                if(num1 % num2 != 0) {
                    return false;
                }
                return true; 
            case "MULTIPLY":
                if(num1 * num2 < 0) {
                    return false;
                }
                return true;
            default: 
                return false;  
        }
    }

    private static double operateNum(String op, double num1, double num2) {
        switch(op) {
            case "SUBTRACT":
                return num1 - num2;
            case "DIVIDE":
                return num1 / num2;
            case "MULTIPLY":
                return num1 * num2;
            default: 
                return -1;  
        }
    }
}