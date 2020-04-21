public class BubbleSorter implements Sort {
    public double [] sorter (double [] array) {
        Swapper swap = new Swapper();

        if (array == null) {
            throw  new NullPointerException("Not array");
        }
        if (array.length == 0) {
            throw new IllegalArgumentException("Array is empty");
        }
        if (array.length == 1) {
            throw new IllegalArgumentException("Nothing to sort");
        }

        int already_sorted = 0;
                while (already_sorted == 0) {
                    already_sorted = 1;
                    for (int i = 1; i < array.length; i++) {
                        if (array[i] < array[i - 1]) {
                            swap.swap(array, i - 1, i);
                            already_sorted = 0;
                        }
                    }
                }
        return array;
    }
}
