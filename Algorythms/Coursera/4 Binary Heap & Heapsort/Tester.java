import java.util.Arrays;
import java.util.Random;

public class Tester {
    public static void main(String[] args) {
        BinaryHeap<Integer> heap = new BinaryHeap<>();
        Random r = new Random();

        System.out.println("Size: " + heap.size());

        for (int i = 0; i < 20; i++) {
            int next = r.nextInt(20);
            heap.insert(next);
        }
        System.out.println("Size: " + heap.size());
        System.out.println(" ----------------- ");
        System.out.println("Deleting: ");

        while (heap.hasNext()) {
            System.out.println(heap.delMax());
        }

        System.out.println("Size: " + heap.size());

        for (int i = 0; i < 20; i++) {
            int next = r.nextInt(20);
            heap.insert(next);
        }

        System.out.println("Size: " + heap.size());
        System.out.println(" ----------------- ");
        System.out.println("Iterator: ");

        for (int i : heap) {
            System.out.println(i);
        }
        System.out.println(" ----------------- ");
        System.out.println("Deleting: ");

        while (heap.hasNext()) {
            System.out.println(heap.delMax());
        }
        System.out.println("Size: " + heap.size());
        System.out.println("Deleting: ");
        System.out.println(heap.delMax());
        System.out.println("Size: " + heap.size());

        System.out.println(" ----------------- ");
        System.out.println("Checking sortign for correctness: ");
        Integer[] arr;
        for (int size = 0; size < 20; size++) {
            arr = new Integer[size];
            for (int i = 0; i < size; i++) {
                arr[i] = r.nextInt(10000);
            }
            HeapSorter.sort(arr);
            for (int i = 1; i < size; i++) {
                if (arr[i - 1].compareTo(arr[i]) > 0) {
                    System.out.println("Wrong ");
                }
            }
            System.out.println(Arrays.toString(arr));
        }

        System.out.println(" ----------------- ");

        for (int size = 500_000; size < 4_000_000; size += 500_000) {
            arr = new Integer[size];
            for (int i = 0; i < size; i++) {
                arr[i] = r.nextInt(5_000_000);
            }
            double t1 = System.nanoTime();
            HeapSorter.sort(arr);
            System.out.println("Time for heapsorting array of size " + size + " : " + (System.nanoTime() - t1) / 1_000_000_000);
        }
    }
}
