public class HeapSorter {
    public static void sort(Comparable[] arr) {
        int len = arr.length;
        for (int i = len / 2; i >= 0; i--) {
            sink(arr, i, len);
        }

        for (int i = len - 1; i > 0; i--) {
            exch(arr, i, 0);
            sink(arr, 0, --len);
        }
    }

    private static void sink(Comparable[] arr, int key, int len) {
        int maxPos = len - 1;
        if (2 * key + 2 > maxPos) {
            if (2 * key + 1 == maxPos) {
                if (less(arr, key, 2 * key + 1)) {
                    exch(arr, key, 2 * key + 1);
                }
            }
            return;
        }
        int child = less(arr, 2 * key + 2,2 * key + 1) ? 2 * key + 1 : 2 * key + 2;
        while (less(arr, key, child)) {
            exch(arr, key, child);
            key = child;
            if (2 * child + 2 > maxPos) return;
            child = less(arr, 2 * child + 2, 2 * child + 1) ? 2 * child + 1 : 2 * child + 2;
        }
    }

    private static void exch(Comparable[] arr, int i, int j) {
        Comparable temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    private static boolean less(Comparable[] arr, int i, int j) {
        return arr[i].compareTo(arr[j]) < 0;
    }
}
