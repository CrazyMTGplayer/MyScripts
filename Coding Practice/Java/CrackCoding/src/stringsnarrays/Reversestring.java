//1.2
package stringsnarrays;
import java.util.Scanner;

public class Reversestring {

	public Reversestring() {
		// Reverse1, is an iterative implementation, runs in O(n) time
		// Reverse2, is a recursive implementation, runs in O(n) time
		// Reverse3, is iterative implementation, runs in O(n) time
	}
	
	public static String reverse1(String str){
		String output = "";
		for(int i = str.length() - 1; i >= 0; i--){
			output = output + str.charAt(i);
		}//for that reverses
		
		return output;
	}//reverse1()
	
	public static String reverse2(String str){
		if (str.length() == 1)//if you are at the last char pop up
			return str;
		
		return str.charAt(str.length()-1) + reverse2(str.substring(0, str.length()-1));
	}//reverse2()
	
	public static String reverse3(String str){
		char[] converted = str.toCharArray();//convert to char array for manip

		for(int i=0;i < str.length()/2;i++){//only do for 1/2 length, mid point rounded down needs no work
			char tmp = converted[i];//save to temp for swapping
			converted[i] = converted[str.length()-i-1];//-i to go inwards, -1 to avoid out of bounds
			converted[str.length()-i-1] = tmp;
		}//for that reverses
		
		str = new String(converted);//convert back to string

		return str;
	}//reverse3()
	
	public static void testReverse(Scanner input){
		
		System.out.println("Input a string to reverse");
    	String user = input.nextLine();
    	
    	System.out.println(user + " reversed with front concat to back is " + Reversestring.reverse1(user));
    	System.out.println(user + " reversed with recursion is " + Reversestring.reverse2(user));
    	System.out.println(user + " reversed with tmp var is " + Reversestring.reverse2(user));
	}//testReverse()
}
