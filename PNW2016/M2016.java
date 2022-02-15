//INCOMPLETE: need help
//I think the problem is im just finding a solution, but not the minimum number of inserts 
package PNW2016;

import java.util.*; 
public class M2016 {
    public static void main (String[] args) {
        String str = "zabcz";
        int count = getCount(str);

        System.out.println(count);
    }

    public static int getCount(String str) {
        int[] bestArr = new int[str.length()]; //array of all longest substring lengths
        for(int i = 0; i < str.length(); i++) {
            int best = 1; //starts at 1 because the substring will be at least 1 
            for(int j = 0; j < i; j++) { //< i to go through all variations 
                if(str.charAt(i) > str.charAt(j) && bestArr[j] + 1 > best) { //if in order and longer substring
                    best = bestArr[j] + 1; //increments best when in order
                } 
            }
            bestArr[i] = best; //update bestArray to either be 1 or increment 1 if new best
        }

        int max = 0;
        for(int b = 0; b < bestArr.length; b++) {
            if(bestArr[b] > max) {
                max = bestArr[b];
            }
        } 

        return 26 - max;
    }
}
