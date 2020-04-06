class EmptyTitle extends Exception {
    @Override
    public String getMessage() {
        return "Назва повинна мати ненульову довжину! ";
    }
}
