import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# ─── Palette ───
BG      = RGBColor(0x0F, 0x17, 0x2A)
CARD    = RGBColor(0x16, 0x20, 0x3A)
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
MUTED   = RGBColor(0x94, 0xA3, 0xBF)
BLUE    = RGBColor(0x3C, 0x6E, 0xF5)
GREEN   = RGBColor(0x38, 0xA1, 0x69)
YELLOW  = RGBColor(0xD6, 0x9E, 0x2E)
RED     = RGBColor(0xE5, 0x3E, 0x3E)
B = "\u25b8"


def bg(s):
    f = s.background.fill; f.solid(); f.fore_color.rgb = BG

def tb(s, l, t, w, h, txt, sz=18, c=WHITE, b=False, a=PP_ALIGN.LEFT):
    tx = s.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = tx.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = txt
    p.font.size = Pt(sz); p.font.color.rgb = c; p.font.bold = b
    p.font.name = "Segoe UI"; p.alignment = a
    return tx

def bul(s, l, t, w, h, items, sz=16, c=WHITE, bc=BLUE):
    tx = s.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = tx.text_frame; tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(6)
        r = p.add_run(); r.text = f"{B}  "; r.font.size = Pt(sz); r.font.color.rgb = bc; r.font.name = "Segoe UI"
        r2 = p.add_run(); r2.text = item; r2.font.size = Pt(sz); r2.font.color.rgb = c; r2.font.name = "Segoe UI"

def card(s, l, t, w, h, fc=CARD):
    sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(l), Inches(t), Inches(w), Inches(h))
    sh.fill.solid(); sh.fill.fore_color.rgb = fc; sh.line.fill.background(); sh.shadow.inherit = False
    return sh

def line(s, l, t, w, c=BLUE):
    sh = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(l), Inches(t), Inches(w), Pt(3))
    sh.fill.solid(); sh.fill.fore_color.rgb = c; sh.line.fill.background()

def quote(s, l, t, w, h, txt, src):
    card(s, l, t, w, h, RGBColor(0x1A, 0x25, 0x42))
    sh = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(l), Inches(t), Pt(4), Inches(h))
    sh.fill.solid(); sh.fill.fore_color.rgb = BLUE; sh.line.fill.background()
    tb(s, l+0.3, t+0.15, w-0.5, h-0.5, f'"{txt}"', sz=14, c=MUTED)
    tb(s, l+0.3, t+h-0.4, w-0.5, 0.3, f"\u2014 {src}", sz=12, c=BLUE, b=True)


# ═══════════════════════════════════════
# SLIDE 1 — Capa
# ═══════════════════════════════════════
sl = prs.slides.add_slide(prs.slide_layouts[6]); bg(sl)
line(sl, 1, 2.4, 2)
tb(sl, 1, 2.6, 11, 1.2, "KPI Explainability MVP", sz=44, b=True)
tb(sl, 1, 3.8, 11, 0.6,
   "Transpar\u00eancia no c\u00e1lculo de indicadores a partir de question\u00e1rios organizacionais",
   sz=20, c=MUTED)
tb(sl, 1, 5.2, 11, 0.4,
   "Tend\u00eancias de Software  \u2022  PPGC / UFRGS",
   sz=14, c=BLUE, b=True)


# ═══════════════════════════════════════
# SLIDE 2 — O Problema
# ═══════════════════════════════════════
sl = prs.slides.add_slide(prs.slide_layouts[6]); bg(sl)
line(sl, 0.8, 0.6, 1.5)
tb(sl, 0.8, 0.8, 11, 0.8, 'O Problema: A "Caixa Preta" dos KPIs', sz=32, b=True)
bul(sl, 0.8, 1.8, 11.5, 4, [
    "Contexto: mestrado envolvendo indicadores gerados por question\u00e1rios organizacionais (Gen_Connect).",
    "KPIs s\u00e3o apresentados como valores num\u00e9ricos finais, sem contexto.",
    "O usu\u00e1rio n\u00e3o consegue entender como o resultado foi obtido.",
    "Necessidade: mostrar quais dados foram usados, como foram agregados e qual f\u00f3rmula foi aplicada.",
], sz=18)


# ═══════════════════════════════════════
# SLIDE 3 — O Que \u00e9 o MVP
# ═══════════════════════════════════════
sl = prs.slides.add_slide(prs.slide_layouts[6]); bg(sl)
line(sl, 0.8, 0.6, 1.5)
tb(sl, 0.8, 0.8, 11, 0.8, "O MVP: Explainability na Pr\u00e1tica", sz=32, b=True)
tb(sl, 0.8, 1.5, 11, 0.5,
   "Prot\u00f3tipo frontend independente do Gen_Connect para demonstrar transpar\u00eancia no c\u00e1lculo de KPIs.",
   sz=18, c=MUTED)

