
import java.io.File;
import java.io.FileNotFoundException;
import java.lang.reflect.Array;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class AOC7 {
    public static BigInteger counter;
    //1843905223553 is too low
    public static void main(String[] args) throws FileNotFoundException {
        //Get file and convert to scanner.

        File f = new File("AOC7.text");
        
        //Run Solution 1 with time and counter output.
        long n = System.nanoTime();
        counter = new BigInteger("0");
        Scanner s = new Scanner(f);
        solution1(s);
        System.out.println(counter);
        n = System.nanoTime() - n;
        System.out.println(n / 1000000 - 18);

        //Run Solution 2 with time and counter output
        n = System.nanoTime();
        counter = new BigInteger("0");
        s = new Scanner(f);
        solution2(s);
        System.out.println(counter);
        n = System.nanoTime() - n;
        System.out.println(n / 1000000);
    }

    public static void solution1(Scanner s) {
        while(s.hasNextLine()) {
            boolean isCorrect = false;
            String t = s.nextLine();
            String[] parts = t.split(": ");
            double value = Double.parseDouble(parts[0]);
            String[] numbers = parts[1].split(" ");
            ArrayList<Double> q = new ArrayList<Double>();
            for (int i = 0; i < numbers.length; i++) {
                q.add(Double.parseDouble(numbers[i]));
            }
            char[] operations = new char[numbers.length - 1];
            for (int i = 0; i < numbers.length - 1; i++) {
                operations[i] = '+';
            }
            for (int i = 0; i < Math.pow(2, (operations.length)); i++) {
                Double total = q.get(0);
                for (int j = 0; j < operations.length; j++) {
                    if (operations[j] == '+') {
                        total += q.get(j + 1);
                    } else {
                        total = total * q.get(j + 1);
                    }
                }
                if (total == value) {
                    counter = counter.add(BigDecimal.valueOf(value).toBigInteger());
                    //System.out.println(counter);
                    isCorrect = true;
                    break;
                }
                operations = findAddOperations(operations);
            }

        }
    }

    public static char[] findAddOperations(char[] prior) {
        boolean add = true;
        for (int i = prior.length - 1; i >= 0; i--) {
            if (add == true && prior[i] == '+') {
                prior[i] = '*';
                add = false;
            } else if (add == true && prior[i] == '*') {
                prior[i] = '+';
            } else {
                break;
            }
        }
        return prior;
    }

    public static char[] findAddOperations2(char[] prior) {
        boolean add = true;
        for (int i = prior.length - 1; i >= 0; i--) {
            if (add == true && prior[i] == '+') {
                prior[i] = '*';
                add = false;
            } else if (add == true && prior[i] == '*') {
                prior[i] = '|';
                add = false;
            } else if (add == true && prior[i] == '|') {
                prior[i] = '+';
            } else {
                break;
            }
        }
        return prior;
    }


    public static void solution2(Scanner s) {
        while(s.hasNextLine()) {
            boolean isCorrect = false;
            String t = s.nextLine();
            String[] parts = t.split(": ");
            double value = Double.parseDouble(parts[0]);
            String[] numbers = parts[1].split(" ");
            ArrayList<Double> q = new ArrayList<Double>();
            for (int i = 0; i < numbers.length; i++) {
                q.add(Double.parseDouble(numbers[i]));
            }
            char[] operations = new char[numbers.length - 1];
            for (int i = 0; i < numbers.length - 1; i++) {
                operations[i] = '+';
            }
            for (int i = 0; i < Math.pow(3, (operations.length)); i += 1) {
                Double total = q.get(0);
                try {
                for (int j = 0; j < operations.length; j++) {
                    if (operations[j] == '+') {
                        total += q.get(j + 1);
                    } else if (operations[j] == '|') {
                        int length = q.get(j + 1).toString().length() - 2;
                        for (int k = 0; k < length; k++) {
                            total *= 10;
                        }
                        total += q.get(j + 1);
                    } else {
                        total = total * q.get(j + 1);
                    }
                }
                } catch (Exception e) {

                }
                if (total == value) {
                    counter = counter.add(BigDecimal.valueOf(value).toBigInteger());
                    break;
                } 
                operations = findAddOperations2(operations);
            }
        }
    }
}