$(function() {
    /*var personRowTemplate = "" +
        "<tr>" +
            "<td>{{name}}</td>" +
        "</tr>"*/
    var $people_table = $('#people_table tbody');
    var $delete_person = $('#people_table tbody tr .delete-me');
    var $addPersonBtn = $('#addPersonBtn');
    function personRow(person) {
        var $elem = "<tr id='tr" + person.id +"'>";
        if (person.picture == null){
            $elem = $elem + '<td><span class="glyphicon glyphicon-user" aria-hidden="true"></span></td>';
        } else {
            $elem = $elem + '<td>' + person.picture + '</td>';
        }
        $elem = $elem + "<td>" + person.name +
        "</td><td class='delete-me' data-id='" + person.id +"' ><span class='glyphicon glyphicon-remove-circle' data-id='" + person.id +
        "' class='removePerson'></span></tr>"
        $people_table.append($elem);
    }


    $.ajax({
        type: 'GET',
        url: '/api/Person/',
        success: function(people) {
            $.each(people, function(i, person){
                personRow(person);
            });
        },
    });

    $addPersonBtn.on('click', function() {
        var addPerson = {
            name: $('#nameInput').val(),
            phone: $('#phoneInput').val(),
        };

        $.ajax({
            type: 'POST',
            url: '/api/Person/',
            data: addPerson,
            success: function(newPerson) {
                personRow(newPerson);
                $('#addPersonForm').trigger("reset");
            },
            error: function(){
                alert("error saving person");
            }
        })
    });

    $people_table.delegate('.delete-me', 'click', function() {
        var $id = $(this).attr('data-id');
        var $elem = $(this).closest('tr');
        $.ajax({
            type: 'DELETE',
            url: '/api/Person/' + $id + '/',
            success: function() {
                $("#tr" + $id).fadeOut(1000, function(){
                    $("#tr" + $id).remove();
                });
            },
            error: function(){
                alert("error deleting person");
            },
        });
     });
});