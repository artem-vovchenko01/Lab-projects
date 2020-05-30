import java.util.Iterator;
import java.util.NoSuchElementException;

import edu.princeton.cs.algs4.StdRandom;
public class RandomizedQueue<Item> implements Iterable<Item> {
    private Item[] arr;
    private static final int INIT_CAPACITY = 16;
    private int capacity;
    private int size;

    // construct an empty randomized queue
    public RandomizedQueue() {
        capacity = INIT_CAPACITY;
        arr = (Item[]) new Object[INIT_CAPACITY];
    }

    // is the randomized queue empty?
    public boolean isEmpty() {
        return size == 0;
    }

    // return the number of items on the randomized queue
    public int size() {
        return size;
    }

    // add the item
    public void enqueue(Item item) {
        if (item == null) {
            throw new IllegalArgumentException();
        }
        arr[size++] = item;
        if (size == capacity) {
            resize(capacity * 2);
        }
    }

    private void resize(int newCapacity) {
        if (capacity >= INIT_CAPACITY) {
            Item[] newArr = (Item[]) new Object[newCapacity];
            for (int i = 0; i < size; i++) {
                newArr[i] = arr[i];
            }
            arr = newArr;
            capacity = newCapacity;
        }
    }

    // remove and return a random item
    public Item dequeue() {
        if (size == 0) {
            throw new NoSuchElementException();
        }
        int pos = StdRandom.uniform(size);
        Item item = arr[pos];
        Item last = arr[size - 1];
        arr[--size] = null;
        if (pos != size) {
            arr[pos] = last;
        }
        if (size == (capacity / 4)) {
            resize(capacity / 2);
        }
        return item;
    }

    // return a random item (but do not remove it)
    public Item sample() {
        if (size == 0) {
            throw new NoSuchElementException();
        }
        int pos = StdRandom.uniform(size);
        return arr[pos];
    }

    // return an independent iterator over items in random order
    public Iterator<Item> iterator() {
        return new Iterator<Item>() {
            int current;
            Object[] objArr;

            {
                if (size != 0) {
                    objArr = new Object[size];
                    for (int i = 0; i < size; i++) {
                        objArr[i] = arr[i];
                    }
                    StdRandom.shuffle(objArr);
                }
            }

            @Override
            public boolean hasNext() {
                return current != size;
            }

            @Override
            public Item next() {
                if (!hasNext()) {
                    throw new NoSuchElementException();
                }
                return (Item) objArr[current++];
            }

            @Override
            public void remove() {
                throw new UnsupportedOperationException();
            }
        };
    }

    @Override
    public String toString() {
        if (size == 0) {
            return "[]";
        }
        StringBuilder s = new StringBuilder("[");
        for (int i = 0; i < size; i++) {
            s.append(arr[i]).append(", ");
        }
        return s.toString() + "\b\b]";
    }

    // unit testing (required)
    public static void main(String[] args) {
        RandomizedQueue<Integer> rq = new RandomizedQueue<>();

        System.out.println("ENQUEUING");
        for (int i = 0; i < 10; i++) {
            rq.enqueue(i);
            System.out.println(rq);
        }
        System.out.println("FOREACH");
        for (int i : rq) {
            System.out.println(i);
        }
        System.out.println("SAMPLING");
        for (int i = 0; i < 5; i++) {
            System.out.println(rq.sample());
        }
        System.out.println("DEQUEUING");
        while (!rq.isEmpty()) {
            System.out.println(rq.dequeue());
            System.out.println(rq);
        }

        System.out.println("SZ: " + rq.size());
        System.out.println("IS_EMPTY: " + rq.isEmpty());
    }

}