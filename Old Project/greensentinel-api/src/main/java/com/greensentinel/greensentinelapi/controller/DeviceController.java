package com.greensentinel.greensentinelapi.controller;

import com.greensentinel.greensentinelapi.service.DeviceService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;

import java.io.IOException;

@Controller
@CrossOrigin(origins = "*", allowedHeaders = "*")
public class DeviceController {

    private DeviceService deviceService;

    public DeviceController(DeviceService deviceService) {
        this.deviceService = deviceService;
    }

    @GetMapping("/devices")
    public ResponseEntity getData() {
        return new ResponseEntity(deviceService.getDevices(), HttpStatus.OK);
    }
}
