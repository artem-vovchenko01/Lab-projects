public class Vehicle implements Run {
    private int speed;
    private String country;
    private String type = "Транспортний засіб";

    public Vehicle(String country, int speed) {
        try {
            this.setCountry(country);
        } catch (IllegalArgumentException ex) {
            System.out.println(ex.getMessage());
        }
        try {
            this.setSpeed(speed);
        }catch (IllegalArgumentException ex) {
            System.out.println(ex.getMessage());
        }
    }


    void setCountry(String country) {
        if (country.length() == 0) {
            throw new IllegalArgumentException("EXCEPTION! Empty string! ");
        } else {
            this.country = country;
        }
    }

    void setSpeed(int s) {
        if (s <=0) {
            throw new IllegalArgumentException ("EXCEPTION! Speed is less or equal to 0! ");
        } else  {
            this.speed = s;
        }
    }

    public String getCountry() {
        return this.country;
    }

    public int getSpeed() {
        return this.speed;
    }

    public String getType() {
        return this.type;
    }

    @Override
    public void run() {
        System.out.println("Це транспортний засіб, і він рухається.");
    }

    @Override
    public String toString() {
        return this.type + " що зареєстрований в країні: " + this.country;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o)
            return true;
        if (o == null)
            return false;
        if (getClass() != o.getClass())
            return false;
        Vehicle vehicle = (Vehicle) o;
        return (getType().equals(vehicle.getType())) & (getSpeed() == vehicle.getSpeed()) & (getCountry().equals(vehicle.getCountry()));
    }
}
