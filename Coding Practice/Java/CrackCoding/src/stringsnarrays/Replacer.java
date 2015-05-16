//1.5
package stringsnarrays;
import java.util.Scanner;

public class Replacer {

	public Replacer() {
		// TODO Auto-generated constructor stub
	}
	
	public static String replacer(String str){
		return str.replaceAll("\\s", "%20");
	}//replacer()

	public static void testReplacer(Scanner input){
		
		System.out.println("Input string with spaces to replace check");
    	String user1 = input.nextLine();
    	
    	System.out.println(user1 + " _ replaced with %20 is "+ Replacer.replacer(user1));
	}//testReplacer
	
}
