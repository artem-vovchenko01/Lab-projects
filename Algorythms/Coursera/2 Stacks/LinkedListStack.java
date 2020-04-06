import java.util.Iterator;

public class LinkedListStack<T> implements Stack<T>, Iterable<T> {
    private Node<T> head;
    private int size;
    private class LinkedListStackIterator implements Iterator<T> {
        Node<T> current;
        LinkedListStackIterator() {
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
            this.next = null;
        }
    }

    public LinkedListStack () {
        this.head = null;
    }

    public boolean isEmpty () {
        return size == 0;
    }

    public void push (T val) {
        Node<T> temp  = head;
        head = new Node<>(val);
        head.next = temp;
        size++;
    }

    public T pop () {
        Node<T> temp = head;
        if (temp == null) {
            return null;
        }
        head = head.next;
        size--;
        return temp.val;
    }

    public int size () {
        return size;
    }

    @Override
    public String toString() {
        StringBuilder str = new StringBuilder("[");
        if (size == 0) {
            return "[]";
        }
        Node<T> temp = head;
        while (temp != null) {
            str.append(temp.val).append(", ");
            temp = temp.next;
        }
        return str.toString() + "\b\b]";
    }

    @Override
    public Iterator<T> iterator() {
        return new LinkedListStackIterator();
    }
}
