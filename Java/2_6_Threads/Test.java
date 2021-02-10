import java.util.*;

public class Test  {
    public static void main(String[] args) throws InterruptedException {
        HashMap<Integer, Double> table = new HashMap<>();
        ArithmeticSum a = new ArithmeticSum();
        int n = 15;
        long N = 8000000000L;
        int minThreads = 2;
        int maxThreads = 512;
        System.out.println("Result by formula: " + a.formulaSum(n, N));
        long t1 = System.nanoTime();
        long res = a.loopSum(n, N);
        double elapsed = (System.nanoTime() - t1) / (double) 1_000_000_000;
        System.out.println("1 thread for loop: " + elapsed);
        System.out.println(res);
        table.put(1, elapsed);
        for (int i = minThreads; i <= maxThreads; i*=2) {
            t1 = System.nanoTime();
            res = a.threadSum(n, N, i);
            elapsed = (System.nanoTime() - t1) / (double) 1_000_000_000;
            System.out.println(i + " thread for loop: " + elapsed);
            System.out.println(res);
            table.put(i, elapsed);
        }
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
