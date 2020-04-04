public class Tester {
    public static void main(String[] args) {
        LinkedListStack<Integer> s = new LinkedListStack<>();
        for (int i = 0; i < 20_000_000; i++) {
            s.push(i);
        }

        while (!s.isEmpty()) {
            s.pop();
        }
    }
}
