import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os, urllib.request

W, H = A4
CREAM = HexColor("#FFF8E7"); SURFACE = HexColor("#FFFEFA"); INK = HexColor("#4B3621"); INK_MUTED = HexColor("#8A6F52")
TAN_DEEP = HexColor("#A66A1C"); HAIRLINE = HexColor("#D8C7A8")

FONT_DIR = "/usr/share/fonts/truetype/nanum"
reg_path = os.path.join(FONT_DIR, "NanumGothic.ttf")
bold_path = os.path.join(FONT_DIR, "NanumGothicBold.ttf")
italic_path = os.path.join(FONT_DIR, "NanumGothic.ttf")
pdfmetrics.registerFont(TTFont("KR", reg_path))
pdfmetrics.registerFont(TTFont("KR-Bold", bold_path))
pdfmetrics.registerFont(TTFont("KR-Italic", italic_path))
kr_prop = fm.FontProperties(fname=reg_path)
kr_bold_prop = fm.FontProperties(fname=bold_path)

REPORT_DATE = "2026.08.23"
REPORT_RANGE = "2026.08.17 - 08.23"
OUT_PDF = "docs/reports/2026-08-23-ice-cream-trends.pdf"
COUNTRIES = [{'key': 'kr', 'name': '한국', 'flavor': '망고', 'soft': '#FFF3DC', 'mid': '#FFC259', 'deep': '#E67E22', 'headline': '망고가 편의점·프랜차이즈 아이스크림 시장을 뒤덮은 한 주', 'summary_paragraphs': ["GS25가 TXT 연준과 다시 손잡고 낸 사워레몬요거트 바가 2,500원에 출시되며 K팝 콜라보 마케팅을 이어갔습니다. 요아정·로로멜로와 협업한 이 제품은 연준 랜덤 포토카드를 동봉해 팬덤 소비를 유도했고, 컵 제품은 4,500원에 별도 판매됩니다. 배스킨라빈스는 배우 박지훈을 앞세운 8월 이달의 맛 '산딸기가 끌리는 연유'와 직영 한정 슈가케인 빙수 2종으로 여름 시즌을 공략했습니다.", "세븐일레븐은 리얼 과일모양 '망고스틴바'와 신맛 챌린지 '시다바'로 SNS 화제성을 유지했고, 일본 오하요유업과 협업한 '오하요 브륄레 밀크'는 출시 열흘 만에 20만 개가 팔리며 폭염 특수를 톡톡히 누렸습니다. 롯데웰푸드는 죠스바·스크류바에 젤리를 채운 신제품으로 Z세대의 '얼려먹는 젤리' 트렌드에 대응했습니다.", '업계 전반에서는 망고가 딸기를 제치고 이번 여름 가장 많이 쓰이는 맛으로 떠올랐으며, 기록적인 폭염 속에 GS25·세븐일레븐 등 주요 편의점의 8월 아이스크림 매출은 전년 대비 20% 안팎 늘었습니다.'], 'flavor_bars': [['망고', 6], ['딸기', 5], ['레몬', 3], ['초콜릿', 3], ['복숭아', 2]], 'pack_bars': [['리얼 과일모양', 5], ['화이트초콜릿 코팅', 4], ['젤리 인서트', 3], ['아이돌 콜라보 굿즈', 2], ['저당·저칼로리', 2]], 'content_bars': [['프로즌소르베 SNS 화제성', 120], ['오하요 브륄레밀크 리뷰 확산', 45], ['시다바 챌린지 영상', 28], ['망고스틴바 리뷰', 15], ['초코송이파르페 리뷰', 10]], 'refs_intro': '이번 리포트는 국내 언론사 기사와 Threads·X 등 웹검색으로 확인 가능한 SNS 게시물을 기반으로 작성됐으며, 인스타그램·틱톡 전체를 실시간 크롤링한 결과는 아닙니다.', 'refs': [{'num': 1, 'title': "GS25, TXT 연준·요아정·로로멜로 협업 '사워레몬요거트' 출시", 'note': '데일리매거진 보도, 팬덤 마케팅과 연계한 아이돌 콜라보 사례.', 'kind': '신제품', 'thumb_url': None}, {'num': 2, 'title': "세븐일레븐 '오하요 브륄레 밀크', 열흘 만에 20만개 판매", 'note': '헤럴드경제, 일본 오하요유업과의 협업 성과 보도.', 'kind': '뉴스', 'thumb_url': None}, {'num': 3, 'title': "배스킨라빈스 8월 이달의 맛 '산딸기가 끌리는 연유'", 'note': '한국경제, 박지훈 광고모델 캠페인 소개.', 'kind': '광고', 'thumb_url': None}, {'num': 4, 'title': '롯데웰푸드, 젤리 넣은 죠스바·스크류바 출시', 'note': '디지틀조선일보, Z세대 트렌드 반영 신제품.', 'kind': '신제품', 'thumb_url': None}, {'num': 5, 'title': '"딸기 가고 망고 온다" 여름 디저트 시장 조기 공략', 'note': '서울파이낸스, 업계 전반의 망고 트렌드 분석.', 'kind': '뉴스', 'thumb_url': None}]}, {'key': 'us', 'name': '미국', 'flavor': '호박', 'soft': '#F3E3D8', 'mid': '#D9A26B', 'deep': '#A66A1C', 'headline': '미국은 벌써 가을 맛으로, 호박·카라멜애플이 앞장서다', 'summary_paragraphs': ['Publix rolled out five fall-limited flavors — pumpkin pie, apple cinnamon, brown sugar cinnamon streusel, eggnog and a banana-brown-sugar-rum swirl — in pints and half gallons, and Dairy Queen previewed a caramel-apple-cheesecake and brown-sugar-cookie-dough Blizzard lineup for an August 26 launch. The back-to-school season is once again pulling menus from summer toward fall flavors earlier than usual, trade press noted.', "Baskin Robbins kept its Brookie Batter and Oreo S'mores collaboration going through August alongside its 'Sundae Scaries' charity promotion, donating a portion of Sunday sundae sales to a children's foundation. Ben & Jerry's drew crowds to a free ice-cream-bar pop-up in Brooklyn, New York, part of its multi-city 'Great Summer Bar Drop' tour, while United Dairy Farmers and Grippo's launched a Cincinnati-only buttered-popcorn barbecue-caramel collaboration.", 'A viral TikTok claiming to show something resembling maggots in ice cream made with a Ninja Creami home maker spread widely this week, prompting many owners to inspect their own machines — an unplanned consumer-safety story that outpaced most branded marketing in social reach.'], 'flavor_bars': [['호박', 4], ['카라멜애플', 3], ['브라운슈가', 3], ['초콜릿·브라우니', 3], ['딸기', 2]], 'pack_bars': [['파인트', 4], ['아이스크림바', 3], ['블리자드·소프트서브 컵', 2], ['하프갤런', 1], ['쿼트', 1]], 'content_bars': [['닌자크리미 이물질 틱톡 확산', 85], ['벤앤제리스 서머바드롭 이벤트 반응', 30], ['퍼블릭스 가을맛 기사 확산', 20], ['데어리퀸 가을블리자드 예고 반응', 18], ['배스킨라빈스 브루키배터 리뷰', 12]], 'refs_intro': '이번 주 미국 시장 리서치는 현지 언론과 웹검색으로 확인 가능한 SNS 게시물을 기반으로 작성됐으며, 인스타그램·틱톡 전체 크롤링 결과는 아닙니다.', 'refs': [{'num': 1, 'title': 'Publix announces limited-edition fall ice cream flavors', 'note': 'ClickOrlando, full five-flavor lineup and pricing.', 'kind': '신제품', 'thumb_url': None}, {'num': 2, 'title': 'Viral TikTok has Ninja Creami users checking their machines', 'note': "Click2Houston, consumer-safety story driving this week's largest social reach.", 'kind': '바이럴', 'thumb_url': None}, {'num': 3, 'title': "Dairy Queen's fall 2026 menu: two new Blizzard flavors", 'note': 'Parade, caramel apple cheesecake and brown sugar cookie dough preview.', 'kind': '뉴스', 'thumb_url': None}, {'num': 4, 'title': "Ben & Jerry's Great Summer Bar Drop hits NYC", 'note': 'PRNewswire, Brooklyn pop-up giveaway details.', 'kind': '광고', 'thumb_url': None}, {'num': 5, 'title': 'Baskin Robbins turns Sunday sundaes into support for children in need', 'note': 'QSR Magazine, Sundae Scaries charity campaign.', 'kind': '광고', 'thumb_url': None}]}, {'key': 'jp', 'name': '일본', 'flavor': '초코', 'soft': '#EFDDD0', 'mid': '#C89173', 'deep': '#6B4226', 'headline': '초콜릿과 배(나시) 아이스가 일본 편의점 진열대를 양분하다', 'summary_paragraphs': ["세븐일레븐은 배 과즙 52%를 담은 2단계 식감의 '마루데 와나시'에 이어, 마스카르포네·코코아파우더·커피소스를 넣은 빙수형 디저트 '티라미스氷'로 mognavi 주간 아이스 랭킹 1위에 올랐습니다. 3년 만에 부활한 이 상품에 더해 모리나가 제조 한정판 '판초코아이스 카라멜푸딩맛', 홍차&오렌지젤리 컵디저트까지 겹치며 세븐일레븐은 이번 주 가장 활발한 브랜드로 떠올랐습니다.", "롯데는 소 사치과실 시리즈 네 번째로 샤인머스캣 쥬레를 넣은 신제품을 전국 발매했고, 모리나가유업은 '바리체 초코&민트'를 편의점 선행 판매 후 전국으로 확대했습니다. 이무라야는 얼음 식감 시리즈 4탄 '샤리리 초콜릿아이스'를, 글리코는 파피코 멀티팩에 초코커피맛을 새로 더하며 초콜릿 계열이 이번 주 가장 많이 반복된 맛으로 나타났습니다.", "아카기유업은 나리타 공항에 후지산·벚꽃 디자인 광고를 걸고 다언어 패키지 배맛 '가리가리군'으로 인바운드 관광객을 겨냥한 마케팅을 9월까지 이어가고 있으며, 롯데는 9월 상순 출시 예정인 가을 한정 유키미다이후쿠 '오츠키미' 패키지를 예고했습니다."], 'flavor_bars': [['초코', 4], ['배', 3], ['캐러멜', 2], ['샤인머스캣', 2], ['커피·티라미스', 2]], 'pack_bars': [['기간한정', 4], ['편의점 한정판', 4], ['수량한정', 2], ['컵·빙수 타입', 2], ['다언어 패키지', 1]], 'content_bars': [['티라미스氷 랭킹1위 화제', 60], ['마루데와나시 리뷰 확산', 35], ['판초코아이스 카라멜푸딩 SNS', 22], ['소 샤인머스캣 기사 확산', 15], ['가리가리군 인바운드 캠페인 반응', 10]], 'refs_intro': '이 섹션은 일본 언론·업계 매체 기사와 웹검색으로 확인 가능한 정보를 바탕으로 작성됐으며, 인스타그램·틱톡 전체 크롤링 결과는 아닙니다.', 'refs': [{'num': 1, 'title': 'ロッテ「爽 贅沢果実シャインマスカット」プレスリリース', 'note': '롯데 공식, 소 시리즈 4탄 전국 발매 소식.', 'kind': '신제품', 'thumb_url': None}, {'num': 2, 'title': '森永製菓「板チョコアイス カラメルプリン味」8/19発売', 'note': '모리나가제과 공식, 세븐일레븐 한정 상품 발매.', 'kind': '신제품', 'thumb_url': None}, {'num': 3, 'title': 'mognavi「2026年8月第4週」アイスランキング', 'note': "세븐일레븐 '티라미스氷' 주간 랭킹 1위 소식.", 'kind': '바이럴', 'thumb_url': None}, {'num': 4, 'title': 'えん食べ、セブン・ファミマ・ローソン新作スイーツまとめ', 'note': '8월 셋째 주 편의점 3사 신상품 정리.', 'kind': '뉴스', 'thumb_url': None}, {'num': 5, 'title': '赤城乳業「ガリガリ君」インバウンド向けPR施策', 'note': '아카기유업 공식, 나리타 공항 광고 캠페인.', 'kind': '광고', 'thumb_url': None}]}]
OVERVIEW = {'highlights': [('#E67E22', '한국은 폭염 속 망고가 딸기를 제치고 최다 언급 맛으로 부상'), ('#A66A1C', '미국은 호박·카라멜애플 등 가을 맛으로 조기 전환'), ('#6B4226', '일본은 세븐일레븐이 신제품 연달아 내며 랭킹 1위 석권')], 'table_rows': [('한국', '망고', '6', '5', '망고·딸기·레몬', '#FFF3DC'), ('미국', '호박', '3', '2', '호박·카라멜애플', '#F3E3D8'), ('일본', '초코', '7', '3', '초코·배·캐러멜', '#EFDDD0')], 'analysis': '이번 주 세 시장은 각기 다른 계절 감각으로 갈렸습니다. 한국은 기록적 폭염 속에 망고·딸기 등 여름 과일 맛과 K팝·캐릭터 콜라보가 편의점 채널을 중심으로 강세를 보였고, GS25·세븐일레븐의 아이스크림 매출은 전년 대비 20% 안팎 늘었습니다. 반면 미국은 개학 시즌과 맞물려 호박·카라멜애플·브라운슈가 등 가을 맛이 예년보다 이르게 등장했고, 정작 이번 주 가장 큰 화제는 브랜드 마케팅이 아닌 닌자 크리미 이물질 논란이라는 소비자 안전 이슈였습니다. 일본은 세븐일레븐이 배·티라미스·초콜릿 신제품을 연달아 내며 주간 랭킹 1위까지 차지해 이번 주 가장 활발한 단일 브랜드로 떠올랐고, 초콜릿 계열이 여러 제조사에 걸쳐 반복 등장했습니다. 세 시장을 종합하면 편의점·프랜차이즈 채널이 신제품 발매 속도를 주도하는 흐름은 공통적이나, 소비자의 관심을 끄는 축은 한국(계절 맛·아이돌 콜라보), 미국(시즌 전환·안전 이슈), 일본(브랜드 경쟁·연속 발매)으로 각기 달랐습니다.'}

