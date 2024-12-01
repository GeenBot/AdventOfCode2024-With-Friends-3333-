import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class AOC1 {
    /*
    public static void main(String args[]) throws FileNotFoundException {
        File f = new File("AOC1.text");
        Scanner s = new Scanner(f);

        Queue<Integer> q1 = new LinkedList<Integer>();
        Queue<Integer> q2 = new LinkedList<Integer>();
        while (s.hasNextLine()) {
            String[] str = s.nextLine().split("   ");
            q1.add(Integer.parseInt(str[0]));
            q2.add(Integer.parseInt(str[1]));
        }
        q1 = SortQueue(q1);
        q2 = SortQueue(q2);
        int count = 0;
        while (!q1.isEmpty()) {
            int num = q1.remove() - q2.remove();
            num = Math.abs(num);
            count += num;
        }
        System.out.println(count);
    }
        */
        public static void main(String args[]) throws FileNotFoundException {
            File f = new File("AOC1.text");
            Scanner s = new Scanner(f);

            Queue<Integer> q1 = new LinkedList<Integer>();
            Queue<Integer> q2 = new LinkedList<Integer>();
            while (s.hasNextLine()) {
                String[] str = s.nextLine().split("   ");
                q1.add(Integer.parseInt(str[0]));
                q2.add(Integer.parseInt(str[1]));
            }
            q1 = SortQueue(q1);
            q2 = SortQueue(q2);
            int count = 0;
            while (!q1.isEmpty()) {
                Queue<Integer> tempQueue = new LinkedList<Integer>();
                tempQueue.addAll(q2);
                int num = q1.remove();
                int occurances = 0;
                while(!tempQueue.isEmpty()) {
                    if (tempQueue.peek() == num) {
                        occurances++;
                    } else if (tempQueue.peek() > num) {
                        break;
                    }
                    tempQueue.remove();
                }
                count += occurances * num;
                while (!q1.isEmpty()) {
                    if (q1.peek() == num) {
                        count += occurances * num;
                        q1.remove();
                    } else {
                        break;
                    }
                }
                q2 = tempQueue;
            }
            System.out.println(count);
            s.close();
        }


    public static Queue<Integer> SortQueue(Queue<Integer> q) {
        ArrayList<Integer> tempList = new ArrayList<Integer>();
        while (!q.isEmpty()) {
            boolean isAdded = false;
            for (int i = 0; i < tempList.size(); i++) {
                if (q.peek() < tempList.get(i)) {
                    tempList.add(i, q.remove());
                    isAdded = true;
                    break;
                }
            }
            if (!isAdded) {
                tempList.add(q.remove());
            }
        }
        for (int i = 0; i < tempList.size(); i++) {
            q.add(tempList.get(i));
        }
        return q;
    }
}
