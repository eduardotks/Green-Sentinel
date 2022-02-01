package com.greensentinel.greensentinelapi.task;

import com.greensentinel.greensentinelapi.service.DeviceService;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
@EnableScheduling
public class UpdateData {

    private DeviceService deviceService;

    public UpdateData(DeviceService deviceService) {
        this.deviceService = deviceService;
    }

@Scheduled(fixedDelay = 5000)
    public void updateData() {
        deviceService.updateDevices();
    }
}
