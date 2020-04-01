public class InsertionSorter implements Sort {
        public double [] sorter (double array[]) {
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
                        Swapper swap = new Swapper();
                        swap.swap(array, i, i+1);
                    }
                    i--;
                }
            }
            return  array;
        }
    }

