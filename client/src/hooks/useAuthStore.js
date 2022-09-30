import { useDispatch, useSelector } from  'react-redux';
import { safeApi } from '../api';

export const useAuthStore = () => {

    const { status, user, errorMessage } = useSelector( state => state.auth );
    const dispatch = useDispatch();

    const startLogin = async({ email, password }) => {
        console.log( {email, password})

        try {
            const resp = await safeApi.post('/login', { email, password });
            console.log({ resp })

        } catch (error) {
            console.log({ error })
        }
    }

    return {
        // Propiedades
        errorMessage,
        status,
        user,

        // Métodos
        startLogin
    }
}