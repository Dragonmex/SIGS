import axios from "axios";

// Configuração inicial do Axios
const api = axios.create({
  baseURL: "http://127.0.0.1:8000", // Altere para o URL do seu backend
});

// Interceptador para adicionar o token em todas as requisições
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("accessToken");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Função de Login
export const login = async (email, password) => {
  try {
    const response = await api.post("/api/token/", { email, password }); // Endpoint do JWT
    const { access, refresh } = response.data;

    // Armazenar os tokens no localStorage
    localStorage.setItem("accessToken", access);
    localStorage.setItem("refreshToken", refresh);

    return response.data;
  } catch (error) {
    console.error("Erro ao fazer login:", error);
    throw new Error("Falha no login. Verifique suas credenciais.");
  }
};

// Função de Logout
export const logout = () => {
  localStorage.removeItem("accessToken");
  localStorage.removeItem("refreshToken");
};

// Função para renovar o token
export const refreshAccessToken = async () => {
  const refreshToken = localStorage.getItem("refreshToken");
  if (!refreshToken) {
    throw new Error("Token de atualização não encontrado. Faça login novamente.");
  }

  try {
    const response = await api.post("/api/token/refresh/", { refresh: refreshToken });
    const { access } = response.data;

    // Atualizar o access token no localStorage
    localStorage.setItem("accessToken", access);

    return access;
  } catch (error) {
    console.error("Erro ao renovar o token:", error);
    throw new Error("Não foi possível renovar o token. Faça login novamente.");
  }
};

// Função para buscar dados da Home
export const fetchHomeData = async () => {
  try {
    const response = await api.get("/api/home/");
    return response.data;
  } catch (error) {
    console.error("Erro ao buscar os dados da home:", error);

    if (error.response && error.response.status === 401) {
      throw new Error("Acesso não autorizado. Faça login novamente.");
    }

    throw new Error("Não foi possível carregar os dados da home.");
  }
};

// Função para buscar detalhes de uma notícia
export const fetchNoticiaDetail = async (id) => {
  try {
    const response = await api.get(`/api/noticia/${id}/`);
    return response.data;
  } catch (error) {
    console.error(`Erro ao buscar os detalhes da notícia ID ${id}:`, error);

    if (error.response && error.response.status === 401) {
      throw new Error("Acesso não autorizado. Faça login novamente.");
    }

    throw new Error("Erro ao carregar os detalhes da notícia.");
  }
};