card(sl, 0.8, 2.2, 5.5, 4.5)
tb(sl, 1.1, 2.4, 5, 0.4, "Tecnologias", sz=16, c=BLUE, b=True)
bul(sl, 1.1, 2.9, 5, 3.5, [
    "React + TypeScript",
    "Vite (build tool)",
    "CSS puro (sem frameworks)",
    "Sem backend, banco de dados ou APIs",
    "Sem autentica\u00e7\u00e3o ou servi\u00e7os externos",
], sz=15)

card(sl, 6.8, 2.2, 5.7, 4.5)
tb(sl, 7.1, 2.4, 5, 0.4, "Funcionalidades", sz=16, c=BLUE, b=True)
bul(sl, 7.1, 2.9, 5.2, 3.5, [
    "Tela de configura\u00e7\u00e3o com entrada de dados pelo usu\u00e1rio",
    "Sele\u00e7\u00e3o de KPI via dropdown",
    "C\u00e1lculo autom\u00e1tico com f\u00f3rmula transparente",
    "Distribui\u00e7\u00e3o visual das respostas",
    "Interpreta\u00e7\u00e3o din\u00e2mica com faixas de cor",
    "Navega\u00e7\u00e3o entre telas (configura\u00e7\u00e3o \u2194 dashboard)",
], sz=15)


# ═══════════════════════════════════════
# SLIDE 4 — Fluxo da Aplica\u00e7\u00e3o
# ═══════════════════════════════════════
sl = prs.slides.add_slide(prs.slide_layouts[6]); bg(sl)
line(sl, 0.8, 0.6, 1.5)
tb(sl, 0.8, 0.8, 11, 0.8, "Fluxo da Aplica\u00e7\u00e3o", sz=32, b=True)

# Step 1
card(sl, 0.8, 1.9, 3.4, 4.3, RGBColor(0x14, 0x1C, 0x35))
tb(sl, 1.1, 2.0, 3, 0.4, "1", sz=36, c=BLUE, b=True)
tb(sl, 1.1, 2.6, 3, 0.4, "Configura\u00e7\u00e3o", sz=18, c=WHITE, b=True)
bul(sl, 1.1, 3.1, 2.8, 2.5, [
    "Escolher KPI no dropdown",
    "Digitar valores de resposta",
    "Aceita v\u00edrgula ou espa\u00e7o",
    "Valida\u00e7\u00e3o autom\u00e1tica (1 a 5)",
], sz=13, bc=BLUE)

# Arrow 1
tb(sl, 4.3, 3.5, 0.8, 0.5, "\u2192", sz=36, c=BLUE, b=True, a=PP_ALIGN.CENTER)

# Step 2
card(sl, 5.0, 1.9, 3.4, 4.3, RGBColor(0x14, 0x1C, 0x35))
tb(sl, 5.3, 2.0, 3, 0.4, "2", sz=36, c=BLUE, b=True)
tb(sl, 5.3, 2.6, 3, 0.4, "C\u00e1lculo", sz=18, c=WHITE, b=True)
bul(sl, 5.3, 3.1, 2.8, 2.5, [
    "M\u00e9dia das respostas",
    "KPI = (m\u00e9dia / 5) \u00d7 100",
    "Classifica\u00e7\u00e3o por faixa",
    "Gera\u00e7\u00e3o da interpreta\u00e7\u00e3o",
], sz=13, bc=BLUE)

# Arrow 2
tb(sl, 8.5, 3.5, 0.8, 0.5, "\u2192", sz=36, c=BLUE, b=True, a=PP_ALIGN.CENTER)

# Step 3
card(sl, 9.2, 1.9, 3.4, 4.3, RGBColor(0x14, 0x1C, 0x35))
tb(sl, 9.5, 2.0, 3, 0.4, "3", sz=36, c=BLUE, b=True)
tb(sl, 9.5, 2.6, 3, 0.4, "Dashboard", sz=18, c=WHITE, b=True)
bul(sl, 9.5, 3.1, 2.8, 2.5, [
    "Valor do KPI com cor",
    "Distribui\u00e7\u00e3o das respostas",
    "F\u00f3rmula e valores usados",
    "Explica\u00e7\u00e3o textual do resultado",
], sz=13, bc=BLUE)

