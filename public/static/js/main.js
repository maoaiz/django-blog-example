// Avoid `console` errors in browsers that lack a console.
if (!(window.console && console.log)) {
    (function() {
        var noop = function() {};
        var methods = ['assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error', 'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log', 'markTimeline', 'profile', 'profileEnd', 'markTimeline', 'table', 'time', 'timeEnd', 'timeStamp', 'trace', 'warn'];
        var length = methods.length;
        var console = window.console = {};
        while (length--) {
            console[methods[length]] = noop;
        }
    }());
}

// Place any jQuery/helper plugins in here.

function main () {
    $("a.btn-delete").on("click", function (e) {
        e.preventDefault();
        e.stopPropagation();
        if ( confirm("Seguro que quiere eliminar?") ){
            top.location = $(this).attr("href");
        }
    });
}


function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });
    return vars;
}

function setAlert(tittle, message, type){
    var l = message.length;
    var t=0;
    if (l===0) t=0;
    else if (l<=50)  t=3000;
    else if (l<=100) t=5000;
    else if (l<=200) t=6000;
    else if (l> 200) t=7000;
    $(type+" h4").html(tittle);
    $(type+" p").html(message);
    $(type).fadeIn().delay(t).fadeOut(1500);
}
function setAlertError(t, m){
    setAlert(t, m, '#alert-error');
}
function setAlertMessage(t, m){
    setAlert(t, m, '#alert-message');
}
function sendAjax(url, params, load_elem, myCallback){
    // $(load_elem).show().html('<img src="/static/img/load16.gif" />');
    $("#ac-load").fadeIn().html('<img src="/static/img/load.gif" />');
    $.get(url, params, function(data,error) {
            myCallback(data,error);
            // $(load_elem).hide();
            $("#ac-load").fadeOut();
        }
    );
}
function setDataTables(id_table){
	var oTable = $(id_table).dataTable( {
		"oLanguage": {
			"sLengthMenu": "Mostrar _MENU_ registros",
			"sZeroRecords": "No hay datos para mostrar",
			"sInfo": "Mostrando _START_ a _END_ de _TOTAL_ registros",
			"sInfoEmpty": "Mostrando 0 a 0 de 0 registros",
			"sInfoFiltered": "(filtro de _MAX_ registros en total)",
			"sSearch": "_INPUT_",
			"oPaginate": {
		        "sFirst": "Primera",
		        "sLast": "Ultima",
		        "sNext": "Siguiente",
		        "sPrevious": "Anterior"
		        	
		      }
			},
        } );
    $("#usersList_filter > label > input").attr("placeholder", "Filtrar");
}
$(document).ready(main);
