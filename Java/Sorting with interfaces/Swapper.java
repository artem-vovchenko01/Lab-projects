public class Swapper implements Swap {
        public void swap(double array[], int i, int min) {
            double temp = array[i];
            array[i] = array[min];
            array[min] = temp;
        }
    }
