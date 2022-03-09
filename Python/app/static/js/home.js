$(document).ready(function(){
    $('#connectSensor').click(function(){
        $teste = '<div>' + $('#selectSensor').val() + '</div>';
        $('#listaSensores').append($teste);
    });
});