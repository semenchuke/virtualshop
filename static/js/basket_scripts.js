window.onload = function () {
    $('.basketitem').on('click', 'input[type="number"]', function () {
        var inputObject = event.target;

        $.ajax({
            url: "/basket/edit/" + inputObject.name + "/" + inputObject.value + "/",

            success: function (data) {
                $('.basketitem').html(data.result);
            },
        });

        event.preventDefault();
    });
}