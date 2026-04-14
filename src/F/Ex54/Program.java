package F.Ex54;
import F.Ex54.model.Product;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

public class Program {

    void main(){

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Set<Product> productSet = new TreeSet<>();

        IO.print("Enter full file path: ");
        String path = sc.next().trim();

        try(BufferedReader br = new BufferedReader(new FileReader(path))){

            String line;

            while((line = br.readLine()) != null){
                String[] fields = line.split(",");
                String name = fields[0].trim();
                Double price = Double.parseDouble(fields[1].trim());
                productSet.add(new Product(name, price));
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        if(productSet.isEmpty()){
            IO.println("No products found.");
            return;
        }

        double averagePrice = productSet.stream()
                .map(Product::getPrice)
                .reduce(Double::sum)
                .orElse(0.0) / productSet.size();

        IO.println(String.format("Average price: %.2f", averagePrice));

        productSet.stream()
                .filter(x -> x.getPrice() <= averagePrice)
                .map(Product::getName)
                .sorted((s1, s2) -> s2.toUpperCase().compareTo(s1.toUpperCase()))
                .forEach(IO::println);
        sc.close();
    }


}
