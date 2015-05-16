//1.4
package stringsnarrays;
import java.util.Scanner;
import java.util.Arrays;

public class Anagrams {

	public Anagrams() {
		// TODO Auto-generated constructor stub
	}
	
	public static boolean anagram(String str1, String str2){
		return Anagrams.sorter(str1).equals(Anagrams.sorter(str2));
	}//anagram() sort strings and compare
	
	public static String sorter(String str){
		str = str.replaceAll("\\s", "");//get rid of white space
		str = str.toLowerCase();//drop everything to same case
		char[] convert = str.toCharArray();
		Arrays.sort(convert);//sorting the letters
		str = new String(convert);
		
		return str;
	}//sorter() fucntion for anagram check
	
	public static void testAnagram(Scanner input){
		
		System.out.println("Input 2 strings to anagram check");
    	String user1 = input.nextLine();
    	String user2 = input.nextLine();
    	
    	System.out.println(user1 + " and " + user2 + " are "+ Anagrams.anagram(user1, user2));
	}//testAnagram()

}
