import java.util.*;

public class Shop implements ShopInterface {
    private String title;
    private Set<String> products = new HashSet<String>();
    private Map<Product, Integer> discounts = new HashMap<Product, Integer>();

    public Shop(String title) throws EmptyTitle {
        if (title.length() == 0) {
            throw new EmptyTitle();
        }
        this.title = title;
        Database.registerShop(this);
    }
    @Override
    public void addProduct(Product product, int price) {
        if (price <= 0) {
            throw new IllegalArgumentException("Ціна має бути більшою від 0. ");
        }
        products.add(product.toString() + ":" +  price);
        product.addShop(this);
    }
    @Override
    public int getPrice(Product product) { ;
        String price_this = "";
        for (String prod : products) {
            if (prod.split(":")[0].equals(product.toString())) {
                price_this = prod.split(":")[1];
            }
        }
        if (price_this.equals("")) {
            throw new IllegalArgumentException("У магазині немає даного товару. ");
        }
        return Integer.valueOf(price_this);
    }

    public void setDiscount(Product product, int percent) {
        if (percent >= 100 || percent <= 0) {
            throw new IllegalArgumentException("Значення процента повинно лежати в межах від 0 до 100");
        }
        int new_price = (int)(getPrice(product) * (double)(100 - percent)/100 );
        String old_product = product.toString() + " " + this.getPrice(product);
        this.products.remove(old_product);
        addProduct(product, new_price);
        discounts.put(product, percent);
    }

    @Override
    public Set<Map.Entry<Product, Integer>> getDiscounts() {
        return discounts.entrySet();
    }

    public Set<Product> getProducts() {
        Set<Product> to_return = new HashSet<Product>();
        Database DB = new Database();
        for (Product prod : Database.getProducts()) {
            for (String our_prod : products) {
                if (prod.toString().equals(our_prod.split(":")[0])) {
                    to_return.add(prod);
                }
            }
        }
        return to_return;
    }
    public Set<String> getProductsWithPrices () {
        return products;
    }
    @Override
    public String toString() {
        return title;
    }

}
