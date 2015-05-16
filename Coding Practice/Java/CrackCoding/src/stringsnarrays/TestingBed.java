package stringsnarrays;
import java.util.Scanner;

public class TestingBed {

	public TestingBed() {
		// TODO Auto-generated constructor stub
	}
	
	public static void test(Scanner input){
		String user = input.nextLine();
		System.out.println(user.length());
		char[] converted = user.toCharArray();
		for(int i = 0; i<user.length();i++){
			System.out.print(converted[i]);
			System.out.println(i);
		}
		
		for(int i=0;i < user.length()/2;i++){
			char tmp = converted[i];
			converted[i] = converted[user.length()-i-1];
			converted[user.length()-i-1] = tmp;
		}
		
		user = new String(converted);
		System.out.println(user);
	}//test()

}
