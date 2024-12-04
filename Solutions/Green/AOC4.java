
package Day4;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
//1018
public class AOC4 {
    public static int counter;

    public static void main(String[] args) throws FileNotFoundException {
        //Get file and convert to scanner.

        File f = new File("Day4\\AOC4.text");
        //File f = new File("Day4\\AOC4Test.text");
        
        //Run Solution 1 with time and counter output.
        long n = System.nanoTime();
        counter = 0;  
        Scanner s = new Scanner(f);
        solution1(s);
        System.out.println(counter);
        n = System.nanoTime() - n;
        System.out.println(n / 1000000 - 63);

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
        int[][] changes = {{0, 1}, {1, 0}, {1, 1}, {-1, 0}, {-1, -1}, {0, -1}, {-1, 1}, {1, -1}};
        ArrayList<char[]> chars = new ArrayList<char[]>();
        while (s.hasNextLine()) {
            chars.add(s.nextLine().toCharArray());
        }
        for (int k = 0; k < chars.size(); k++) {
            for (int i = 0; i < chars.get(k).length; i++) {
                if (chars.get(k)[i] == 'X') {
                    for (int j = 0; j < 8; j++) {
                        try {
                        if (
                               chars.get(k + 1 * changes[j][0])[i + 1 * changes[j][1]] == 'M' 
                            && chars.get(k + 2 * changes[j][0])[i + 2 * changes[j][1]] == 'A' 
                            && chars.get(k + 3 * changes[j][0])[i + 3 * changes[j][1]] == 'S') {
                            counter++;
                        }
                        } catch (Exception e) {
        
                        }
                    }

                }
            }
    }
    }

    public static void solution2(Scanner s) {
        int[][] changes = {{1, 1}, {-1, -1}};
        ArrayList<char[]> chars = new ArrayList<char[]>();
        while (s.hasNextLine()) {
            chars.add(s.nextLine().toCharArray());
        }
        for (int k = 0; k < chars.size(); k++) {
            for (int i = 0; i < chars.get(k).length; i++) {
                if (chars.get(k)[i] == 'A') {
                    for (int j = 0; j < 4; j++) {
                        try {
                        if (    chars.get(k + 1 * changes[j][0])[i + 1 * changes[j][1]] == 'M' && chars.get(k - 1 * changes[j][0])[i - 1 * changes[j][1]] == 'S') {
                            if (chars.get(k - 1 * changes[j][0])[i + 1 * changes[j][1]] == 'M' && chars.get(k + 1 * changes[j][0])[i - 1 * changes[j][1]] == 'S'
                            ||  chars.get(k + 1 * changes[j][0])[i - 1 * changes[j][1]] == 'M' && chars.get(k - 1 * changes[j][0])[i + 1 * changes[j][1]] == 'S') {
                            counter++;
                            }
                        }
                        } catch (Exception e) {
        
                        }
                    }

                }
            }
    }


}
}