os.makedirs(os.path.dirname(OUT_PDF), exist_ok=True)
c = canvas.Canvas(OUT_PDF, pagesize=A4)
TMP = os.path.join(os.path.dirname(OUT_PDF) or ".", "_pdf_tmp")
os.makedirs(TMP, exist_ok=True)

def bg():
    c.setFillColor(CREAM); c.rect(0, 0, W, H, fill=1, stroke=0)

def wrap_text(text, font, size, max_width):
    c.setFont(font, size)
    lines, cur = [], ""
    for ch in text:
        test = cur + ch
        if c.stringWidth(test, font, size) > max_width and cur:
            lines.append(cur); cur = ch
        else:
            cur = test
    if cur: lines.append(cur)
    return lines

def draw_paragraph(text, x, y, max_width, font="KR", size=10, leading=15.5, color=INK):
    c.setFont(font, size); c.setFillColor(color)
    for line in wrap_text(text, font, size, max_width):
        c.drawString(x, y, line); y -= leading
    return y

def draw_box(x, y, w, h, radius=3.5*mm):
    c.setFillColor(SURFACE); c.roundRect(x, y, w, h, radius, fill=1, stroke=0)
    c.setStrokeColor(HAIRLINE); c.setLineWidth(0.6); c.roundRect(x, y, w, h, radius, fill=0, stroke=1)

