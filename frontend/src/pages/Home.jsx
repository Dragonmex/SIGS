import React, { useEffect, useState } from "react";
import { fetchHomeData } from "../services/api";
import "../pages/Home.css";

const Home = () => {
  const [servicos, setServicos] = useState([]);
  const [noticias, setNoticias] = useState([]);
  const [categoriasNoticias, setCategoriasNoticias] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchHomeData()
      .then((data) => {
        setServicos(data.servicos);
        setNoticias(data.noticias);
        setCategoriasNoticias(data.categorias_noticias);
      })
      .catch((err) => {
        setError("Erro ao carregar os dados. Tente novamente mais tarde.");
        console.error(err);
      });
  }, []);

  return (
    <div className="home-container">
      {/* Seção de Serviços */}
      <section className="section servicos">
        <h2>O que a prefeitura pode fazer por você hoje?</h2>
        <div className="search-bar">
          <input
            type="text"
            placeholder="Busque por serviços ou palavra-chave..."
          />
        </div>
        {error && <p className="error-message">{error}</p>}
        <div className="grid-container">
          {servicos.map((servico) => (
            <div key={servico.id} className="card">
              <div className="card-icon">
                <img src={servico.icone || "/placeholder-icon.png"} alt="" />
              </div>
              <div className="card-content">
                <h3>{servico.nome}</h3>
                <p>{servico.descricao}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Seção de Notícias */}
      <section className="section noticias">
        <h2>Últimas Notícias</h2>
        <p className="subtitulo">Assuntos mais buscados</p>
        <div className="categorias-container">
          {categoriasNoticias.map((categoria) => (
            <button key={categoria.id} className="categoria-btn">
              {categoria.nome}
            </button>
          ))}
        </div>
        <div className="grid-container noticias-grid">
          {noticias.map((noticia, index) => (
            <div key={index} className="noticia-card">
              <div className="noticia-imagem">
                <img
                  src={noticia.imagem || "/placeholder-news.jpg"}
                  alt={noticia.titulo}
                />
              </div>
              <div className="noticia-conteudo">
                <h3>{noticia.titulo}</h3>
                <p>{noticia.resumo}</p>
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};

export default Home;
