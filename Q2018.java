import java.util.Collections;
import java.util.Map;
import java.util.HashMap;
import java.util.Scanner;
class Q2018{
  public static void main(String[] args) {
    Scanner scn = new Scanner(System.in);
    Map<Character, Integer> map = new HashMap<>();
    String input = scn.nextLine();

    Scanner scan = new Scanner(input);
    while(scan.hasNext()) {
      String card = scan.next();
      char rank = card.charAt(0);
      if(!map.containsKey(rank)) {
        map.put(rank, 1);
      } else {
        int count = map.get(rank);
        map.put(rank, count + 1);
      }
    }
    //output max
    int max = Collections.max(map.values()); //max 
    System.out.println(max); //:)
    scan.close();
    scn.close();
  }
}