def draw_boxed_paragraphs(paras, x, y, box_width, font="KR", size=10, leading=15.5, color=INK, pad=6*mm, gap=3*mm):
    all_lines = [wrap_text(p, font, size, box_width - 2*pad) for p in paras]
    total_lines = sum(len(l) for l in all_lines)
    box_h = total_lines*leading + 2*pad + (len(paras)-1)*4*mm
    draw_box(x, y-box_h, box_width, box_h)
    ty = y - pad - size*0.8
    c.setFont(font, size); c.setFillColor(color)
    for lines in all_lines:
        for line in lines:
            c.drawString(x+pad, ty, line); ty -= leading
        ty -= 4*mm
    return y - box_h - gap

def hexrgb(h):
    h = h.lstrip("#"); return tuple(int(h[i:i+2], 16)/255 for i in (0,2,4))

def lerp(c1, c2, t):
    return tuple(a+(b-a)*t for a,b in zip(c1,c2))

def draw_tri_gradient(x, y, w, h, hex1, hex2, hex3, steps=140):
    c1_, c2_, c3_ = hexrgb(hex1), hexrgb(hex2), hexrgb(hex3)
    sw = w/steps
    for i in range(steps):
        t = i/(steps-1)
        col = lerp(c1_, c2_, t/0.5) if t < 0.5 else lerp(c2_, c3_, (t-0.5)/0.5)
        c.setFillColorRGB(*col); c.rect(x+i*sw, y, sw+0.6, h, fill=1, stroke=0)

