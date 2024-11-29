import React, { useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

function Header() {
  const { isAuthenticated, logout } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleLogout = () => {
    logout(); // Remove os tokens do localStorage e atualiza o estado de autenticação
    navigate("/login"); // Redireciona para a página de login
  };

  return (
    <header className="bg-dark py-3">
      <div className="container d-flex justify-content-between align-items-center">
        <Link to="/" className="text-white text-decoration-none fs-4 fw-bold">
          Home
        </Link>
        <nav>
          {!isAuthenticated ? (
            <>
              <Link to="/register" className="btn btn-outline-light me-2">
                Cadastrar
              </Link>
              <Link to="/login" className="btn btn-light text-dark">
                Login
              </Link>
            </>
          ) : (
            <>
              <Link to="/profile" className="btn btn-outline-light me-2">
                Meu Perfil
              </Link>
              <button className="btn btn-light text-dark" onClick={handleLogout}>
                Logout
              </button>
            </>
          )}
        </nav>
      </div>
    </header>
  );
}

export default Header;
