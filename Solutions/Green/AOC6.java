package Day6;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class AOC6 {
    public static int counter;
    //2426 is too high.
    //1743 is too low.
    // 1911
    //2253
    public static void main(String[] args) throws FileNotFoundException {

        File f = new File("Day6\\AOC6.text");
        Scanner s = new Scanner(f);
        solution1(s);
        
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
        char[][] a = new char[130][];
        int c = 0;
        int[] start = {};
        while (s.hasNextLine()) {
            a[c] = s.nextLine().toCharArray(); 
            for (int i = 0; i < a[c].length; i++) {
                if (a[c][i] == '^') {
                    start = new int[] {c,i};
                    a[c][i] = 'X';
                    counter++;
                }
            }
            c++;
        }
        int[] currentPos = start;
        int[] currentDirection = {-1, 0};
        while (true) {
            try {
                int[] newPos = new int[] {currentPos[0] + currentDirection[0], currentPos[1] + currentDirection[1]};
                if (a[newPos[0]][newPos[1]] == '.') {
                    currentPos = newPos;
                    a[newPos[0]][newPos[1]] = 'X';
                    counter++;
                } else if (a[newPos[0]][newPos[1]] == 'X') {
                    currentPos = newPos;
                } else {
                    if (Arrays.equals(currentDirection, new int[] {-1,0})) {
                        currentDirection = new int[] {0,1};
                    } else if (Arrays.equals(currentDirection, new int[] {0,1})) {
                        currentDirection = new int[] {1,0};
                    } else if (Arrays.equals(currentDirection, new int[] {1,0})) {
                        currentDirection = new int[] {0,-1};
                    } else {
                        currentDirection = new int[] {-1,0};
                    }
                }
            } catch (Exception e) {
                break;
            }
        }
    }

    public static void solution2(Scanner s) {
        char[][] a = new char[130][];
        int c = 0;
        int[] start = {};
        while (s.hasNextLine()) {
            a[c] = s.nextLine().toCharArray(); 
            for (int i = 0; i < a[c].length; i++) {
                if (a[c][i] == '^') {
                    start = new int[] {c,i};
                    a[c][i] = '.';
                }
            }
            c++;
        }
        for (int[] path : findAllPaths(start, a)) {
            a[path[0]][path[1]] = '#';
            if (checkLoop(start, a)) {
                counter++;
            }
            a[path[0]][path[1]] = '.';
        }
    }
    public static ArrayList<int[]> findAllPaths(int[] start, char[][] arr) {
        ArrayList<int[]> paths = new ArrayList<int[]>();
        char[][] a = new char[arr.length][arr[0].length];
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                a[i][j] = arr[i][j];
            }
        }
        int[] currentPos = start;
        int[] currentDirection = {-1, 0};
        while (true) {
            try {
                int[] newPos = new int[] {currentPos[0] + currentDirection[0], currentPos[1] + currentDirection[1]};
                if (a[newPos[0]][newPos[1]] == '.') {
                    currentPos = newPos;
                    a[newPos[0]][newPos[1]] = 'X';
                    paths.add(currentPos);
                } else if (a[newPos[0]][newPos[1]] == 'X') {
                    currentPos = newPos;
                } else {
                    if (Arrays.equals(currentDirection, new int[] {-1,0})) {
                        currentDirection = new int[] {0,1};
                    } else if (Arrays.equals(currentDirection, new int[] {0,1})) {
                        currentDirection = new int[] {1,0};
                    } else if (Arrays.equals(currentDirection, new int[] {1,0})) {
                        currentDirection = new int[] {0,-1};
                    } else {
                        currentDirection = new int[] {-1,0};
                    }
                }
            } catch (Exception e) {
                return paths;
            }
        }
    }

    
    public static boolean checkLoop(int[] start, char[][] arr) {
        ArrayList<int[]> founds = new ArrayList<int[]>();
        char[][] b = new char[arr.length][arr[0].length];
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                b[i][j] = arr[i][j];
            }
        }
        int[] currentDirection = {-1,0};
        int[] currentPos = start;
        while (true) {
            try {
                int[] newPos = new int[] { currentPos[0] + currentDirection[0], currentPos[1] + currentDirection[1] };
                if (b[newPos[0]][newPos[1]] == '.') {
                    currentPos = newPos;
                } else {
                    currentDirection = turnRight(currentDirection);
                    int index = indexWithin(founds, newPos);
                    if (index != -1) {
                        founds.get(index)[2]++;
                        if (founds.get(index)[2] >= 4) {
                            return true;
                        }
                    } else {
                        founds.add(new int[] { newPos[0], newPos[1], 0 });
                    }
                }
            } catch (Exception e) {
                return false;
            }
        }
    }

    public static int[] turnRight(int[] currentDirection) {
        if (Arrays.equals(currentDirection, new int[] { -1, 0 })) {
            currentDirection = new int[] { 0, 1 };
        } else if (Arrays.equals(currentDirection, new int[] { 0, 1 })) {
            currentDirection = new int[] { 1, 0 };
        } else if (Arrays.equals(currentDirection, new int[] { 1, 0 })) {
            currentDirection = new int[] { 0, -1 };
        } else {
            currentDirection = new int[] { -1, 0 };
        }
        return currentDirection;
    }

    public static int indexWithin(ArrayList<int[]> arr, int[] toFind) {
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i)[0] == toFind[0] && arr.get(i)[1] == toFind[1]) {
                return i;
            }
        }
        return -1;
    }
}