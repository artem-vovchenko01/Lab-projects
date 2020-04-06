import java.util.Iterator;

public class Tester {
    public static void main(String[] args) {
        LinkedListStack<Integer> s = new LinkedListStack<>();
        for (int i = 0; i < 100; i++) {
            s.push(i);
            System.out.println(s);
        }
        for (int i : s) {
            System.out.println(i);
        }
        while (!s.isEmpty()) {
            s.pop();
            System.out.println(s);
        }
    }
}
