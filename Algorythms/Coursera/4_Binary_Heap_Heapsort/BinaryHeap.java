import java.util.Arrays;
import java.util.Iterator;

public class BinaryHeap <T extends Comparable<T>> implements Iterable<T> {
    private T[] arr;
    private int pointer;
    private final int INIT_CAPACITY = 4;
    private int capacity;

    public BinaryHeap() {
        this.arr = (T[]) new Comparable[INIT_CAPACITY];
        capacity = INIT_CAPACITY;
    }

    public void insert(T item) {
        if (pointer + 1 == capacity) {
            resize(capacity * 2);
        }
        arr[++pointer] = item;
        swim(pointer);
    }

    public T delMax() {
        if (pointer == 0) return null;
        T item = arr[1];
        arr[1] = arr[pointer];
        arr[pointer--] = null;
        sink(1);
        return item;
    }

    public boolean hasNext() {
        return pointer >= 1;
    }

    public int size() {return pointer; }

    private void swim(int key) {
        int parent = key / 2;
        while (parent >= 1 && less(parent, key)) {
            exch(key, parent);
            key = parent;
            parent /= 2;
        }
    }

    private void sink(int key) {
        if (2 * key + 1 > pointer) return;
        int child = less(2 * key + 1,2 * key) ? 2 * key : 2 * key + 1;
        while (less(key, child)) {
            exch(key, child);
            key = child;
            if (2 * child + 1 > pointer) return;
            child = less(2 * child + 1, 2 * child) ? 2 * child : 2 * child + 1;
        }
    }

    private void exch(int i, int j) {
        T temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    private boolean less(int i, int j) {
        return arr[i].compareTo(arr[j]) < 0;
    }

    private void resize(int newCapacity) {
        T[] newArr = (T[]) new Comparable[newCapacity];
        for (int i = 0; i <= pointer; i++) {
            newArr[i] = arr[i];
        }
        arr = newArr;
        capacity = newCapacity;
    }

    @Override
    public Iterator<T> iterator() {
        return new Iterator<T>() {
            BinaryHeap<T> copy;
            {
                BinaryHeap<T> copy = new BinaryHeap<>();
                    copy.arr = Arrays.copyOf(arr, arr.length);
                    copy.capacity = capacity;
                    copy.pointer = pointer;
                    this.copy = copy;
            }
            @Override
            public boolean hasNext() {
                return copy.hasNext();
            }

            @Override
            public T next() {
                return copy.delMax();
            }
        };
    }
}
