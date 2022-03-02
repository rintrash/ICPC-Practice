package PNW2015;
import java.util.*;
public class M2015 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int numOperations = scan.nextInt();
        int invalid = 0;
        for(int num = 1; num <= 100; num++) {
            double num1 = num;
            for(int i = 0; i < numOperations; i++) {
                String operation = scan.next();
                int num2 = scan.nextInt();
                scan.nextLine();
                double result = operate(operation, num1, num2);
                if(operation.equals("DIVIDE")) {
                    int(num1) / int(num2) != 
                }
                num1 = result; 
            }
        }   
    }
    //so I go through all the numbers 1 to 100 
    private static double operate(String op, double num1, double num2) {
        switch(op) {
            case "SUBTRACT":
                return num1 - num2;
            case "DIVIDE":
                return num1 / num2; 
            case "MULTIPLY":
                return num1 * num2;
            default: 
                return 0.5;  
        }
    }
}