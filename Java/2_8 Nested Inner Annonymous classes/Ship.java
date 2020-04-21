public class Ship extends Vehicle {
    private String type = "Корабель";

    public Ship(String country, int speed) {
        super(country, speed);
    }

    @Override
    public void run() {
        super.run();
        System.out.println("Корабель пливе зі швидкістю " + getSpeed());
    }

    public void run(String direction) {
        System.out.print("Корабель пливе зі швидкістю " + getSpeed());
        System.out.println(" в напрямку на " + direction);
    }

    @Override
    public String toString() {
        return type + " що зареєстрований в країні: " + this.getCountry();
    }
}
