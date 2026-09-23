import { useState } from "react";
import SetupScreen from "./SetupScreen";

type ResponseDistribution = {
  level: number;
  count: number;
};

type ThresholdBand = {
  className: string;
  label: string;
  interpretation: string;
};

const KPI_LABELS: Record<string, string> = {
  "clareza-metas": "Clareza de metas e objetivos",
};

function getThresholdBand(kpiValue: number): ThresholdBand {
  if (kpiValue < 60) {
    return {
      className: "danger",
      label: "Atenção urgente",
      interpretation:
        "O resultado está abaixo de 60%, indicando que os respondentes percebem problemas significativos. Este indicador exige atenção urgente e ações corretivas imediatas para reverter a percepção negativa.",
    };
  }
  if (kpiValue <= 80) {
    return {
      className: "warning",
      label: "Precisa de atenção",
      interpretation:
        "O resultado está entre 60% e 80%, sinalizando que há espaço relevante para melhorias. Embora não seja crítico, este indicador merece atenção e ações de melhoria planejadas.",
    };
  }
  return {
    className: "success",
    label: "Bom desempenho",
    interpretation:
      "O resultado está acima de 80%, indicando uma percepção positiva por parte dos respondentes. O indicador está em um nível saudável, mas acompanhamento contínuo é recomendado.",
  };
}

export default function App() {
  const [screen, setScreen] = useState<"setup" | "dashboard">("setup");
  const [responseValues, setResponseValues] = useState<number[]>([]);
  const [kpiName, setKpiName] = useState("clareza-metas");

  function handleCalculate(selectedKpi: string, values: number[]) {
    setKpiName(selectedKpi);
    setResponseValues(values);
    setScreen("dashboard");
  }

  function handleBack() {
    setScreen("setup");
  }

  if (screen === "setup") {
    return (
      <SetupScreen
        initialValues={responseValues}
        initialKpi={kpiName}
        onCalculate={handleCalculate}
      />
    );
  }

  // Dashboard calculations
  const distribution: ResponseDistribution[] = [1, 2, 3, 4, 5].map((level) => ({
    level,
    count: responseValues.filter((value) => value === level).length,
  }));

  const totalResponses = responseValues.length;
  const totalSum = responseValues.reduce((acc, value) => acc + value, 0);
  const averageScore = totalSum / totalResponses;
  const kpiValue = (averageScore / 5) * 100;
  const formula = "KPI = (média das respostas / 5) × 100";
  const maxCount = Math.max(...distribution.map((item) => item.count), 1);
  const band = getThresholdBand(kpiValue);

  const explanation = `A média geral foi ${averageScore.toFixed(2)} em uma escala de 1 a 5, resultando em um KPI de ${kpiValue.toFixed(1)}%. ${band.interpretation}`;

  return (
    <main className="page">
      <section className="card">
        <header className="header">
          <div>
            <p className="eyebrow">KPI Explainability MVP</p>
            <h1>{KPI_LABELS[kpiName] || kpiName}</h1>
          </div>
          <div className="header-actions">
            <span className={`tag tag-${band.className}`}>{band.label}</span>
            <button type="button" className="btn-back" onClick={handleBack}>
              ← Voltar
            </button>
          </div>
        </header>

        <div className="summary-grid">
          <article className={`summary-box primary primary-${band.className}`}>
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
