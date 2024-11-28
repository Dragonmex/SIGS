import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000', // Altere para o URL do seu back-end
});

// Função de Login
export const login = async (email, password) => {
  try {
    const response = await api.post('/api/login/', { email, password });
    const { access_token, refresh_token } = response.data;

    // Armazenar os tokens no localStorage
    localStorage.setItem('access_token', access_token);
    localStorage.setItem('refresh_token', refresh_token);

    return response.data;
  } catch (error) {
    console.error('Login error:', error);
    throw error;
  }
};

// Função de Cadastro
export const register = async (email, password, perfil) => {
  try {
    const response = await api.post('/api/register/', { email, password, perfil });
    return response.data;
  } catch (error) {
    console.error('Registration error:', error);
    throw error;
  }
};
