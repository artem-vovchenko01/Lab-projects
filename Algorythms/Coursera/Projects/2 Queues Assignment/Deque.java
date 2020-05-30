import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {
    private int size;
    private Node head;
    private Node tail;
    private class Node {
        Node next;
        Node prev;
        Item val;
        Node (Item val) {
            this.val = val;
        }
    }

    // construct an empty deque
    public Deque() {}

    // is the deque empty?
    public boolean isEmpty() {
        return size == 0;
    }

    // return the number of items on the deque
    public int size() {
        return size;
    }

    // add the item to the front
    public void addFirst(Item item) {
        if (item == null) {
            throw new IllegalArgumentException();
        }
        Node newNode = new Node(item);
        if (head == null) {
            head = tail = newNode;
            size++;
            return;
        }
        head.prev = newNode;
        newNode.next = head;
        head = newNode;
        size++;
    }

    // add the item to the back
    public void addLast(Item item) {
        if (item == null) {
            throw new IllegalArgumentException();
        }
        Node newNode = new Node(item);
        if (tail == null) {
            head = tail = newNode;
            size++;
            return;
        }
        tail.next = newNode;
        newNode.prev = tail;
        tail = newNode;
        size++;
    }

    // remove and return the item from the front
    public Item removeFirst() {
        if (head == null) {
            throw new NoSuchElementException();
        }
        Item val = head.val;
        head = head.next;
        if (head == null) {
            tail = null;
        } else {
            head.prev = null;
        }
        size--;
        return val;
    }

    // remove and return the item from the back
    public Item removeLast() {
        if (tail == null) {
            throw new NoSuchElementException();
        }
        Item val = tail.val;
        tail = tail.prev;
        if (tail != null) {
            tail.next = null;
        } else {
            head = null;
        }
        size--;
        return val;
    }

    @Override
    public String toString() {
        if (size == 0) {
            return "[]";
        }
        StringBuilder s = new StringBuilder("[");
        Node temp = head;
        while (temp != null) {
            s.append(temp.val).append(", ");
            temp = temp.next;
        }
        return s.toString() + "\b\b]";
    }

    // return an iterator over items in order from front to back
    public Iterator<Item> iterator() {return new Iterator<Item>() {
        Node current = head;
        @Override
        public boolean hasNext() {
            return current != null;
        }

        @Override
        public Item next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            Item val = current.val;
            current = current.next;
            return val;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }
    };}

    // unit testing (required)
    public static void main(String[] args) {
        Deque<Integer> deq = new Deque<>();
        System.out.println("SZ: " + deq.size());
        System.out.println("ADD_LAST");
        for (int i = 0; i < 10; i++) {
            deq.addLast(i);
            System.out.println(deq);
            System.out.println("SZ: " + deq.size());
        }
        System.out.println("FOREACH");
        for (int i : deq) {
            System.out.println(i);
        }
        System.out.println("REMOVE_LAST");
        while (!deq.isEmpty()) {
            System.out.println(deq.removeLast());
            System.out.println(deq);
            System.out.println("SZ: " + deq.size());
        }
        System.out.println("SZ: " + deq.size());
        System.out.println("ADD_FIRST");
        for (int i = 10; i < 20; i++) {
            deq.addFirst(i);
            System.out.println(deq);
            System.out.println("SZ: " + deq.size());
        }
        System.out.println("REMOVE_FIRST");
        while (!deq.isEmpty()) {
            System.out.println(deq.removeFirst());
            System.out.println(deq);
            System.out.println("SZ: " + deq.size());
        }
    }

}