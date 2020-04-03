import edu.princeton.cs.algs4.WeightedQuickUnionUF;
public class Percolation {
    private static class LList {
        Node head;
        LList () {
            head = null;
        }

        void add (int val) {
            if (head == null) {
                head = new Node(val);
            } else {
                Node temp = head;
                while (temp.next != null) {
                    temp = temp.next;
                }
                temp.next = new Node(val);
            }
        }

        int pop () {
            int result = 0;
            Node temp = head;
            if (temp.next == null) {
                result = head.val;
                head = null;
                return result;
            }
            while (temp.next.next != null) {
                temp = temp.next;
            }
            result = temp.next.val;
            temp.next = null;
            return result;
        }
    }
    private static class Node {
        int val;
        Node next;
        Node (int val) {
            this.next = null;
            this.val = val;
        }
    }
    private final int n;
    private int openCount;
    private final WeightedQuickUnionUF wuf;
    private final boolean[][] grid;

    // creates n-by-n grid, with all sites initially blocked
    public Percolation(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException("N outside of allowed range");
        }
        this.n = n;
        this.wuf = new WeightedQuickUnionUF(n * n + 2);
        this.grid = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = false;
            }
        }
    }

    private void connectToTop(int pos) {
        wuf.union(pos, n*n);
    }

    private void connectToBottom(int pos) {
        wuf.union(pos, n*n + 1);
    }

    // opens the site (row, col) if it is not open already
    public void open(int row, int col) {
        if (row < 1 || row > n || col < 1 || col > n) {
            throw new IllegalArgumentException("Row / col outside of allowed range");
        }

        int pos = (row - 1) * n + col -1;
        if (!isOpen(row, col)) {
            grid[--row][--col] = true;
            openCount ++;
        } else {
            return;
        }
        if (row == 0) {
            connectToTop(pos);
        }
        if (row == n - 1) {
            connectToBottom(pos);
        }
        if (row > 0 && grid[row - 1][col]) { // check up
            wuf.union(pos, pos - n);
        }
        if (row < (n-1) && grid[row + 1][col]) { // check bottom
            wuf.union(pos, pos + n);
        }
        if (col > 0 && grid[row][col - 1]) { // check left
            wuf.union(pos, pos - 1);
        }
        if (col < (n-1) && grid[row][col + 1 ]) { // check right
            wuf.union(pos, pos + 1);
        }
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        if (row < 1 || row > n || col < 1 || col > n) {
            throw new IllegalArgumentException("Row / col outside of allowed range");
        }
        return grid[--row][--col];
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        if (row < 1 || row > n || col < 1 || col > n) {
            throw new IllegalArgumentException("Row / col outside of allowed range");
        }
        int pos = (row - 1) * n + col -1;

        if (wuf.find(pos) == wuf.find(n *n)) {
            return true;
        }
        return false;
    }

    // returns the number of open sites
    public int numberOfOpenSites() {
        return openCount;
    }

    // does the system percolate?
    public boolean percolates() {
        return wuf.find(n *n) == wuf.find(n*n + 1);
    }

    //    private void print () {
    //        StdOut.print("  ");
    //        for (int k=1; k<n+1; k++) {
    //            StdOut.print("  " +k + "   ");
    //        }
    //        StdOut.println();
    //        for (int i=0; i<n; i++) {
    //            for (int j=0; j<n; j++) {
    //                if (j == 0) {
    //                    StdOut.print((i+1) + " ");;
    //                }
    //                StdOut.print(grid[i][j] + " ");
    //            }
    //            StdOut.println();
    //        }
    //    }

}