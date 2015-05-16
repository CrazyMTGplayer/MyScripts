//1.3
package stringsnarrays;
import java.util.Scanner;

public class Removedups {

	public Removedups() {
		//removedups1 is nested for loop. O(n^2) run time
		//removedups2 can use constant extra memory. boolean flags
	}
	
	public static String removedups1(String str){
		
		for(int i = 0; i < str.length(); i++){
			for(int j = i+1; j < str.length(); j++){
				if (str.charAt(i) == str.charAt(j))
					str = str.substring(0,j) + str.substring(j+1);
				
			}//for that checks for dups over string
		}//for that picks up each letter
		
		return str;
	}//removedups()
	
	public static String removedups2(String str){
		return str;
	}//removedups2()
	
	public static void testRemoveDups(Scanner input){
		
		System.out.println("Input a string to reverse");
    	String user = input.nextLine();
    	
    	System.out.println(user + " with dups removed is " + Removedups.removedups1(user));
    	
    	input.close();
	}//testReverse()

}
