import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

class Lab13 {
    public static void main(String[] args) {

        Shop fora = null; Shop dobrunya = null; Shop silpo = null; Shop atb = null; Product water = null; Product bread = null; Product chocolate = null; Product milk = null;
        TestExceptions testEx = new TestExceptions();
        testEx.catchChecked();
        try {
            testEx.getFromArray(11);
        } catch (IndexOutOfBoundsException e) {
            System.out.println("Стався RuntimeException");
            System.out.println(e.getMessage());
            System.out.println();
        }

        try {
            testEx.divide(5, 0);
        } catch (ArithmeticException e) {
            System.out.println("Стався ArithmeticException");
            System.out.println(e.getMessage());
            System.out.println();
        }

        try {
            dobrunya = new Shop("Добриня");
            silpo = new Shop("Сільпо");
            atb = new Shop("АТБ");
            fora = new Shop("Фора");

            water = new Product("Вода", 15);
            bread = new Product("Хліб", 20);
            milk = new Product("Молоко", 28);
            chocolate = new Product("Шоколад", 40);

            dobrunya.addProduct(water, 14);
            silpo.addProduct(water, 16);
            atb.addProduct(water, 13);
            fora.addProduct(water, 13);

            dobrunya.addProduct(bread, 18);
            silpo.addProduct(bread, 20);
            atb.addProduct(bread, 19);
            fora.addProduct(bread, 20);

            dobrunya.addProduct(milk, 27);
            silpo.addProduct(milk, 30);
            atb.addProduct(milk, 25);

            silpo.addProduct(chocolate, 39);
            atb.addProduct(chocolate, 39);
            fora.addProduct(chocolate, 40);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        fora.setDiscount(bread, 10);
        fora.setDiscount(chocolate, 15);

        Set<Product> products = new HashSet<Product>();
        products.add(water); products.add(bread); products.add(milk); products.add(chocolate);
        for (Product product : products) {
            System.out.println("Найменша ціна на " + product + ": " + product.findMinPrice());
            Iterator best_shops_iter = product.findBestShops().iterator();
            String best_shop_string = "";
            while (best_shops_iter.hasNext()) {
                Shop shop = (Shop) best_shops_iter.next();
                best_shop_string += shop.toString() + " ";
            }
            System.out.println("Товар " + product + " продається за найкращою ціною " + product.findMinPrice() + " в магазинах " + best_shop_string + "\n");
        }

        String discount_list = "Знижки, доступні в магазині " + fora + "\n";
        Set<Map.Entry<Product, Integer>> entries = fora.getDiscounts();
        for (Map.Entry<Product, Integer> entry : entries) {
            discount_list += entry.getKey().toString() + " : -" + entry.getValue() + " %. Нова ціна - " + fora.getPrice( entry.getKey() ) + "\n";
        }
        if (fora.getDiscounts().size() == 0) {
            System.out.println("На жаль, магазині " + fora + " зараз немає знижок. \n");
        }
        else {
            System.out.println(discount_list);
        }

        Searcher main_search = new Searcher();
        System.out.println("Магазини, в яких ціни менші, ніж рекомендовані: ");
        String cheapest_string = "";
        Iterator<Shop> cheapest_iter = main_search.isCheapestExists().iterator();
        while (cheapest_iter.hasNext()) {
            cheapest_string += cheapest_iter.next().toString() + " ";
        }
        if (cheapest_string.length() != 0) {
            System.out.println(cheapest_string);
        } else {
            System.out.println("Немає магазинів, у яких ціни менші за рекомендовані. ");
        }
    }
}