tb(sl, 0.8, 6.5, 11.5, 0.5,
   "F\u00f3rmula: KPI = (m\u00e9dia das respostas / 5) \u00d7 100",
   sz=16, c=BLUE, b=True, a=PP_ALIGN.CENTER)


# ═══════════════════════════════════════
# SLIDE 5 — Faixas de Interpreta\u00e7\u00e3o
# ═══════════════════════════════════════
sl = prs.slides.add_slide(prs.slide_layouts[6]); bg(sl)
line(sl, 0.8, 0.6, 1.5)
tb(sl, 0.8, 0.8, 11, 0.8, "Interpreta\u00e7\u00e3o Autom\u00e1tica por Faixas", sz=32, b=True)
tb(sl, 0.8, 1.5, 11, 0.5,
   "O resultado do KPI \u00e9 classificado automaticamente e comunica o significado ao usu\u00e1rio:",
   sz=18, c=MUTED)

# Red
card(sl, 0.8, 2.3, 3.6, 3.8, RGBColor(0x2A, 0x12, 0x12))
sh = sl.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(2.3), Inches(3.6), Pt(4))
sh.fill.solid(); sh.fill.fore_color.rgb = RED; sh.line.fill.background()
tb(sl, 1.1, 2.6, 3, 0.4, "< 60%", sz=28, c=RED, b=True)
tb(sl, 1.1, 3.2, 3, 0.4, "Aten\u00e7\u00e3o Urgente", sz=18, c=WHITE, b=True)
tb(sl, 1.1, 3.8, 3, 1.2,
   "Indica problemas significativos na percep\u00e7\u00e3o dos respondentes. Exige a\u00e7\u00f5es corretivas imediatas.",
   sz=14, c=MUTED)

# Yellow
card(sl, 4.8, 2.3, 3.6, 3.8, RGBColor(0x2A, 0x24, 0x10))
sh = sl.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(4.8), Inches(2.3), Inches(3.6), Pt(4))
sh.fill.solid(); sh.fill.fore_color.rgb = YELLOW; sh.line.fill.background()
tb(sl, 5.1, 2.6, 3, 0.4, "60% \u2013 80%", sz=28, c=YELLOW, b=True)
tb(sl, 5.1, 3.2, 3, 0.4, "Precisa de Aten\u00e7\u00e3o", sz=18, c=WHITE, b=True)
tb(sl, 5.1, 3.8, 3, 1.2,
   "H\u00e1 espa\u00e7o relevante para melhorias. Merece acompanhamento e a\u00e7\u00f5es planejadas.",
   sz=14, c=MUTED)

# Green
card(sl, 8.8, 2.3, 3.6, 3.8, RGBColor(0x10, 0x22, 0x15))
sh = sl.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(8.8), Inches(2.3), Inches(3.6), Pt(4))
sh.fill.solid(); sh.fill.fore_color.rgb = GREEN; sh.line.fill.background()
tb(sl, 9.1, 2.6, 3, 0.4, "> 80%", sz=28, c=GREEN, b=True)
tb(sl, 9.1, 3.2, 3, 0.4, "Bom Desempenho", sz=18, c=WHITE, b=True)
tb(sl, 9.1, 3.8, 3, 1.2,
   "Percep\u00e7\u00e3o positiva. N\u00edvel saud\u00e1vel com acompanhamento cont\u00ednuo recomendado.",
   sz=14, c=MUTED)

tb(sl, 0.8, 6.5, 11.5, 0.5,
   "A cor do card do KPI no dashboard muda automaticamente conforme a faixa",
   sz=14, c=MUTED, a=PP_ALIGN.CENTER)


# ═══════════════════════════════════════
# SLIDE 6 — Processo Spec-Driven
# ═══════════════════════════════════════
sl = prs.slides.add_slide(prs.slide_layouts[6]); bg(sl)
line(sl, 0.8, 0.6, 1.5)
tb(sl, 0.8, 0.8, 11, 0.8, "Processo: Spec-Driven Development", sz=32, b=True)
tb(sl, 0.8, 1.5, 11, 0.5,
   "Todo o desenvolvimento foi guiado por artefatos OpenSpec, documentando antes de codificar:",
   sz=18, c=MUTED)

