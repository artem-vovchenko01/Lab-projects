public class ArrayStack<T> implements Stack<T> {
    private T[] arr;
    private int pointer;
    private int capacity;
    private final int INIT_CAPACITY = 16;

    public ArrayStack () {
        arr =  (T[]) new Object[INIT_CAPACITY];
        capacity = INIT_CAPACITY;
    }

    @Override
    public boolean isEmpty() {
        return pointer == 0;
    }

    @Override
    public int size() {
        return pointer;
    }

    @Override
    public T pop() {
        if (pointer == 0) {
            return null;
        }
        T val = arr[--pointer];
        arr[pointer] = null;
        if (pointer == (capacity / 4)) {
            resize(capacity / 2);
        }
        return val;
    }

    @Override
    public void push(T val) {
        if (pointer + 1 == capacity) {
            resize(capacity * 2);
        }
        arr[pointer++] = val;
    }

    private void resize (int newSize) {
        capacity = newSize;
        T[] copy = (T[]) new Object[newSize];
        for (int i = 0; i < pointer; i++) {
            copy[i] = arr[i];
        }
        arr = copy;
    }

    @Override
    public String toString () {
        if (pointer == 0) {
            return "[]";
        }
        StringBuilder s = new StringBuilder("[");
        for (int i = 0; i < pointer; i++) {
            s.append(arr[i]).append(", ");
        }
        return s.toString() + "\b\b]";
    }
}
