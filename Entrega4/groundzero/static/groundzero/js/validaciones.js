            $(function() 
            {
              $("#mi-formulario").validate({
                   rules: {
                        numero_identificaion: "required",
                        nombre_completo: "required",
                        telefono: "required",
                        direccion: "required",
                        email: {
                            required: true,
                            email: true
                        },
                        contraseña: "required",
                        moneda: "required",
                          
                      }, //rules
                  messages: {
                    numero_identificaion: {
                        required: 'Ingrese su numero',
                    },  
                    nombre_completo: {
                        required: 'Ingrese su nombre completo',
                    },
                    telefono:{
                        required: 'Ingrese su numero de telefono'
                    },
                    direccion:{
                        required: 'Ingrese su direccion'
                    },
                    email: {
                        required: 'Ingresa tu correo electrónico',
                        email: 'Formato de correo no válido'
                    },
                    pais:{
                        required: 'Ingrese tu apellido',
                    },
                    contraseña:{
                        required: 'Seleccione el motivo de su contacto',
                    },
                    moneda:{
                          required: 'Indique la moneda'
                      }
                  }//messages
              }); //$('#mi-formulario').validate
          }); //function



        function dialogBox(){
            alert('Se han limpiado correctamente los cuadros.');
          }

