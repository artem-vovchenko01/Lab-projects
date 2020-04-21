public class Auto extends Vehicle {
    private int acceleration;
    private String type = "Автомобіль";

    void setAcceleraion(int a) {
        if (a==0) {
            throw new IllegalArgumentException("EXCEPTION! Acceleration should differ from 0. ");
        }
        this.acceleration = a;
    }

    public Auto(String country, int speed) {
        super(country, speed);
    }

    public Auto (String country, int speed, int acceleration) {
        super(country, speed);
        try {
            this.setAcceleraion(acceleration);
        } catch (IllegalArgumentException ex) {
            System.out.println(ex.getMessage());
        }
    }

    public int getAcceleration() {
        return acceleration;
    }

    public String getType() {
        return this.type;
    }

    @Override
    public void run() {
        super.run();
        System.out.println("Автомобіль їздить зі швидкістю " + getSpeed());
    }

    public void run(int acceleration) {
        System.out.print("Автомобіль їздить зі швидкістю " + getSpeed());
        System.out.println(" і прискоренням " + acceleration);
    }

    @Override
    public String toString() {
        return "Country: " + this.getCountry() + " Speed: " + this.getSpeed();
    }
}
