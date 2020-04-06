public interface Queue<T> {
    void enqueue(T val);
    T dequeue();
    boolean isEmpty();
    int size();
}