# 4 artifact cards
artifacts = [
    ("proposal.md", "Motiva\u00e7\u00e3o e escopo", "Define o porqu\u00ea da mudan\u00e7a, o que muda e o impacto esperado."),
    ("spec.md", "Requisitos e cen\u00e1rios", "Comportamentos esperados com cen\u00e1rios WHEN/THEN test\u00e1veis."),
    ("design.md", "Decis\u00f5es t\u00e9cnicas", "Como implementar: arquitetura, trade-offs e riscos."),
    ("tasks.md", "Checklist de tarefas", "Tarefas verific\u00e1veis quebradas por componente."),
]
for i, (name, title, desc) in enumerate(artifacts):
    x = 0.8 + i * 3.1
    card(sl, x, 2.3, 2.8, 3.8)
    tb(sl, x + 0.2, 2.5, 2.4, 0.3, name, sz=12, c=BLUE, b=True)
    tb(sl, x + 0.2, 3.0, 2.4, 0.4, title, sz=16, c=WHITE, b=True)
    tb(sl, x + 0.2, 3.5, 2.4, 2, desc, sz=13, c=MUTED)

quote(sl, 0.8, 6.3, 11.5, 0.9,
      "A especifica\u00e7\u00e3o ajudou a limitar o desenvolvimento ao problema definido para o MVP.",
      "relato.md")


# ═══════════════════════════════════════
# SLIDE 7 — Exemplo de C\u00f3digo / Artefatos
# ═══════════════════════════════════════
sl = prs.slides.add_slide(prs.slide_layouts[6]); bg(sl)
line(sl, 0.8, 0.6, 1.5)
tb(sl, 0.8, 0.8, 11, 0.8, "Trechos dos Artefatos", sz=32, b=True)

quote(sl, 0.8, 1.7, 11.5, 1.6,
      "O c\u00e1lculo utilizado \u00e9: KPI = (m\u00e9dia das respostas / 5) \u00d7 100\n"
      "\u2022 14 respostas  \u2022 soma: 55  \u2022 m\u00e9dia: 3,93  \u2022 escala: 5  \u2022 KPI: 78,6%",
      "README.md")

quote(sl, 0.8, 3.6, 11.5, 1.4,
      "A capability agora aceita valores fornecidos pelo usu\u00e1rio ao inv\u00e9s de dados est\u00e1ticos, "
      "adiciona uma tela de setup para entrada de dados, e gera interpreta\u00e7\u00e3o din\u00e2mica baseada em faixas de threshold.",
      "proposal.md")

quote(sl, 0.8, 5.3, 11.5, 1.4,
      "O KPI \u00e9 classificado em tr\u00eas faixas, cada uma com cor e texto de interpreta\u00e7\u00e3o: "
      "abaixo de 60% (vermelho), 60-80% (amarelo), acima de 80% (verde).",
      "design.md")


# ═══════════════════════════════════════
# SLIDE 8 — Dificuldades
# ═══════════════════════════════════════
sl = prs.slides.add_slide(prs.slide_layouts[6]); bg(sl)
line(sl, 0.8, 0.6, 1.5)
tb(sl, 0.8, 0.8, 11, 0.8, "Dificuldades Encontradas", sz=32, b=True)

card(sl, 0.8, 1.8, 3.6, 4.5)
tb(sl, 1.1, 1.95, 0.5, 0.5, "1", sz=28, c=BLUE, b=True)
tb(sl, 1.1, 2.5, 3, 0.4, "Restringir o escopo", sz=16, c=WHITE, b=True)
tb(sl, 1.1, 3.0, 3, 2.5,
   "Separar completamente o MVP da infraestrutura complexa do Gen_Connect. "
   "Resistir \u00e0 tenta\u00e7\u00e3o de adicionar APIs reais, banco de dados ou autentica\u00e7\u00e3o.",
   sz=13, c=MUTED)

card(sl, 4.8, 1.8, 3.6, 4.5)
tb(sl, 5.1, 1.95, 0.5, 0.5, "2", sz=28, c=BLUE, b=True)
tb(sl, 5.1, 2.5, 3, 0.4, "Representa\u00e7\u00e3o visual", sz=16, c=WHITE, b=True)
tb(sl, 5.1, 3.0, 3, 2.5,
   "Traduzir uma f\u00f3rmula matem\u00e1tica em uma interface rastre\u00e1vel e amig\u00e1vel. "
   "Comunicar significado atrav\u00e9s de cores e texto sem sobrecarregar o usu\u00e1rio.",
   sz=13, c=MUTED)

card(sl, 8.8, 1.8, 3.6, 4.5)
tb(sl, 9.1, 1.95, 0.5, 0.5, "3", sz=28, c=BLUE, b=True)
tb(sl, 9.1, 2.5, 3, 0.4, "Disciplina Spec-Driven", sz=16, c=WHITE, b=True)
tb(sl, 9.1, 3.0, 3, 2.5,
   "Manter a pr\u00e1tica de documentar primeiro e codificar apenas o que os artefatos especificam. "
   "Atualizar artefatos quando novas decis\u00f5es s\u00e3o tomadas.",
   sz=13, c=MUTED)


