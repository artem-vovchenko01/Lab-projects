import java.util.Iterator;

public class LinkedListQueue<T> implements Queue<T>, Iterable<T> {
    private Node<T> head;
    private Node<T> tail;
    private int size;
    private class LinkedListQueueIterator implements Iterator<T> {
        Node<T> current;
        LinkedListQueueIterator() {
            current = head;
        }
        @Override
        public boolean hasNext() {
            return current != null;
        }

        @Override
        public T next() {
            T val = current.val;
            current = current.next;
            return val;
        }
    }
    private static class Node<T> {
        Node<T> next;
        T val;
        Node (T val) {
            this.val = val;
            next = null;
        }
    }
    public LinkedListQueue() {
        head = null;
        tail = null;
    }

    @Override
    public void enqueue(T val) {
        Node<T> node = new Node<T>(val);
        if (tail == null) {
            head = node;
            tail = head;
        } else {
            tail.next = node;
            tail = tail.next;
        }
        size++;
    }

    @Override
    public T dequeue() {
        T val = null;
        if (head != null) {
            val = head.val;
            head = head.next;
            size--;
            if (head == null) {
                tail = null;
            }
        }
        return val;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public String toString() {
        if (head == null) {
            return "[]";
        }
        StringBuilder s = new StringBuilder("[");
        Node<T> temp = head;
        while (temp != null) {
            s.append(temp.val).append(", ");
            temp = temp.next;
        }
        return s.toString() + "\b\b]";
    }

    @Override
    public Iterator<T> iterator() {
        return new LinkedListQueueIterator();
    }
}
