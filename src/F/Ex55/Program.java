package F.Ex55;

import F.Ex55.model.Employee;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.function.Predicate;

public class Program {
    void main(){

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Set<Employee> employees = new HashSet<>();

        IO.print("Enter full file path: ");
        String path = sc.next();
        addEmployees(employees, path);

        IO.print("Enter salary: ");
        double salary = sc.nextDouble();
        IO.println(String.format("Email of people whose salary is more than %.2f:", salary));
        List<Employee> filterSalary = employees.stream()
                        .filter(e -> e.getSalary() >= salary)
                        .sorted((e1, e2) -> e1.getEmail().toLowerCase().compareTo(e2.getEmail().toLowerCase()))
                        .toList();
        filterSalary.forEach(x -> IO.println(x.getEmail()));

        char filter = 'M';
        double sum = sumSalaryFilter(employees, x-> x.getName().toUpperCase().charAt(0) == filter);

        String msgFormat = String.format("Sum of salary of people whose name starts with '%s': %.2f", filter, sum);
        IO.println(msgFormat);

        sc.close();
    }

    private void addEmployees(Set<Employee> employees, String path){
        try(BufferedReader br = new BufferedReader(new FileReader(path))){

            String line;
            while((line = br.readLine()) != null) {

                String[] fields = line.split(",");
                String name = fields[0];
                String email = fields[1];
                double price = Double.parseDouble(fields[2]);
                employees.add(new Employee(name, email, price));
            }
        } catch (IOException e) {
            IO.println("Error: " + e.getMessage());
        }
    }

    private double sumSalaryFilter(Set<Employee> employees, Predicate<Employee> filterPredicate){
        return employees.stream()
                .filter(filterPredicate)
                .map(Employee::getSalary)
                .reduce(0.0, Double::sum);
    }


}
