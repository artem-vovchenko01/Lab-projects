public class IncorrectPrice extends Exception {
    @Override
    public String getMessage() {
        return "Ціна повинна бути більшою від 0";
    }
}
