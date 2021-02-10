import java.util.Arrays;
import java.util.Random;

public class Tester {
    public static void main(String[] args) {
        Integer[] arr = {4, 2, -1, 4, 6, 20, 48, 482, 6, -10, 2, 1, 4, 0, 5};

        Sorter.selectionSort(arr);
        System.out.println(Arrays.toString(arr));
        Sorter.shuffle(arr);
        System.out.println(Arrays.toString(arr));

        System.out.println();
        Sorter.insertionSort(arr);
        System.out.println(Arrays.toString(arr));
        Sorter.shuffle(arr);
        System.out.println(Arrays.toString(arr));

        System.out.println();
        Sorter.shellSort(arr);
        System.out.println(Arrays.toString(arr));
        Sorter.shuffle(arr);
        System.out.println(Arrays.toString(arr));

        System.out.println();
        Sorter.mergeSort(arr);
        System.out.println(Arrays.toString(arr));
        Sorter.shuffle(arr);
        System.out.println(Arrays.toString(arr));

        Random random = new Random();
        int huge_num = 5_000_001;
        Integer[] big_arr = new Integer[huge_num];
        for (int i = 0; i < huge_num; i++)
            big_arr[i] = random.nextInt(huge_num);

        long t1 = System.nanoTime();
        Sorter.bottomUpMergeSort(big_arr);
        System.out.println("Bottom-up merge sort, elapsed: " + (System.nanoTime() - t1) / (double) 1_000_000_000);
        for (int i = 1; i < big_arr.length; i++) {
            if (!(big_arr[i - 1] <= big_arr[i]))
                System.out.println("wrong");
        }

        t1 = System.nanoTime();
        Sorter.threeWayQuickSort(big_arr);
        System.out.println("Three way quick sort, elapsed: " + (System.nanoTime() - t1) / (double) 1_000_000_000);
        for (int i = 1; i < big_arr.length; i++) {
            if (!(big_arr[i - 1] <= big_arr[i]))
                System.out.println("wrong");
        }

        t1 = System.nanoTime();
        Sorter.threeWayQuickSort(big_arr);
        System.out.println("Classical quick sort, elapsed: " + (System.nanoTime() - t1) / (double) 1_000_000_000);
        for (int i = 1; i < big_arr.length; i++) {
            if (!(big_arr[i - 1] <= big_arr[i]))
                System.out.println("wrong");
        }

        Integer[] manyEqualKeys = new Integer[huge_num];
        for (int i = 0; i < huge_num; i++)
        {
            manyEqualKeys[i] = random.nextInt(2);
        }

        t1 = System.nanoTime();
        Sorter.classicQuickSort(manyEqualKeys);
        System.out.println("Classical quick sort, many equal keys, elapsed: " + (System.nanoTime() - t1) / (double) 1_000_000_000);
        for (int i = 1; i < big_arr.length; i++) {
            if (!(big_arr[i - 1] <= big_arr[i]))
                System.out.println("wrong");
        }

        t1 = System.nanoTime();
        Sorter.threeWayQuickSort(manyEqualKeys);
        System.out.println("Three way quick sort, many equal keys, elapsed: " + (System.nanoTime() - t1) / (double) 1_000_000_000);
        for (int i = 1; i < big_arr.length; i++) {
            if (!(big_arr[i - 1] <= big_arr[i]))
                System.out.println("wrong");
        }

        int k = huge_num / 2;
        System.out.println(k + "th largest: " + Sorter.select(big_arr, k));
        System.out.println("0th largest (min): " + Sorter.select(big_arr, 0));
        System.out.println(big_arr.length - 1 + "th largest (max): " + Sorter.select(big_arr, big_arr.length - 1));
    }
}
