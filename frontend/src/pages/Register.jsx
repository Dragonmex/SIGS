import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "../pages/Register.css";

const Register = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [perfil, setPerfil] = useState("cidadao");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const [cpf, setCpf] = useState("");

  const handleSubmit = async (e) => {
  e.preventDefault();
  setError("");
  try {
    const response = await axios.post("http://127.0.0.1:8000/api/register/", {
      email,
      password,
      perfil,
      cpf: cpf || null, // Envia null caso o CPF esteja vazio
    });

    if (response.status === 201) {
      navigate("/login");
    } else {
      setError("Erro ao registrar. Tente novamente.");
    }
  } catch (err) {
    setError("Erro ao registrar. Tente novamente.");
  }
};

  return (
    <div className="register-container">
      <div className="register-card">
        <h2>Cadastro</h2>
        {error && <div className="alert alert-danger">{error}</div>}
        <form onSubmit={handleSubmit}>
          <input
            type="email"
            className="input-field"
            placeholder="Digite seu e-mail"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <input
            type="password"
            className="input-field"
            placeholder="Digite sua senha"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <select
            className="input-field"
            value={perfil}
            onChange={(e) => setPerfil(e.target.value)}
            required
          >
            <option value="cidadao">Cidadão</option>
            <option value="servidor">Servidor</option>
          </select>
          <button type="submit" className="btn-register">Cadastrar</button>
        </form>
        <div className="login-link">
          <p>
            Já tem uma conta?{" "}
            <a href="/login" className="btn-create">
              Faça login
            </a>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Register;
