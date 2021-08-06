    import java.io.*;  
    import java.net.*;  
    import java.util.Scanner;
    class Server extends Thread {
    Socket s;
    String k;
	Server(Socket s,String k){
		this.s=s;
	        this.k=k;
	}  
    public void run(){
    try{
    Scanner out=new Scanner(k);
    
    Scanner in=new Scanner(s.getInputStream());
    String stri=in.next();
    System.out.println(stri);


    String stro=out.next();
    PrintStream p=new PrintStream(s.getOutputStream());
    p.println(stri+stro);

    
    

    //PrintStream p1=new PrintStream(s.getOutputStream());
    //p1.println(stro+stri);
    s.close();
    }
    catch (IOException e){
	    e.printStackTrace();
	}
    }
    }
public class EchoServer{
	public static void main(String []args) throws IOException{
	   ServerSocket ss=new ServerSocket(6970);  
	   while(true){
           Socket s=ss.accept();
           Scanner out=new Scanner(args[0]);
           String j=out.next();
           Server w=new Server(s,j);
           w.start();
}
}
}
