public class Lab4 {
    public static void main(String[] args) {
        int[] passed = {4,-3,5,2,1,9,-2,10,-4,5,6,0,-2};
        int length = 13;
        try {
            printResults(passed,length);
        } catch (IndexOutOfBoundsException e) {
            System.out.println("EXCEPTION! "+ e.getMessage());
        }
        try {
            rangeSum.sumInRange(passed,length);
        } catch (IndexOutOfBoundsException e) {
            System.out.println("EXCEPTION!" + e.getMessage());
        }
        try {
            Reverse.getReverse(passed,length);
        } catch (IndexOutOfBoundsException e) {
            System.out.println("EXCEPTION!" + e.getMessage());
        }
    }
    static int printResults(int[] passed,int length){
        int[] results = new int[length];
                for (int i=0; i<results.length;i++) {
                    results[i] = passed[i];
                }
                if (passed.length != results.length) {
                    throw new IndexOutOfBoundsException("length passed = " + passed.length);
                }
                int sum = 0;
                for (int x=0; x<results.length; x++) {
                    if (results[x]<0) {
                        sum += results[x];
                    }
        }
        System.out.print("Початковий масив: ");
                for (int element: results) {

                    System.out.print(element);
                    System.out.print(" ");
                }
                System.out.println();
                System.out.println("Сума всіх від'ємних чисел: " + sum);
        return sum;
    }
}

class rangeSum {
    static int sumInRange(int[] passed,int length) {
        int[] results = new int[length];
        for (int i=0; i<results.length;i++) {
        results[i] = passed[i];
        }
        if (passed.length != results.length) {
        throw new IndexOutOfBoundsException("length passed = " + passed.length);
        }
        int sum = 0;
        for (int x=5; x<11; x++) {
        sum += results[x];
        }
        System.out.println("Сума елементів з 5 по 11: " + sum);
        return sum;
        }


        }

        class Reverse {
    static  int[] getReverse(int[] passed,int length) {
        int[] result = new int[length];
        for (int y=0; y<result.length; y++) {
            result[y] = passed[length-y-1];
        }
        if (passed.length != result.length) {
            throw new IndexOutOfBoundsException("length passed = " + passed.length);
        }
        System.out.print("Перевернутий масив: ");
        for (int element: result) {
            System.out.print(element);
            System.out.print(" ");
        }
        return  result;
    }

        }
