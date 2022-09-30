import { useAuthStore, useForm } from '../../hooks';
import './LoginPage.css';

const loginFormFields = {
  loginEmail: '',
  loginPassword: '',
}

const registerFormFields = {
  registerName: '',
  registerEmail: '',
  registerCedula: '',
  registerPassword: '',
  registerPassword2: '',

}

export const LoginPage = () => {

  const { startLogin } = useAuthStore();

  const { loginEmail, loginPassword, onInputChange: onLoginInputChange } = useForm(loginFormFields);

  const loginSubmit = (event) => {
    event.preventDefault();
    startLogin({ email: loginEmail, password: loginPassword });
    startLogin()
  }

  return (
    <div className='body-login text-center'>
      <div className='form-signin w-100 m-auto'>
        <img src="" alt="" />
        <div className='icon'>
          <i className="fa-sharp fa-solid fa-person"></i>
        </div>
        <h1 className='h3 mb-3 fw-normal'>Inicia Sesión</h1>
        <form onSubmit={ loginSubmit }>
          <div className='form-floating'>
            <input
              type="email"
              className='form-control'
              id="floatingInput"
              placeholder='Email Address'
              name="loginEmail"
              value={loginEmail}
              onChange={onLoginInputChange}
            />
            <label htmlFor="floatingInput">Email Address</label>
          </div>
          <div className="form-floating">
            <input
              type="password"
              className="form-control"
              id="floatingPassword"
              placeholder='Password'
              name="loginPassword"
              value={loginPassword}
              onChange={onLoginInputChange}
            />
            <label htmlFor="floatingPassword">Password</label>
          </div>
          <button className="w-100 btn btn-lg btn-primary" type="submit">Ingresar</button>
        </form>
      </div>
    </div>
  )
}