public class Lab3 {
    public static void main(String[] args) {
        printResults(10,20);
        printResults(2,35);
        printResults(1,10);
        printResults(2,1);

        Task10.result10(10,20);
        Task10.result10(-5,15);
        Task10.result10(20,40);

        Task15.result15(-0.1);
        Task15.result15(0.1);
        Task15.result15(0.01);
        Task15.result15(0.001);
    }

    static void printResults(double s, double k) {
        try {
            System.out.println("Result in task 5: " + " s = " + s + " k = " +  k + "      " + sumEval(s, k));
        }
        catch (IllegalArgumentException e) {
            System.err.println("EXCEPTION! "+ e.getMessage());
        }
    }

    static double sumEval(double s, double k) {
        double sum = 0;
        int i = 1;
        if (k < 1 || k >= 35) {
            throw new IllegalArgumentException("param. k = " + k);
        }
        while (i<=k) {
            sum += (Math.log(Math.sqrt(s / (i * i))) / Math.log(10));
            i++;
        }
        return sum;
    }

    }




 class Task10 {
    public static void result10(double t,double n) {
        try {
        System.out.println("Result in task 10: " + " t = " + t + " n = " +  n + "       " +  evalSecond(t,n));
    }
    catch (IllegalArgumentException e) {
        System.out.println("EXCEPTION! "+ e.getMessage());
    }
    }
    static double evalSecond(double t, double n) {
        double sum2 = 0;
        double i = 0;
        if (n < 1) {
            throw new IllegalArgumentException("param. n" + n);
        }
        if (t > 0) {
            while (i < n) {
                sum2 = sum2 + Math.sqrt(t*i);
                i++;
            }}
            if (t < 0) {
                while (i < n) {
                    sum2 = sum2 + t*t*i;
                    i++;
                }

            }
            return sum2;
        }

}



    class Task15 {
        public static void result15(double e_num) {
            try {
                System.out.println("Result in task 15: " + " e_num = " + e_num + "      " + evalThird(e_num));
            }
            catch (IllegalArgumentException e) {
                System.out.println("EXCEPTION! "+ e.getMessage());
            }
        }
    static double evalThird(double e) {
        double sum3 = -100;
        int i = 1;
         double add = 100;
        if (e <= 0) {
            throw new IllegalArgumentException("param. e = " + e);
        }
        while (Math.abs(add) >= e) {
            sum3 = sum3 + add;
            add = ( Math.pow(-1,i+1) / (i*(i+1)*(i+2)) );
            i ++;
        }
return sum3;
    }
    }