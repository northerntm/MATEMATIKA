## MANIM
## https://docs.manim.community/en/latest/examples.html
## https://en.wikibooks.org/wiki/LaTeX/Mathematics
## %% manim -ql manim1.py  ... 

from manim import *

class Kruznice(MovingCameraScene):
    def construct(self):
        # stred kruznice - doleva a dolu
        center = 2*LEFT+1*DOWN
        # nadpis
        kruznice = Text("Kružnice").scale(2).shift(3*UP)
        self.play(Write(kruznice))
        # kruznice samotna
        circle = Circle().scale(2).shift(center).set_color(WHITE)
        self.play(GrowFromCenter(circle))
        # S = stred
        stred = Dot(center)
        stred_text = Text('S').next_to(stred, LEFT+DOWN).set_color(YELLOW)
        self.add(stred, stred_text)
        self.wait()
        # polomer
        r = Line(stred.get_center(), center+2*RIGHT).set_color(YELLOW)
        # a kota polomeru
        kota = Brace(r)
        kota_text = kota.get_text("r")
        self.add(r, kota, kota_text)
        self.wait()
        # polomer obiha dokola
        r_moving = r.copy().set_color(YELLOW)
        def dokola(mobj, dt):
            mobj.rotate(dt, about_point=center)
        r_moving.add_updater(dokola)
        self.add(r_moving)
        self.wait(2*PI)
        r_moving.remove_updater(dokola)
        self.remove(r_moving)
        # dobehal - smazat
        self.wait()
        # nadpis obvod
        obvod_text = Text("Obvod").shift(UP+3*RIGHT)
        self.play(Write(obvod_text))
        # vzorec obvod
        vzorec1=MathTex("O = ","?").scale(2).shift(DOWN+3*RIGHT)
        self.play(Write(vzorec1))
        self.wait(2)
        # trojuhelnik
        r1 = r.copy().set_color(WHITE).rotate(PI/3, about_point=center)
        r2 = r.copy().set_color(YELLOW).rotate(-PI/3, about_point=center+2*RIGHT)
        self.add(r1, r2)
        kota2 = Brace(r2, direction=r2.copy().rotate(PI / 2).get_unit_vector())
        kota2_text = kota2.get_text("r")
        self.add(kota2, kota2_text)
        # seskupit trojuhelnik a 5x (1,2,3,4,5) zopakovat - pootocit a vzorec
        grp = VGroup(r1, r2)
        for i in range(1,6):
            grpcopy = grp.copy().rotate(i*PI/3, about_point=center)
            self.wait(1)
            self.add(grpcopy)
            self.play(Transform(vzorec1, MathTex('O {\\approx} ',i+1," \\times", " r").scale(2).shift(DOWN+3*RIGHT)))
        # prepsat vzorec na 2*3*r
        vzorec2=MathTex('O {\\approx} ',"2", "\\times", "3", "\\times", "r").scale(2).shift(DOWN+3*RIGHT)
        self.play(Transform(vzorec1, vzorec2))
        self.wait(2)
        # oranzove r
        r2c = r2.copy().set_color(ORANGE)
        self.add(r2c)
        self.wait()
        # oranzovy oblouk, delka 1
        a = Arc(radius=2.0, start_angle=0, angle=1, arc_center=center).set_color(ORANGE)
        self.play(Transform(r2c,a))
        # zazoomovat
        self.camera.frame.save_state()
        self.wait(2)
        self.play(self.camera.frame.animate.scale(0.2).move_to(UP+LEFT))
        self.wait(2)
        self.add(Arc(radius=2.0, start_angle=1, angle=PI/3-1, arc_center=center).set_color(RED))
        self.wait(2)
        # odzoomovat
        self.play(Restore(self.camera.frame))
        # napsat pi
        self.play(Write(MathTex("\pi = ","3.1415928...").shift(2*DOWN+3*RIGHT)))
        self.wait(2)
        # prepsat vzorec s pi
        vzorec2=MathTex("O = ","2", "\\times", "\pi", "\\times", "r").scale(2).shift(DOWN+3*RIGHT)
        self.play(Transform(vzorec1, vzorec2))
        self.wait(2)
        # prepsat vzorec finalni podoba
        vzorec3=MathTex("O = ","2 ","\pi ","r").scale(2).shift(DOWN+3*RIGHT)
        self.play(Transform(vzorec1, vzorec3))
        self.wait()

