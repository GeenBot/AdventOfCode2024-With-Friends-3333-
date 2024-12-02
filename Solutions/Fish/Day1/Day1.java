import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Scanner;

public class Day1
{
    public static void main(String args[]) throws FileNotFoundException
    {
        S2();
    }


       public static void S1() throws FileNotFoundException{
       File f = new File("Day1\\Day1List.txt");
       Scanner s = new Scanner(f);
       int Counter = 0;
       int Answer = 0;

       int[] Lines1 = new int[1000];
       int[] Lines2 = new int[1000];
        
       while(s.hasNext())
       {
        String day1 = s.nextLine();
        String[] arr = day1.split("   ");

        Lines1[Counter] = Integer.parseInt(arr[0]);
        Lines2[Counter] = Integer.parseInt(arr[1]);

        Counter += 1;
       }


       Arrays.sort(Lines1);
       Arrays.sort(Lines2);

       for (int i = 0; i < 1000; i++) {
        Answer += Math.abs(Lines1[i] - Lines2[i]);
        System.out.println(Answer);
      }       
    }


    public static void S2() throws FileNotFoundException
    {
        File f = new File("Day1\\Day1List.txt");
        Scanner s = new Scanner(f);
        int Counter = 0;
        int Answer = 0;
        int TimesAppeared = 0;
 
        int[] Lines1 = new int[1000];
        int[] Lines2 = new int[1000];
         
        while(s.hasNext())
        {
         String day1 = s.nextLine();
         String[] arr = day1.split("   ");
 
         Lines1[Counter] = Integer.parseInt(arr[0]);
         Lines2[Counter] = Integer.parseInt(arr[1]);
 
         Counter += 1;
        }
 
 
        Arrays.sort(Lines1);
        Arrays.sort(Lines2);

        ArrayList<Integer> NumbersDoneAlready = new ArrayList<Integer>();
 
        for (int i = 0; i < 1000; i++) {
         if(!NumbersDoneAlready.contains(Lines1[i]))
         {
            TimesAppeared = 0;
            for (int e = 0; e < 1000; e++) {
              if(Lines1[i] == Lines2[e])
              {
                TimesAppeared += 1; 
              }
            }
              Answer += Lines1[i] * TimesAppeared;
              System.out.println(Answer);
         }
       }    
       s.close();
    }
}