def download_thumb(url, dest):
    try:
        urllib.request.urlretrieve(url, dest)
        return dest
    except Exception:
        return None

def draw_thumb_or_placeholder(x, y, size, url, kind_label, accent_hex):
    path = None
    if url:
        path = download_thumb(url, os.path.join(TMP, f"thumb_{abs(hash(url))}.jpg"))
    if path and os.path.exists(path):
        try:
            c.drawImage(path, x, y, width=size, height=size, mask='auto', preserveAspectRatio=True, anchor='c')
            return
        except Exception:
            pass
    c.setFillColor(HexColor(accent_hex))
    c.roundRect(x, y, size, size, 2*mm, fill=1, stroke=0)
    c.setFont("KR-Bold", 8); c.setFillColor(SURFACE)
    c.drawCentredString(x+size/2, y+size/2-3, kind_label)

def make_bar_chart(path, labels, values, color, title):
    fig, ax = plt.subplots(figsize=(3.1, 2.0), dpi=200)
    ypos = list(range(len(labels)))
    ax.barh(ypos[::-1], values, color=color, height=0.55)
    ax.set_yticks(ypos[::-1]); ax.set_yticklabels(labels, fontproperties=kr_prop, fontsize=8)
    ax.set_title(title, fontproperties=kr_bold_prop, fontsize=9, loc="left", color="#4B3621")
    for s in ["top","right","left"]: ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#D8C7A8")
    ax.tick_params(colors="#4B3621", labelsize=7.5); ax.set_xticks([])
    for i, v in enumerate(values[::-1]):
        ax.text(v+max(values)*0.02, i, str(v), va="center", fontsize=7.5, color="#4B3621")
    fig.tight_layout(); fig.savefig(path, transparent=True); plt.close(fig)

