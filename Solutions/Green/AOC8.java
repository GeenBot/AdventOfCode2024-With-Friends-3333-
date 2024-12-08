import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Hashtable;
import java.util.Map;
import java.util.Scanner;

public class AOC8 {
    public static int counter;
    public static int width;
    public static int height;
    public static void main(String[] args) throws FileNotFoundException {
        //Get file and convert to scanner.

        File f = new File("AOC8.text");
        
        //Run Solution 1 with time and counter output.
        long n = System.nanoTime();
        counter = 0;
        Scanner s = new Scanner(f);
        solution1(s);
        System.out.println(counter);
        n = System.nanoTime() - n;
        System.out.println(n / 1000000 - 18);

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
        ArrayList<Node[]> a = new ArrayList<Node[]>();
        ArrayList<String> d = new ArrayList<String>();
        ArrayList<int[]> found = new ArrayList<int[]>();
        Map<String, ArrayList<Node>> p = new Hashtable<String, ArrayList<Node>>();
        int it = 0;
       while (s.hasNextLine()) {
        char[] t = s.nextLine().toCharArray();
        Node[] n = new Node[t.length];
        width = t.length;
        for (int i = 0; i < t.length; i++) {
            n[i] = new Node(t[i], new int[] {it, i});
            if (t[i] != '.') {
            if (!p.containsKey(String.valueOf(t[i])) ) {
                ArrayList<Node> real = new ArrayList<Node>();
                real.add(n[i]);
                p.put(String.valueOf(t[i]), real);
                d.add(String.valueOf(t[i]));
            } else {
                ArrayList<Node> real = p.get(String.valueOf(t[i]));
                real.add(n[i]);
                p.put(String.valueOf(t[i]), real);
            }
            }
        }
        a.add(n);
        it++;
        height = it;
       }
       for (int i = 0; i < d.size(); i++) {
            ArrayList<Node> nodes = p.get(d.get(i));
            if (nodes.size() >= 2) {
                for (int j = 0; j < nodes.size(); j++) {
                    for (int k = 0; k < nodes.size(); k++) {
                        int[] POSition = new int[2];
                        int[] NEGition = new int[2];
                        if (j != k) {
                                POSition[0] = 2 * nodes.get(j).pos[0] - nodes.get(k).pos[0];
                                POSition[1] = 2 * nodes.get(j).pos[1] - nodes.get(k).pos[1];
                                NEGition[0] = 2 * nodes.get(k).pos[0] - nodes.get(j).pos[0];
                                NEGition[1] = 2 * nodes.get(k).pos[1] - nodes.get(j).pos[1];

                            

                            try {
                                Node n = a.get(POSition[0])[POSition[1]];
                                if (!containsPos(found, POSition)) {
                                    counter++;
                                    found.add(POSition);
                                } 
                            } catch (Exception e) {

                            }
                            try {
                                Node n = a.get(NEGition[0])[NEGition[1]];
                                if (!containsPos(found, NEGition)) {
                                    counter++;
                                    found.add(NEGition);
                                } 
                            } catch (Exception e) {

                            }

                        }
                    }
                }
            }
       }
    }

    

    public static boolean contains(ArrayList<String> strings, String target) {
        for (int i = 0; i < strings.size(); i++) {
            if (strings.get(i).equals(target)) {
                return true;
            }
        }
        return false;
    }
    public static boolean containsPos(ArrayList<int[]> ints, int[] target) {
        for (int i = 0; i < ints.size(); i++) {
            if (ints.get(i)[0] == target[0] && ints.get(i)[1] == target[1]) {
                return true;
            }
        }
        return false;
    }



    public static void solution2(Scanner s) {
        ArrayList<Node[]> a = new ArrayList<Node[]>();
        ArrayList<String> d = new ArrayList<String>();
        ArrayList<int[]> found = new ArrayList<int[]>();
        Map<String, ArrayList<Node>> p = new Hashtable<String, ArrayList<Node>>();
        int it = 0;
       while (s.hasNextLine()) {
        char[] t = s.nextLine().toCharArray();
        Node[] n = new Node[t.length];
        width = t.length;
        for (int i = 0; i < t.length; i++) {
            n[i] = new Node(t[i], new int[] {it, i});
            if (t[i] != '.') {
            if (!p.containsKey(String.valueOf(t[i])) ) {
                ArrayList<Node> real = new ArrayList<Node>();
                real.add(n[i]);
                p.put(String.valueOf(t[i]), real);
                d.add(String.valueOf(t[i]));
            } else {
                ArrayList<Node> real = p.get(String.valueOf(t[i]));
                real.add(n[i]);
                p.put(String.valueOf(t[i]), real);
            }
            }
        }
        a.add(n);
        it++;
        height = it;
       }
       for (int i = 0; i < d.size(); i++) {
            ArrayList<Node> nodes = p.get(d.get(i));
            if (nodes.size() >= 2) {
                for (int j = 0; j < nodes.size(); j++) {
                    for (int k = 0; k < nodes.size(); k++) {
                        if (j != k) {
                            int r = nodes.get(j).pos[0] - nodes.get(k).pos[0];
                            int count = (nodes.get(j).pos[1] - nodes.get(k).pos[1]);                           
                            int repeats = 0;
                            int dir = 0;
                            if (nodes.get(j).pos[0] > nodes.get(k).pos[0]) {
                                dir = 1;
                            } else {
                                dir = -1;
                            }
                            while (true) {
                                try {
                                    Node n = a.get(nodes.get(j).pos[0] +  r * repeats)[nodes.get(j).pos[1] + count * repeats];
                                    if (!containsPos(found, n.pos)) {
                                        counter++;
                                        found.add(n.pos);
                                    }
                                    repeats++;
                                } catch (Exception e) {
                                    break;
                                }

                            }
                            repeats = 1;
                            while (true) {
                                try {
                                    Node n = a.get(nodes.get(k).pos[0] - r * repeats)[nodes.get(k).pos[1] - count * repeats];
                                    if (!containsPos(found, n.pos)) {
                                        counter++;
                                        found.add(n.pos);
                                    }
                                    repeats++;
                                } catch (Exception e) {
                                    int test = 0;
                                    break;
                                }

                            }
                            



                        }
                    }
                }
            }
       }
    }
}