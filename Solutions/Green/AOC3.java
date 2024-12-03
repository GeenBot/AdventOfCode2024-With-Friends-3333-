import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;

public class AOC3 { 
    public static void main (String[] args) throws IOException {
        boolean isProblem2 = true;
        byte[] bytes = Files.readAllBytes(Paths.get("AOC3.txt"));
        String content = new String(bytes, "UTF-8");
        String[] strings = content.split("mul\\(");
        boolean currentlyDo = true;
        ArrayList<String> order = new ArrayList<String>();
        for (int i = 0; i < strings.length; i++) {
            if (currentlyDo) {
                order.add(strings[i]);
            }
            String[] temps = strings[i].split("do");
            if (temps.length > 1) {
                try {
                if (temps[temps.length - 1].substring(0, 5).equals("n't()")) {
                    currentlyDo = false;
                } else {
                    currentlyDo = true;
                } }
                catch (Exception e) {
                    currentlyDo = true;
                }
            }
        }
        if (isProblem2) {
            strings = order.toArray(new String[order.size()]);
        }
        int count = 0;
        for (int i = 1; i < strings.length; i++) {
            String cur = strings[i];
            String[] c = cur.split("\\)");
            cur = c[0];
            try {
                String[] nums = cur.split(",");
                try {
                    nums[2] = "";
                    
                } catch (Exception e) {
                    int[] ints = new int[2];
                    ints[0] = Integer.parseInt(nums[0]);
                    ints[1] = Integer.parseInt(nums[1]);
                    count += ints[0] * ints[1];
                }

            } catch (Exception e) {
                System.out.println("AAAAAAAAA");
            }

        }
        System.out.println(count);
    }
}
