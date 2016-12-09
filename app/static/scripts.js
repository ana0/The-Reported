$("#police_dept").click(function() {
    var police_dept_id = $(this).find(":selected").val();
    if (police_dept_id != 'u') {
        var request = $.ajax({
            type: 'GET',
            url: '/models/' + police_dept_id,
        });
        request.done(function(data){
            console.log(data)
            // var option_list = [["", "--- Select One ---"]].concat(data);

            // $("#model_select").empty();
            // for (var i = 0; i < option_list.length; i++) {
            //     $("#model_select").append(
            //         $("<option></option>").attr(
            //             "value", option_list[i][0]).text(option_list[i][1])
            //     );
            // }
        });
    }
});