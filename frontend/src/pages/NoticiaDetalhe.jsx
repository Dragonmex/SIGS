import React, { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom"; // Adicionado Link para navegação
import { fetchNoticiaDetail } from "../services/api"; // Função de API que busca os detalhes da notícia
import "../pages/NoticiaDetalhe.css"; // Estilos para o componente

const NoticiaDetalhe = () => {
  const { id } = useParams(); // Obtém o ID da notícia da URL
  const [noticia, setNoticia] = useState(null); // Estado para armazenar os dados da notícia
  const [error, setError] = useState(""); // Estado para mensagens de erro
  const [loading, setLoading] = useState(true); // Estado para o carregamento

  useEffect(() => {
    // Busca os detalhes da notícia ao carregar o componente
    const loadNoticia = async () => {
      setLoading(true);
      try {
        const data = await fetchNoticiaDetail(id);
        setNoticia(data);
        setError(""); // Limpa qualquer erro anterior
      } catch (err) {
        console.error("Erro ao carregar os detalhes da notícia:", err);
        setError("Erro ao carregar os detalhes. Tente novamente mais tarde.");
      } finally {
        setLoading(false);
      }
    };

    loadNoticia();
  }, [id]);

  if (loading) {
    return <p>Carregando...</p>;
  }

  if (error) {
    return <p className="error-message">{error}</p>;
  }

  return (
    <div className="noticia-detalhe-container">
      {/* Título e informações principais */}
      <h1>{noticia.titulo}</h1>
      <small>{new Date(noticia.data_publicacao).toLocaleDateString()}</small>
      {noticia.imagem && (
        <img
          src={noticia.imagem}
          alt={noticia.titulo}
          className="noticia-imagem-detalhe"
        />
      )}
      <p>{noticia.conteudo}</p>
      <small>Autor: {noticia.autor}</small>

      {/* Seção de notícias relacionadas */}
      <h3>Notícias Relacionadas</h3>
      <div className="noticias-relacionadas">
        {noticia.noticias_relacionadas && noticia.noticias_relacionadas.length > 0 ? (
          noticia.noticias_relacionadas.map((relacionada) => (
            <div key={relacionada.id} className="relacionada-card">
              <h4>{relacionada.titulo}</h4>
              <p>{relacionada.resumo}</p>
              <small>
                Publicado em:{" "}
                {new Date(relacionada.data_publicacao).toLocaleDateString()}
              </small>
              {/* Link para os detalhes da notícia relacionada */}
              <Link to={`/noticia/${relacionada.id}`} className="btn-relacionada">
                Ver mais
              </Link>
            </div>
          ))
        ) : (
          <p>Não há notícias relacionadas.</p>
        )}
      </div>
    </div>
  );
};

export default NoticiaDetalhe;
