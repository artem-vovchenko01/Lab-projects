import java.util.Random;
public class Sorter {
    private static final int CUTOFF = 16;
    public static Comparable select(Comparable[] arr, int k)
    {
        shuffle(arr);
        int lo = 0, hi = arr.length - 1;
        int j;
        while (lo < hi)
        {
            j = partition(arr, lo, hi);
            if (k > j) lo = j + 1;
            else if (k < j) hi = j - 1;
            else return arr[k];
        }
        return arr[k];
    }

    public static void selectionSort(Comparable[] arr)
    {
        int min;
        for (int i = 0; i < arr.length; i++)
        {
            min = i;
            for (int j = i; j < arr.length; j++)
                if (less(arr[j], arr[min]))
                    min = j;
            exchange(arr, i, min);
        }
    }

    public static void insertionSort(Comparable[] arr)
    {
        sectionInsertionSort(arr, 0, arr.length - 1);
    }

    public static void shellSort(Comparable[] arr)
    {
        int len = arr.length;
        int x = (len - 1) / 3;
        for (int gap = 3 * x + 1; gap > 0; gap = 3 * x + 1)
        {
            for (int i = gap; i < len; i += 1)
            {
                for (int j = i; j > 0; j-= gap)
                {
                    if (less(arr[j], arr[j - 1]))
                        exchange(arr, j, j - 1);
                    else break;
                }
            }
            x--;
        }
    }

    public static void mergeSort(Comparable[] arr)
    {
        Comparable[] aux = new Comparable[arr.length];
        sort(arr, aux, 0, arr.length - 1);
    }

    public static void bottomUpMergeSort(Comparable[] arr)
    {
        int N = arr.length;
        Comparable[] aux = new Comparable[N];
        for (int sz = 1; sz < N; sz+=sz)
        {
            for (int lo = 0; lo < N - sz; lo+=sz + sz)
                merge(arr, aux, lo, lo + sz - 1, Math.min(lo + sz + sz - 1, N - 1));
        }
    }

    public static void shuffle(Object[] arr)
    {
        Random random = new Random();
        for (int i = 0; i < arr.length; i++)
        {
            int pos = random.nextInt(i + 1);
             exchange(arr, pos, i);
        }
    }

    public static void classicQuickSort(Comparable[] arr)
    {
        shuffle(arr);
        classicQuickSorting(arr, 0, arr.length - 1);
    }

    public static void threeWayQuickSort(Comparable[] arr)
    {
        shuffle(arr);
        threeWayQuickSorting(arr, 0, arr.length - 1);
    }

    private static void classicQuickSorting(Comparable[] arr, int lo, int hi)
    {
        if (hi <= lo) return;
        if (hi <= lo + CUTOFF - 1)
        {
            sectionInsertionSort(arr, lo, hi);
            return;
        }
        int pivot = partition(arr, lo, hi);
        classicQuickSorting(arr, lo, pivot - 1);
        classicQuickSorting(arr, pivot + 1, hi);
    }

    private static void threeWayQuickSorting(Comparable[] arr, int lo, int hi)
    {
        if (hi <= lo) return;
        int lt = lo, gt = hi;
        int i = lo;
        Comparable v = arr[lo];
        while (i <= gt)
        {
            int cmp = arr[i].compareTo(v);
            if (cmp < 0) exchange(arr, lt++, i++);
            else if (cmp > 0) exchange(arr, i, gt--);
            else i++;
        }
        threeWayQuickSorting(arr, lo, lt - 1);
        threeWayQuickSorting(arr, gt + 1, hi);
    }

    private static int partition(Comparable[] arr, int lo, int hi)
    {
        int i = lo, j = hi + 1;
        while (true)
        {
            while (less(arr[++i], arr[lo]))
                if (i == hi) break;

            while (less(arr[lo], arr[--j]))
                if (j == lo) break;

            if (i >= j)
                break;

            exchange(arr, i, j);
        }
        exchange(arr, lo, j);
        return j;
    }

    private static boolean less(Comparable left, Comparable right)
    {
        return left.compareTo(right) < 0;
    }

    private static void exchange(Object[] arr, int first, int last)
    {
        Object temp = arr[first];
        arr[first] = arr[last];
        arr[last] = temp;
    }

    private static void sectionInsertionSort(Comparable[] arr, int lo, int hi)
    {
        for (int i = lo; i <= hi; i++)
        {
            for (int j = i; j > lo; j--)
            {
                if (less(arr[j], arr[j - 1]))
                    exchange(arr, j - 1, j);
                 else break;
            }
        }
    }

    private static void merge(Comparable[] arr, Comparable[] aux, int lo, int mid, int hi)
    {
        for (int k = lo; k <= hi; k++)
            aux[k] = arr[k];
        int i = lo;
        int j = mid + 1;
        for (int k = lo; k <= hi; k++)
        {
            if (i > mid)
                arr[k] = aux[j++];
             else if (j > hi)
                arr[k] = aux[i++];
             else if (less(aux[i], aux[j]))
                arr[k] = aux[i++];
             else arr[k] = aux[j++];
        }
    }

    private static void sort(Comparable[] arr, Comparable[]aux, int lo, int hi)
    {
        if (hi <= lo + CUTOFF - 1)
        {
            sectionInsertionSort(arr, lo, hi);
            return;
        }
            int mid = lo + (hi - lo) / 2;
            sort(arr, aux, lo, mid);
            sort(arr, aux, mid + 1, hi);
            if (less(arr[mid + 1], arr[mid]))
            {
                merge(arr, aux, lo, mid, hi);
            }
    }
}
