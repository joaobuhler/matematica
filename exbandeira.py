from manim import *

FUNDO         = "#121214"  # Grafite escuro elegante
COR_TITULO    = "#00f0ff"  # Ciano elétrico (Foco/Destaque)
COR_TRIANGULO = "#eceff4"  # Branco gelo para estruturas principais
COR_ALTURA    = "#ff5555"  # Coral/Vermelho suave
COR_EQUACOES  = "#81a1c1"  # Azul pastel para manipulações algébricas
COR_FINAL     = "#50fa7b"  # Verde neon suave para respostas finais
COR_AUXILIAR  = "#ffb86c"  # Laranja pastel para valores intermediários


class ResolucaoBandeira(Scene):

    def tit(self, txt, size=28, cor=COR_TITULO):
        return Text(txt, font_size=size, color=cor, weight=SEMIBOLD)

    def eq(self, latex, size=24, cor=WHITE):
        return MathTex(latex, font_size=size, color=cor)

    def moldura(self, mob, cor=COR_TITULO, pad=0.15):
        return SurroundingRectangle(mob, color=cor, buff=pad, stroke_width=1.5, corner_radius=0.05)

    def construct(self):
        self.camera.background_color = FUNDO
        
        self._introducao_problema()
        self._resolucao_item_a()
        self._resolucao_item_b()

    # ══════════════════════════════════════════════════════════════════════════
    # 1. INTRODUÇÃO E DADOS DO PROBLEMA
    # ══════════════════════════════════════════════════════════════════════════
    def _introducao_problema(self):
        t1 = self.tit("Resolução Matemática: Bandeira do Brasil", size=32)
        t2 = Text("Cálculo de Áreas e Porcentagens com Geometria", font_size=18, color=COR_EQUACOES)
        t2.next_to(t1, DOWN, buff=0.25)
        intro = VGroup(t1, t2).center()

        self.play(Write(t1), FadeIn(t2, shift=UP))
        self.wait(1.5)
        self.play(FadeOut(intro, shift=DOWN))

        self.titulo_atual = self.tit("Dados Iniciais da Bandeira")
        self.titulo_atual.to_edge(UP, buff=0.5).to_edge(LEFT, buff=0.6)
        self.play(FadeIn(self.titulo_atual, shift=RIGHT))

        d1 = self.eq(r"\text{Retângulo (Total): } 2\,\text{m} \times 1{,}40\,\text{m} = 200\,\text{cm} \times 140\,\text{cm}", size=20)
        d2 = self.eq(r"\text{Distância dos vértices do losango às bordas: } 17\,\text{cm}", size=20, cor=COR_AUXILIAR)
        d3 = self.eq(r"\text{Raio do círculo (} r \text{): } 35\,\text{cm} \quad \left(\pi \approx \frac{22}{7}\right)", size=20)
        
        dados = VGroup(d1, d2, d3).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        dados.center().shift(UP * 0.5)
        
        self.play(FadeIn(dados, shift=RIGHT, lag_ratio=0.3))
        self.wait(2.5)
        self.play(FadeOut(dados))

    # ══════════════════════════════════════════════════════════════════════════
    # 2. RESOLUÇÃO DO ITEM A (ÁREA VERDE)
    # ══════════════════════════════════════════════════════════════════════════
    def _resolucao_item_a(self):
        novo_titulo = self.tit("Item a) Área da Região Verde")
        novo_titulo.align_to(self.titulo_atual, UL)
        self.play(Transform(self.titulo_atual, novo_titulo))

        # Passo 1: Área do Retângulo
        step1 = self.eq(r"A_{\text{retangulo}} = 200 \cdot 140 = 28.000\,\text{cm}^2", size=22)
        step1.to_edge(UP, buff=1.5).set_x(0)
        self.play(Write(step1))
        self.wait(0.8)

        # Passo 2: Dimensões do Losango
        step2_1 = self.eq(r"\text{Diagonal Maior (} D \text{): } 200 - 2(17) = 166\,\text{cm}", size=21, cor=COR_AUXILIAR)
        step2_2 = self.eq(r"\text{Diagonal Menor (} d \text{): } 140 - 2(17) = 106\,\text{cm}", size=21, cor=COR_AUXILIAR)
        diagonais = VGroup(step2_1, step2_2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        diagonais.next_to(step1, DOWN, buff=0.4)
        
        self.play(Write(diagonais))
        self.wait(1)

        # Passo 3: Área do Losango
        step3 = self.eq(r"A_{\text{losango}} = \frac{D \cdot d}{2} = \frac{166 \cdot 106}{2} = 8.798\,\text{cm}^2", size=22)
        step3.next_to(diagonais, DOWN, buff=0.4)
        self.play(Write(step3))
        self.wait(1.5)

        self.play(
            FadeOut(diagonais),
            step1.animate.to_edge(UP, buff=1.5).set_x(-3),
            step3.animate.next_to(step1, DOWN, buff=0.4, aligned_edge=LEFT)
        )

        sub_verde = self.eq(r"A_{\text{verde}} = A_{\text{retangulo}} - A_{\text{losango}}", size=22, cor=COR_EQUACOES)
        sub_verde.to_edge(RIGHT, buff=1.2).align_to(step1, UP)
        
        res_verde = self.eq(r"A_{\text{verde}} = 28.000 - 8.798 = 19.202\,\text{cm}^2", size=24, cor=COR_FINAL)
        res_verde.next_to(sub_verde, DOWN, buff=0.4, aligned_edge=LEFT)
        
        self.play(Write(sub_verde))
        self.wait(0.5)
        self.play(Write(res_verde))
        
        mold_verde = self.moldura(res_verde, cor=COR_FINAL, pad=0.18)
        self.play(Create(mold_verde))
        self.wait(3)

        self.play(FadeOut(VGroup(step1, step3, sub_verde, res_verde, mold_verde)))
        
        self.A_total = 28000
        self.A_losango = 8798

    # ══════════════════════════════════════════════════════════════════════════
    # 3. RESOLUÇÃO DO ITEM B (PORCENTAGEM DA ÁREA AMARELA)
    # ══════════════════════════════════════════════════════════════════════════
    def _resolucao_item_b(self):
        novo_titulo = self.tit("Item b) Porcentagem da Área Amarela")
        novo_titulo.align_to(self.titulo_atual, UL)
        self.play(Transform(self.titulo_atual, novo_titulo))

        # Passo 1: Área do Círculo com pi = 22/7
        c1 = self.eq(r"A_{\text{circulo}} = \pi \cdot r^2 = \frac{22}{7} \cdot 35^2", size=22)
        c1.to_edge(UP, buff=1.5).set_x(0)
        c2 = self.eq(r"A_{\text{circulo}} = \frac{22}{7} \cdot 1225 = 22 \cdot 175 = 3.850\,\text{cm}^2", size=22)
        c2.next_to(c1, DOWN, buff=0.3)
        
        self.play(Write(c1))
        self.wait(0.6)
        self.play(Write(c2))
        self.wait(1.5)

        self.play(FadeOut(c1), c2.animate.to_edge(UP, buff=1.5).set_x(0))

        # Passo 2: Área Amarela Líquida (Losango - Círculo)
        c3 = self.eq(r"A_{\text{amarela}} = A_{\text{losango}} - A_{\text{circulo}}", size=22, cor=COR_EQUACOES)
        c3.next_to(c2, DOWN, buff=0.4)
        c4 = self.eq(r"A_{\text{amarela}} = 8.798 - 3.850 = 4.948\,\text{cm}^2", size=22, cor=COR_AUXILIAR)
        c4.next_to(c3, DOWN, buff=0.3)

        self.play(Write(c3))
        self.wait(0.5)
        self.play(Write(c4))
        self.wait(1.5)
        self.play(FadeOut(c2), FadeOut(c3), c4.animate.to_edge(UP, buff=1.5).set_x(0))

        pct1 = self.eq(r"P = \frac{A_{\text{amarela}}}{A_{\text{total}}} \cdot 100\%", size=22)
        pct1.next_to(c4, DOWN, buff=0.4)
        
        pct2 = self.eq(r"P = \frac{4.948}{28.000} \cdot 100\% \approx 0{,}176714 \cdot 100\%", size=21)
        pct2.next_to(pct1, DOWN, buff=0.3)

        self.play(Write(pct1))
        self.wait(0.5)
        self.play(Write(pct2))
        self.wait(1.5)

        self.play(FadeOut(c4), FadeOut(pct1), pct2.animate.to_edge(UP, buff=1.5).set_x(0))

        res_final = self.eq(r"P \approx 17{,}67\%", size=28, cor=COR_FINAL)
        res_final.next_to(pct2, DOWN, buff=0.5)
        
        self.play(Write(res_final))
        
        mold_final = self.moldura(res_final, cor=COR_FINAL, pad=0.2)
        self.play(Create(mold_final))
        
        self.play(
            Flash(res_final.get_center(), color=COR_FINAL, flash_radius=0.9, line_length=0.18, num_lines=10),
            self.titulo_atual.animate.set_color(COR_FINAL)
        )
        self.wait(4)

        self.play(FadeOut(VGroup(self.titulo_atual, pct2, res_final, mold_final)))