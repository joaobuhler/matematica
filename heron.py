from manim import *

FUNDO         = "#121214"  
COR_TITULO    = "#00f0ff"  
COR_TRIANGULO = "#eceff4"  
COR_ALTURA    = "#ff5555"  
COR_EQUACOES  = "#81a1c1"  
COR_FINAL     = "#50fa7b"  
COR_AUXILIAR  = "#ffb86c"  


class DeducaoHeron(Scene):

    def tit(self, txt, size=28, cor=COR_TITULO):
        return Text(txt, font_size=size, color=cor, weight=SEMIBOLD)

    def eq(self, latex, size=24, cor=WHITE):
        return MathTex(latex, font_size=size, color=cor)

    def moldura(self, mob, cor=COR_TITULO, pad=0.15):
        return SurroundingRectangle(mob, color=cor, buff=pad, stroke_width=1.5, corner_radius=0.05)

    def _build_triangle(self, escala=0.7, offset=LEFT * 3.2):
        A = UP * 2.0 * escala + offset
        B = LEFT * 3.0 * escala + DOWN * 1.2 * escala + offset
        C = RIGHT * 2.6 * escala + DOWN * 1.2 * escala + offset
        H = np.array([offset[0], -1.2 * escala, 0])

        tri   = Polygon(B, A, C, color=COR_TRIANGULO, stroke_width=2)
        alt   = Line(A, H, color=COR_ALTURA, stroke_width=2.5)
        ang_r = RightAngle(Line(B, H), Line(H, A), length=0.15, color=COR_ALTURA, stroke_width=1.5)

        lA = MathTex("A", font_size=20, color=COR_TITULO).next_to(A, UP, buff=0.1)
        lB = MathTex("B", font_size=20, color=COR_TITULO).next_to(B, DL, buff=0.05)
        lC = MathTex("C", font_size=20, color=COR_TITULO).next_to(C, DR, buff=0.05)

        la  = MathTex("a",   font_size=20, color=WHITE).next_to(Line(B, C).get_center(), DOWN, buff=0.2)
        lb  = MathTex("b",   font_size=20, color=WHITE).next_to(Line(A, C).get_center(), UR, buff=0.05)
        lc  = MathTex("c",   font_size=20, color=WHITE).next_to(Line(A, B).get_center(), UL, buff=0.05)
        lx  = MathTex("x",   font_size=18, color=COR_AUXILIAR).next_to(Line(B, H).get_center(), UP, buff=0.08)
        lax = MathTex("a-x", font_size=18, color=COR_AUXILIAR).next_to(Line(H, C).get_center(), UP, buff=0.08)
        lh  = MathTex("h",   font_size=18, color=COR_ALTURA).next_to(alt.get_center(), RIGHT, buff=0.08)

        return VGroup(tri, alt, ang_r, lA, lB, lC, la, lb, lc, lx, lax, lh)

    def construct(self):
        self.camera.background_color = FUNDO
        
        self._cena_abertura()
        self._cena_algebrica_inicial()
        self._cena_fatoracao_avancada()
        self._cena_conclusao_heron()

    # ══════════════════════════════════════════════════════════════════════════
    # 1. ABERTURA E APRESENTAÇÃO GEOMÉTRICA
    # ══════════════════════════════════════════════════════════════════════════
    def _cena_abertura(self):
        t1 = self.tit("A Geometria por trás de Heron", size=32)
        t2 = Text("Construindo a fórmula a partir de Pitágoras", font_size=18, color=COR_EQUACOES)
        t2.next_to(t1, DOWN, buff=0.25)
        intro = VGroup(t1, t2).center()

        self.play(Write(t1), FadeIn(t2, shift=UP))
        self.wait(1.5)
        self.play(FadeOut(intro, shift=DOWN))

        self.titulo_atual = self.tit("1. Relações Métricas no Triângulo")
        self.titulo_atual.to_edge(UP, buff=0.5).to_edge(LEFT, buff=0.6)
        self.play(FadeIn(self.titulo_atual, shift=RIGHT))

        self._tri = self._build_triangle()
        self.play(Create(self._tri[0]), run_time=1) 
        self.play(Write(VGroup(*self._tri[3:9]))) 
        self.wait(0.5)
        
        self.play(Create(self._tri[1]), Create(self._tri[2]), Write(self._tri[11])) 
        self.play(Write(self._tri[9]), Write(self._tri[10])) 
        self.wait(1.5)

    # ══════════════════════════════════════════════════════════════════════════
    # 2. O SISTEMA E O ISOLAMENTO DE X
    # ══════════════════════════════════════════════════════════════════════════
    def _cena_algebrica_inicial(self):
        novo_titulo = self.tit("2. Sistema de Pitágoras")
        novo_titulo.align_to(self.titulo_atual, UL)
        
        eq1 = self.eq(r"c^2 = h^2 + x^2 \implies h^2 = c^2 - x^2", cor=COR_EQUACOES)
        eq2 = self.eq(r"b^2 = h^2 + (a-x)^2", cor=COR_EQUACOES)
        sistema = VGroup(eq1, eq2).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        sistema.to_edge(RIGHT, buff=0.6).shift(UP * 0.3) 

        self.play(Transform(self.titulo_atual, novo_titulo))
        self.play(Write(eq1))
        self.wait(0.8)
        self.play(Write(eq2))
        self.wait(1.5)

        eq3 = self.eq(r"b^2 = (c^2 - x^2) + (a^2 - 2ax + x^2)", size=22)
        eq4 = self.eq(r"b^2 = c^2 + a^2 - 2ax", size=22)
        eq_x = self.eq(r"x = \frac{a^2 + c^2 - b^2}{2a}", size=24, cor=COR_AUXILIAR)
        
        desenvolvimento = VGroup(eq3, eq4, eq_x).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        desenvolvimento.next_to(sistema, DOWN, buff=0.4, aligned_edge=LEFT)

        self.play(Write(eq3))
        self.wait(0.6)
        self.play(Write(eq4))
        self.wait(0.6)
        self.play(Write(eq_x))
        
        mold_x = self.moldura(eq_x, cor=COR_AUXILIAR)
        self.play(Create(mold_x))
        self.wait(2)

        self.play(
            FadeOut(self._tri), FadeOut(sistema), FadeOut(eq3), FadeOut(eq4), FadeOut(mold_x),
            eq_x.animate.to_corner(UL, buff=0.5).shift(DOWN * 0.9)
        )
        self._x_estatico = eq_x

    # ══════════════════════════════════════════════════════════════════════════
    # 3. ÁREA E DIFERENÇA DE QUADRADOS
    # ══════════════════════════════════════════════════════════════════════════
    def _cena_fatoracao_avancada(self):
        novo_titulo = self.tit("3. Álgebra da Área Quadrática")
        novo_titulo.align_to(self.titulo_atual, UL)
        self.play(Transform(self.titulo_atual, novo_titulo))

        eq_area1 = self.eq(r"A = \frac{a \cdot h}{2} \implies A^2 = \frac{a^2 \cdot h^2}{4}", size=24)
        eq_area1.to_edge(RIGHT, buff=0.8).shift(UP * 1.2)
        self.play(Write(eq_area1))
        
        eq_subst = self.eq(r"A^2 = \frac{a^2}{4} \left[ c^2 - \left(\frac{a^2+c^2-b^2}{2a}\right)^2 \right]", size=22)
        eq_subst.next_to(eq_area1, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(eq_subst))
        self.wait(1.5)

        self.play(
            FadeOut(self._x_estatico), FadeOut(eq_area1), 
            eq_subst.animate.to_edge(UP, buff=1.4).set_x(0)
        )

        eq_dif = self.eq(r"A^2 = \frac{4a^2c^2 - (a^2+c^2-b^2)^2}{16}", size=24, cor=COR_EQUACOES)
        eq_dif.next_to(eq_subst, DOWN, buff=0.5)
        self.play(Write(eq_dif))
        self.wait(1.5)

        self.play(FadeOut(eq_subst), eq_dif.animate.to_edge(UP, buff=1.4))

        fat1 = self.eq(r"A^2 = \frac{[(2ac) + (a^2+c^2-b^2)] \cdot [(2ac) - (a^2+c^2-b^2)]}{16}", size=20)
        fat1.next_to(eq_dif, DOWN, buff=0.5)
        self.play(Write(fat1))
        self.wait(1)

        fat2 = self.eq(r"A^2 = \frac{[(a+c)^2 - b^2] \cdot [b^2 - (a-c)^2]}{16}", size=22)
        fat2.next_to(fat1, DOWN, buff=0.5)
        self.play(Write(fat2))
        self.wait(2)

        self.play(
            FadeOut(eq_dif), FadeOut(fat1),
            fat2.animate.to_edge(UP, buff=1.5).set_x(0)
        )
        self._expressao_chave = fat2

    # ══════════════════════════════════════════════════════════════════════════
    # 4. INTRODUÇÃO DO SEMIPERÍMETRO E RESULTADO
    # ══════════════════════════════════════════════════════════════════════════
    def _cena_conclusao_heron(self):
        novo_titulo = self.tit("4. O Semiperímetro (p)")
        novo_titulo.align_to(self.titulo_atual, UL)
        self.play(Transform(self.titulo_atual, novo_titulo))

        fatores_4 = self.eq(
            r"A^2 = \left(\frac{a+b+c}{2}\right)\left(\frac{-a+b+c}{2}\right)\left(\frac{a-b+c}{2}\right)\left(\frac{a+b-c}{2}\right)",
            size=19
        ).next_to(self._expressao_chave, DOWN, buff=0.8)

        self.play(FadeIn(fatores_4, shift=UP))
        self.wait(1.5)

        p_def = self.eq(r"p = \frac{a+b+c}{2}", size=22, cor=COR_FINAL)
        p_a   = self.eq(r"p-a = \frac{-a+b+c}{2}", size=20)
        p_b   = self.eq(r"p-b = \frac{a-b+c}{2}", size=20)
        p_c   = self.eq(r"p-c = \frac{a+b-c}{2}", size=20)
        
        bloco_p = VGroup(p_def, p_a, p_b, p_c).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        bloco_p.to_edge(LEFT, buff=1.0).shift(DOWN * 1.0)

        self.play(Write(p_def))
        self.play(FadeIn(VGroup(p_a, p_b, p_c), shift=RIGHT, lag_ratio=0.2))
        self.wait(1.5)

        heron_quadrada = self.eq(r"A^2 = p(p-a)(p-b)(p-c)", size=24)
        heron_quadrada.to_edge(RIGHT, buff=1.2).align_to(p_def, UP)
        
        self.play(Write(heron_quadrada))
        self.wait(1)

        heron_final = self.eq(
            r"A = \sqrt{p(p-a)(p-b)(p-c)}",
            size=26, cor=COR_FINAL
        ).next_to(heron_quadrada, DOWN, buff=0.5)

        seta = Line(heron_quadrada.get_bottom(), heron_final.get_top(), color=COR_EQUACOES).add_tip(tip_length=0.12)
        
        self.play(Create(seta))
        self.play(FadeIn(heron_final, shift=UP, run_time=1))
        
        mold_final = self.moldura(heron_final, cor=COR_FINAL, pad=0.2)
        self.play(Create(mold_final))
        
        self.play(
            Flash(heron_final.get_center(), color=COR_FINAL, flash_radius=1.0, line_length=0.2, num_lines=12),
            self.titulo_atual.animate.set_color(COR_FINAL)
        )
        self.wait(3.5)

        self.play(FadeOut(VGroup(self.titulo_atual, self._expressao_chave, fatores_4, bloco_p, heron_quadrada, seta, heron_final, mold_final)))