margin = 14*mm

bg()
fx0, fy0, fx1, fy1 = margin, margin, W-margin, H-margin
c.setStrokeColor(INK); c.setLineWidth(1.4); c.rect(fx0, fy0, fx1-fx0, fy1-fy0, fill=0, stroke=1)
c.setLineWidth(0.5); c.rect(fx0+3*mm, fy0+3*mm, fx1-fx0-6*mm, fy1-fy0-6*mm, fill=0, stroke=1)

c.setFont("KR-Italic", 12); c.setFillColor(INK_MUTED)
c.drawCentredString(W/2, H-58*mm, "SCOOP REPORT")
c.drawCentredString(W/2, H-65*mm, "Weekly Ice Cream Intelligence")

c.setFont("KR-Bold", 40); c.setFillColor(INK)
c.drawCentredString(W/2, H-100*mm, "아이스크림")
c.drawCentredString(W/2, H-116*mm, "트렌드 리포트")

c.setFont("KR", 11); c.setFillColor(INK_MUTED)
c.drawCentredString(W/2, H-132*mm, f"{REPORT_DATE}  ·  한국 · 미국 · 일본 3개 시장 종합")

band_h = 46*mm
mids = [ctry["mid"] for ctry in COUNTRIES] + ["#B7CE8C", "#C98A7C"]
draw_tri_gradient(fx0+3*mm, fy0+3*mm, fx1-fx0-6*mm, band_h, mids[0], mids[1], mids[2])
cx, cy = W/2, fy0+3*mm+band_h/2
c.setFillColor(SURFACE); c.circle(cx, cy, 13*mm, fill=1, stroke=0)
c.setFillColor(TAN_DEEP); c.circle(cx, cy-2*mm, 5.2*mm, fill=1, stroke=0)
p = c.beginPath(); p.moveTo(cx-4.2*mm, cy-1*mm); p.lineTo(cx+4.2*mm, cy-1*mm); p.lineTo(cx, cy-11*mm); p.close()
c.drawPath(p, fill=1, stroke=0)
c.showPage()

