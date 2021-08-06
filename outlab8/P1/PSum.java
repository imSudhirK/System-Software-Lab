import java.util.Scanner;
public class PSum{
public static void main(String[] args) {
	Scanner input=new Scanner(System.in);
 int n =input.nextInt();
 int p =input.nextInt();
 int q=(int) Math.pow(p,n);
 int[] inp =new int[q];
 int a=q/p; 
 for(int i=0;i<q;i++){
	inp[i]=input.nextInt();
 }
 input.close();
 while(a>0){
 Thread[] dev=new Thread[a];
 for(int l=0;l<a;l++){
	 final int innerl=l;
 dev[l] =new Thread(new Runnable() {	
	public void run(){
						 int add=0;
 						for(int m=0;m<p;m++){
							 add=add+inp[(innerl*p)+m];
 						}
 						
 						inp[innerl]=add;
					 }
					}
				   );
				   dev[l].start();

 }

try{
	for(int i=0;i<a;i++){
	dev[i].join();
}
}
catch(Exception ex){

}
a=a/p;
}
System.out.println(inp[0]);
}}





