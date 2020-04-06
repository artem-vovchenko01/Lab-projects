import java.util.Arrays;

public class Lab5 {
    public  static void main(String[] args) {
    int [][] initial = new int[][] {
            {7, -5, 4, 3, 2},
            {8, -10, 15, 23, 4},
            {2, -8, -17, 5, 10},
            {17, 9, 0, 7, 2},
            {1, 2, 3, 4, 5}
    };
    int [][] championship = new int[][] {
            {0,0,1,0,1,1,1},
            {2,0,1,2,0,0,2},
            {1,1,0,2,1,2,2},
            {2,0,0,0,1,2,0},
            {1,2,1,1,0,1,0},
            {1,2,0,0,1,0,2},
            {1,0,0,2,2,0,0}
    };

    System.out.println("Початкова матриця: ");
    for (int k=0; k<5; k++) {
        for (int j=0; j<5; j++) {
            System.out.print(initial[k][j] + "\t");
        }
        System.out.println();
    }

    try {
        clearNE(initial);
        clearNE(null);
    } catch (NullPointerException e) {
        System.out.println("EXCEPTION! " + e.getMessage());
    }
    int[][] wrong = new int[4][5];
    try {
        clearNE(wrong);
    } catch (IllegalArgumentException w) {
        System.out.println("EXCEPTION! " + w.getMessage());
    }


        System.out.println("Результати чемпіонату: ");
        for (int i = 0; i < 7; i++) {
            System.out.print("Команда " + (i+1) + "\t");
        }

        System.out.println();
        for (int k=0; k<7; k++) {
            for (int j=0; j<7; j++) {
                System.out.print(championship[k][j] + "\t\t\t");
            }
            System.out.println();
        }

        int [] teams = Football.getFlawless(championship);
        int wrong2 [][] = new int [6][6];
        try {
            Football.getFlawless(wrong2);
        } catch (IndexOutOfBoundsException e) {
            System.out.println("EXCEPTION! " + e.getMessage());
        }
        System.out.println("Команди, які не програли жодного матчу: ");
        for (int i=0; i< teams.length;i++) {
            if (teams[i] > 0) {
                System.out.print(teams[i] + "\t");
            }
        }
        System.out.println();
    }


    static void clearNE (int[][] matrix) {
        System.out.println();
        if (matrix.length != matrix[0].length) {
            throw new IllegalArgumentException("Matrix should be squared.");
        }
        if (matrix == null) {
            throw new NullPointerException("Null isn't allowed");
        }
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (i <= j) {
                    matrix[i][j] = 0;
                }
            }
        }
        System.out.println("Нова матриця: ");
            for (int k=0;k<5;k++) {
                for ( int h=0;h<5;h++){
       System.out.print(matrix[k][h] + "\t");
                }
                System.out.println();
            }
    }
    }


    class Football {
    static int[] getFlawless(int[][] results){
        if (results.length != 7 | results[0].length != 7) {
            throw new IndexOutOfBoundsException("The array here should be 7x7");
        }
        int [] noLoss = new int[7];
        int place = 0;
        for (int i=0; i<7; i++) {
            int noLossCount = 0;
            for (int k=0; k<7; k++){
                if (results[k][i] == 1 || results[k][i] == 2 || (i == k && results[k][i] == 0)) {
                    noLossCount += 1;
                }
            }
            if (noLossCount == 7) {
                noLoss[place] = i + 1;
                place +=1;
            }
        }
 return noLoss;
    }
    }

