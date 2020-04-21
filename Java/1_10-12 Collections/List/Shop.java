import java.util.List;
import java.util.LinkedList;

public class Shop implements ShopInterface {
    private String title;
    private List<Product> products = new LinkedList();
    private List<Integer> prices = new LinkedList();

    public Shop(String title) {
        if (title.length() == 0) {
            throw new IllegalArgumentException("EXCEPTION! Назва не може бути порожньою. ");
        }
        this.title = title;
        Database.registerShop(this);
    }
    @Override
    public void addProduct(Product product, int price) {
        if (price <= 0) {
            throw new IllegalArgumentException("EXCEPTION! Ціна має бути більшою від 0. ");
        }
        products.add(product);
        prices.add(price);
        product.addShop(this);
    }
    @Override
    public int getPrice(Product product) {
        int place = 0;
        int price = -1;
        for (Product prod : products) {
            if (prod == product) {
                price = prices.get(place);
            }
            place++;
        }
        if (price == -1) {
            throw new IllegalArgumentException("EXCEPTION! У магазині немає даного товару. ");
        }
        return price;
    }

    public List<Product> getProducts () {
        return products;
    }
    public List<Integer> getPrices () {
        return prices;
    }
    @Override
    public String toString() {
        return title;
    }
}
