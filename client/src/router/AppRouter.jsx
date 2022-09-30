import { Route, Routes, Navigate } from "react-router-dom"
import { LoginPage, RegisterPage } from "../auth";
import { getEnvVariables } from "../helpers";
import { SafePage } from "../safe";


export const AppRouter = () => {

    const authStatus = 'not-authenticated';  //'authenticated'; //'not-authenticated';
    console.log(getEnvVariables())
  return (
    <Routes>
        {
            
            (authStatus == 'not-authenticated')
                ? <Route path="/auth/*" element={ <LoginPage /> }/>

                : <Route path="/*" element={ <SafePage /> }/>
        }

        <Route path="/*" element={ <Navigate to="/auth/login" /> } />
        <Route path="/register" element={ <RegisterPage /> }></Route>

    </Routes>
  )
}
