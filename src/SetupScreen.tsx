import { useState } from "react";

type SetupScreenProps = {
  initialValues: number[];
  initialKpi: string;
  onCalculate: (kpiName: string, values: number[]) => void;
};

const KPI_OPTIONS = [
  { value: "clareza-metas", label: "Clareza de metas e objetivos" },
];

export default function SetupScreen({
  initialValues,
  initialKpi,
  onCalculate,
}: SetupScreenProps) {
  const [selectedKpi, setSelectedKpi] = useState(initialKpi || KPI_OPTIONS[0].value);
  const [inputText, setInputText] = useState("");
  const [parsedValues, setParsedValues] = useState<number[]>(initialValues);
  const [error, setError] = useState("");

  function handleAddValues() {
    if (!inputText.trim()) return;

    const raw = inputText.split(/[\s,;]+/).filter(Boolean);
    const valid: number[] = [];
    const invalid: string[] = [];

    for (const token of raw) {
      const num = Number(token);
      if (Number.isInteger(num) && num >= 1 && num <= 5) {
        valid.push(num);
      } else {
        invalid.push(token);
      }
    }

    if (invalid.length > 0) {
      setError(
        `Valores inválidos ignorados: ${invalid.join(", ")}. Use apenas números inteiros de 1 a 5.`
      );
    } else {
      setError("");
    }

    if (valid.length > 0) {
      setParsedValues((prev) => [...prev, ...valid]);
      setInputText("");
    }
  }

  function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleAddValues();
    }
  }

  function handleRemoveValue(index: number) {
    setParsedValues((prev) => prev.filter((_, i) => i !== index));
  }

  function handleClearAll() {
    setParsedValues([]);
    setError("");
  }

  const canCalculate = parsedValues.length > 0;

  return (
    <main className="page">
      <section className="card setup-card">
        <header className="header">
          <div>
            <p className="eyebrow">KPI Explainability MVP</p>
            <h1>Configuração</h1>
          </div>
          <span className="tag">Entrada de dados</span>
        </header>

        <div className="setup-section">
          <label className="setup-label" htmlFor="kpi-select">
            Selecione o KPI
          </label>
          <select
            id="kpi-select"
            className="setup-select"
            value={selectedKpi}
            onChange={(e) => setSelectedKpi(e.target.value)}
          >
            {KPI_OPTIONS.map((opt) => (
              <option key={opt.value} value={opt.value}>
                {opt.label}
              </option>
            ))}
          </select>
        </div>

        <div className="setup-section">
          <label className="setup-label" htmlFor="values-input">
            Valores de resposta (1 a 5)
          </label>
          <p className="setup-hint">
            Digite os valores separados por vírgula, espaço ou ponto-e-vírgula.
            Pressione Enter ou clique em "Adicionar" para incluir.
          </p>
          <div className="input-row">
            <textarea
              id="values-input"
              className="setup-textarea"
              placeholder="Ex: 4, 5, 3, 4, 5, 2, 4, 5, 3, 4"
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              onKeyDown={handleKeyDown}
              rows={3}
            />
            <button
              type="button"
              className="btn-add"
              onClick={handleAddValues}
              disabled={!inputText.trim()}
            >
              Adicionar
            </button>
          </div>
          {error && <p className="input-error">{error}</p>}
        </div>

        {parsedValues.length > 0 && (
          <div className="setup-section">
            <div className="values-header">
              <span className="setup-label">
                Valores adicionados ({parsedValues.length})
              </span>
              <button
                type="button"
                className="btn-clear"
                onClick={handleClearAll}
              >
                Limpar tudo
              </button>
            </div>
            <div className="values-row">
              {parsedValues.map((value, index) => (
                <span key={`${value}-${index}`} className="value-pill removable">
                  {value}
                  <button
                    type="button"
                    className="pill-remove"
                    onClick={() => handleRemoveValue(index)}
                    aria-label={`Remover valor ${value}`}
                  >
                    ×
                  </button>
                </span>
              ))}
            </div>
          </div>
        )}

        <button
          type="button"
          className="btn-calculate"
          disabled={!canCalculate}
          onClick={() => onCalculate(selectedKpi, parsedValues)}
        >
          Calcular e Visualizar
        </button>
      </section>
    </main>
  );
}
