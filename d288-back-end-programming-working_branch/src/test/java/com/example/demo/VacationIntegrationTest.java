package com.example.demo;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.http.ResponseEntity;
import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class VacationIntegrationTest {

    @Autowired
    private TestRestTemplate restTemplate;

    @Test
    public void testGetVacations() {
        // Replace "/api/vacations" with the correct path to your vacations API endpoint
        ResponseEntity<String> response = restTemplate.getForEntity("/api/vacations", String.class);

        // Check that the HTTP status is 200 (OK)
        assertThat(response.getStatusCodeValue()).isEqualTo(200);

        // Optionally: Check if response body contains specific expected content
        // assertThat(response.getBody()).contains("expectedText");
    }
}