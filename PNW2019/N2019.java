package PNW2019;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class N2019 {
    public static void main (String[]args) {
        //top left rectangle is black
        //A rect vertical, B rect horizontal
        //R and C grid.
        Scanner scan = new Scanner(System.in); //R C A B. Next a lines are 
        String str = scan.nextLine(); 

        Scanner scn = new Scanner(str); 
        int r = scn.nextInt();
        int c = scn.nextInt();
        int A = scn.nextInt();
        int B = scn.nextInt();
        scn.close(); 

        int[] heights = new int [A];
        int[] widths = new int [B];

        //gets block heights
        for(int i = 0; i < A; i++) {
            heights[i] = scan.nextInt();
            scan.nextLine();
        }

        //gets block widths 
        for(int j = 0; j < B; j++) {
            widths[j] = scan.nextInt();
            scan.nextLine();
        }

        int color = 0; 
    
        for(int h : heights) {
            for(int row = 0; row < h; row++) {
                int count = 0;
                for(int w : widths) { 
                    for(int tile = 0; tile < w; tile++) {
                        if(color % 2 == 0) {
                            System.out.print("B"); 
                        }  else {
                            System.out.print("W");
                        }
                    }
                    if(widths.length % 2 == 1 && count == widths.length - 1) { //odd means at BB WW BB it needs not change
                        
                    } else {
                        color++;
                    }
                    count++;
                     //unsures it doesnt change when going to next row
                }
                System.out.println();
            }
            color++; 
            
        }
        scan.close();

    }
}
