import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import { useContext } from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import { AuthContext } from "./context/AuthContext";

function App() {
  const { isAuthenticated } = useContext(AuthContext);

  return (
    <Router>
      {/* Header fixo */}
      <Header />

      <main className="main-content">
        <Routes>
          {/* Página inicial acessível a todos */}
          <Route path="/" element={<Home />} />

          {/* Páginas de autenticação */}
          <Route path="/login" element={!isAuthenticated ? <Login /> : <Navigate to="/" />} />
          <Route path="/register" element={!isAuthenticated ? <Register /> : <Navigate to="/" />} />

          {/* Rotas protegidas */}
          <Route
            path="/dashboard"
            element={isAuthenticated ? <div>Dashboard</div> : <Navigate to="/login" />}
          />
        </Routes>
      </main>

      <Footer />
    </Router>
  );
}

export default App;
