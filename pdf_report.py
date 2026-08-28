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

REPORT_DATE = "2026.08.28"
REPORT_RANGE = "2026.08.21 - 08.28"
OUT_PDF = "docs/reports/2026-08-28-ice-cream-trends.pdf"
COUNTRIES = [
    {
        'key': 'kr', 'name': '한국', 'flavor': '딸기',
        'soft': '#FCEAF0', 'mid': '#F6A9BE', 'deep': '#C85476',
        'headline': '기록적 폭염 속 딸기 아이스크림과 편의점 콜라보 열풍',
        'summary_paragraphs': [
            "기록적인 폭염이 이어지며 편의점 아이스크림 매출이 급증한 가운데, 배스킨라빈스는 '산딸기가 끌리는 연유'를 8월 이달의 맛으로 내세워 딸기 트렌드를 이끌고 있습니다. 배우 박지훈을 광고모델로 기용하고 싱글레귤러를 더블주니어로 업그레이드해주는 여름 프로모션도 함께 진행 중입니다.",
            "GS25는 현대자동차와 손잡은 '현차는 빵빵'에 이어 TXT 연준·요아정·로로멜로와 3자 협업한 '사워레몬요거트'를 잇달아 선보이며 콜라보 마케팅 경쟁에 불을 지폈습니다. 세븐일레븐의 '오하요 브륄레 밀크'는 일본 오하요유업과 협업해 출시 열흘 만에 20만개가 팔렸고, 3단계 신맛 아이스바 '시다바'도 SNS 챌린지 콘텐츠로 확산되고 있습니다.",
            "한국마즈는 스니커즈·트윅스를 아이스바로 국내 최초 출시해 GS25·CU·세븐일레븐에 동시 입점시켰고, CU의 저당 아이스바 '라라스윗'은 6월부터 1+1 프로모션을 이어가고 있습니다. 42.5도까지 치솟은 폭염 속에 아이스크림 관련 검색량은 일주일 새 3배 가까이 늘어난 것으로 추정됩니다.",
        ],
        'flavor_bars': [['딸기', 10], ['초콜릿', 7], ['크림브륄레', 5], ['신맛', 4], ['커피', 3]],
        'pack_bars': [['과일 모양', 6], ['캐릭터 콜라보', 5], ['젤리 인클루전', 4], ['저당 헬시', 4], ['브랜드 콜라보 외형', 3]],
        'content_bars': [['오하요 브륄레 밀크', 18], ['GS25 아이스크림 대란', 12], ['신맛질주 시다바', 9], ['산딸기 연유', 7], ['스니커즈 아이스바', 5]],
        'refs_intro': '이번 리포트는 국내 언론사 기사와 Threads·X 등 웹검색으로 확인 가능한 SNS 게시물을 기반으로 작성됐으며, 인스타그램·틱톡 전체를 실시간 크롤링한 결과는 아닙니다.',
        'refs': [
            {'num': 1, 'title': "세븐일레븐, 일본 협업 '오하요 브륄레 밀크' 열흘만에 20만개", 'note': '헤럴드경제, 일본 오하요유업과의 협업 성과 보도.', 'kind': '신제품', 'thumb_url': None},
            {'num': 2, 'title': "GS25, 현대자동차와 '현차는 빵빵' 아이스크림 출시", 'note': '헤럴드경제, 자동차 브랜드 굿즈 결합 콜라보 소식.', 'kind': '신제품', 'thumb_url': None},
            {'num': 3, 'title': "배스킨라빈스 8월 이달의 맛 '산딸기가 끌리는 연유'", 'note': '한국경제, 박지훈 광고모델 캠페인 소개.', 'kind': '신제품', 'thumb_url': None},
            {'num': 4, 'title': "'아이스크림 대란' GS25 콘 9개 9,900원 완판 행렬", 'note': 'Threads, 편의점 아이스크림 품절 SNS 화제.', 'kind': 'SNS', 'thumb_url': None},
            {'num': 5, 'title': '기록적 폭염에 아이스크림 검색량 일주일 새 3배 급증', 'note': 'Nate뉴스, 폭염과 편의점 매출 특수 분석.', 'kind': '뉴스', 'thumb_url': None},
        ],
    },
    {
        'key': 'us', 'name': '미국', 'flavor': '초코',
        'soft': '#EFDDD0', 'mid': '#C89173', 'deep': '#6B4226',
        'headline': '미국, 초콜릿과 캐러멜애플 앞세워 가을 시즌 조기 전환',
        'summary_paragraphs': [
            "Dairy Queen kicked off fall flavor season with the Caramel Apple Cheesecake Blizzard, running through August 30 with a buy-one-get-one deal for app members. Publix followed with a five-flavor fall grocery lineup spanning banana-brown-sugar-rum, brown sugar cinnamon streusel and apple varieties, signaling an industry-wide early pivot to autumn.",
            "Blue Bell debuted its first new flavor of 2026, Honey Vanilla, while Cold Stone Creamery and Trader Joe's leaned into loaded, chocolate-and-peanut-butter-driven treats. Ben & Jerry's ran a free 'Great Summer Bar Drop' giveaway tour in Brooklyn, and Van Leeuwen partnered with singer Laufey on a limited fro-yo benefiting her foundation.",
            "The week's biggest viral moment came from Costco's hyper-realistic 3D fruit-shaped ice bars from Aiko Garden, which sold out fast as 'cut-open reveal' videos spread on TikTok, alongside a separate trend of stuffing whole Magnum bars into hollowed-out croissants — the so-called 'Cragnum' hack.",
        ],
        'flavor_bars': [['캐러멜애플', 4], ['초콜릿', 4], ['브라운슈거', 3], ['땅콩버터', 3], ['베리', 3]],
        'pack_bars': [['파인트', 5], ['바(스틱형)', 5], ['버라이어티팩', 3], ['한정판', 3], ['쿼트', 2]],
        'content_bars': [['3D 과일 아이스바', 35], ['크래그넘 레시피', 28], ['콜드스톤 콜라보', 14], ['DQ 블리자드', 11], ['벤앤제리스 이벤트', 9]],
        'refs_intro': '이번 주 미국 시장 리서치는 현지 언론과 웹검색으로 확인 가능한 SNS 게시물을 기반으로 작성됐으며, 인스타그램·틱톡 전체 크롤링 결과는 아닙니다.',
        'refs': [
            {'num': 1, 'title': 'Dairy Queen Kicks Off Fall With Caramel Apple Cheesecake Blizzard', 'note': 'Tasting Table, 8월 3일부터 30일까지 진행되는 신메뉴 소식.', 'kind': '신제품', 'thumb_url': None},
            {'num': 2, 'title': 'Blue Bell Debuts Honey Vanilla, Its First New Flavor of 2026', 'note': 'KRIS TV, 2026년 첫 신맛 출시 보도.', 'kind': '신제품', 'thumb_url': None},
            {'num': 3, 'title': "Costco's Hyper-Realistic 3D Fruit Ice Bars Go Viral on TikTok", 'note': 'Anka Foods, 코스트코 아이코가든 3D 아이스바 확산.', 'kind': '바이럴', 'thumb_url': None},
            {'num': 4, 'title': "Stuffing a Whole Magnum Bar Into a Croissant Goes Viral", 'note': 'Food Republic, 크래그넘 SNS 레시피 유행.', 'kind': 'SNS', 'thumb_url': None},
            {'num': 5, 'title': "Ben & Jerry's Great Summer Bar Drop Hits NYC", 'note': 'Dairy Foods, 브루클린 무료 증정 투어 보도.', 'kind': '광고', 'thumb_url': None},
        ],
    },
    {
        'key': 'jp', 'name': '일본', 'flavor': '호지차',
        'soft': '#F1E4D3', 'mid': '#C9A579', 'deep': '#8B5E34',
        'headline': '호지차·샤인머스캣 프리미엄 라인과 원신 콜라보 예약 개시',
        'summary_paragraphs': [
            "세븐일레븐 재팬은 누적 2.2억개 판매를 넘은 '마루데' 시리즈의 여름 신작으로 배맛에 이어 쿄호 포도맛을 8월 25일부터 순차 발매했습니다. 롯데·메이지 등도 같은 주에 독립적으로 포도·머스캣 계열 신제품을 내놓으며 카테고리 전반의 쏠림이 뚜렷했습니다.",
            "하겐다즈 재팬은 땅콩버터와 버터캐러멜을 바삭한 웨하스로 감싼 크리스피 샌드 신제품을 선보였고, 이무라야는 우지 호지차를 사용한 3층 구조의 화과자풍 아이스 '야와모찌 호지차와라비'를 8월 31일부터 계절 한정으로 출시합니다. 호지차 계열은 프리미엄·화과자 라인에서 지속적으로 강세를 보이고 있습니다.",
            "원신과 배스킨라빈스 재팬의 첫 콜라보 사전예약이 오늘(8월 28일) 오전 11시부터 시작되며 게임 팬덤 사이에서 큰 화제를 모으고 있고, 인기 코미디 듀오 카마이타치의 편의점 신상 아이스 리뷰 영상도 꾸준히 조회수를 쌓고 있습니다. 가리가리군은 20주년을 맞아 포도맛 신상과 축구 유니폼 증정 캠페인을 동시에 전개 중입니다.",
        ],
        'flavor_bars': [['샤인머스캣', 5], ['호지차', 4], ['복숭아', 3], ['멜론', 3], ['버터캐러멜', 3]],
        'pack_bars': [['미니컵', 5], ['바/스틱형', 4], ['한입 소포장', 3], ['박스 리뉴얼', 2], ['콜라보 굿즈', 2]],
        'content_bars': [['원신 콜라보 예약', 40], ['카마이타치 리뷰', 30], ['3D 과일 아이스', 22], ['가리가리군 캠페인', 15], ['하겐다즈 신작', 10]],
        'refs_intro': '이 섹션은 일본 언론·업계 매체 기사와 웹검색으로 확인 가능한 정보를 바탕으로 작성됐으며, 인스타그램·틱톡 전체 크롤링 결과는 아닙니다.',
        'refs': [
            {'num': 1, 'title': 'セブン-イレブン、梨・巨峰の「まるで」シリーズ夏の新作を発売', 'note': 'SEJ 공식, 마루데 시리즈 여름 신작 소식.', 'kind': '신제품', 'thumb_url': None},
            {'num': 2, 'title': 'ハーゲンダッツ、ピーナッツバター×バターキャラメルのクリスピーサンド発売', 'note': 'entabe, 크리스피 샌드 신제품 보도.', 'kind': '신제품', 'thumb_url': None},
            {'num': 3, 'title': '井村屋、ほうじ茶わらび餅風アイス「やわもちアイス」発売', 'note': 'Imuraya 공식, 호지차 화과자풍 아이스 소식.', 'kind': '신제품', 'thumb_url': None},
            {'num': 4, 'title': '原神×サーティワン、初コラボの事前予約が本日スタート', 'note': 'PR TIMES, 게임 콜라보 사전예약 개시 소식.', 'kind': '광고', 'thumb_url': None},
            {'num': 5, 'title': 'かまいたち、2026年コンビニ新作アイスレビュー動画が話題', 'note': 'YouTube, 코미디 듀오 편의점 아이스 리뷰 영상.', 'kind': '바이럴', 'thumb_url': None},
        ],
    },
]
OVERVIEW = {
    'highlights': [
        ('#C85476', '한국, 폭염 특수 속 딸기 신맛 트렌드와 편의점 콜라보 경쟁 가속'),
        ('#6B4226', '미국, 초콜릿·캐러멜애플 앞세운 가을 시즌 조기 전환'),
        ('#8B5E34', '일본, 호지차·샤인머스캣 프리미엄 라인과 원신 콜라보 예약 개시'),
    ],
    'table_rows': [
        ('한국', '딸기', '5', '2', '딸기·초콜릿', '#FCEAF0'),
        ('미국', '초코', '2', '2', '파인트·바', '#EFDDD0'),
        ('일본', '호지차', '4', '1', '미니컵·샤인머스캣', '#F1E4D3'),
    ],
    'analysis': '이번 주(8/21~8/28) 한국·미국·일본 3개 시장은 폭염과 계절 전환이라는 서로 다른 배경 속에서도 활발한 신제품·마케팅 경쟁을 이어갔습니다. 한국은 기록적 폭염 속에 배스킨라빈스가 딸기 시그니처 맛을 내세우고 GS25가 현대자동차·TXT 연준과 잇단 콜라보 신제품을 선보이며 편의점발 화제성이 두드러졌습니다. 미국은 여름에서 가을로의 전환이 본격화되며 캐러멜애플·초콜릿 계열 신제품이 동시다발적으로 쏟아졌고, 코스트코의 3D 과일모양 아이스바와 크래그넘 레시피 등 SNS발 바이럴 콘텐츠가 강세를 보였습니다. 일본은 세븐일레븐의 마루데 시리즈와 하겐다즈 신작이 프리미엄 과일·호지차 트렌드를 이끄는 가운데, 원신×배스킨라빈스 재팬 콜라보 사전예약 개시가 게임 팬덤을 중심으로 큰 화제를 모았습니다. 세 시장 공통적으로 유명 IP·셀럽과의 협업 마케팅이 신제품 화제성을 견인하는 핵심 전략으로 자리잡고 있습니다.',
}

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
