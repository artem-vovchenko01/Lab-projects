public class TestExceptions {
    void catchChecked() {
        try {
            Shop exampleShop = new Shop("");
            System.out.println("Створено об'єкт Shop");
        } catch (EmptyTitle e) {
            System.out.println("Сталася виняткова ситуація, вхід у блок catch");
            System.out.println(e.getMessage());
        } finally {
            System.out.println("Це блок finally, він виконається незалежно від того, відловлюється виняткова ситуація чи ні \n");
        }
    }

    void getFromArray (int place) {
        int [] testArray = new int [10];
        System.out.println(testArray[place]);
    }

    int divide (int a, int b) {
        return (int) a / b;
    }
}
