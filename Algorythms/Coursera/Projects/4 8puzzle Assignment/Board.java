import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.Queue;
import edu.princeton.cs.algs4.StdOut;

import java.util.Arrays;

public class Board {
    private int N;
    private int[][] board;
    // create a board from an n-by-n array of tiles,
    // where tiles[row][col] = tile at (row, col)
    public Board(int[][] tiles) {
        N = tiles.length;
        int[][] board = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                    board[i][j] = tiles[i][j];
                }
            }
        this.board = board;
    }

    // string representation of this board
    public String toString() {
        StringBuilder str = new StringBuilder();
        str.append(N + "\n");
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                str.append(board[i][j] + " ");
            }
            str.append("\n");
        }
        return str.toString();
    }

    // board dimension n
    public int dimension() {
        return N;
    }

    // number of tiles out of place
    public int hamming() {
        int wrongPos = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (i == N - 1 && j == N - 1) break;
                if (board[i][j] != (j + 1) + (i * N)) {
                    wrongPos++;
                }
            }
        }
        return wrongPos;
    }

    // sum of Manhattan distances between tiles and goal
    public int manhattan() {
        int dif = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int cur = board[i][j];
                if (cur == 0) continue;
                int row = cur / N;
                int col = cur % N - 1;
                if (col == -1) {
                    row--;
                    col = N - 1;
                }
                int newDif = Math.abs(row - i) + Math.abs(col - j);
                dif += newDif;
            }
        }
        return dif;
    }

    // is this board the goal board?
    public boolean isGoal() {
       return hamming() == 0;
    }

    // does this board equal y?
    public boolean equals(Object y) {
        if (y == this) return true;
        if (y == null) return false;
        if (y.getClass() != this.getClass()) return false;
        Board that = (Board) y;
        if (this.dimension() != that.dimension()) return false;
        return Arrays.deepEquals(this.board, that.board);
    }

    // all neighboring boards
    public Iterable<Board> neighbors() {
        Queue<Board> q = new Queue<>();
        int zeroRow = 0;
        int zeroCol = 0;
        outer: for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 0) {
                    zeroRow = i;
                    zeroCol = j;
                    break outer;
                }
            }
        }
        // right
        if (zeroCol != N - 1) {
            int newBoard[][] = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    newBoard[i][j] = board[i][j];
                }
            }
            exch(newBoard, zeroRow, zeroCol, zeroRow, zeroCol + 1);
            q.enqueue(new Board(newBoard));
        }
        // bottom
        if (zeroRow != N - 1) {
            int newBoard[][] = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    newBoard[i][j] = board[i][j];
                }
            }
            exch(newBoard, zeroRow, zeroCol, zeroRow + 1, zeroCol);
            q.enqueue(new Board(newBoard));
        }
        // left
        if (zeroCol != 0) {
            int newBoard[][] = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    newBoard[i][j] = board[i][j];
                }
            }
            exch(newBoard, zeroRow, zeroCol, zeroRow, zeroCol - 1);
            q.enqueue(new Board(newBoard));
        }
        // top
        if (zeroRow != 0) {
            int newBoard[][] = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    newBoard[i][j] = board[i][j];
                }
            }
            exch(newBoard, zeroRow, zeroCol, zeroRow - 1, zeroCol);
            q.enqueue(new Board(newBoard));
        }
        return q;
    }

    private void exch(int[][] newBoard, int row1, int col1, int row2, int col2) {
        int temp = newBoard[row1][col1];
        newBoard[row1][col1] = newBoard[row2][col2];
        newBoard[row2][col2] = temp;
    }

    // a board that is obtained by exchanging any pair of tiles
    public Board twin() {
        int newBoard[][] = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                newBoard[i][j] = board[i][j];
            }
        }
        if (board[0][0] != 0 && board[0][1] != 0) {
            exch(newBoard, 0, 0, 0, 1);
        } else {
            exch(newBoard, 1, 0, 1, 1);
        }
        return new Board(newBoard);
    }

    // unit testing (not graded)
        public static void main(String[] args) {
            // create initial board from file
            In in = new In(args[0]);
            int n = in.readInt();
            int[][] tiles = new int[n][n];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    tiles[i][j] = in.readInt();
            Board initial = new Board(tiles);

            // solve the puzzle
            Solver solver = new Solver(initial);

            // print solution to standard output
            if (!solver.isSolvable())
                StdOut.println("No solution possible");
            else {
                StdOut.println("Minimum number of moves = " + solver.moves());
                for (Board board : solver.solution())
                    StdOut.println(board);
            }
        }
}
