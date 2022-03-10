$(document).ready(function(){
    $('#connectSensor').click(function(){
        $teste = '<div>' + $('#selectSensor').find(':selected').text() + '</div>';
        $('#listaSensores').append($teste);

        $('#selectSensor').find(':selected').remove();
    });
});