import { useForm } from '../../hooks';
import './LoginPage.css';


const registerFormFields = {
    registerName: '',
    registerEmail: '',
    registerCedula: '',
    registerPassword: '',
    registerPassword2: '',
  
  }
export const RegisterPage = () => {

    const { registerName, registerEmail, registerCedula, registerPassword, registerPassword2, onInputChange: onRegisterInputChange } = useForm( registerFormFields )

    const registerSubmit = (event) => {
        event.preventDefault();
        console.log({ registerName, registerEmail, registerCedula, registerPassword, registerPassword2 });
    }

    return (
        <div className='body-login text-center'>
            <div className='form-signin w-100 m-auto'>
                <img src="" alt="" />
                <div className='icon'>
                    <i className="fa-sharp fa-solid fa-person"></i>
                </div>
                <h1 className='h3 mb-3 fw-normal'>Registrarse</h1>
                <form onSubmit={ registerSubmit }>
                    <div className='form-floating'>
                        <input
                            type="text"
                            className='form-control'
                            placeholder='Name'
                            name='registerName'
                            value={ registerName }
                            onChange={ onRegisterInputChange }
                        />
                        <label htmlFor="floatingInput">Nombre</label>
                    </div>
                    <div className='form-floating'>
                        <input
                            type="email"
                            className='form-control'
                            placeholder='Email Address'
                            name='registerEmail'
                            value={ registerEmail }
                            onChange={ onRegisterInputChange }
                        />
                        <label htmlFor="floatingInput">Correo</label>
                    </div>  
                    <div className='form-floating'>
                        <input
                            type="text"
                            className='form-control'
                            placeholder='Cedula'
                            name='registerCedula'
                            value={ registerCedula }
                            onChange={ onRegisterInputChange }
                        />
                        <label htmlFor="floatingInput">Cedula</label>
                    </div>
                    <div className="form-floating">
                        <input
                            type="password"
                            className="form-control"
                            placeholder='Password'
                            name='registerPassword'
                            value={ registerPassword }
                            onChange={ onRegisterInputChange }
                        />
                        <label htmlFor="floatingPassword">Contraseña</label>
                    </div>
                    <div className="form-floating">
                        <input
                            type="password"
                            className="form-control"
                            placeholder='Password'
                            name='registerPassword2'
                            value={ registerPassword2 }
                            onChange={ onRegisterInputChange }
                        />
                        <label htmlFor="floatingPassword">Confirmar contraseña</label>
                    </div>
                    
                    <button className="w-100 btn btn-lg btn-primary" type="submit">Registrarse</button>
                </form>
            </div>
        </div>
    )
}
