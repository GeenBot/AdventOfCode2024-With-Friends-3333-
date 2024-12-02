import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class AOC1 {
    public static void main(String args[]) throws FileNotFoundException {
        File f = new File("AOC1.text");
        Scanner s = new Scanner(f);

        List<Integer> q1 = new ArrayList<>();
        List<Integer> q2 = new ArrayList<>();

        while (s.hasNextLine()) {
            String[] str = s.nextLine().split("   ");
            q1.add(Integer.parseInt(str[0]));
            q2.add(Integer.parseInt(str[1]));
        }

        int[] q1Array = q1.stream().mapToInt(i -> i).toArray();
        int[] q2Array = q2.stream().mapToInt(i -> i).toArray();

        Arrays.parallelSort(q1Array);
        Arrays.parallelSort(q2Array);

        q1.clear();
        q2.clear();
        for (int i : q1Array) q1.add(i);
        for (int i : q2Array) q2.add(i);

        int count = 0;
        for (int i = 0; i < q1.size(); i++) {
            count += Math.abs(q1.get(i) - q2.get(i));
        }
        System.out.println(count);

        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : q2) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        int count2 = 0;
        for (int num : q1) {
            int occurrences = freqMap.getOrDefault(num, 0);
            count2 += occurrences * num;
        }
        System.out.println(count2);

        s.close();
    }
}
