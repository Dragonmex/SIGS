import React, { createContext, useState, useEffect } from "react";
import { refreshAccessToken } from "../services/api"; // Para renovar o token

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const checkAuth = async () => {
      const token = localStorage.getItem("accessToken");
      if (token) {
        try {
          // Renova o token se necessário
          await refreshAccessToken();
          setIsAuthenticated(true);
        } catch (error) {
          console.error("Sessão expirada:", error);
          logout();
        }
      }
    };

    checkAuth();
  }, []);

  const login = (accessToken, refreshToken) => {
    localStorage.setItem("accessToken", accessToken);
    localStorage.setItem("refreshToken", refreshToken);
    setIsAuthenticated(true); // Marca como autenticado
  };

  const logout = () => {
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
    setIsAuthenticated(false); // Marca como não autenticado
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
