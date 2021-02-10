public class Tester {
    public static void main(String[] args) {
        ArrayQueue<Integer> list = new ArrayQueue<>();
        int size = 10;
        System.out.println("Enqueuing: ");
        for (int i = 0; i < size; i++) {
            list.enqueue(i);
            System.out.println(list);
        }
        System.out.println("ForEach: ");
        for (int i : list) {
            System.out.println(i);
        }
        System.out.println("Dequeuing: ");
        while (! list.isEmpty()) {
            System.out.println(list.dequeue());
            System.out.println(list);
        }
    }
}
