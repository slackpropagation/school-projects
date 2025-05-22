package com.example.demo.bootstrap;

import com.example.demo.domain.InhousePart;
import com.example.demo.domain.OutsourcedPart;
import com.example.demo.repositories.InhousePartRepository;
import com.example.demo.repositories.OutsourcedPartRepository;
import com.example.demo.repositories.PartRepository;
import com.example.demo.repositories.ProductRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;
import com.example.demo.domain.Product;

@Component
public class BootStrapData implements CommandLineRunner {

    private final PartRepository partRepo;
    private final ProductRepository productRepo;
    private final InhousePartRepository inhouseRepo;
    private final OutsourcedPartRepository outsourcedRepo;

    public BootStrapData(PartRepository partRepo, ProductRepository productRepo,
                         InhousePartRepository inhouseRepo, OutsourcedPartRepository outsourcedRepo) {
        this.partRepo = partRepo;
        this.productRepo = productRepo;
        this.inhouseRepo = inhouseRepo;
        this.outsourcedRepo = outsourcedRepo;
    }

    @Override
    public void run(String... args) {

        // In-house parts
        InhousePart neck = createInhousePart("Roasted Maple Neck", 229.00, 5);
        InhousePart tuners = createInhousePart("Locking Tuners", 99.00, 10);
        InhousePart pots = createInhousePart("CTS 500k Pots", 14.00, 20);
        InhousePart toggleSwitch = createInhousePart("3-Way Toggle Switch", 12.00, 15);
        InhousePart strapLocks = createInhousePart("Strap Locks", 24.99, 12);

        // Outsourced parts
        OutsourcedPart clothWiring = createOutsourcedPart(10, "Vintage Cloth Wiring", 9.99, 10, "ToneTech");
        OutsourcedPart graphTechNut = createOutsourcedPart(11, "GraphTech Nut", 18.50, 8, "GraphTech");
        OutsourcedPart knurledKnobs = createOutsourcedPart(12, "Custom Knurled Knobs", 11.99, 15, "MetalWorks");
        OutsourcedPart pickupCovers = createOutsourcedPart(13, "Gold Pickup Covers", 29.99, 10, "ShinyTone");
        OutsourcedPart tremoloBridge = createOutsourcedPart(14, "Nickel Tremolo Bridge", 89.99, 6, "SmoothPlay Hardware");

        if (partRepo.count() == 0) {
            partRepo.save(neck);
            partRepo.save(tuners);
            partRepo.save(pots);
            partRepo.save(toggleSwitch);
            partRepo.save(strapLocks);
            partRepo.save(clothWiring);
            partRepo.save(graphTechNut);
            partRepo.save(knurledKnobs);
            partRepo.save(pickupCovers);
            partRepo.save(tremoloBridge);
        }

        if (productRepo.count() == 0) {
            productRepo.save(new Product("Axecellent Firestorm", 999.99, 10));
            productRepo.save(new Product("Axecellent Breeze", 799.99, 12));
            productRepo.save(new Product("Axecellent Thunder", 899.99, 8));
            productRepo.save(new Product("Axecellent Flame", 299.99, 15));
            productRepo.save(new Product("Axecellent Waves", 149.99, 20));
        }

    }

    private InhousePart createInhousePart(String name, double price, int inventory) {
        InhousePart part = new InhousePart();
        part.setName(name);
        part.setPrice(price);
        part.setInv(inventory);
        part.setMinInventory(1);
        part.setMaxInventory(100);
        return part;
    }

    private OutsourcedPart createOutsourcedPart(int id, String name, double price, int inventory, String company) {
        OutsourcedPart part = new OutsourcedPart();
        part.setId(id);
        part.setName(name);
        part.setPrice(price);
        part.setInv(inventory);
        part.setCompanyName(company);
        part.setMinInventory(1);
        part.setMaxInventory(100);
        return part;
    }
}