import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class AOC2 {
    
        public static void main(String[] args) throws FileNotFoundException {
            File f = new File("AOC2.text");
            Scanner s = new Scanner(f);
            Long nanoTime = System.nanoTime();
            sr2(s);
            nanoTime = (System.nanoTime() - nanoTime) / 100000;
            System.out.println(nanoTime);
            s.close();
            s = new Scanner(f);
            nanoTime = System.nanoTime();
            s2(s);
            nanoTime = (System.nanoTime() - nanoTime) / 100000;
            System.out.println(nanoTime);
            s.close();
        }
    
        public static void s1(Scanner s) {
            int counter = 0;
            while (s.hasNextLine()) {
                String[] array = s.nextLine().split(" ");
                if (isGood(array)) {
                    counter++;
                }
            }
            System.out.println(counter);
        }
    
        public static void s2(Scanner s) {
            int counter = 0;
            while (s.hasNextLine()) {
                String[] array = s.nextLine().split(" ");
                if (isGoodDampener(array)) {
                    counter++;
                    //System.out.println(1);
                } else {
                    //System.out.println(0);
                }
            }
            System.out.println(counter);
        }
    
        public static void sr2(Scanner s) {
            int counter = 0;
            while (s.hasNextLine()) {
                boolean isAdded = false;
                String[] array = s.nextLine().split(" ");
                if (isGood(array)) {
                    counter++;
                    isAdded = true;
                    //System.out.println(1);
                } else {
                    for (int j = 0; j < array.length; j++) {
                        String[] ar2 = new String[array.length - 1];
                        for (int i = 0; i < array.length; i++) {
                            if (i < j) {
                                ar2[i] = array[i];
                            } else if (i == j) {

                            } else {
                                ar2[i - 1] = array[i];
                            }
                        }
                        if (isGood(ar2)) {
                            counter++;
                            isAdded = true;
                            //System.out.println(1);
                            break;
                        }
                    }

                }
                /*
                if (!isAdded) {
                    System.out.println(0);
                }
                */
            }
            System.out.println(counter);
        }
    
        public static boolean isGood(String[] line) {
            int dir[] = new int[line.length - 1];
            for (int i = 1; i < line.length; i++) {
                dir[i - 1] = Integer.parseInt(line[i]) - Integer.parseInt(line[i - 1]);
            }

            for (int i = 1; i < line.length; i++) {
                if (Math.abs(dir[i - 1]) > 3 || Math.abs(dir[i - 1]) < 1) {
                    return false;
                }
            }
            int direction;
            try {
                direction = dir[0] / Math.abs(dir[0]);
            } catch (Exception e) {
                return false;
            }
            
            for (int i = 1; i < line.length - 1; i++) {
                try {
                    if(!(direction == dir[i] / Math.abs(dir[i]))) {
                        return false;
                    }
                } catch (Exception e) {
                    return false;
                }
            }

            
            return true;
        }

    
    //Works aside from 2 cases but I don't want to finish it if the other one is already working :///////
    public static boolean isGoodDampener(String[] line) {
        boolean isChanged = false;
        int dir[] = new int[line.length - 1];
        int dir2[] = new int[line.length - 2];
        int direction;
        for (int i = 1; i < line.length; i++) {
            dir[i - 1] = Integer.parseInt(line[i]) - Integer.parseInt(line[i - 1]);
        }
        for (int i = 2; i < line.length; i++) {
            dir2[i - 2] = Integer.parseInt(line[i]) - Integer.parseInt(line[i - 2]);
        }
        //Finds out if the direction is positive or negative.
        try {
            if (dir[0] / Math.abs(dir[0]) == dir[1] / Math.abs(dir[1])) {
                direction = dir[1] / Math.abs(dir[1]);
            } else if (dir[2] / Math.abs(dir[2]) == dir[3] / Math.abs(dir[3])) {
                direction = dir[3] / Math.abs(dir[3]);
            } else {
                return false;
            }
        } catch (Exception e) {
            try {
                if (dir[2] / Math.abs(dir[2]) == dir[3] / Math.abs(dir[3])) {
                    direction = dir[3] / Math.abs(dir[3]);
                } else {
                    return false;
                }
            } catch (Exception a) {
                return false;
            }
        }
        int start = 0;
        try {
            if (dir[0] * direction > 3 || dir[0] * direction < 1) {
                if (dir[1] * direction > 3 || dir[1] * direction < 1) {
                    if (dir2[0] * direction > 3 || dir2[0] * direction < 1) {
                        return false;
                    } else {
                        isChanged = true;
                        start += 2;
                    }
                } else {
                    isChanged = true;
                    start++;  
                }


            }
        for (int i = start; i < line.length - 1; i++) {
            int num = dir[i] * direction;
            if (num < 1 || num > 3) {
                if (!isChanged) {
                    num = dir2[i] * direction;
                    if (num < 1 || num > 3) {
                        if (i == line.length - 2) {
                            return true;
                        }
                        return false;
                    } else {
                        isChanged = true;
                        i++;
                    }
                } else {
                    return false;
                }
            }
        }
    } catch (Exception e) {
        return true;
    }

        

        
        return true;
    }
    /*         for (int i = 1; i < line.length; i++) {
            int difference;
            if (!isFixed) {
                difference = priordiff + shiftFactor + (Integer.parseInt(line[i]) - Integer.parseInt(line[i - 1])) * direction;
                isFixed = true;
            } else {
                difference = (Integer.parseInt(line[i]) - Integer.parseInt(line[i - 1])) * direction;
                
            }
            if (difference > 3 || difference < 1) {
                if (!isChanged) {
                    shiftFactor = difference;
                    isChanged = true;
                    isFixed = false;
                } else {
                    return false;
                }
            }
            if (!isFixed) {
                difference = difference -= priordiff;
                if (!(difference > 3 || difference < 1)) {
                    isChanged = true;
                    isFixed = true;
                } else if (i == 1) {
                    priordiff = 256;
                }
                
            }
            if (priordiff != 256) {
                priordiff = difference;
            } else {
                priordiff = difference * -1;
            }
            
        } */
}