# ═══════════════════════════════════════
# SLIDE 9 — Resultados
# ═══════════════════════════════════════
sl = prs.slides.add_slide(prs.slide_layouts[6]); bg(sl)
line(sl, 0.8, 0.6, 1.5)
tb(sl, 0.8, 0.8, 11, 0.8, "Resultados Alcan\u00e7ados", sz=32, b=True)

card(sl, 0.8, 1.8, 3, 2.5, RGBColor(0x12, 0x1E, 0x15))
tb(sl, 1.0, 2.0, 2.6, 1, "78,6%", sz=52, c=GREEN, b=True, a=PP_ALIGN.CENTER)
tb(sl, 1.0, 3.2, 2.6, 0.6, "KPI Resultante\n14 respostas  \u2022  m\u00e9dia 3,93",
   sz=11, c=MUTED, a=PP_ALIGN.CENTER)

bul(sl, 4.2, 1.8, 8.5, 5, [
    "Aplica\u00e7\u00e3o standalone que comprova a viabilidade t\u00e9cnica da explainability.",
    "O usu\u00e1rio insere seus pr\u00f3prios dados e v\u00ea o KPI calculado em tempo real.",
    "Conex\u00e3o visual direta: dados de entrada \u2192 f\u00f3rmula \u2192 resultado \u2192 interpreta\u00e7\u00e3o.",
    "Feedback imediato com cores: vermelho / amarelo / verde conforme o resultado.",
    "Processo inteiro documentado via OpenSpec antes da implementa\u00e7\u00e3o.",
    "Base concreta para discuss\u00f5es futuras no projeto de mestrado.",
    "Demonstra que transpar\u00eancia \u00e9 poss\u00edvel sem complexidade excessiva.",
], sz=16)


# ═══════════════════════════════════════
# SLIDE 10 — Limita\u00e7\u00f5es e Pr\u00f3ximos Passos
# ═══════════════════════════════════════
sl = prs.slides.add_slide(prs.slide_layouts[6]); bg(sl)
line(sl, 0.8, 0.6, 1.5)
tb(sl, 0.8, 0.8, 11, 0.8, "Limita\u00e7\u00f5es e Pr\u00f3ximos Passos", sz=32, b=True)

card(sl, 0.8, 1.8, 5.5, 4.8)
tb(sl, 1.1, 2.0, 5, 0.5, "Limita\u00e7\u00f5es Atuais", sz=18, c=RED, b=True)
bul(sl, 1.1, 2.6, 5, 3.5, [
    "Uma \u00fanica f\u00f3rmula de c\u00e1lculo (m\u00e9dia / escala).",
    "N\u00e3o contempla diferentes tipos de KPI.",
    "Dados ef\u00eameros (sem persist\u00eancia entre sess\u00f5es).",
    "Sem t\u00e9cnicas avan\u00e7adas de explicabilidade (SHAP, LIME).",
    "Faixas de threshold fixas no c\u00f3digo (60% / 80%).",
], sz=15, bc=RED)

card(sl, 6.8, 1.8, 5.7, 4.8)
tb(sl, 7.1, 2.0, 5, 0.5, "Pr\u00f3ximos Passos", sz=18, c=GREEN, b=True)
bul(sl, 7.1, 2.6, 5.2, 3.5, [
    "Adicionar mais KPIs ao dropdown de sele\u00e7\u00e3o.",
    "Avaliar diferentes formas de apresentar explica\u00e7\u00f5es.",
    "Comparar estrat\u00e9gias de visualiza\u00e7\u00e3o.",
    "Investigar como usu\u00e1rios interpretam as explica\u00e7\u00f5es.",
    "Integrar conclus\u00f5es no projeto de pesquisa (Gen_Connect).",
], sz=15, bc=GREEN)


# ═══════════════════════════════════════
# SLIDE 11 — Obrigado
# ═══════════════════════════════════════
sl = prs.slides.add_slide(prs.slide_layouts[6]); bg(sl)
line(sl, 4.5, 2.8, 4)
tb(sl, 1, 3.0, 11.3, 1, "Obrigado!", sz=48, b=True, a=PP_ALIGN.CENTER)
tb(sl, 1, 4.2, 11.3, 0.6, "Perguntas?", sz=24, c=MUTED, a=PP_ALIGN.CENTER)


# ─── Save ───
prs.save(r'apresentacao_kpi_explainability.pptx')
print(f"Salvo! {len(prs.slides)} slides.")
