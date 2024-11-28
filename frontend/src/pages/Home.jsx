import React, { useState, useEffect } from "react";
import { fetchHomeData } from "../services/api";
import "../pages/Home.css";

const Home = () => {
  // Estados para Serviços
  const [servicos, setServicos] = useState([]);
  const [filteredServicos, setFilteredServicos] = useState([]);
  const [search, setSearch] = useState("");

  // Estados para Notícias
  const [noticias, setNoticias] = useState([]);
  const [filteredNoticias, setFilteredNoticias] = useState([]);
  const [categorias, setCategorias] = useState([]);
  const [selectedCategoria, setSelectedCategoria] = useState("Todas");

  const [error, setError] = useState("");

  // Busca dados do backend
  useEffect(() => {
    fetchHomeData()
      .then((data) => {
        // Configuração dos serviços
        setServicos(data.servicos);
        setFilteredServicos(data.servicos);

        // Configuração das notícias
        setNoticias(data.noticias);
        setFilteredNoticias(data.noticias);

        // Configuração das categorias de notícias
        setCategorias(data.categorias_noticias);
      })
      .catch((err) => {
        console.error("Erro ao carregar os dados:", err);
        setError("Erro ao carregar os dados. Tente novamente mais tarde.");
      });
  }, []);

  // Lógica para filtro de serviços
  const handleSearch = (e) => {
    const query = e.target.value.toLowerCase();
    setSearch(query);

    const filtered = servicos.filter(
      (servico) =>
        servico.nome.toLowerCase().includes(query) ||
        servico.descricao.toLowerCase().includes(query)
    );
    setFilteredServicos(filtered);
  };

  // Lógica para filtro de notícias por categoria
  const handleCategoriaClick = (categoriaNome) => {
    setSelectedCategoria(categoriaNome);

    if (categoriaNome === "Todas") {
      setFilteredNoticias(noticias); // Mostra todas as notícias
    } else {
      const filtered = noticias.filter(
        (noticia) => noticia.categoria === categoriaNome
      );
      setFilteredNoticias(filtered); // Mostra apenas as notícias da categoria selecionada
    }
  };

  return (
    <div className="home-container">
      {/* Sessão de Serviços */}
      <section className="section">
        <div className="search-bar">
          <input
            type="text"
            placeholder="Busque por serviços ou palavra-chave..."
            value={search}
            onChange={handleSearch}
          />
        </div>

        <h2>O que a prefeitura pode fazer por você hoje?</h2>
        {error && <p className="error-message">{error}</p>}

        <div className="cards-container">
          {filteredServicos.length > 0 ? (
            filteredServicos.map((servico) => (
              <div key={servico.id} className="card">
                <div className="card-icon">
                  <img src={servico.icone || "/placeholder-icon.png"} alt="" />
                </div>
                <div className="card-content">
                  <h3>{servico.nome}</h3>
                  <p>{servico.descricao}</p>
                </div>
              </div>
            ))
          ) : (
            <p>Nenhum serviço encontrado para a pesquisa: "{search}"</p>
          )}
        </div>
      </section>

      {/* Sessão de Notícias */}
      <section className="section">
        <h2>Últimas Notícias</h2>

        <div className="categorias-container">
          <button
            className={`categoria-btn ${
              selectedCategoria === "Todas" ? "active" : ""
            }`}
            onClick={() => handleCategoriaClick("Todas")}
          >
            Todas
          </button>
          {categorias.map((categoria) => (
            <button
              key={categoria.id}
              className={`categoria-btn ${
                selectedCategoria === categoria.nome ? "active" : ""
              }`}
              onClick={() => handleCategoriaClick(categoria.nome)}
            >
              {categoria.nome}
            </button>
          ))}
        </div>

        <div className="noticias-container">
          {filteredNoticias.length > 0 ? (
            filteredNoticias.map((noticia) => (
              <div key={noticia.id} className="noticia-card">
                <div className="noticia-imagem">
                  <img src={noticia.imagem || "/placeholder-news.png"} alt="" />
                </div>
                <div className="noticia-conteudo">
                  <h3>{noticia.titulo}</h3>
                  <p>{noticia.resumo}</p>
                  <small>{noticia.data_publicacao}</small>
                </div>
              </div>
            ))
          ) : (
            <p>Nenhuma notícia encontrada para a categoria: {selectedCategoria}</p>
          )}
        </div>
      </section>
    </div>
  );
};

export default Home;
