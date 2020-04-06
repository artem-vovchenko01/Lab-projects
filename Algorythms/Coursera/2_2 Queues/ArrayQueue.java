import java.util.Iterator;

public class ArrayQueue<T> implements Queue<T>, Iterable<T> {
    private static final int INIT_CAPACITY = 16;
    private int capacity;
    private int head;
    private int tail;
    private T[] arr;
    private int size;
    private class ArrayQueueIterator implements Iterator<T> {
        int current;
        ArrayQueueIterator() {
            current = head;
        }
        @Override
        public boolean hasNext() {
            return current != tail;
        }

        @Override
        public T next() {
            return arr[current++];
        }
    }
    public ArrayQueue () {
        arr = (T[]) new Object[INIT_CAPACITY];
    }
    @Override
    public void enqueue(T val) {
        arr[tail++] = val;
        size++;
        if (tail == capacity) {
            resize(capacity * 2);
        }
    }

    @Override
    public T dequeue() {
        if (size == 0) {
            return null;
        }
        T val = arr[head];
        arr[head++] = null;
        size--;
        if (size == (capacity / 4)) {
            resize(capacity / 2);
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

    private void resize(int newCapacity) {
        if (capacity >= INIT_CAPACITY) {
            T[] newArr = (T[]) new Object[newCapacity];
            int pos = 0;
            for (int i = head; i < tail; i++) {
                newArr[pos++] = arr[i];
            }
            arr = newArr;
            capacity = newCapacity;
            head = 0;
            tail = size - 1;
        }
    }

    @Override
    public String toString() {
        if (size == 0) {
            return "[]";
        }
        StringBuilder s = new StringBuilder("[");
        for (int i = head; i < tail; i++) {
            s.append(arr[i]).append(", ");
        }
        return s.toString() + "\b\b]";
    }

    @Override
    public Iterator<T> iterator() {
        return new ArrayQueueIterator();
    }
}
