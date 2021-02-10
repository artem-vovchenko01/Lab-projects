import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class UI {
    public static void main(String[] args) {
        startUI();
    }

    static void startUI () {
        WeightedFlattenUF uf = new WeightedFlattenUF(10);
        Scanner sc = new Scanner(System.in);
        System.out.println(uf);
        System.out.println(uf.getRawRepr());
        while (sc.hasNextInt()) {
            uf.union(sc.nextInt(), sc.nextInt());
            System.out.println(uf);
            System.out.println(uf.getRawRepr());
            System.out.println(uf.findMaxInComponent(1));
        }
        sc = new Scanner(System.in);
        System.out.println("Test connect");
        while (sc.hasNextInt()) {
            System.out.println(uf.isConnected(sc.nextInt(), sc.nextInt()));
            System.out.println(uf);
            System.out.println(uf.getRawRepr());
        }
    }

    static void randomized (boolean show) {
        Random r = new Random();
        int size = 10_000;
        int operations = 100;
        ArrayList<Integer> randoms = new ArrayList<>();
        for (int i=0; i < operations * 2; i++) {
            randoms.add(r.nextInt(size - 1));
        }
        UF qFind = new SlowUF(size);
        UF qUnion = new QuickUF(size);
        UF weight = new WeightedUF(size);
        UF flat = new WeightedFlattenUF(size);

        long t1 = System.nanoTime();
        for (int j=0; j < randoms.size(); j += 2) {
            if (show) {
                System.out.println("Quick Find");
            }
            int low = randoms.get(j);
            int high = randoms.get(j + 1);
            qFind.union(low, high);
            if (show) {
                System.out.println(qFind);
                System.out.println(qFind.isConnected(low, high));
            }
        }
        long t2 = System.nanoTime();
        System.out.println("Elapsed: " + (t2 - t1) / (double)1_000_000_000);
        t2 = System.nanoTime();

                for (int j=0; j < randoms.size(); j += 2) {
                    if (show) {
                        System.out.println("Quick Union");
                    }
            int low = randoms.get(j);
            int high = randoms.get(j + 1);
            qUnion.union(low, high);
            if (show) {
                System.out.println(qUnion);
                System.out.println(qUnion.isConnected(low, high));
            }
        }
                long t3 = System.nanoTime();
        System.out.println("Elapsed: " + (t3 - t2) / (double)1_000_000_000);
        t3 = System.nanoTime();

                for (int j=0; j < randoms.size(); j += 2) {
                    if (show) {
                        System.out.println("Weighted Union");
                    }
            int low = randoms.get(j);
            int high = randoms.get(j + 1);
            weight.union(low, high);
                    if (show) {
                        System.out.println(weight);
                        System.out.println(weight.isConnected(low, high));
                    }
        }
        long t4 = System.nanoTime();
        System.out.println("Elapsed: " + (t4 - t3) / (double)1_000_000_000);
        t4  = System.nanoTime();

                for (int j=0; j < randoms.size(); j += 2) {
                    if (show) {
                        System.out.println("Flatten Weighted Union");
                    }
            int low = randoms.get(j);
            int high = randoms.get(j + 1);
            flat.union(low, high);
                    if (show) {
                        System.out.println(flat);
                        System.out.println(flat.isConnected(low, high));
                    }
        }

        long t5 = System.nanoTime();

        System.out.println("All time: " + (t5 - t1) / (double)1_000_000_000);
    }

}