class Kruh(Scene):
    def construct(self):
        # stred kruhu - doleva a trochu dolu
        center = 3*LEFT+0.5*DOWN
        # nadpis
        nadpis = Text("Kruh").scale(2).shift(3*UP)
        self.play(Write(nadpis))
        # kruh samotny
        circle = Circle().scale(2).shift(center).set_color(YELLOW).set_fill(YELLOW, opacity=1)
        self.play(GrowFromCenter(circle))
        # pridat kotu prumeru
        kota = Brace(circle)
        kota_text = kota.get_text("d = 2r")
        self.add(kota, kota_text)
        self.wait(2)
        # nadpis obsah
        obsah_text = Text("Obsah").shift(1.5*UP+3*RIGHT)
        self.play(Write(obsah_text))
        # vzorec obsah
        vzorec1 = MathTex("S = ","?").scale(2).shift(3*RIGHT)
        self.play(Write(vzorec1))
        self.wait(2)
        # kruh se zmeni na pole oblouku a ty na pole car
        arcs = []
        lines = []
        group = VGroup()
        for i in range (21):
            y = i*2.0/20
            arc = Arc(radius=y, start_angle=-PI/2, angle=2*PI, arc_center=center).set_color(YELLOW)
            arcs.append(arc)
            self.add(arcs[i])
            lines.append(Line(center+y*DOWN,center+y*DOWN+PI*y*RIGHT).set_color(YELLOW))
        # smazat kruh, zbydou oblouky
        self.remove(circle)
        # smazat kotu, prekazi
        self.remove(kota, kota_text)
        # pridat stin posledniho oblouku
        self.add(arcs[20].copy().set_stroke(YELLOW, opacity=0.5))
        self.wait(2)
        # oblouky -> lines
        for i in range (21):
            self.play(Transform(arcs[i], lines[i]))
        self.wait(2)
        # kota dole
        kota = Brace(lines[20])
        kota_text = kota.get_tex("2 \pi r")
        self.add(kota, kota_text)
        self.wait(2)
        # kota svisla
        svisla = Line(center,center+2*DOWN).set_stroke(GRAY, opacity=0)
        kota2 = Brace(svisla, direction=svisla.copy().rotate(-PI/2).get_unit_vector())
        kota2_text = kota2.get_text("r")
        self.add(svisla, kota2, kota2_text)
        self.wait(2)
        # prepsat vzorec - obsah trojuhelniku
        vzorec2 = MathTex("S = \\frac{1}{2} \\times r \\times 2 \pi r").scale(2).shift(3*RIGHT)
        self.play(Transform(vzorec1, vzorec2))
        self.wait(2)
        # prepsat vzorec finalni podoba
        vzorec3 = MathTex("S = \pi r^2").scale(2).shift(3*RIGHT)
        self.play(Transform(vzorec1, vzorec3))
        self.wait(2)

class Valec(ThreeDScene):
    def construct(self):
        # stred valce - doleva a dolu
        center = 3*LEFT+1.5*DOWN
        # nadpis
        nadpis = Text("Válec").scale(2).shift(3*UP)
        self.add_fixed_in_frame_mobjects(nadpis)
        self.play(Write(nadpis))
        # posunout kameru
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        # pridat osy a valec
        axes = ThreeDAxes().shift(center)
        valec = Cylinder(radius=2, height=3).shift(center)
        self.add(valec, axes)
        # pridat vyska - zatim neviditelna
        vyska = Line(start=center+2*LEFT+1.5*IN, end=center+2*LEFT+1.5*OUT).set_color(YELLOW).set_opacity(0)
        self.add(vyska)
        self.wait()
        # zatocit valcem
        self.begin_3dillusion_camera_rotation(rate=2)
        self.wait(3)
        self.stop_3dillusion_camera_rotation()
        self.wait(3)
        # pridat nadpis objem
        objem_text = Text("Objem").shift(1.5*UP+3*RIGHT)
        self.add_fixed_in_frame_mobjects(objem_text)
        self.play(Write(objem_text))
        # vzorec pro objem
        vzorec1 = MathTex("V = ","?").scale(2).shift(3*RIGHT)
        self.add_fixed_in_frame_mobjects(vzorec1)
        self.play(Write(vzorec1))
        self.wait(2)
        self.remove(vzorec1)
        vzorec2 = MathTex("V = ", "S", " \\times", " v").scale(2).shift(3*RIGHT)
        self.add_fixed_in_frame_mobjects(vzorec2)
        self.play(Write(vzorec2))
        self.wait(2)
        # posun kameru na pohled zhora
        self.remove(vzorec2)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, frame_center=center)
        self.wait(5)     
        # vzorec pro objem - prepsat S na pi*r^2
        vzorec3 = MathTex("V = ", "\pi r^2", " \\times", " v").scale(2).shift(3*RIGHT)
        self.add_fixed_in_frame_mobjects(vzorec3)
        self.play(Write(vzorec3))
        # zvyraznit pi*r^2
        framebox1 = SurroundingRectangle(vzorec3[1], buff = .1)
        self.add_fixed_in_frame_mobjects(framebox1)
        self.play(ShowCreationThenFadeOut(framebox1))
        self.wait()
        # posun kameru na bok
        self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, frame_center=center)
        self.wait()
        # ukazat vysku zlute
        vyska.set_opacity(1)
        # napsat 'v'
        kota_v = Text("v").shift(center+3*LEFT+0.3*UP).set_color(YELLOW)
        self.add_fixed_in_frame_mobjects(kota_v)
        self.add(kota_v)
        # zvyraznit vysku ve vzorci
        framebox2 = SurroundingRectangle(vzorec3[3], buff = .1)
        self.add_fixed_in_frame_mobjects(framebox2)
        self.play(ShowCreationThenFadeOut(framebox2))
        self.wait()
        # hotovo        


