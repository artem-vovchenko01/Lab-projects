import java.util.*;

public class Tester  {
    public static void main(String[] args) throws InterruptedException {
        // Test for 1 thread, print rarest words
        ConcurrentTextAnalyzer an = new ConcurrentTextAnalyzer(1);
        ArrayList<String> lst = an.rarestWords();
        for (String word : lst) {
            System.out.println(word);
        }

        HashMap<Integer, Double> table = new HashMap<>();
        int minThreads = 1;
        int maxThreads = 32;
        double t1;
        double elapsed;
        // Testing different thread configuration, from 1 to 128 threads
        for (int i = minThreads; i <= maxThreads; i*=2) {
            t1 = System.nanoTime();
            ConcurrentTextAnalyzer analyzer = new ConcurrentTextAnalyzer(i);
            analyzer.rarestWords();
            elapsed = (System.nanoTime() - t1) / (double) 1_000_000_000;
            System.out.println(i + " threads: " + elapsed);
            table.put(i, elapsed);
        }
        // Neatly printing data
        TreeSet<Double> times = new TreeSet<>();
        for (Double t : table.values()) {
            times.add(t);
        }
        ArrayList<Integer> cores = new ArrayList<>();
        for (Double time : times) {
            for (Map.Entry<Integer, Double> entry : table.entrySet()) {
                if (time == entry.getValue()) {
                    cores.add(entry.getKey());
                    break;
                }
            }
        }
        for (Integer core : cores) {
            System.out.println("Time for " + core + " threads: " + table.get(core));
        }
    }
}