import java.util.ArrayList;
import java.util.Random;
import java.util.stream.Stream;

public class Test {
    public static void main(String[] args) {
        BSTTable<Integer, String> table = new BSTTable<>();
        table.put(10, "s1");
        table.put(20, "s2");
        System.out.println(table.rank(20));
        System.out.println(table.rank(10));
        table.deleteMin();
        System.out.println(table);
        table.deleteMax();
        System.out.println(table);
        System.out.println(table.size());
        ArrayList<Integer> list = new ArrayList<>();
        Random r = new Random();
        int times = 5;
        Stream.iterate(0, i -> i + 1).limit(times).forEach(list::add);

        for (int i = 0; i < list.size(); i++) {
            int idx = r.nextInt(i + 1);
            int temp = list.get(i);
            list.set(i, list.get(idx));
            list.set(idx, temp);
        }
        System.out.println("Start putting pairs with random keys ...");
        long t1 = System.nanoTime();
        for (int key : list) table.put(key, String.valueOf(System.nanoTime()));
        long t2 = System.nanoTime();
        System.out.println("Time for putting: " + (t2 - t1) /(double) 1_000_000_000);

        System.out.println("Deleting floors until empty");
        System.out.println(table);
        while (! table.isEmpty()) {
            Integer integer = r.nextInt(times + 1);
            Integer floor = table.floor(integer);
            if (floor == null) continue;
            System.out.println("Flor for " + integer + " is " + floor);
            table.delete(floor);
            System.out.println("Floor deleted");
            System.out.println(table);
            System.out.println("Table size: " + table.size());
        }

        System.out.println("Testing floor, ceiling, delete");
       int tests = 1;
        for (int i = 0; i < tests; i++) {
            System.out.println("---------- TEST " + (i+1) + "-----------");
            if (table.size() != 0) throw new IllegalArgumentException();
            for (int j = 0; j < times; j++) {
                table.put(r.nextInt(100), String.valueOf(System.nanoTime()));
            }
            System.out.println(table);
            System.out.println("Table size: " + table.size());
            while (! table.isEmpty()) {
                int num = r.nextInt(100);
                Integer ceil = table.ceiling(num);
                System.out.println("Num " + num + " ceil "  + ceil);
                if (ceil == null) {
                    continue;
                }
                table.delete(ceil);
                System.out.println(table.keys());
                System.out.println(table);
                System.out.println("Table size: " + table.size());
            }
        }

        System.out.println();

        System.out.println(table);
    }
}
