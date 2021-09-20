$(document).ready(function (){
        $("#form").submit(function (e){
            e.preventDefault();
            $.ajax({
            type:'POST',
            url:'signup',
            data:$("#form").serialize(),
            dataType:'json',
            success:function (res){
                if(res.msg == 'not-code'){
                    $('#sms-code').removeClass('hidden');
                    $('#sms-code').addClass('show');
                    $('#submit').html('ثبت عضویت')
                    }
                else {
                    if(res.ok == 'true'){
                        if ($('#error').length){
                        $("#error").remove();
                        $("#success").html(res.msg);
                        $("#success").removeClass('hidden');
                        $("#success").addClass('show');
                        }
                        else{
                        $("#success").html(res.msg);
                        $("#success").removeClass('hidden');
                        $("#success").addClass('show');
                        }

                    }
                    else {
                        if($('#success').length){
                        $("#success").remove();
                        $("#error").html(res.msg);
                        $("#error").removeClass('hidden');
                        $("#error").addClass('show');
                        }
                        else{
                         $("#error").html(res.msg);
                        $("#error").removeClass('hidden');
                        $("#error").addClass('show');
                        }
                    }
                }
                },
            error:function (){
                    $("#error").html(res.msg);
                    $("#error").removeClass('hidden');
                    $("#error").addClass('show');
                    // alert('ridi');
                }
            })
        })

        $("#loginform").submit(function (e){
            e.preventDefault();
            $.ajax({
            type:'POST',
            url:'login',
            data:$("#loginform").serialize(),
            dataType:'json',
            success:function (res){
                if(res.msg == 'not-code'){
                    $('#sms-code').removeClass('hidden');
                    $('#sms-code').addClass('show');
                    $('#submit').html('وارد شوید')
                    }
                else {
                    if(res.ok == 'true'){
                        if ($('#error').length){
                        $("#error").remove();
                        $("#success").html(res.msg);
                        $("#success").removeClass('hidden');
                        $("#success").addClass('show');
                        }
                        else{
                        $("#success").html(res.msg);
                        $("#success").removeClass('hidden');
                        $("#success").addClass('show');
                        }

                    }
                    else {
                        if($('#success').length){
                        $("#success").remove();
                        $("#error").html(res.msg);
                        $("#error").removeClass('hidden');
                        $("#error").addClass('show');
                        }
                        else{
                         $("#error").html(res.msg);
                        $("#error").removeClass('hidden');
                        $("#error").addClass('show');
                        }
                    }
                }
                },
            error:function (){
                    $("#error").html(res.msg);
                    $("#error").removeClass('hidden');
                    $("#error").addClass('show');
                }
            })
        })
    })

