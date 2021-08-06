import java.util.*; 
import java.io.*;

public class FrequencyCollection{
	public static void countFrequencies(ArrayList<String> list){ 
        	Set<String> st = new HashSet<String>(list);
        	List<String> mylist = new ArrayList<String>(st);
        	Collections.sort(mylist);
        	for(String sw : mylist)
            	System.out.println(sw +" , " +Collections.frequency(mylist, sw));
  	}    		
	public static void main (String []args)throws IOException{
		if( args.length > 0){
			File file = new File ( args[0]);
			Scanner sc = new Scanner(file); 
			List<String> stopWords =Arrays.asList("and", "the","is", "in", "at", "of", "his", "her", "him");	
        	ArrayList<String> list = new ArrayList<String>();
        	while (sc.hasNextLine()){
        		String str =sc.nextLine();
	      		StringTokenizer st1 = new StringTokenizer(str);
				for (int i = 1; st1.hasMoreTokens(); i++){
					String str1=st1.nextToken();
					boolean ans = stopWords.contains(str1.toLowerCase());
					if(!ans)
						list.add(str1.toLowerCase());
				}
         	}
         	countFrequencies(list);	 		
		}
	}
}