class Povrch(Scene):
    def construct(self):
        # stred kruhu - doleva a trochu dolu
        center = 3*LEFT+0.5*DOWN
        # nadpis
        nadpis = Text("Válec").scale(2).shift(3*UP)
        self.play(Write(nadpis))
        # pridat nadpis povrch
        povrch_text = Text("Povrch").shift(1.5*UP+3*RIGHT)
        self.play(Write(povrch_text))
        # vzorec povrch
        vzorec1 = MathTex("S = ","?").scale(2).shift(3*RIGHT)
        self.play(Write(vzorec1))
        self.wait(2)
        # kruhy
        circle1 = Circle().shift(center+1.5*UP+1*LEFT).set_color(YELLOW).set_fill(YELLOW, opacity=0.5)
        self.play(GrowFromCenter(circle1))
        rect = Rectangle(width=5, height=1.5).shift(center+0.25*DOWN+1*LEFT).set_color(YELLOW).set_fill(YELLOW, opacity=0.5)
        self.play(GrowFromCenter(rect))
        circle2 = Circle().shift(center+2*DOWN+1*LEFT).set_color(YELLOW).set_fill(YELLOW, opacity=0.5)
        self.play(GrowFromCenter(circle2))
        self.wait(2)
        circle1.set_fill(YELLOW, opacity=1)
        circle2.set_fill(YELLOW, opacity=1)
        self.wait(2)
        vzorec2 = MathTex("S = ","2 \\times \pi r^2", "+").scale(2).shift(DOWN+3*RIGHT)
        self.play(Transform(vzorec1, vzorec2))
        framebox1 = SurroundingRectangle(vzorec2[1], buff = .1)
        self.play(ShowCreationThenFadeOut(framebox1))
        self.wait(2)
        rect.set_fill(YELLOW, opacity=1)
        self.wait(2)
        vzorec3 = MathTex("2 \pi r \\times v").scale(2).shift(2*DOWN+3*RIGHT)
        self.play(Write(vzorec3))
        framebox2 = SurroundingRectangle(vzorec3[0], buff = .1)
        self.play(ShowCreationThenFadeOut(framebox2))
        self.wait(2)
        vzorec4 = MathTex("S = ","2 \pi r ( r + v )").scale(2).shift(DOWN+3*RIGHT)
        self.remove(vzorec3)
        self.play(Transform(vzorec1, vzorec4))        
        self.wait(2)


