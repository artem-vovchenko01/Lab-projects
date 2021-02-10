import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdIn;

public class Permutation {

    public static void main(String[] args) {
        RandomizedQueue<String> q = new RandomizedQueue<>();
        int k = Integer.parseInt(args[0]);
        for (int i = 0; i < k; i++) {
            q.enqueue(StdIn.readString());
        }
    for (int i = 0; i < k; i++) {
            if (q.isEmpty()) {
                break;
            }
            System.out.println(q.dequeue());
        }
    }
}