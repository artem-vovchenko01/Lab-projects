import edu.princeton.cs.algs4.MinPQ;
import edu.princeton.cs.algs4.Stack;

public class Solver {
    private Node solution = null;
    private boolean unsovlable = false;

    private static class Node implements Comparable<Node> {
        private int manhattan;
        private int moves;
        private Board board;
        private Node prev;
        Node(Board board, Node prev, int manhattan, int moves) {
            this.board = board;
            this.manhattan = manhattan;
            this.moves = moves;
            this.prev = prev;
        }
        int priority() {
            return moves + manhattan;
        }
        public int compareTo(Node node) {
            return Integer.compare(this.priority(), node.priority());
        }
    }

    // find a solution to the initial board (using the A* algorithm)
    public Solver(Board initial) {
        if (initial == null) throw new IllegalArgumentException();
        MinPQ<Node> pq = new MinPQ<>();
        MinPQ<Node> otherPq = new MinPQ<>();
        pq.insert(new Node(initial, null, initial.manhattan(), 0));
        Board twin = initial.twin();
        otherPq.insert(new Node(twin, null, twin.manhattan(), 0));

        while (true) {
            if (!pq.isEmpty()) {
                Node curNode = pq.delMin();
                if (curNode.manhattan == 0) {
                    this.solution = curNode;
                    break;
                }
                Board curBoard = curNode.board;
                for (Board child : curBoard.neighbors()) {
                    if (curNode.prev == null || !curNode.prev.board.equals(child)) {
                        pq.insert(new Node(child, curNode, child.manhattan(), curNode.moves + 1));
                    }
                }
            }

            if (!otherPq.isEmpty()) {
                Node curNodeTwin = otherPq.delMin();
                if (curNodeTwin.manhattan == 0) {
                    this.unsovlable = true;
                    break;
                }
                Board curBoardTwin = curNodeTwin.board;
                for (Board child : curBoardTwin.neighbors()) {
                    if (curNodeTwin.prev == null || !curNodeTwin.prev.board.equals(child)) {
                        otherPq.insert(new Node(child, curNodeTwin, child.manhattan(),
                                                curNodeTwin.moves + 1));
                    }
                }
            }
        }
    }

    // is the initial board solvable? (see below)
    public boolean isSolvable() {
        return !unsovlable;
    }

    // min number of moves to solve initial board
    public int moves() {
        return solution == null ? -1 : solution.moves;
    }

    // sequence of boards in a shortest solution
    public Iterable<Board> solution() {
        if (solution == null) {
            return null;
        }
        Stack<Board> q = new Stack<>();
        Node cur = solution;
        do {
            q.push(cur.board);
            cur = cur.prev;
        } while (cur != null);
        return q;
    }

    // test client (see below)
    public static void main(String[] args) {

    }

}