package com.greensentinel.greensentinelapi.model.repository;

import com.greensentinel.greensentinelapi.model.Device;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;

import java.util.Date;
import java.util.List;

public interface DeviceRepository extends JpaRepository<Device, Long> {

   List<Device> findAll();

   @Modifying
   @Query("update Device device set device.temperature = ?2," +
           " device.humidity = ?3, device.luminosity = ?4, device.date = CURRENT_TIMESTAMP  where device.id = ?1")
   void saveDevice(Long id, Integer temperature, Integer humidity, Integer luminosity );
}