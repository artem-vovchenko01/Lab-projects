import java.util.ArrayList;

public class ArithmeticSum {
    public long formulaSum (int n, long N) {
        return ((n + n * N) * N) / 2;
    }

    public long loopSum (int n, long N) {
        long sum = 0;
        for (long k = 1; k <= N; k++) {
            sum += k * n;
        }
        return sum;
    }

    public long threadSum(int n, long N, int threads) throws InterruptedException {
        ArrayList<Long> sums = new ArrayList<>();
        ArrayList<Thread> threadPool = new ArrayList<>();
        long step = N / threads;
        long last = 0;
        for (long k = 1; k + step < N; k += step) {
            last = k;
            threadPool.add(new Thread(new Summator(k, step, n, sums)));
        }

        for (Thread thread : threadPool) {
            thread.start();
        }
        for (Thread thread : threadPool) {
            thread.join();
        }
        long sum = 0;
        for (long value : sums) {
            sum += value;
        }
        for (long k = last + step; k <= N; k++) {
            sum += k * n;
        }
        return sum;
    }
}

class Summator implements Runnable {
    long start;
    long step;
    int n;
    ArrayList<Long> list;
    public Summator (long start, long step, int n, ArrayList<Long> sums) {
        this.start = start;
        this.step = step;
        this.n = n;
        this.list = sums;
    }
    @Override
    public void run () {
        long sum = 0;
        long end = start + step;
        for (long k = start; k < end; k++) {
            sum += k * n;
        }
        synchronized (list) {
            list.add(sum);
        }
    }
}
