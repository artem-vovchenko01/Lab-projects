public class SelectionSorter implements Sort {
        public double [] sorter(double array[]) {
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
                Swapper swap = new Swapper();
                swap.swap(array, i, min);
            }
            return array;
        }

    }
