$(document).ready(function () {
    setInterval(() => {
        $('.humidity').each(function(){
            $(this).text(Math.floor(Math.random() * (100 - 5 + 1) + 5) + '%');
        });

        $('.temperature').each(function(){
            $(this).text(Math.floor(Math.random() * (50 - 10 + 1) + 10) + '°C');
        });

        $('.luminosity').each(function(){
            $(this).text(Math.floor(Math.random() * (100 - 20 + 1) + 20) + 'lx');
        });
    }, 5000);

	$("#connectSensor").click(function () {
		$humidity = Math.floor(Math.random() * (100 - 5 + 1) + 5);
		$temperature = Math.floor(Math.random() * (50 - 10 + 1) + 10);
		$luminosity = Math.floor(Math.random() * (100 - 20 + 1) + 20);

        $selectedSensor = $("#selectSensor").find(":selected");

        if ($selectedSensor.val() !== '-1') {
            $tr =
			'<tr><td>' +
			$("#selectSensor").find(":selected").text() +
			'</td><td class="humidity">' +
			$humidity +
			'%</td><td class="temperature">' +
			$temperature +
			'°C</td><td class="luminosity">' +
			$luminosity +
			'lx</td></tr>';

		$("#tableSensores").append($tr);

		$("#selectSensor").find(":selected").remove();
        }
	});
});
