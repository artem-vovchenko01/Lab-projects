public class Lab7 {
        public  static  void  main(String[] args) {
            double array[] = {4.5, 1.3, 2.3, 18.5, 9.2,  5.7, 8.0};
            double array1[] = null;
            double array2[] = {4};
            double array3[] = {};
            Sort sel = new SelectionSorter();
            Sort ins = new InsertionSorter();
            Sort bub = new BubbleSorter();
            Print printer = new Printer();

            try {
                printer.printResults( sel.sorter(array) );
            } catch (NullPointerException | IllegalArgumentException e) {
                System.out.println("EXCEPTION! " + e.getMessage() );
            }
            try {
                printer.printResults( ins.sorter(array) );
            } catch (NullPointerException | IllegalArgumentException e) {
                System.out.println("EXCEPTION! " + e.getMessage() );
            }
            try {
                printer.printResults( bub.sorter(array) );
            } catch (NullPointerException | IllegalArgumentException e) {
                System.out.println("EXCEPTION! " + e.getMessage() );
            }
            try {
                printer.printResults( sel.sorter(array1));
            } catch (NullPointerException | IllegalArgumentException e) {
                System.out.println("EXCEPTION! " + e.getMessage() );
            }
            try {
                printer.printResults( ins.sorter(array2));
            } catch (NullPointerException | IllegalArgumentException e) {
                System.out.println("EXCEPTION! " + e.getMessage() );
            }
            try {
                printer.printResults( sel.sorter(array3) );
            } catch (NullPointerException | IllegalArgumentException e) {
                System.out.println("EXCEPTION! " + e.getMessage() );
            }
        }
}
