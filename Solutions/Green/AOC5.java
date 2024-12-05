




import java.util.ArrayList;
import java.util.Dictionary;
import java.util.Hashtable;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class AOC5 {
    public static int counter;
    public static int indexToFix;
    public static int indexFrom;
    //11144
    public static void main(String[] args) throws FileNotFoundException {
        //Get file and convert to scanner.

        File f = new File("AOC5.text");
        Scanner s = new Scanner(f);
        solution1(s);
        //File f = new File("Day5\\AOC5Test.text");
        
        //Run Solution 1 with time and counter output.
        long n = System.nanoTime();
        counter = 0;
        s = new Scanner(f);
        solution1(s);
        System.out.println(counter);
        n = System.nanoTime() - n;
        System.out.println(n / 1000000);

        //Run Solution 2 with time and counter output
        n = System.nanoTime();
        counter = 0;
        s = new Scanner(f);
        solution2(s);
        System.out.println(counter);
        n = System.nanoTime() - n;
        System.out.println(n / 1000000);
    }

    public static void solution1(Scanner s) {
        String string;
        ArrayList<Integer[]> d = new ArrayList<Integer[]>();
        while(s.hasNextLine()) {
            string = s.nextLine();
            if (string.equals("")) {
                break;
            }
            
            String[] n = string.split("\\|");
            Integer n0 = Integer.parseInt(n[0]);
            Integer n1 = Integer.parseInt(n[1]);
            d.add(new Integer[] {n0, n1});
        
        }
        while (s.hasNextLine()) {
            String[] arr = s.nextLine().split(",");
            Integer[] t = new Integer[arr.length];
            for (int i = 0; i < arr.length; i++) {
                t[i] = Integer.parseInt(arr[i]);
            }
            checkIfCorrect(d, t);
        }
    }

    public static int findIndexIn(Integer[] arr, Integer value) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].equals(value)) {
                return i;
            }
        }
        return 1000;
    }

    public static boolean checkIfCorrect(ArrayList<Integer[]> _d, Integer[] _t) {
        boolean isCorrect = true;
        for (int i = 0; i < _t.length; i++) {
            ArrayList<Integer> found = findAllOccurances(_d, _t[i]);
            if (found.size() > 0) {
                for (int j = 0; j < found.size(); j++) {
                if (findIndexIn(_t, found.get(j) ) <= i) {
                    isCorrect = false;
                    indexFrom = i;
                    indexToFix = findIndexIn(_t, found.get(j));
                    break;
                }
            }
            }
        }
        if (isCorrect) {
            counter += _t[_t.length / 2];
        }
        return isCorrect;
    }

    public static ArrayList<Integer> findAllOccurances(ArrayList<Integer[]> a, Integer value) {
        ArrayList<Integer> c = new ArrayList<Integer>();
        for (int i = 0; i < a.size(); i++) {
            if (a.get(i)[0].equals(value)) {
                c.add(a.get(i)[1]);
            }
        }
        return c;
    }

    public static void solution2(Scanner s) {
        String string;
        ArrayList<Integer[]> d = new ArrayList<Integer[]>();
        while(s.hasNextLine()) {
            string = s.nextLine();
            if (string.equals("")) {
                break;
            }
            
            String[] n = string.split("\\|");
            Integer n0 = Integer.parseInt(n[0]);
            Integer n1 = Integer.parseInt(n[1]);
            d.add(new Integer[] {n0, n1});
        
        }
        while (s.hasNextLine()) {
            String[] arr = s.nextLine().split(",");
            Integer[] t = new Integer[arr.length];
            for (int i = 0; i < arr.length; i++) {
                t[i] = Integer.parseInt(arr[i]);
            }
            if (checkIfCorrect(d, t)) {
                    counter -= t[t.length / 2];
            } else {
                while (!checkIfCorrect(d, t)) {
                    Integer temp = t[indexFrom];
                    t[indexFrom] = t[indexToFix];
                    t[indexToFix] = temp;
                }
            }

        }
    }
}