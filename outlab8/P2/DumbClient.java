import java.io.*;  
import java.net.*; 
import java.util.Scanner; 
public class DumbClient {  
public static void main(String[] args) throws UnknownHostException,IOException
{      
Socket s=new Socket("localhost",6970);  

//Scanner in=new Scanner(s.getInputStream());
//String str1=in.next();
//System.out.println(str1);
System.out.println(args[0]);

PrintStream p=new PrintStream(s.getOutputStream());
p.println(args[0]);

Scanner in1=new Scanner(s.getInputStream());
String str2=in1.next();
System.out.println(str2);

}  
}  
