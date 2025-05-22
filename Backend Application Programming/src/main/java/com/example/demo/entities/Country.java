package com.example.demo.entities;

import jakarta.persistence.*;
import lombok.*;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import java.util.Date;
import java.util.HashSet;
import java.util.Set;

@Entity
@Table(name = "countries")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Country {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "country_id")
    private Long id;

    // matches your `country` column
    @Column(name = "country", nullable = false)
    private String country_name;

    @CreationTimestamp
    @Column(name = "create_date", nullable = false, updatable = false)
    private Date create_date;

    @UpdateTimestamp
    @Column(name = "last_update", nullable = false)
    private Date last_update;

    @OneToMany(mappedBy = "country", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private Set<Division> divisions = new HashSet<>();
}