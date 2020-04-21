public class Lab6 {
    public  static  void  main(String[] args) {
        double array[] = {4.5, 1.3, 2.3,  5.7, 8.0};
        double array1[] = null;
        double array2[] = {4};
        try {
            printResults( selectionSort(array) );
            printResults( insertionSort(array) );
            printResults( selectionSort(array1));
            //printResults( insertionSort(array2));
        } catch (NullPointerException | IllegalArgumentException e) {
            System.out.println("EXCEPTION! " + e.getMessage() );
        }
    }

    public static double [] selectionSort(double array[]) {
        if (array == null) {
            throw  new NullPointerException("Not array");
        }
        if (array.length == 0) {
            throw new IllegalArgumentException("Array is empty");
        }
        if (array.length == 1) {
            throw new IllegalArgumentException("Nothing to sort");
        }
        for (int i = 0; i < array.length; i++) {
            int min = i;
            for (int j = i+1; j < array.length; j++) {
                if (array[j] < array[min]) {
                    min = j;
                }
            }
            swap(array, i, min);
        }
        return  array;
    }

    public static double [] insertionSort (double array[]) {
        if (array == null) {
            throw  new NullPointerException("Not array");
        }
        if (array.length == 0) {
            throw new IllegalArgumentException("Array is empty");
        }
        if (array.length == 1) {
            throw new IllegalArgumentException("Nothing to sort");
        }
        for (int j=1; j<array.length;j++) {
            double key = array[j];
            int i = j-1;
            while (i > -1) {
                if (array[i] > array[i+1]){
                    swap(array, i, i+1);
                }
                i--;
            }
        }
        return  array;
    }

    public static void swap(double array[], int i, int min) {
        double temp = array[i];
        array[i] = array[min];
        array[min] = temp;
    }

    public static void printResults(double array[]) {
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + "\t");
        }
        System.out.println();
    }
}
