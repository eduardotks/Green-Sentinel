package com.greensentinel.greensentinelapi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.transaction.annotation.EnableTransactionManagement;

@SpringBootApplication
@Configuration
@EnableJpaRepositories
@EnableTransactionManagement
public class GreensentinelApiApplication {

    public static void main(String[] args) {
        SpringApplication.run(GreensentinelApiApplication.class, args);
    }

}