bg()
top = H-20*mm
c.setFont("KR-Bold", 10); c.setFillColor(INK_MUTED)
c.drawString(margin, top, "SCOOP REPORT"); c.drawRightString(W-margin, top, "02")
c.setStrokeColor(HAIRLINE); c.line(margin, top-4*mm, W-margin, top-4*mm)

y = top-16*mm
colw = (W-2*margin-10*mm)/2
c.setFont("KR-Bold", 11); c.setFillColor(INK); c.drawString(margin, y, "리포트 정보")
info_rows = [("리포트","주간 아이스크림 트렌드"), ("기간",REPORT_RANGE), ("발행일",f"{REPORT_DATE} (월)"), ("작성","Scoop Report 자동 리서치")]
box1_top = y-6*mm
box1_h = len(info_rows)*7*mm + 8*mm
draw_box(margin, box1_top-box1_h, colw, box1_h)
y2 = box1_top-6*mm
for label, val in info_rows:
    c.setFont("KR", 9); c.setFillColor(INK_MUTED); c.drawString(margin+5*mm, y2, label)
    c.setFont("KR", 9.5); c.setFillColor(INK); c.drawString(margin+27*mm, y2, val)
    y2 -= 7*mm

x2 = margin+colw+10*mm
c.setFont("KR-Bold", 11); c.setFillColor(INK); c.drawString(x2, y, "이번 주 하이라이트")
box2_h = len(OVERVIEW["highlights"])*12*mm + 6*mm
draw_box(x2, box1_top-box2_h, colw, box2_h)
yy = box1_top-9*mm
for col, text in OVERVIEW["highlights"]:
    c.setFillColor(HexColor(col)); c.circle(x2+6.2*mm, yy+1.2*mm, 1.2*mm, fill=1, stroke=0)
    c.setFont("KR", 9.3); c.setFillColor(INK)
    for i, line in enumerate(wrap_text(text, "KR", 9.3, colw-14*mm)):
        c.drawString(x2+10*mm, yy-i*5.2*mm, line)
    yy -= 12*mm

y = box1_top-box1_h-12*mm
c.setFont("KR-Bold", 11); c.setFillColor(INK); c.drawString(margin, y, "국가별 요약 대시보드"); y -= 6*mm
headers = ["국가","시그니처 맛","신제품","바이럴","Top 키워드"]
colws = [22*mm, 34*mm, 20*mm, 20*mm, 60*mm]
draw_tri_gradient(margin, y-7*mm, sum(colws), 7*mm, COUNTRIES[0]["deep"], "#7E9A4E", "#8C3A2E")
cx0 = margin
c.setFont("KR-Bold", 9); c.setFillColor(SURFACE)
for h, w in zip(headers, colws):
    c.drawString(cx0+3*mm, y-5*mm, h); cx0 += w
ry = y-7*mm
for name, flavor, new, viral, kw, soft in OVERVIEW["table_rows"]:
    c.setFillColor(HexColor(soft)); c.rect(margin, ry-8*mm, sum(colws), 8*mm, fill=1, stroke=0)
    cx0 = margin
    for v, w in zip([name, flavor, new, viral, kw], colws):
        c.setFont("KR", 9); c.setFillColor(INK); c.drawString(cx0+3*mm, ry-5.5*mm, v); cx0 += w
    ry -= 8*mm
c.setStrokeColor(HAIRLINE); c.setLineWidth(0.6)
c.roundRect(margin, ry, sum(colws), (y-7*mm)-ry+7*mm, 3.5*mm, fill=0, stroke=1)

y = ry-12*mm
c.setFont("KR-Bold", 11); c.setFillColor(INK); c.drawString(margin, y, "종합 분석"); y -= 7*mm
draw_boxed_paragraphs([OVERVIEW["analysis"]], margin, y, W-2*margin, size=9.8, leading=15.5)
c.showPage()

