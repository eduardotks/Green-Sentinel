package com.greensentinel.greensentinelapi.service;

import com.greensentinel.greensentinelapi.model.Device;
import com.greensentinel.greensentinelapi.model.repository.DeviceRepository;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.List;
import java.util.Random;

@Service
public class DeviceService {
    private DeviceRepository deviceRepository;

    public DeviceService(DeviceRepository deviceRepository) {
        this.deviceRepository = deviceRepository;
    }

    public List<Device> getDevices() {
        return deviceRepository.findAll();
    }

    @Transactional
    public void updateDevices() {
        System.out.println("Atualizando dispositivos");
        Random random = new Random();
        List<Device> ds = deviceRepository.findAll();
        for (Device d : ds) {
            deviceRepository.saveDevice(d.getId(),
                    d.getTemperature() + random.ints(-3, -2)
                            .findFirst()
                            .getAsInt(),
                    d.getHumidity() + random.ints(-3, -2)
                            .findFirst()
                            .getAsInt(),
                    d.getLuminosity() + random.ints(-50, 50)
                            .findFirst()
                            .getAsInt());

        }
    }
}