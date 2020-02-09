$(document).ready(function(){
    $('#Modal button[type="submit"]').on('click', function(e) {
        e.preventDefault();
        $(this).prop('disabled', true);

        name = $('#Modal input[name="name"]').val();
        email_or_phone = $('#Modal input[name="email_or_phone"]').val();
        text = $('#Modal textarea[name="text"]').val();
        csrf_token = $('#Modal input[name="csrfmiddlewaretoken"]').val();
        recaptcha = $('#Modal [name="g-recaptcha-response"]').val();

        data = {
            'csrfmiddlewaretoken': csrf_token,
            'g-recaptcha-response': recaptcha,
            name: name,
            email_or_phone: email_or_phone,
            text: text,
        }

        $.ajax({
        	type: 'POST',
        	url: $('#Modal form').attr('action'),
        	data: data,
            success: function(data) {
                if (data.status) {
                    $('#Modal .modal-success').removeClass('d-none');
                    $('#Modal .modal-success').addClass('d-flex');
                } else {
                    $('#Modal .alert-danger').removeClass('d-none');
                }
        	}
        });
    });

    $('#CallBackModal button[type="submit"]').on('click', function(e) {
        e.preventDefault();
        $(this).prop('disabled', true);

        phone = $('#CallBackModal input[name="phone"]').val();
        csrf_token = $('#CallBackModal input[name="csrfmiddlewaretoken"]').val();

        data = {
            'csrfmiddlewaretoken': csrf_token,
            phone: phone,
        }

        $.ajax({
        	type: 'POST',
        	url: $('#CallBackModal form').attr('action'),
        	data: data,
            success: function(data) {
                if (data.status) {
                    $('#CallBackModal .modal-success').removeClass('d-none');
                    $('#CallBackModal .modal-success').addClass('d-flex');
                } else {
                    $('#CallBackModal .alert-danger').removeClass('d-none');
                }
        	}
        });
    });

    $('button.service-btn').on('click', function(e) {
        e.preventDefault();
        $(this).prop('disabled', true);
        
        order_form = $(this).parents('form');

        data = {};

        order_form.find('input, textarea, select').each(function() {
            data[this.name] = $(this).val();
        });

        data['service'] = $(this).attr('id');

        $.ajax({
        	type: 'POST',
        	url: order_form.attr('action'),
        	data: data,
            success: function(data) {
                if (data.status) {
                    order_form.siblings('.modal-success').removeClass('d-none');
                    order_form.siblings('.modal-success').addClass('d-flex');
                } else {
                    order_form.siblings('.alert-danger').removeClass('d-none');
                }
        	}
        });
    });
});