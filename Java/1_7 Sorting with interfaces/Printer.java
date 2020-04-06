public class Printer implements Print {
        public void printResults(double array[]) {
            for (int i = 0; i < array.length; i++) {
                System.out.print(array[i] + "\t");
            }
            System.out.println();
        }
    }
