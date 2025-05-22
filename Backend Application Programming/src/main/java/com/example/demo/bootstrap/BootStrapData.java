package com.example.demo.BootStrapData;

import com.example.demo.dao.CustomerRepository;
import com.example.demo.dao.DivisionRepository;
import com.example.demo.entities.Customer;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class BootStrapData implements CommandLineRunner {

    private final CustomerRepository customerRepository;
    private final DivisionRepository divisionRepository;

    public BootStrapData(CustomerRepository customerRepository,
                         DivisionRepository divisionRepository) {
        this.customerRepository = customerRepository;
        this.divisionRepository = divisionRepository;
    }

    @Override
    public void run(String... args) throws Exception {
        // [ firstName, lastName, phone, address, postalCode, divisionId ]
        String[][] data = {
                { "Ahmet",  "Yildirim", "(153) 646‑4650", "1 Main St", "29986", "2" },
                { "Mehmet","Karadag",   "(542) 634‑8764", "2 Elm St",  "23466", "3" },
                { "Huseyin","Topal",   "(567) 974‑8372", "3 Oak St",  "90210", "4" },
                { "Burak",   "Yilmaz",  "(282) 887‑2687", "4 Pine St", "42069", "5" },
                { "Mahmut", "Tuncer",  "(889) 920‑4764", "5 Maple St","80823", "6" }
        };

        // only insert once
        if (customerRepository.count() > 5) {
            return;
        }

        for (String[] row : data) {
            Customer c = new Customer();
            c.setFirstName(row[0]);
            c.setLastName(row[1]);
            c.setPhone(row[2]);
            c.setAddress(row[3]);
            c.setPostal_code(row[4]);                          // ← camel‑case setter
            c.setDivision(
                    divisionRepository
                            .findById(Long.parseLong(row[5]))
                            .orElseThrow(() -> new IllegalStateException("Division not found"))
            );
            customerRepository.save(c);
        }
    }
}