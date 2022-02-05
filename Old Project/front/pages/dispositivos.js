getData = async function() {
    $result = await Promise.resolve($.get('http://localhost:8080/devices'));

    $('#sensores').text('');
    $('#alertas').text('');

    $result.forEach(item => {
        let id = item.id;
        let humidity = item.humidity;
        let temperature = item.temperature;
        let luminosity = item.luminosity;

        var humidityHtml = '';
        var temperatureHtml = '';

        if (humidity < 50) {
            humidityHtml = `<div class="alerta alerta-humidity">
            <div class="warning">ALERTA!</div>
            <img class="alerta-humidity" src="../images/humidity.png">Umidade crítica no sensor #${id}
        </div>`

            $('#alertas').append(humidityHtml);
        }

        if (temperature < 10) {
            temperatureHtml = `<div class="alerta alerta-temperature">
            <div class="warning">ALERTA!</div>
            <img class="alerta-humidity" src="../images/temperature.png">Temperatura crítica no sensor #${id}
        </div>`

        $('#alertas').append(temperatureHtml);
        }

        let html = `<div class="grey-content sensor">
        <div class="img-container">
            <img class="img-sensor" src="../images/sensor.png">
    
            <div class="sensor-id">#${id}</div>
        </div>
    
        <div class="sensor-data">
            <div class="sensor-data-row">
                <div class="sensor-info sensor-info-humidity">
                    <img src="../images/humidity.png"><div id="humidity-value" class="sensor-info-value">${humidity}%</div>
                </div>
    
                <div class="sensor-info sensor-info-temperature">
                    <img src="../images/temperature.png"><div id="temperature-value" class="sensor-info-value">${temperature} °C</div>
                </div>
            </div>
            <div class="sensor-data-row">
                <div class="sensor-info sensor-info-luminosity">
                    <img src="../images/luminosity.png"><div id="luminosity-value" class="sensor-info-value">${luminosity}lx</div>
                </div>
    
                <div class="sensor-info sensor-info-timer">
                    <img src="../images/timer.png"><div id="timer-value" class="sensor-info-value">01:48:35</div>
                </div>
            </div>
        </div>
    </div>`;

    $('#sensores').append(html);
    });

    setTimeout(() => {
        $('#alertas').text('');
    }, 2000);
}

getData();

setInterval(() => {
    getData();
}, 5000);


