type ResponseDistribution = {
  level: number;
  count: number;
};

const responseValues = [4, 5, 3, 4, 5, 2, 4, 5, 3, 4, 5, 4, 3, 4];

const distribution: ResponseDistribution[] = [1, 2, 3, 4, 5].map((level) => ({
  level,
  count: responseValues.filter((value) => value === level).length,
}));

const totalResponses = responseValues.length;
const totalSum = responseValues.reduce((acc, value) => acc + value, 0);
const averageScore = totalSum / totalResponses;
const kpiValue = (averageScore / 5) * 100;
const formula = "KPI = (média das respostas / 5) × 100";
const explanation = `A média geral foi ${averageScore.toFixed(2)} em uma escala de 1 a 5. Como a maioria das respostas ficou nos níveis 4 e 5, o resultado indica uma percepção positiva, embora ainda haja espaço para melhorar a clareza dos objetivos.`;

export default function App() {
  const maxCount = Math.max(...distribution.map((item) => item.count), 1);

  return (
    <main className="page">
      <section className="card">
        <header className="header">
          <div>
            <p className="eyebrow">KPI Explainability MVP</p>
            <h1>Clareza de metas e objetivos</h1>
          </div>
          <span className="tag">Pesquisa interna</span>
        </header>

        <div className="summary-grid">
          <article className="summary-box primary">
            <span className="label">Valor do KPI</span>
            <strong>{kpiValue.toFixed(1)}%</strong>
          </article>

          <article className="summary-box">
            <span className="label">Quantidade de respostas</span>
            <strong>{totalResponses}</strong>
          </article>

          <article className="summary-box">
            <span className="label">Média das respostas</span>
            <strong>{averageScore.toFixed(2)}</strong>
          </article>
        </div>

        <div className="two-columns">
          <section className="panel">
            <h2>Distribuição das respostas</h2>
            <div className="distribution-list">
              {distribution.map(({ level, count }) => (
                <div key={level} className="distribution-row">
                  <div className="distribution-meta">
                    <span className="level">{level}</span>
                    <span className="count">{count} respostas</span>
                  </div>
                  <div className="bar-track">
                    <div className="bar" style={{ width: `${(count / maxCount) * 100}%` }} />
                  </div>
                </div>
              ))}
            </div>
          </section>

          <section className="panel">
            <h2>Fórmula de cálculo</h2>
            <div className="formula-box">
              <span className="formula-label">Método</span>
              <p>{formula}</p>
            </div>

            <div className="calc-grid">
              <div>
                <span className="mini-label">Soma</span>
                <strong>{totalSum}</strong>
              </div>
              <div>
                <span className="mini-label">Média</span>
                <strong>{averageScore.toFixed(2)}</strong>
              </div>
              <div>
                <span className="mini-label">Escala</span>
                <strong>5</strong>
              </div>
            </div>
          </section>
        </div>

        <section className="panel explanation-panel">
          <h2>Explicação do resultado</h2>
          <p>{explanation}</p>
        </section>

        <section className="panel">
          <h2>Valores utilizados</h2>
          <div className="values-row">
            {responseValues.map((value, index) => (
              <span key={`${value}-${index}`} className="value-pill">
                {value}
              </span>
            ))}
          </div>

          <div className="calc-grid bottom-grid">
            <div>
              <span className="mini-label">Mínimo</span>
              <strong>{Math.min(...responseValues)}</strong>
            </div>
            <div>
              <span className="mini-label">Máximo</span>
              <strong>{Math.max(...responseValues)}</strong>
            </div>
            <div>
              <span className="mini-label">Média</span>
              <strong>{averageScore.toFixed(2)}</strong>
            </div>
          </div>
        </section>
      </section>
    </main>
  );
}
