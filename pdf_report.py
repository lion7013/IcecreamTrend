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

REPORT_DATE = "2026.09.06"
REPORT_RANGE = "2026.08.30 - 09.06"
OUT_PDF = "docs/reports/2026-09-06-ice-cream-trends.pdf"
COUNTRIES = [
    {
        'key': 'kr', 'name': '한국', 'flavor': '초코',
        'soft': '#EFDDD0', 'mid': '#C89173', 'deep': '#6B4226',
        'headline': '도쿄바나나 콜라보와 하겐다즈 팝업, 초코·브륄레 열풍 이끌어',
        'summary_paragraphs': [
            "배스킨라빈스가 일본 도쿄바나나와 협업해 9월 이달의 맛 '도쿄바나나 크렘브륄레'를 출시하며 초콜릿·브륄레 계열 신제품 경쟁에 불을 지폈습니다. 크리스피크림도넛은 아이스크림 바 형태의 '도넛바' 4종을 9월 17일까지 판매 중이며, 요아정은 카카오프렌즈 리틀어피치와 협업한 저당 복숭아 요거트 아이스 8종으로 SNS 화제성을 이어가고 있습니다.",
            "하겐다즈는 9월 5일부터 13일까지 서울 성수동에서 크루즈 콘셉트 팝업 '더 하겐 크루즈'를 열어 리뉴얼한 벨지안 초콜릿을 선보였고, 코코아 가격 폭등에도 오히려 함량을 높이는 역발상 프리미엄 전략을 택했습니다. 롯데웰푸드는 설레임 모델 기안84와 함께 3,000명 규모 러닝 행사 '설레임런'을 열어 티켓이 2시간 만에 매진됐고, 폭염과 수출 호조에 힘입어 8월 31일 롯데웰푸드·빙그레 주가가 나란히 52주 신고가를 기록했습니다.",
        ],
        'flavor_bars': [['초코', 5], ['딸기', 3], ['복숭아', 3], ['요거트', 3], ['바나나', 2]],
        'pack_bars': [['캐릭터 콜라보', 6], ['굿즈 동봉', 3], ['반반바', 2], ['설탕코팅 깨먹기', 2], ['젤리 변신', 2]],
        'content_bars': [['하겐다즈 성수 팝업', 12], ['도쿄바나나 크렘브륄레', 10], ['설레임런 행사', 8], ['편의점 신상 비교', 6], ['52주 신고가 뉴스', 5]],
        'refs_intro': '이번 리포트는 국내 언론사 기사와 Threads·X 등 웹검색으로 확인 가능한 SNS 게시물을 기반으로 작성됐으며, 인스타그램·틱톡 전체를 실시간 크롤링한 결과는 아닙니다.',
        'refs': [
            {'num': 1, 'title': "배스킨라빈스, 9월 맛 '도쿄바나나 크렘브륄레' 출시", 'note': '국제뉴스, 도쿄바나나 협업 9월 신제품 보도.', 'kind': '신제품', 'thumb_url': None},
            {'num': 2, 'title': "하겐다즈, 성수동 팝업 '더 하겐 크루즈' 오픈", 'note': '한국경제, 9/5~9/13 크루즈 콘셉트 팝업 소식.', 'kind': '광고', 'thumb_url': None},
            {'num': 3, 'title': "롯데웰푸드, 기안84와 '설레임런' 3,000명 개최", 'note': '한국경제, 9월 5일 하남 러닝 이벤트 보도.', 'kind': '광고', 'thumb_url': None},
            {'num': 4, 'title': '폭염·수출 훈풍에 빙그레·롯데웰푸드 52주 신고가', 'note': '한국경제, 8월 31일 주가 기록 보도.', 'kind': '뉴스', 'thumb_url': None},
            {'num': 5, 'title': '하겐다즈, 카카오값 폭등에도 초콜릿 함량 오히려 높여', 'note': '이투데이, 프리미엄 역발상 전략 소개.', 'kind': '뉴스', 'thumb_url': None},
        ],
    },
    {
        'key': 'us', 'name': '미국', 'flavor': '캐러멜',
        'soft': '#F3E3D8', 'mid': '#D9A26B', 'deep': '#A66A1C',
        'headline': '타코벨x솔트앤스트로 추로 타코가 이끈 초콜릿·캐러멜 열풍',
        'summary_paragraphs': [
            "타코벨이 9월 1일 솔트앤스트로와 협업한 초콜릿 코팅 '추로 아이스크림 타코'를 3.99달러에 전국 재출시하며 단종된 초코 타코의 후속작이라는 평가를 받았습니다. 벤앤제리스는 중간선거 투표 독려 캠페인과 연계한 한정판 '라즈 업!'을 선보이는 한편, 인기 파인트 맛을 낱개 바 형태로 옮긴 신제품 라인도 출시해 편의점 채널을 공략했습니다.",
            "매그넘은 두바이·튀르키예 등에서 화제였던 '두바이 초콜릿' 바를 샘스클럽 대용량 팩으로 미국에 정식 출시했고, 반 리우웬은 닥터수스와 협업한 크로거 단독 신맛 3종을 선보여 빠르게 품절되고 있습니다. 콜드스톤과 제니스는 각각 가을 신맛 컬렉션을 내놓았으며, 알디의 프리미엄 '카라멜 콘' 아이스크림은 벤앤제리스 인기 제품과 흡사하다는 레딧 후기로 SNS에서 화제를 모았습니다. 한편 미국 아이스크림 평균 수입 관세가 25%에서 34%로 오를 것으로 전해지는 가운데도 소매가 인상 발표는 아직 없습니다.",
        ],
        'flavor_bars': [['캐러멜', 6], ['초코', 6], ['바닐라', 5], ['추로·시나몬', 4], ['펌킨·가을향신료', 4]],
        'pack_bars': [['한정메뉴(QSR)', 6], ['파인트', 5], ['노벨티바', 5], ['스쿱컵', 4], ['멀티팩', 4]],
        'content_bars': [['타코벨×솔트앤스트로', 16], ['두바이초콜릿 매그넘', 12], ['알디 카라멜콘 레딧', 9], ['제니스 가을 컬렉션', 7], ['콜드스톤 코지 컬렉션', 6]],
        'refs_intro': '이번 주 미국 시장 리서치는 현지 언론과 웹검색으로 확인 가능한 SNS 게시물을 기반으로 작성됐으며, 인스타그램·틱톡 전체 크롤링 결과는 아닙니다.',
        'refs': [
            {'num': 1, 'title': 'Taco Bell Relaunches Salt & Straw Churro Ice Cream Taco Nationwide', 'note': 'Taco Bell Newsroom, 9월 1일 전국 재출시 보도.', 'kind': '신제품', 'thumb_url': None},
            {'num': 2, 'title': "Magnum's Viral 'Dubai Chocolate' Bars Debut in US via Sam's Club", 'note': 'Parade, 두바이 초콜릿 미국 정식 출시 소식.', 'kind': '신제품', 'thumb_url': None},
            {'num': 3, 'title': "Aldi's Caramel Cone Ice Cream Goes Viral as a Ben & Jerry's Dupe", 'note': 'Yahoo Lifestyle, 레딧발 그로서리 듀프 트렌드 보도.', 'kind': 'SNS', 'thumb_url': None},
            {'num': 4, "title": "Jeni's Splendid Ice Creams Launches Fall Collection on Sept. 3", 'note': 'Yo! Venice, 가을 신맛 컬렉션 출시 소식.', 'kind': '신제품', 'thumb_url': None},
            {'num': 5, 'title': 'US Ice Cream Import Tariffs Set to Climb From 25% to 34%', 'note': 'Yahoo Finance, 관세·원가 부담 분석 기사.', 'kind': '뉴스', 'thumb_url': None},
        ],
    },
    {
        'key': 'jp', 'name': '일본', 'flavor': '멜론',
        'soft': '#EAF7E0', 'mid': '#A9DE93', 'deep': '#4FA65B',
        'headline': '롯데·모리나가 아이스크림 값 인상 속 이색 신제품 경쟁',
        'summary_paragraphs': [
            "롯데가 쿨리시 등 약 30개 품목의 아이스크림 가격을 9월 1일 출하분부터 5.1~16.0% 인상했고, 모리나가유업도 '피노'·'파르므' 등 61개 품목의 가격을 같은 시기 올리며 업계 전반에 값인상 도미노가 이어졌습니다. 인건비·물류비·원재료비 상승이 공통적인 배경으로 꼽힙니다.",
            "가격 인상 속에서도 신제품 경쟁은 이어져, 세븐일레븐은 우지 말차 초콜릿바와 홋카이도 멜론 와플콘을 내놓았고 하겐다즈는 검은깨·콩가루 미니컵과 고구마·캐러멜 신맛을 잇달아 출시했습니다. 이무라야는 40주년을 맞아 '타이야키 아이스'를 8년 만에 리뉴얼했고, 모리나가는 피노 50주년을 앞두고 '파우 패트롤'과 첫 협업에 나섰습니다. 이와테현의 '굴 소프트아이스크림'은 Threads에서 약 62만 회 조회를 기록하며 SNS에서 가장 화제가 된 콘텐츠로 떠올랐습니다.",
        ],
        'flavor_bars': [['과일맛(멜론·망고 등)', 6], ['초코', 5], ['밀크', 4], ['캐러멜', 2], ['말차', 1]],
        'pack_bars': [['컵', 4], ['미니컵', 3], ['콜라보 패키지', 3], ['바', 3], ['어소트박스', 2]],
        'content_bars': [['굴 소프트아이스크림', 62], ['모리나가 값 인상', 14], ['롯데 값 인상', 12], ['세븐일레븐 말차·멜론', 9], ['하겐다즈 신맛 2종', 7]],
        'refs_intro': '이 섹션은 일본 언론·업계 매체 기사와 웹검색으로 확인 가능한 정보를 바탕으로 작성됐으며, 인스타그램·틱톡 전체 크롤링 결과는 아닙니다.',
        'refs': [
            {'num': 1, 'title': "롯데, 9월 출하분부터 아이스크림 30여 품목 가격 인상", 'note': '후쿠이신문 온라인, 롯데 9월 가격 인상 보도.', 'kind': '뉴스', 'thumb_url': None},
            {'num': 2, 'title': "모리나가유업, '피노'·'파르므' 등 61개 품목 가격 인상", 'note': '니혼게이자이신문, 모리나가 9월 가격 인상 보도.', 'kind': '뉴스', 'thumb_url': None},
            {'num': 3, 'title': "이무라야, 8년 만에 '타이야키 아이스' 리뉴얼", 'note': 'Japaaan, 40주년 기념 리뉴얼 소식.', 'kind': '신제품', 'thumb_url': None},
            {'num': 4, 'title': "이와테 '굴 소프트아이스크림', Threads서 62만 회 표시 화제", 'note': '라이브도어뉴스, 로드사이드 스테이션 바이럴 소식.', 'kind': '바이럴', 'thumb_url': None},
            {'num': 5, 'title': "모리나가 '피노', 첫 '파우 패트롤' 콜라보 9월 21일 출시", 'note': 'PR TIMES, 피노 50주년 콜라보 소식.', 'kind': '신제품', 'thumb_url': None},
        ],
    },
]
OVERVIEW = {
    'highlights': [
        ('#6B4226', '한국, 도쿄바나나 콜라보와 하겐다즈 성수 팝업이 이끈 초콜릿 열풍'),
        ('#A66A1C', '미국, 타코벨×솔트앤스트로 추로 타코와 두바이초콜릿 매그넘 확산'),
        ('#4FA65B', '일본, 롯데·모리나가 아이스크림 90여 개 품목 값 인상'),
    ],
    'table_rows': [
        ('한국', '초코', '3', '2', '캐릭터 콜라보', '#EFDDD0'),
        ('미국', '캐러멜', '6', '2', '초코·캐러멜', '#F3E3D8'),
        ('일본', '멜론', '8', '1', '과일맛·초코', '#EAF7E0'),
    ],
    'analysis': '이번 주(8/30~9/6) 세 시장은 모두 브랜드 협업과 프리미엄화 전략이 두드러졌습니다. 한국은 도쿄바나나·하겐다즈 팝업 등 일본발 콜라보로 초콜릿·브륄레 계열이 강세를 보였고, 미국은 두바이 초콜릿 트렌드가 실제 매대 제품으로 안착하며 초콜릿·캐러멜이 동반 상승했습니다. 일본은 롯데·모리나가가 총 90여개 품목의 가격을 동시에 인상하며 원가 압박이 표면화된 가운데도 세븐일레븐·하겐다즈 등은 신제품 경쟁을 멈추지 않았습니다. 세 시장 공통적으로 캐릭터·셀럽 협업과 한정판 전략이 소비자 관심을 끄는 핵심 축으로 작동했으며, 관세·원가 부담은 아직 소매가에 본격 반영되지 않은 미국과 이미 반영되기 시작한 일본이 대조를 이뤘습니다.',
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
info_rows = [("리포트","주간 아이스크림 트렌드"), ("기간",REPORT_RANGE), ("발행일",f"{REPORT_DATE} (일)"), ("작성","Scoop Report 자동 리서치")]
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
