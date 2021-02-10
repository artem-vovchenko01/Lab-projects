public class DijkstraAlgorythm {
    public static void main(String[] args) {
        String expression = "(1 +  (( 2 + 3 ) * (4 * 5 )))";
        ArrayStack<String> operations = new ArrayStack<>();
        ArrayStack<Integer> values = new ArrayStack<>();
        String numbers = "0123456789";
        String allowedOperations = "*+";
        for (String el : expression.split("")) {
            if (numbers.contains(el)) {
                values.push(Integer.valueOf(el));
            } else if (allowedOperations.contains(el)) {
                operations.push(el);
            } else if (el.equals(")")) {
                String operation = operations.pop();
                switch (operation) {
                    case "+":
                        values.push(values.pop() + values.pop());
                        break;
                    case "-":
                        values.push(values.pop() - values.pop());
                        break;
                    case "*":
                        values.push(values.pop() * values.pop());
                        break;
                    case "/":
                        values.push(values.pop() / values.pop());
                        break;
                }
            }
        }
        System.out.println("Result: " + values.pop());
    }
}
