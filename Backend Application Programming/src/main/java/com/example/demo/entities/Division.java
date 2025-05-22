package com.example.demo.entities;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import java.util.Date;
import java.util.HashSet;
import java.util.Set;

@Entity
@Table(name = "divisions")
@Getter
@Setter
public class Division {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "division_id")
    private Long id;

    // matches your "division" column
    @Column(name = "division", nullable = false)
    private String division;

    @CreationTimestamp
    @Column(name = "create_date", nullable = false, updatable = false)
    private Date createDate;

    @UpdateTimestamp
    @Column(name = "last_update", nullable = false)
    private Date lastUpdate;

    // foreign key column
    @Column(name = "country_id", nullable = false)
    private Long countryId;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "country_id", insertable = false, updatable = false)
    private Country country;

    @OneToMany(mappedBy = "division", cascade = CascadeType.ALL)
    private Set<Customer> customers = new HashSet<>();
}