class Opakovani(Scene):
    def construct(self):
        # nadpis
        nadpis = Text("Opakování").scale(2).shift(3.25*UP)
        self.play(Write(nadpis))
        podnadpis1 = Text("Jak zní vzorec pro obvod kruhu?").shift(2*UP)
        self.play(Write(podnadpis1))
        # vzorce - obvod kruhu
        vzorec1 = MathTex("a) O = 2 \\pi d").scale(2).shift(3*LEFT)
        self.play(Write(vzorec1))
        self.wait(2)
        vzorec2 = MathTex("b) O = 2 \\pi r").scale(2).shift(2*DOWN+3*LEFT)
        self.play(Write(vzorec2))
        self.wait(2)
        vzorec3 = MathTex("c) O = \\pi d").scale(2).shift(3*RIGHT)
        self.play(Write(vzorec3))
        self.wait(2)
        vzorec4 = MathTex("d) O = \\pi r^2").scale(2).shift(2*DOWN+3*RIGHT)
        self.play(Write(vzorec4))
        self.wait(2)
        framebox1 = SurroundingRectangle(vzorec2[0], buff = .1)
        self.play(Create(framebox1))
        self.wait(2)
        framebox2 = SurroundingRectangle(vzorec3[0], buff = .1)
        self.play(Create(framebox2))
        self.wait(2)
        self.remove(vzorec1, vzorec2, vzorec3, vzorec4, framebox1, framebox2)

        podnadpis2 = Text("Jak zní vzorec pro obsah kruhu?").shift(2*UP)
        self.play(Transform(podnadpis1, podnadpis2))
        # vzorce - obvod kruhu
        vzorec1 = MathTex("a) S = 2 \\pi r^2").scale(2).shift(3*LEFT)
        self.play(Write(vzorec1))
        self.wait(2)
        vzorec2 = MathTex("b) S = \\pi d^2").scale(2).shift(2*DOWN+3*LEFT)
        self.play(Write(vzorec2))
        self.wait(2)
        vzorec3 = MathTex("c) S = \\pi r d").scale(2).shift(3*RIGHT)
        self.play(Write(vzorec3))
        self.wait(2)
        vzorec4 = MathTex("d) S = \\pi r^2").scale(2).shift(2*DOWN+3*RIGHT)
        self.play(Write(vzorec4))
        self.wait(2)
        framebox1 = SurroundingRectangle(vzorec4[0], buff = .1)
        self.play(Create(framebox1))
        self.wait(2)
        self.remove(vzorec1, vzorec2, vzorec3, vzorec4, framebox1)

        podnadpis3 = Text("Odhadněte plochu kruhu o průměru 4 metry").shift(2*UP)
        self.play(Transform(podnadpis1, podnadpis3))
        # vzorce - obvod kruhu
        vzorec1 = MathTex("a) S = 48m^2").scale(2).shift(3*LEFT)
        self.play(Write(vzorec1))
        self.wait(2)
        vzorec2 = MathTex("b) S = 12m^2").scale(2).shift(2*DOWN+3*LEFT)
        self.play(Write(vzorec2))
        self.wait(2)
        vzorec3 = MathTex("c) S = 16m^2").scale(2).shift(3*RIGHT)
        self.play(Write(vzorec3))
        self.wait(2)
        vzorec4 = MathTex("d) S = 22m^2").scale(2).shift(2*DOWN+3*RIGHT)
        self.play(Write(vzorec4))
        self.wait(2)
        framebox1 = SurroundingRectangle(vzorec2[0], buff = .1)
        self.play(Create(framebox1))
        vzorec5 = MathTex("r = 2m").shift(3.5*DOWN+2*LEFT)
        self.play(Write(vzorec5))
        vzorec6 = MathTex("S = \\pi \\times 2^2 \\approx 12m^2").shift(3.5*DOWN+2*RIGHT)
        self.play(Write(vzorec6))
        self.wait(2)
        self.remove(vzorec1, vzorec2, vzorec3, vzorec4, vzorec5, vzorec6, framebox1)
        self.wait(2)

        podnadpis4 = Text("Odhadněte obvod stejného kruhu (průměr 4m)").shift(2*UP)
        self.play(Transform(podnadpis1, podnadpis4))
        # vzorce - obvod kruhu
        vzorec1 = MathTex("a) O = 12m").scale(2).shift(3*LEFT)
        self.play(Write(vzorec1))
        self.wait(2)
        vzorec2 = MathTex("b) O = 6m").scale(2).shift(2*DOWN+3*LEFT)
        self.play(Write(vzorec2))
        self.wait(2)
        vzorec3 = MathTex("c) O = 16m").scale(2).shift(3*RIGHT)
        self.play(Write(vzorec3))
        self.wait(2)
        vzorec4 = MathTex("d) O = 8m").scale(2).shift(2*DOWN+3*RIGHT)
        self.play(Write(vzorec4))
        self.wait(2)
        framebox1 = SurroundingRectangle(vzorec1[0], buff = .1)
        self.play(Create(framebox1))
        vzorec5 = MathTex("d = 4m").shift(3.5*DOWN+2*LEFT)
        self.play(Write(vzorec5))
        vzorec6 = MathTex("O = \\pi \\times d \\approx 12m").shift(3.5*DOWN+2*RIGHT)
        self.play(Write(vzorec6))
        self.wait(2)
        self.remove(vzorec1, vzorec2, vzorec3, vzorec4, vzorec5, vzorec6, framebox1)
        self.wait(2)
