import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {
    private final double[] factors;
    private final int n;
    private final int t;
    // perform independent trials on an n-by-n grid
    public PercolationStats(int n, int trials) {
        if (n <= 0 || trials <= 0) {
            throw new IllegalArgumentException("N / trials not fit to allowed range");
        }
        this.n = n;
        this.t = trials;
        factors = new double[trials];
        Percolation p;
        for (int i = 0; i < trials; i++) {
            p = new Percolation(n);
            fillTable(p);
            factors[i] = (double) p.numberOfOpenSites() / (n*n);
        }
    }

    private void fillTable(Percolation p) {
        int row; int col;
        while (!p.percolates()) {
             row = StdRandom.uniform(1, n + 1);
             col = StdRandom.uniform(1, n + 1);
            p.open(row, col);
        }
    }

    // sample mean of percolation threshold
    public double mean() {
        return StdStats.mean(factors);
    }

    // sample standard deviation of percolation threshold
    public double stddev() {
        return StdStats.stddev(factors);
    }

    // low endpoint of 95% confidence interval
    public double confidenceLo() {
        return mean() - 1.96 * (stddev() / Math.sqrt(t));
    }

    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        return mean() + 1.96 * (stddev() / Math.sqrt(t));
    }

    // test client (see below)
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int t = Integer.parseInt(args[1]);
        PercolationStats ps = new PercolationStats(n, t);
        StdOut.println("mean = " + ps.mean());
        StdOut.println("stddev = " + ps.stddev());
        StdOut.println("95% confidence interval = [ " + ps.confidenceLo() + ", " + ps.confidenceHi() + " ]");
    }
}