page_num = 3
for ctry in COUNTRIES:
    bg()
    top = H-20*mm
    c.setFont("KR-Bold", 10); c.setFillColor(INK_MUTED)
    c.drawString(margin, top, f"SCOOP REPORT · {ctry['name']}"); c.drawRightString(W-margin, top, f"{page_num:02d}")
    c.setStrokeColor(HAIRLINE); c.line(margin, top-4*mm, W-margin, top-4*mm)

    y = top-14*mm
    c.setFillColor(HexColor(ctry["soft"])); c.rect(margin, y-16*mm, W-2*margin, 16*mm, fill=1, stroke=0)
    c.setFont("KR-Bold", 9); c.setFillColor(HexColor(ctry["deep"]))
    c.drawString(margin+6*mm, y-6*mm, f"이주의 시그니처 · {ctry['flavor']}")
    c.setFont("KR-Bold", 15); c.setFillColor(INK)
    c.drawString(margin+6*mm, y-13*mm, ctry["headline"])

    y -= 22*mm
    y = draw_boxed_paragraphs(ctry["summary_paragraphs"], margin, y, W-2*margin, size=10, leading=15.5)

    y -= 4*mm
    c.setFont("KR-Bold", 10.5); c.setFillColor(INK); c.drawString(margin, y, "차트로 보는 이번 주"); y -= 6*mm
    f1 = os.path.join(TMP, f"{ctry['key']}_c1.png"); f2 = os.path.join(TMP, f"{ctry['key']}_c2.png"); f3 = os.path.join(TMP, f"{ctry['key']}_c3.png")
    fl = [x[0] for x in ctry["flavor_bars"]]; fv = [x[1] for x in ctry["flavor_bars"]]
    pl = [x[0] for x in ctry["pack_bars"]]; pv = [x[1] for x in ctry["pack_bars"]]
    cl = [x[0] for x in ctry["content_bars"]]; cvv = [x[1] for x in ctry["content_bars"]]
    make_bar_chart(f1, fl, fv, ctry["deep"], "맛(Flavor) Top 5")
    make_bar_chart(f2, pl, pv, ctry["mid"], "패키징 Top 5")
    make_bar_chart(f3, cl, cvv, ctry["deep"], "콘텐츠별 조회/추천수(만)")
    chart_w = (W-2*margin-2*8*mm-2*6*mm)/3; img_h = chart_w*0.65
    chart_box_h = img_h + 12*mm
    draw_box(margin, y-chart_box_h, W-2*margin, chart_box_h)
    for i, img in enumerate([f1, f2, f3]):
        cxp = margin+6*mm+i*(chart_w+8*mm)
        c.drawImage(img, cxp, y-6*mm-img_h, width=chart_w, height=img_h, mask='auto')
    y -= chart_box_h+10*mm

    c.setFont("KR-Bold", 10.5); c.setFillColor(INK); c.drawString(margin, y, "참고자료 분석"); y -= 6*mm
    thumb_sz = 16*mm; pad = 6*mm
    intro_lines = wrap_text(ctry["refs_intro"], "KR", 9, W-2*margin-2*pad)
    refs_box_h = len(intro_lines)*13 + 5*mm + len(ctry["refs"])*(thumb_sz+5*mm) + 2*pad
    draw_box(margin, y-refs_box_h, W-2*margin, refs_box_h)
    y -= pad
    c.setFont("KR", 9); c.setFillColor(INK_MUTED)
    for line in intro_lines:
        c.drawString(margin+pad, y-8, line); y -= 13
    y -= 5*mm
    for ref in ctry["refs"]:
        row_top = y
        draw_thumb_or_placeholder(margin+pad, row_top-thumb_sz+2, thumb_sz, ref["thumb_url"], ref["kind"], ctry["deep"])
        tx0 = margin+pad+thumb_sz+4*mm
        c.setFont("KR-Bold", 9); c.setFillColor(INK)
        c.drawString(tx0, row_top, f"{ref['num']}.  {ref['title']}")
        ny = draw_paragraph(ref["note"], tx0, row_top-5*mm, W-margin-pad-tx0, size=8.5, leading=12.5, color=INK_MUTED)
        y = min(ny, row_top-thumb_sz)-5*mm

    c.showPage()
    page_num += 1

c.save()
