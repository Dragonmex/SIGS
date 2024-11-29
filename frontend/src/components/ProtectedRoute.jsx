import { useNavigate } from 'react-router-dom';

const ProtectedRoute = ({ children }) => {
  const navigate = useNavigate();
  const token = localStorage.getItem('access_token'); // Verifica se o token está no localStorage

  if (!token) {
    // Se não houver token, redireciona o usuário para a página de login
    navigate('/login');
    window.location.reload();
    return null;
  }

  return children; // Se o token estiver presente, exibe o conteúdo da rota
};

export default ProtectedRoute;
